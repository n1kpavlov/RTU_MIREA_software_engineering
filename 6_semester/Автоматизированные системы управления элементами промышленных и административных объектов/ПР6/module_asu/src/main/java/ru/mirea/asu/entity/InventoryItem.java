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
@Table(name = "inventory_items")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class InventoryItem {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "id", updatable = false, nullable = false)
    private UUID id;

    @Column(name = "barcode", unique = true, nullable = false, length = 50)
    private String barcode;

    @Column(name = "product_name", nullable = false, length = 200)
    private String productName;

    @Column(name = "size", length = 20)
    private String size;

    @Column(name = "flex_rating", length = 20)
    private String flexRating;

    @Column(name = "binding_type", length = 50)
    private String bindingType;

    @Column(name = "manufacture_date")
    private LocalDate manufactureDate;

    @Column(name = "commissioning_date")
    private LocalDate commissioningDate;

    @Enumerated(EnumType.STRING)
    @Column(name = "status", nullable = false)
    private InventoryStatus status = InventoryStatus.AVAILABLE;

    @Column(name = "current_holder_id")
    private UUID currentHolderId;

    @Column(name = "warehouse_location", length = 100)
    private String warehouseLocation;

    @CreationTimestamp
    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;

    public enum InventoryStatus {
        AVAILABLE,      // доступен на складе
        RESERVED,       // зарезервирован
        ISSUED,         // выдан спортсмену
        UNDER_REPAIR,   // в ремонте
        DEFECTIVE,      // бракован
        WRITTEN_OFF     // списан
    }
}