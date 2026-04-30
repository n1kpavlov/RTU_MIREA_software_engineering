INSERT INTO "user" (full_name, email, phone, login, password_hash, role, registration_date, is_active) VALUES
('Иванов Иван Иванович', 'ivanov@ski.ru', '+79161234567', 'ivanov', 'hash_ivanov_123', 'athlete', '2024-09-01', TRUE),
('Петров Петр Петрович', 'petrov@ski.ru', '+79162345678', 'petrov', 'hash_petrov_123', 'athlete', '2024-09-01', TRUE),
('Сидоров Сидор Сидорович', 'sidorov@ski.ru', '+79163456789', 'sidorov', 'hash_sidorov_123', 'athlete', '2024-09-02', TRUE),
('Смирнова Анна Сергеевна', 'smirnova@ski.ru', '+79164567890', 'asmirnova', 'hash_smirnova_123', 'athlete', '2024-09-02', TRUE),
('Кузнецов Дмитрий Алексеевич', 'kuznetsov@ski.ru', '+79165678901', 'dkuznetsov', 'hash_kuznetsov_123', 'athlete', '2024-09-03', TRUE),
('Попова Елена Викторовна', 'popova@ski.ru', '+79166789012', 'epopova', 'hash_popova_123', 'athlete', '2024-09-03', TRUE),
('Васильев Алексей Николаевич', 'vasiliev@ski.ru', '+79167890123', 'avasiliev', 'hash_vasiliev_123', 'athlete', '2024-09-04', TRUE),
('Новикова Мария Игоревна', 'novikova@ski.ru', '+79168901234', 'mnovikova', 'hash_novikova_123', 'athlete', '2024-09-04', TRUE),
('Морозов Сергей Владимирович', 'morozov@ski.ru', '+79169012345', 'smorozov', 'hash_morozov_123', 'athlete', '2024-09-05', TRUE),
('Волкова Ольга Дмитриевна', 'volkova@ski.ru', '+79160123456', 'ovolkova', 'hash_volkova_123', 'athlete', '2024-09-05', TRUE),
('Соколов Роман Андреевич', 'sokolov@ski.ru', '+79161234568', 'rsokolov', 'hash_sokolov_123', 'athlete', '2024-09-06', TRUE),
('Орлова Татьяна Павловна', 'orlova@ski.ru', '+79162345679', 'torlova', 'hash_orlova_123', 'athlete', '2024-09-06', TRUE),
('Лебедев Андрей Викторович', 'lebedev@ski.ru', '+79163456780', 'alebedev', 'hash_lebedev_123', 'athlete', '2024-09-07', TRUE),
('Козлова Наталья Игоревна', 'kozlova@ski.ru', '+79164567891', 'nkozlova', 'hash_kozlova_123', 'athlete', '2024-09-07', TRUE),
('Федоров Михаил Сергеевич', 'fedorov@ski.ru', '+79165678902', 'mfedorov', 'hash_fedorov_123', 'athlete', '2024-09-08', TRUE),
('Тренеров Алексей Юрьевич', 'trenerov@ski.ru', '+79161239876', 'trenerov', 'hash_trenerov_123', 'coach', '2024-08-01', TRUE),
('Наставников Игорь Петрович', 'nastavnikov@ski.ru', '+79162348765', 'nastavnikov', 'hash_nastavnikov_123', 'coach', '2024-08-15', TRUE),
('Старцев Павел Николаевич', 'startsev@ski.ru', '+79163459876', 'pstartsev', 'hash_startsev_123', 'coach', '2024-09-01', TRUE),
('Складской Михаил Семенович', 'skladskoy@ski.ru', '+79163457654', 'skladskoy', 'hash_skladskoy_123', 'storekeeper', '2024-08-01', TRUE),
('Инвентарев Игорь Васильевич', 'inventarev@ski.ru', '+79164568765', 'inventarev', 'hash_inventarev_123', 'storekeeper', '2024-09-01', TRUE),
('Закупочный Владимир Ильич', 'zakupochny@ski.ru', '+79164566543', 'zakupochny', 'hash_zakupochny_123', 'purchase_manager', '2024-08-01', TRUE),
('Снабженцев Андрей Петрович', 'snabzhentsev@ski.ru', '+79165677654', 'asnabzhentsev', 'hash_snabzhentsev_123', 'purchase_manager', '2024-09-01', TRUE),
('Руководителев Павел Борисович', 'rukovoditelev@ski.ru', '+79165675432', 'rukovoditelev', 'hash_rukovoditelev_123', 'manager', '2024-07-01', TRUE),
('Бухгалтерова Наталья Алексеевна', 'buhgalterova@ski.ru', '+79166784321', 'buhgalterova', 'hash_buhgalterova_123', 'accountant', '2024-08-01', TRUE),
('Админов Денис Валерьевич', 'adminov@ski.ru', '+79167893210', 'adminov', 'hash_adminov_123', 'administrator', '2024-07-01', TRUE);

