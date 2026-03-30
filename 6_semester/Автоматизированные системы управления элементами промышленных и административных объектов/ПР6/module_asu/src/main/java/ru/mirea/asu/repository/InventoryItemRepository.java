package ru.mirea.asu.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.transaction.annotation.Transactional;
import ru.mirea.asu.entity.InventoryItem;

import java.util.Optional;
import java.util.UUID;

public interface InventoryItemRepository extends JpaRepository<InventoryItem, UUID> {

    Optional<InventoryItem> findByBarcode(String barcode);

    @Modifying
    @Transactional
    @Query("UPDATE InventoryItem i SET i.status = :status, i.currentHolderId = :holderId " +
            "WHERE i.barcode = :barcode")
    int updateStatusAndHolder(@Param("barcode") String barcode,
                              @Param("status") InventoryItem.InventoryStatus status,
                              @Param("holderId") UUID holderId);

    @Query("SELECT i.status FROM InventoryItem i WHERE i.barcode = :barcode")
    InventoryItem.InventoryStatus getStatusByBarcode(@Param("barcode") String barcode);
}