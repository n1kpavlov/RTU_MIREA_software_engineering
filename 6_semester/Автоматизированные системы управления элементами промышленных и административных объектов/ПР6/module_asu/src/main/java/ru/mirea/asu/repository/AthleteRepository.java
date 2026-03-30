package ru.mirea.asu.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import ru.mirea.asu.entity.Athlete;

import java.util.Optional;
import java.util.UUID;

public interface AthleteRepository extends JpaRepository<Athlete, UUID> {

    Optional<Athlete> findByEmail(String email);

    @Query("SELECT a.hasActiveDebt FROM Athlete a WHERE a.id = :athleteId")
    boolean hasActiveDebt(@Param("athleteId") UUID athleteId);
}