INSERT INTO warehouse (warehouse_name, address, type) VALUES
('Основной склад', 'г. Москва, ул. Лыжная, д. 1', 'main'),
('Склад сервисного центра', 'г. Москва, ул. Техническая, д. 5', 'service'),
('Резервный склад', 'г. Химки, ул. Запасная, д. 10', 'reserve'),
('Склад лыжной базы "Снежинка"', 'г. Москва, Ленинградское шоссе, 45', 'main'),
('Склад соревновательного инвентаря', 'г. Москва, ул. Спортивная, 12', 'main'),
('Склад расходных материалов', 'г. Москва, ул. Складская, 3', 'service'),
('Склад запасных частей', 'г. Химки, Вашутинское шоссе, 8', 'service'),
('Склад сезонного хранения', 'г. Долгопрудный, ул. Лесная, 20', 'reserve'),
('Склад экипировки сборной', 'г. Москва, Олимпийский пр-т, 5', 'main'),
('Склад утилизации', 'г. Мытищи, ул. Промышленная, 7', 'reserve');

INSERT INTO coach (coach_user_id, specialization, coach_category) VALUES
(16, 'Лыжные гонки', 'Высшая'),
(17, 'Биатлон', 'Первая'),
(18, 'Горные лыжи', 'Высшая');

INSERT INTO "group" (group_name, group_coach_id, group_created_at) VALUES
('Группа начальной подготовки №1', 1, '2024-09-01'),
('Группа начальной подготовки №2', 1, '2024-09-01'),
('Группа спортивного совершенствования', 1, '2024-09-01'),
('Юниорская сборная (лыжные гонки)', 1, '2024-09-01'),
('Биатлонная группа №1', 2, '2024-09-01'),
('Биатлонная группа №2', 2, '2024-09-01'),
('Горнолыжная группа "Слалом"', 3, '2024-09-01'),
('Горнолыжная группа "Гигант"', 3, '2024-09-01'),
('Спортивно-оздоровительная группа', 1, '2024-10-01'),
('Группа высшего спортивного мастерства', 1, '2024-10-01');

INSERT INTO athlete (athlete_user_id, sports_category, birth_year, athlete_group_id, athlete_coach_id, has_active_debt) VALUES
(1, 'КМС', 2005, 3, 1, FALSE),
(2, 'МС', 2003, 3, 1, FALSE),
(3, '1 разряд', 2007, 1, 1, TRUE),
(4, 'КМС', 2006, 4, 1, FALSE),
(5, 'МС', 2002, 4, 1, FALSE),
(6, '1 разряд', 2008, 2, 1, FALSE),
(7, 'КМС', 2004, 3, 1, FALSE),
(8, '2 разряд', 2009, 1, 1, FALSE),
(9, 'МС', 2001, 4, 1, TRUE),
(10, 'КМС', 2005, 3, 1, FALSE),
(11, '1 разряд', 2007, 5, 2, FALSE),
(12, 'КМС', 2006, 5, 2, FALSE),
(13, 'МС', 2003, 6, 2, FALSE),
(14, '1 разряд', 2008, 7, 3, FALSE),
(15, 'КМС', 2005, 8, 3, FALSE);

