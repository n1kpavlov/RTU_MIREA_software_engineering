package ru.mirea.asu.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import ru.mirea.asu.entity.IssuanceDocument;

import java.util.List;
import java.util.UUID;

public interface IssuanceDocumentRepository extends JpaRepository<IssuanceDocument, UUID> {

    List<IssuanceDocument> findByAthleteId(UUID athleteId);

    List<IssuanceDocument> findByInventoryItemId(UUID inventoryItemId);

    @Query("SELECT COUNT(d) > 0 FROM IssuanceDocument d " +
            "WHERE d.athlete.id = :athleteId " +
            "AND d.status IN ('ACTIVE', 'OVERDUE')")
    boolean hasActiveIssuances(@Param("athleteId") UUID athleteId);
}