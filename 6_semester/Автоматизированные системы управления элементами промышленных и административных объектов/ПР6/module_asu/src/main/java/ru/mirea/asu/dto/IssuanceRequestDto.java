package ru.mirea.asu.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import lombok.Data;

import java.time.LocalDate;
import java.util.UUID;

@Data
public class IssuanceRequestDto {

    @NotNull(message = "ID спортсмена обязателен")
    private UUID athleteId;

    @NotBlank(message = "Штрих-код инвентаря обязателен")
    @Size(min = 5, max = 50, message = "Штрих-код должен содержать от 5 до 50 символов")
    private String barcode;

    @NotNull(message = "Дата планируемого возврата обязательна")
    private LocalDate plannedReturnDate;

    @NotNull(message = "ID кладовщика обязателен")
    private UUID storekeeperId;

    private String notes;
}