INSERT INTO storekeeper (storekeeper_user_id, storekeeper_warehouse_id, certificate_number) VALUES
(19, 1, 'СКЛ-2024-001'),
(20, 2, 'СКЛ-2024-002');

INSERT INTO purchase_manager (purchase_manager_user_id, department) VALUES
(21, 'Отдел снабжения'),
(22, 'Отдел закупок спортивного инвентаря');

INSERT INTO manager (manager_user_id, position, manager_access_level) VALUES
(23, 'Директор спортивной школы', 3);

INSERT INTO accountant (accountant_user_id, section) VALUES
(24, 'Материальный учет');

INSERT INTO administrator (administrator_user_id, administrator_access_level) VALUES
(25, 'FULL');

INSERT INTO nomenclature (article, nomenclature_name, nomenclature_category, unit, standard_service_life, min_stock_level, manufacturer) VALUES
('SKI-001', 'Лыжи гоночные Fischer Speedmax', 'skis', 'pair', 24, 5, 'Fischer'),
('SKI-002', 'Лыжи гоночные Madshus Redline', 'skis', 'pair', 24, 5, 'Madshus'),
('SKI-003', 'Лыжи тренировочные Fischer RCS', 'skis', 'pair', 18, 10, 'Fischer'),
('SKI-004', 'Лыжи горные Atomic Redster', 'skis', 'pair', 24, 3, 'Atomic'),
('SKI-005', 'Лыжи для классического хода Rossignol', 'skis', 'pair', 24, 5, 'Rossignol'),
('BOOT-001', 'Ботинки лыжные Salomon S/Lab', 'boots', 'pair', 18, 8, 'Salomon'),
('BOOT-002', 'Ботинки лыжные Fischer Carbonlite', 'boots', 'pair', 18, 8, 'Fischer'),
('BOOT-003', 'Ботинки тренировочные Madshus', 'boots', 'pair', 12, 12, 'Madshus'),
('BOOT-004', 'Ботинки горнолыжные Atomic Hawx', 'boots', 'pair', 24, 5, 'Atomic'),
('POLE-001', 'Палки лыжные Swix Triac', 'poles', 'pair', 12, 10, 'Swix'),
('POLE-002', 'Палки лыжные Leki HRC', 'poles', 'pair', 12, 10, 'Leki'),
('POLE-003', 'Палки горнолыжные Komperdell', 'poles', 'pair', 12, 5, 'Komperdell'),
('WAX-001', 'Парафин Swix LF4', 'wax', 'pcs', 6, 20, 'Swix'),
('WAX-002', 'Парафин Swix HF6', 'wax', 'pcs', 6, 15, 'Swix'),
('WAX-003', 'Порошок ускоритель Swix FC7', 'wax', 'pcs', 12, 10, 'Swix');

