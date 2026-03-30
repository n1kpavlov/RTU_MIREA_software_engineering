package ru.mirea.asu.service;

import ru.mirea.asu.dto.IssuanceRequestDto;
import ru.mirea.asu.dto.IssuanceResponseDto;

import java.util.UUID;

public interface IssuanceService {

    /**
     * Выполнить выдачу инвентаря спортсмену
     * @param request DTO с данными для выдачи
     * @return DTO с результатом выдачи
     * @throws ru.mirea.asu.exception.AthleteHasDebtException если спортсмен имеет задолженность
     * @throws ru.mirea.asu.exception.InventoryItemNotFoundException если инвентарь не найден
     */
    IssuanceResponseDto issueInventory(IssuanceRequestDto request);

    /**
     * Зарегистрировать возврат инвентаря
     * @param issuanceId ID документа выдачи
     * @return обновленный документ выдачи
     */
    IssuanceResponseDto returnInventory(UUID issuanceId);
}