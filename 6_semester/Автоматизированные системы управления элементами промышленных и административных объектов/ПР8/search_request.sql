-- Поиск спортсменов-должников (с просроченным инвентарем)
SELECT 
    u.full_name AS athlete_name,
    u.email,
    u.phone,
    a.sports_category,
    g.group_name,
    cu.full_name AS coach_name,
    COUNT(d.issuance_document_id) AS overdue_items_count,
    STRING_AGG(i.barcode || ' (' || n.nomenclature_name || ', просрочен на ' || 
               (CURRENT_DATE - d.planned_return_date) || ' дн.)', '; ') AS overdue_items
FROM athlete a
JOIN "user" u ON a.athlete_user_id = u.user_id
LEFT JOIN "group" g ON a.athlete_group_id = g.group_id
LEFT JOIN coach c ON a.athlete_coach_id = c.coach_id
LEFT JOIN "user" cu ON c.coach_user_id = cu.user_id
JOIN issuance_document d ON a.athlete_id = d.issuance_document_athlete_id
JOIN inventory_item i ON d.issuance_document_inventory_item_id = i.inventory_item_id
JOIN nomenclature n ON i.inventory_item_nomenclature_id = n.nomenclature_id
WHERE d.issuance_document_status IN ('ACTIVE', 'OVERDUE') 
  AND d.planned_return_date < CURRENT_DATE
GROUP BY u.full_name, u.email, u.phone, a.sports_category, g.group_name, cu.full_name
ORDER BY overdue_items_count DESC;