INSERT INTO supplier (supplier_name, inn, kpp, legal_address, contact_person, supplier_phone, supplier_email, rating) VALUES
('ООО "СпортТовары"', '7712345678', '771201001', 'г. Москва, ул. Спортивная, 10', 'Иванов А.А.', '+74951234567', 'info@sporttovary.ru', 4.8),
('ООО "Лыжный Мир"', '7723456789', '772301001', 'г. Москва, ул. Снежная, 5', 'Петров Б.Б.', '+74952345678', 'sales@skimirs.ru', 4.5),
('ООО "Фишер Рус"', '7734567890', '773401001', 'г. Москва, ул. Горнолыжная, 15', 'Сидоров В.В.', '+74953456789', 'info@fischer-rus.ru', 4.9),
('ООО "Свикс Россия"', '7745678901', '774501001', 'г. Санкт-Петербург, пр. Лыжный, 20', 'Козлов Г.Г.', '+78123456789', 'sales@swix-russia.ru', 4.7),
('ООО "Саломон СНГ"', '7756789012', '775601001', 'г. Москва, ул. Зимняя, 8', 'Новиков Д.Д.', '+74954567890', 'info@salomon-cis.ru', 4.6),
('ООО "СпортМастер"', '7767890123', '776701001', 'г. Москва, ул. Торговая, 1', 'Морозов Е.Е.', '+74955678901', 'corp@sportmaster.ru', 4.4),
('ООО "Декатлон"', '7778901234', '777801001', 'г. Москва, ш. Дмитровское, 100', 'Волков Ж.Ж.', '+74956789012', 'b2b@decathlon.ru', 4.3),
('ООО "Кант"', '7789012345', '778901001', 'г. Москва, пр. Мира, 50', 'Зайцев З.З.', '+74957890123', 'opt@kant.ru', 4.5),
('ООО "Триал-Спорт"', '7790123456', '779001001', 'г. Москва, ул. Профсоюзная, 30', 'Медведев И.И.', '+74958901234', 'wholesale@trial-sport.ru', 4.2),
('ООО "АльпИндустрия"', '7701234567', '770101001', 'г. Москва, ул. Первомайская, 40', 'Волков К.К.', '+74959012345', 'opt@alpindustria.ru', 4.4),
('ООО "Спорт-Экспресс"', '7711122233', '771101001', 'г. Москва, ул. Ленина, 15', 'Быстров С.С.', '+74951239876', 'info@sport-express.ru', 4.6),
('ООО "Лыжный стандарт"', '7722233344', '772201001', 'г. Екатеринбург, ул. Уральская, 10', 'Уралов М.М.', '+73431234567', 'sales@skistandard.ru', 4.3);

INSERT INTO purchase_request (purchase_request_number, purchase_request_created_date, purchase_request_status, author_id, approved_by, planned_amount, purchase_request_comment) VALUES
('ЗАЯВ-2026-001', '2026-01-10 09:00:00', 'APPROVED', 16, 23, 250000.00, 'Закупка инвентаря на сезон 2026'),
('ЗАЯВ-2026-002', '2026-01-15 10:30:00', 'ON_APPROVAL', 17, NULL, 150000.00, 'Дополнительная закупка лыж для юниоров'),
('ЗАЯВ-2026-003', '2026-01-20 11:45:00', 'DRAFT', 18, NULL, 50000.00, 'Закупка смазочных материалов'),
('ЗАЯВ-2026-004', '2026-02-01 08:15:00', 'APPROVED', 16, 23, 180000.00, 'Закупка ботинок для группы НП-1'),
('ЗАЯВ-2026-005', '2026-02-10 14:20:00', 'REJECTED', 17, 23, 95000.00, 'Закупка палок (отклонено - пересмотреть бюджет)'),
('ЗАЯВ-2026-006', '2026-02-15 16:00:00', 'APPROVED', 18, 23, 75000.00, 'Закупка креплений'),
('ЗАЯВ-2026-007', '2026-03-01 10:00:00', 'ON_APPROVAL', 16, NULL, 220000.00, 'Плановая закупка на весну'),
('ЗАЯВ-2026-008', '2026-03-05 11:30:00', 'DRAFT', 17, NULL, 35000.00, 'Закупка расходных материалов'),
('ЗАЯВ-2026-009', '2026-03-10 09:45:00', 'APPROVED', 16, 23, 310000.00, 'Крупная закупка лыж Fischer'),
('ЗАЯВ-2026-010', '2026-03-15 13:15:00', 'ON_APPROVAL', 18, NULL, 120000.00, 'Закупка горнолыжного инвентаря');

INSERT INTO purchase_request_item (purchase_request_item_request_id, purchase_request_item_nomenclature_id, quantity, expected_price, priority) VALUES
(1, 1, 10, 45000.00, 'HIGH'),
(1, 6, 15, 25000.00, 'HIGH'),
(1, 10, 20, 8000.00, 'MEDIUM'),
(2, 2, 5, 50000.00, 'HIGH'),
(2, 7, 10, 28000.00, 'MEDIUM'),
(3, 13, 50, 500.00, 'LOW'),
(3, 14, 30, 600.00, 'LOW'),
(4, 6, 12, 25000.00, 'HIGH'),
(4, 8, 10, 12000.00, 'MEDIUM'),
(5, 10, 25, 8000.00, 'MEDIUM'),
(6, 5, 8, 52000.00, 'HIGH'),
(7, 3, 15, 35000.00, 'HIGH'),
(8, 15, 20, 1200.00, 'LOW'),
(9, 1, 20, 45000.00, 'HIGH'),
(10, 4, 6, 48000.00, 'HIGH');

