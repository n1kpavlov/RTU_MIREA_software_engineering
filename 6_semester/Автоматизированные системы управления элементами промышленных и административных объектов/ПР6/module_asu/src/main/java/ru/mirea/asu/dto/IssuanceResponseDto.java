package ru.mirea.asu.dto;

import lombok.Builder;
import lombok.Data;

import java.time.LocalDate;
import java.util.UUID;

@Data
@Builder
public class IssuanceResponseDto {

    private UUID issuanceId;
    private UUID athleteId;
    private String athleteName;
    private UUID inventoryItemId;
    private String inventoryName;
    private String barcode;
    private LocalDate issuanceDate;
    private LocalDate plannedReturnDate;
    private String status;
    private String message;
}