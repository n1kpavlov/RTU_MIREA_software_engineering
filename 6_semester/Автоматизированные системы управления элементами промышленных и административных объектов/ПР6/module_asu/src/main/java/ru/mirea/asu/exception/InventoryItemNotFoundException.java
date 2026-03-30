package ru.mirea.asu.exception;

import java.util.UUID;

public class InventoryItemNotFoundException extends RuntimeException {

    public InventoryItemNotFoundException(String barcode) {
        super("Единица инвентаря со штрих-кодом '" + barcode + "' не найдена в системе.");
    }

    public InventoryItemNotFoundException(UUID id) {
        super("Единица инвентаря с ID " + id + " не найдена.");
    }
}