INSERT INTO purchase_order (purchase_order_number, purchase_order_created_date, purchase_order_status, purchase_order_supplier_id, purchase_order_manager_id, total_amount, expected_delivery_date) VALUES
('ЗАКАЗ-2026-001', '2026-01-12', 'SENT', 3, 1, 825000.00, '2026-08-15'),
('ЗАКАЗ-2026-002', '2026-01-18', 'DELIVERED', 4, 2, 160000.00, '2026-02-01'),
('ЗАКАЗ-2026-003', '2026-02-05', 'IN_TRANSIT', 1, 1, 250000.00, '2026-03-10'),
('ЗАКАЗ-2026-004', '2026-02-12', 'SENT', 2, 2, 180000.00, '2026-09-01'),
('ЗАКАЗ-2026-005', '2026-02-20', 'DRAFT', 5, 1, 95000.00, NULL),
('ЗАКАЗ-2026-006', '2026-03-01', 'DELIVERED', 6, 1, 120000.00, '2026-03-20'),
('ЗАКАЗ-2026-007', '2026-03-10', 'SENT', 3, 2, 450000.00, '2026-10-01'),
('ЗАКАЗ-2026-008', '2026-03-15', 'CLOSED', 4, 1, 75000.00, '2026-03-25'),
('ЗАКАЗ-2026-009', '2026-03-20', 'IN_TRANSIT', 8, 2, 210000.00, '2026-04-15'),
('ЗАКАЗ-2026-010', '2026-03-25', 'SENT', 11, 1, 135000.00, '2026-08-20');

INSERT INTO inventory_item (barcode, inventory_item_nomenclature_id, serial_number, inventory_status, inventory_item_warehouse_id, receipt_date, purchase_cost, size, current_holder_id, inventory_notes) VALUES
('SKI001-2024-001', 1, 'FS-2024-001', 'AVAILABLE', 1, '2024-10-01', 45000.00, '190', NULL, 'Новые'),
('SKI001-2024-002', 1, 'FS-2024-002', 'ISSUED', 1, '2024-10-01', 45000.00, '195', 1, 'Выданы Иванову'),
('SKI001-2024-003', 1, 'FS-2024-003', 'AVAILABLE', 1, '2024-10-01', 45000.00, '200', NULL, 'Новые'),
('SKI001-2024-004', 1, 'FS-2024-004', 'RESERVED', 1, '2024-10-01', 45000.00, '192', NULL, 'Зарезервированы для сборов'),
('SKI001-2024-005', 1, 'FS-2024-005', 'ISSUED', 1, '2024-10-01', 45000.00, '198', 2, 'Выданы Петрову'),
('SKI002-2024-001', 2, 'MR-2024-001', 'AVAILABLE', 1, '2024-10-15', 50000.00, '192', NULL, NULL),
('SKI002-2024-002', 2, 'MR-2024-002', 'ISSUED', 1, '2024-10-15', 50000.00, '198', 4, 'Выданы Смирновой'),
('SKI002-2024-003', 2, 'MR-2024-003', 'UNDER_REPAIR', 2, '2024-10-15', 50000.00, '195', NULL, 'Ремонт скользящей поверхности'),
('BOOT001-2024-001', 6, 'SL-2024-001', 'AVAILABLE', 1, '2024-11-01', 25000.00, '42', NULL, NULL),
('BOOT001-2024-002', 6, 'SL-2024-002', 'ISSUED', 1, '2024-11-01', 25000.00, '43', 1, 'Выданы Иванову'),
('BOOT001-2024-003', 6, 'SL-2024-003', 'AVAILABLE', 1, '2024-11-01', 25000.00, '44', NULL, NULL),
('BOOT001-2024-004', 6, 'SL-2024-004', 'ISSUED', 1, '2024-11-01', 25000.00, '41', 5, 'Выданы Кузнецову'),
('POLE001-2024-001', 10, 'SW-2024-001', 'AVAILABLE', 1, '2024-11-15', 8000.00, '155', NULL, NULL),
('POLE001-2024-002', 10, 'SW-2024-002', 'ISSUED', 1, '2024-11-15', 8000.00, '160', 2, 'Выданы Петрову'),
('POLE001-2024-003', 10, 'SW-2024-003', 'DEFECTIVE', 1, '2024-11-15', 8000.00, '150', NULL, 'Трещина на древке'),
('WAX001-2024-001', 13, 'WAX-LF4-001', 'AVAILABLE', 1, '2024-12-01', 500.00, NULL, NULL, NULL),
('WAX001-2024-002', 13, 'WAX-LF4-002', 'AVAILABLE', 1, '2024-12-01', 500.00, NULL, NULL, NULL),
('WAX002-2024-001', 14, 'WAX-HF6-001', 'AVAILABLE', 1, '2024-12-01', 600.00, NULL, NULL, NULL),
('WAX002-2024-002', 14, 'WAX-HF6-002', 'ISSUED', 1, '2024-12-01', 600.00, NULL, 3, 'Выданы сервисной бригаде'),
('WAX003-2024-001', 15, 'WAX-FC7-001', 'AVAILABLE', 1, '2024-12-01', 1200.00, NULL, NULL, NULL);

