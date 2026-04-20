-- Поиск спортсменов-должников (с просроченным инвентарем)
SELECT 
    u.full_name AS athlete_name,
    u.email,
    u.phone,
    a.sports_category,
    g.name AS group_name,
    cu.full_name AS coach_name,
    COUNT(d.id) AS overdue_items_count,
    STRING_AGG(i.barcode || ' (' || n.name || ', просрочен на ' || 
               (CURRENT_DATE - d.planned_return_date) || ' дн.)', '; ') AS overdue_items
FROM athletes a
JOIN users u ON a.user_id = u.id
LEFT JOIN groups g ON a.group_id = g.id
LEFT JOIN coaches c ON a.coach_id = c.id
LEFT JOIN users cu ON c.user_id = cu.id
JOIN issuance_documents d ON a.id = d.athlete_id
JOIN inventory_items i ON d.inventory_item_id = i.id
JOIN nomenclature n ON i.nomenclature_id = n.id
WHERE d.status IN ('ACTIVE', 'OVERDUE') 
  AND d.planned_return_date < CURRENT_DATE
GROUP BY u.full_name, u.email, u.phone, a.sports_category, g.name, cu.full_name
ORDER BY overdue_items_count DESC;