package ru.mirea.asu.entity;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "issuance_documents")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class IssuanceDocument {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "id", updatable = false, nullable = false)
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "athlete_id", nullable = false)
    private Athlete athlete;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "inventory_item_id", nullable = false)
    private InventoryItem inventoryItem;

    @Column(name = "issuance_date", nullable = false)
    private LocalDate issuanceDate;

    @Column(name = "planned_return_date")
    private LocalDate plannedReturnDate;

    @Column(name = "actual_return_date")
    private LocalDate actualReturnDate;

    @Enumerated(EnumType.STRING)
    @Column(name = "status", nullable = false)
    private IssuanceStatus status = IssuanceStatus.ACTIVE;

    @Column(name = "storekeeper_id", nullable = false)
    private UUID storekeeperId;

    @Column(name = "notes", length = 500)
    private String notes;

    @CreationTimestamp
    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;

    public enum IssuanceStatus {
        ACTIVE,         // активная выдача (инвентарь у спортсмена)
        RETURNED,       // инвентарь возвращен
        OVERDUE,        // просрочен возврат
        EXTENDED        // срок возврата продлен
    }
}