INSERT INTO receipt_invoice (receipt_invoice_number, receipt_invoice_date, receipt_invoice_order_id, receipt_invoice_storekeeper_id, receipt_invoice_status, actual_amount) VALUES
('ПН-2024-001', '2024-10-01', 1, 1, 'POSTED', 825000.00),
('ПН-2024-002', '2024-11-15', 2, 1, 'POSTED', 160000.00),
('ПН-2024-003', '2024-12-01', 3, 2, 'POSTED', 250000.00),
('ПН-2025-001', '2025-01-15', 4, 1, 'POSTED', 180000.00),
('ПН-2025-002', '2025-02-01', 6, 2, 'POSTED', 120000.00),
('ПН-2025-003', '2025-02-15', 8, 1, 'POSTED', 75000.00),
('ПН-2025-004', '2025-03-01', 7, 1, 'DRAFT', 450000.00),
('ПН-2025-005', '2025-03-10', 9, 2, 'POSTED', 210000.00),
('ПН-2025-006', '2025-03-20', 5, 1, 'CANCELLED', 0.00),
('ПН-2025-007', '2025-03-25', 10, 2, 'DRAFT', 135000.00);

INSERT INTO issuance_document (issuance_document_inventory_item_id, issuance_document_athlete_id, issuance_document_storekeeper_id, issuance_date, planned_return_date, actual_return_date, issuance_document_status, condition_on_issue, condition_on_return, issuance_document_notes) VALUES
(2, 1, 1, '2024-12-01', '2025-03-30', NULL, 'ACTIVE', 'NEW', NULL, 'На сезон 2024-2025'),
(5, 2, 1, '2024-12-05', '2025-03-30', NULL, 'ACTIVE', 'NEW', NULL, 'На сезон 2024-2025'),
(7, 4, 2, '2024-12-10', '2025-03-30', NULL, 'ACTIVE', 'NEW', NULL, 'На сезон 2024-2025'),
(12, 5, 1, '2024-12-15', '2025-03-30', NULL, 'ACTIVE', 'NEW', NULL, 'На сезон 2024-2025'),
(10, 6, 2, '2025-01-10', '2025-04-15', NULL, 'ACTIVE', 'NEW', NULL, 'Выданы Поповой'),
(3, 7, 1, '2024-11-01', '2024-12-01', '2024-11-28', 'RETURNED', 'NEW', 'GOOD', NULL),
(4, 8, 2, '2024-11-05', '2024-12-05', '2024-12-01', 'RETURNED', 'NEW', 'GOOD', NULL),
(6, 9, 1, '2024-11-10', '2024-12-10', '2024-12-05', 'RETURNED', 'NEW', 'MINOR_SCRATCHES', 'Небольшие царапины'),
(8, 10, 2, '2024-11-15', '2024-12-15', '2024-12-10', 'RETURNED', 'NEW', 'GOOD', NULL),
(11, 11, 1, '2024-11-20', '2024-12-20', '2024-12-18', 'RETURNED', 'NEW', 'GOOD', NULL),
(9, 3, 1, '2024-10-01', '2024-11-01', NULL, 'OVERDUE', 'USED', NULL, 'Просрочен возврат!'),
(13, 12, 2, '2024-10-15', '2024-11-15', NULL, 'OVERDUE', 'USED', NULL, 'Просрочен возврат!'),
(1, 13, 1, '2024-11-01', '2024-12-01', NULL, 'OVERDUE', 'USED', NULL, 'Просрочен возврат!'),
(14, 14, 2, '2024-11-01', '2025-01-01', NULL, 'EXTENDED', 'NEW', NULL, 'Продлено до 01.02.2025'),
(15, 15, 1, '2024-11-15', '2025-01-15', NULL, 'EXTENDED', 'NEW', NULL, 'Продлено до 15.02.2025');

