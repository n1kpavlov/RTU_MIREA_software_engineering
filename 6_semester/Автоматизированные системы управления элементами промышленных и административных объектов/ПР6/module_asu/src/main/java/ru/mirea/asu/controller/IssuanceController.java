package ru.mirea.asu.controller;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ru.mirea.asu.dto.IssuanceRequestDto;
import ru.mirea.asu.dto.IssuanceResponseDto;
import ru.mirea.asu.exception.AthleteHasDebtException;
import ru.mirea.asu.exception.InventoryItemNotFoundException;
import ru.mirea.asu.service.IssuanceService;

import java.util.UUID;

@Slf4j
@RestController
@RequestMapping("/api/issuance")
@RequiredArgsConstructor
public class IssuanceController {

    private final IssuanceService issuanceService;

    /**
     * Выдача инвентаря спортсмену
     * POST /api/issuance/issue
     *
     * @param request DTO с данными для выдачи
     * @return DTO с результатом выдачи
     */
    @PostMapping("/issue")
    public ResponseEntity<IssuanceResponseDto> issueInventory(
            @Valid @RequestBody IssuanceRequestDto request) {

        log.info("POST /api/issuance/issue - получен запрос на выдачу");

        IssuanceResponseDto response = issuanceService.issueInventory(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    /**
     * Регистрация возврата инвентаря
     * POST /api/issuance/return/{issuanceId}
     *
     * @param issuanceId ID документа выдачи
     * @return DTO с результатом возврата
     */
    @PostMapping("/return/{issuanceId}")
    public ResponseEntity<IssuanceResponseDto> returnInventory(
            @PathVariable UUID issuanceId) {

        log.info("POST /api/issuance/return/{} - регистрация возврата", issuanceId);

        IssuanceResponseDto response = issuanceService.returnInventory(issuanceId);
        return ResponseEntity.ok(response);
    }

    /**
     * Обработчик исключения "Спортсмен-должник"
     * Возвращает HTTP 409 Conflict
     */
    @ExceptionHandler(AthleteHasDebtException.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    public ResponseEntity<ErrorResponse> handleAthleteHasDebt(AthleteHasDebtException ex) {
        log.error("Ошибка выдачи: {}", ex.getMessage());
        return ResponseEntity
                .status(HttpStatus.CONFLICT)
                .body(new ErrorResponse("DEBTOR_BLOCKED", ex.getMessage()));
    }

    /**
     * Обработчик исключения "Инвентарь не найден"
     * Возвращает HTTP 404 Not Found
     */
    @ExceptionHandler(InventoryItemNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ResponseEntity<ErrorResponse> handleInventoryNotFound(InventoryItemNotFoundException ex) {
        log.error("Ошибка выдачи: {}", ex.getMessage());
        return ResponseEntity
                .status(HttpStatus.NOT_FOUND)
                .body(new ErrorResponse("INVENTORY_NOT_FOUND", ex.getMessage()));
    }

    /**
     * Внутренний класс для форматирования ошибок
     */
    record ErrorResponse(String code, String message) {}
}