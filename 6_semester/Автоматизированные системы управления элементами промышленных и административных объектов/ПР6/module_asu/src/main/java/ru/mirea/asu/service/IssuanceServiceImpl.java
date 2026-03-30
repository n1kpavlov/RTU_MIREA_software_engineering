package ru.mirea.asu.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import ru.mirea.asu.dto.IssuanceRequestDto;
import ru.mirea.asu.dto.IssuanceResponseDto;
import ru.mirea.asu.entity.Athlete;
import ru.mirea.asu.entity.InventoryItem;
import ru.mirea.asu.entity.IssuanceDocument;
import ru.mirea.asu.exception.AthleteHasDebtException;
import ru.mirea.asu.exception.InventoryItemNotFoundException;
import ru.mirea.asu.repository.AthleteRepository;
import ru.mirea.asu.repository.InventoryItemRepository;
import ru.mirea.asu.repository.IssuanceDocumentRepository;

import java.time.LocalDate;
import java.util.UUID;

@Slf4j
@Service
@RequiredArgsConstructor
public class IssuanceServiceImpl implements IssuanceService {

    private final AthleteRepository athleteRepository;
    private final InventoryItemRepository inventoryItemRepository;
    private final IssuanceDocumentRepository issuanceDocumentRepository;

    @Override
    @Transactional
    public IssuanceResponseDto issueInventory(IssuanceRequestDto request) {
        log.info("Начало выдачи инвентаря: спортсмен ID={}, штрих-код={}",
                request.getAthleteId(), request.getBarcode());

        // Шаг 1: Проверка существования спортсмена и наличия задолженности
        Athlete athlete = athleteRepository.findById(request.getAthleteId())
                .orElseThrow(() -> new IllegalArgumentException(
                        "Спортсмен с ID " + request.getAthleteId() + " не найден"));

        // Альтернативный поток: блокировка выдачи должнику
        if (athlete.isHasActiveDebt() || issuanceDocumentRepository.hasActiveIssuances(athlete.getId())) {
            log.warn("Попытка выдачи инвентаря спортсмену-должнику: {}", athlete.getFullName());
            throw new AthleteHasDebtException(athlete.getId());
        }

        // Шаг 2: Поиск инвентаря по штрих-коду
        InventoryItem inventoryItem = inventoryItemRepository.findByBarcode(request.getBarcode())
                .orElseThrow(() -> new InventoryItemNotFoundException(request.getBarcode()));

        // Шаг 3: Проверка доступности инвентаря
        if (inventoryItem.getStatus() != InventoryItem.InventoryStatus.AVAILABLE) {
            throw new IllegalStateException(
                    "Инвентарь со штрих-кодом " + request.getBarcode() +
                            " недоступен для выдачи. Текущий статус: " + inventoryItem.getStatus());
        }

        // Шаг 4: Создание документа выдачи
        IssuanceDocument issuanceDocument = new IssuanceDocument();
        issuanceDocument.setAthlete(athlete);
        issuanceDocument.setInventoryItem(inventoryItem);
        issuanceDocument.setIssuanceDate(LocalDate.now());
        issuanceDocument.setPlannedReturnDate(request.getPlannedReturnDate());
        issuanceDocument.setStorekeeperId(request.getStorekeeperId());
        issuanceDocument.setNotes(request.getNotes());
        issuanceDocument.setStatus(IssuanceDocument.IssuanceStatus.ACTIVE);

        IssuanceDocument savedDocument = issuanceDocumentRepository.save(issuanceDocument);

        // Шаг 5: Обновление статуса инвентаря и привязка к спортсмену
        inventoryItem.setStatus(InventoryItem.InventoryStatus.ISSUED);
        inventoryItem.setCurrentHolderId(athlete.getId());
        inventoryItemRepository.save(inventoryItem);

        log.info("Выдача инвентаря успешно завершена. ID документа: {}", savedDocument.getId());

        // Формирование ответа
        return IssuanceResponseDto.builder()
                .issuanceId(savedDocument.getId())
                .athleteId(athlete.getId())
                .athleteName(athlete.getFullName())
                .inventoryItemId(inventoryItem.getId())
                .inventoryName(inventoryItem.getProductName())
                .barcode(inventoryItem.getBarcode())
                .issuanceDate(savedDocument.getIssuanceDate())
                .plannedReturnDate(savedDocument.getPlannedReturnDate())
                .status(savedDocument.getStatus().name())
                .message("Инвентарь успешно выдан спортсмену " + athlete.getFullName())
                .build();
    }

    @Override
    @Transactional
    public IssuanceResponseDto returnInventory(UUID issuanceId) {
        log.info("Регистрация возврата инвентаря по документу: {}", issuanceId);

        IssuanceDocument issuanceDocument = issuanceDocumentRepository.findById(issuanceId)
                .orElseThrow(() -> new IllegalArgumentException(
                        "Документ выдачи с ID " + issuanceId + " не найден"));

        // Проверка, что инвентарь еще не возвращен
        if (issuanceDocument.getStatus() == IssuanceDocument.IssuanceStatus.RETURNED) {
            throw new IllegalStateException("Инвентарь уже был возвращен");
        }

        // Обновление документа выдачи
        issuanceDocument.setActualReturnDate(LocalDate.now());
        issuanceDocument.setStatus(IssuanceDocument.IssuanceStatus.RETURNED);
        issuanceDocumentRepository.save(issuanceDocument);

        // Обновление статуса инвентаря
        InventoryItem inventoryItem = issuanceDocument.getInventoryItem();
        inventoryItem.setStatus(InventoryItem.InventoryStatus.AVAILABLE);
        inventoryItem.setCurrentHolderId(null);
        inventoryItemRepository.save(inventoryItem);

        log.info("Возврат инвентаря успешно зарегистрирован. Штрих-код: {}",
                inventoryItem.getBarcode());

        return IssuanceResponseDto.builder()
                .issuanceId(issuanceDocument.getId())
                .athleteId(issuanceDocument.getAthlete().getId())
                .athleteName(issuanceDocument.getAthlete().getFullName())
                .inventoryItemId(inventoryItem.getId())
                .inventoryName(inventoryItem.getProductName())
                .barcode(inventoryItem.getBarcode())
                .issuanceDate(issuanceDocument.getIssuanceDate())
                .plannedReturnDate(issuanceDocument.getActualReturnDate())
                .status(issuanceDocument.getStatus().name())
                .message("Инвентарь успешно возвращен на склад")
                .build();
    }
}