INSERT INTO operation_log (operation_log_user_id, action, entity_type, entity_id, details, ip_address, operation_log_created_at) VALUES
(25, 'CREATE_USER', 'user', 1, '{"created_by": "admin", "role": "athlete"}', '192.168.1.100', '2024-09-01 09:00:00'),
(25, 'CREATE_USER', 'user', 16, '{"created_by": "admin", "role": "coach"}', '192.168.1.100', '2024-09-01 09:05:00'),
(16, 'CREATE_REQUEST', 'purchase_request', 1, '{"amount": 250000}', '192.168.1.101', '2026-01-10 09:00:00'),
(23, 'APPROVE_REQUEST', 'purchase_request', 1, '{"approved": true}', '192.168.1.104', '2026-01-11 10:00:00'),
(21, 'CREATE_ORDER', 'purchase_order', 1, '{"supplier_id": 3, "total": 825000}', '192.168.1.103', '2026-01-12 11:00:00'),
(19, 'RECEIVE_GOODS', 'receipt_invoice', 1, '{"order_id": 1, "amount": 825000}', '192.168.1.102', '2024-10-01 14:00:00'),
(19, 'ISSUE_INVENTORY', 'issuance_document', 1, '{"athlete_id": 1, "barcode": "SKI001-2024-002"}', '192.168.1.102', '2024-12-01 10:00:00'),
(19, 'ISSUE_INVENTORY', 'issuance_document', 2, '{"athlete_id": 2, "barcode": "SKI001-2024-005"}', '192.168.1.102', '2024-12-05 10:30:00'),
(20, 'ISSUE_INVENTORY', 'issuance_document', 3, '{"athlete_id": 4, "barcode": "SKI002-2024-002"}', '192.168.1.105', '2024-12-10 11:00:00'),
(19, 'RETURN_INVENTORY', 'issuance_document', 6, '{"condition": "GOOD"}', '192.168.1.102', '2024-11-28 15:00:00'),
(17, 'CREATE_REQUEST', 'purchase_request', 2, '{"amount": 150000}', '192.168.1.106', '2026-01-15 10:30:00'),
(22, 'CREATE_ORDER', 'purchase_order', 2, '{"supplier_id": 4, "total": 160000}', '192.168.1.107', '2026-01-18 09:00:00'),
(25, 'BLOCK_USER', 'user', 3, '{"reason": "debt"}', '192.168.1.100', '2024-11-02 08:00:00'),
(24, 'EXPORT_REPORT', 'report', NULL, '{"type": "OSV", "period": "2024-Q4"}', '192.168.1.108', '2025-01-10 16:00:00'),
(23, 'VIEW_DASHBOARD', 'dashboard', NULL, '{"section": "analytics"}', '192.168.1.104', '2025-01-15 09:00:00');