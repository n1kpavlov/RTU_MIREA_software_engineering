package ru.mirea.asu.exception;

import java.util.UUID;

public class AthleteHasDebtException extends RuntimeException {

    public AthleteHasDebtException(String message) {
        super(message);
    }

    public AthleteHasDebtException(UUID athleteId) {
        super("Спортсмен с ID " + athleteId + " имеет активную задолженность. " +
                "Выдача нового инвентаря невозможна до возврата предыдущего.");
    }
}