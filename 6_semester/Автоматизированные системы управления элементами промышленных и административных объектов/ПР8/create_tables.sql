-- Базовая таблица пользователей
CREATE TABLE "user" (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(200) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    login VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(30) NOT NULL CHECK (role IN ('athlete', 'coach', 'storekeeper', 'purchase_manager', 'manager', 'accountant', 'administrator')),
    registration_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    user_created_at TIMESTAMP DEFAULT NOW(),
    user_updated_at TIMESTAMP DEFAULT NOW()
);

-- Справочник складов
CREATE TABLE warehouse (
    warehouse_id SERIAL PRIMARY KEY,
    warehouse_name VARCHAR(100) NOT NULL,
    address TEXT,
    type VARCHAR(50) CHECK (type IN ('main', 'reserve', 'service'))
);

-- Тренеры
CREATE TABLE coach (
    coach_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(user_id) ON DELETE CASCADE,
    specialization VARCHAR(100),
    coach_category VARCHAR(50)
);

-- Группы спортсменов
CREATE TABLE "group" (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL,
    coach_id INTEGER REFERENCES coach(coach_id) ON DELETE SET NULL,
    group_created_at TIMESTAMP DEFAULT NOW()
);

-- Спортсмены
CREATE TABLE athlete (
    athlete_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(user_id) ON DELETE CASCADE,
    sports_category VARCHAR(50),
    birth_year INTEGER,
    group_id INTEGER REFERENCES "group"(group_id) ON DELETE SET NULL,
    coach_id INTEGER REFERENCES coach(coach_id) ON DELETE SET NULL,
    has_active_debt BOOLEAN DEFAULT FALSE
);

-- Кладовщики
CREATE TABLE storekeeper (
    storekeeper_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(user_id) ON DELETE CASCADE,
    warehouse_id INTEGER REFERENCES warehouse(warehouse_id) ON DELETE SET NULL,
    certificate_number VARCHAR(50)
);

-- Менеджеры по закупкам
CREATE TABLE purchase_manager (
    purchase_manager_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(user_id) ON DELETE CASCADE,
    department VARCHAR(100)
);

-- Руководители
CREATE TABLE manager (
    manager_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(user_id) ON DELETE CASCADE,
    position VARCHAR(100),
    manager_access_level INTEGER DEFAULT 1 CHECK (manager_access_level BETWEEN 1 AND 3)
);

-- Бухгалтеры
CREATE TABLE accountant (
    accountant_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(user_id) ON DELETE CASCADE,
    section VARCHAR(100)
);

-- Администраторы
CREATE TABLE administrator (
    administrator_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(user_id) ON DELETE CASCADE,
    administrator_access_level VARCHAR(30) DEFAULT 'FULL' CHECK (administrator_access_level IN ('FULL', 'PARTIAL', 'READONLY'))
);

-- Номенклатура
CREATE TABLE nomenclature (
    nomenclature_id SERIAL PRIMARY KEY,
    article VARCHAR(50) UNIQUE NOT NULL,
    nomenclature_name VARCHAR(200) NOT NULL,
    nomenclature_category VARCHAR(50) NOT NULL CHECK (nomenclature_category IN ('skis', 'boots', 'poles', 'bindings', 'wax', 'accessories')),
    unit VARCHAR(20) NOT NULL DEFAULT 'pcs',
    standard_service_life INTEGER,
    min_stock_level INTEGER DEFAULT 0,
    manufacturer VARCHAR(100),
    nomenclature_created_at TIMESTAMP DEFAULT NOW()
);

-- Поставщики
CREATE TABLE supplier (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(200) NOT NULL,
    inn VARCHAR(12) UNIQUE NOT NULL,
    kpp VARCHAR(9),
    legal_address TEXT,
    contact_person VARCHAR(200),
    supplier_phone VARCHAR(20),
    supplier_email VARCHAR(100),
    rating DECIMAL(3,2) DEFAULT 0 CHECK (rating BETWEEN 0 AND 5),
    supplier_created_at TIMESTAMP DEFAULT NOW()
);

-- Заявки на инвентарь
CREATE TABLE purchase_request (
    purchase_request_id SERIAL PRIMARY KEY,
    purchase_request_number VARCHAR(50) UNIQUE NOT NULL,
    purchase_request_created_date TIMESTAMP DEFAULT NOW(),
    purchase_request_status VARCHAR(30) NOT NULL DEFAULT 'DRAFT' CHECK (purchase_request_status IN ('DRAFT', 'ON_APPROVAL', 'APPROVED', 'REJECTED')),
    author_id INTEGER NOT NULL REFERENCES "user"(user_id),
    approved_by INTEGER REFERENCES "user"(user_id),
    planned_amount DECIMAL(14,2),
    purchase_request_comment TEXT,
    purchase_request_created_at TIMESTAMP DEFAULT NOW(),
    purchase_request_updated_at TIMESTAMP DEFAULT NOW()
);

-- Позиции заявок
CREATE TABLE purchase_request_item (
    purchase_request_item_id SERIAL PRIMARY KEY,
    purchase_request_id INTEGER NOT NULL REFERENCES purchase_request(purchase_request_id) ON DELETE CASCADE,
    nomenclature_id INTEGER NOT NULL REFERENCES nomenclature(nomenclature_id) ON DELETE RESTRICT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    expected_price DECIMAL(12,2),
    priority VARCHAR(20) DEFAULT 'MEDIUM' CHECK (priority IN ('HIGH', 'MEDIUM', 'LOW'))
);

-- Заказы поставщикам
CREATE TABLE purchase_order (
    purchase_order_id SERIAL PRIMARY KEY,
    purchase_order_number VARCHAR(50) UNIQUE NOT NULL,
    purchase_order_created_date DATE DEFAULT CURRENT_DATE,
    purchase_order_status VARCHAR(30) NOT NULL DEFAULT 'DRAFT' CHECK (purchase_order_status IN ('DRAFT', 'SENT', 'IN_TRANSIT', 'DELIVERED', 'CLOSED')),
    supplier_id INTEGER NOT NULL REFERENCES supplier(supplier_id),
    purchase_manager_id INTEGER NOT NULL REFERENCES purchase_manager(purchase_manager_id),
    total_amount DECIMAL(14,2),
    expected_delivery_date DATE,
    purchase_order_created_at TIMESTAMP DEFAULT NOW()
);

-- Единицы инвентаря
CREATE TABLE inventory_item (
    inventory_item_id SERIAL PRIMARY KEY,
    barcode VARCHAR(50) UNIQUE NOT NULL,
    nomenclature_id INTEGER NOT NULL REFERENCES nomenclature(nomenclature_id) ON DELETE RESTRICT,
    serial_number VARCHAR(100),
    inventory_status VARCHAR(30) NOT NULL DEFAULT 'AVAILABLE' CHECK (inventory_status IN ('AVAILABLE', 'RESERVED', 'ISSUED', 'UNDER_REPAIR', 'DEFECTIVE', 'WRITTEN_OFF')),
    warehouse_id INTEGER REFERENCES warehouse(warehouse_id) ON DELETE SET NULL,
    receipt_date DATE,
    write_off_date DATE,
    purchase_cost DECIMAL(12,2),
    size VARCHAR(20),
    athlete_id INTEGER REFERENCES athlete(athlete_id) ON DELETE SET NULL,
    inventory_notes TEXT,
    inventory_created_at TIMESTAMP DEFAULT NOW()
);

-- Приходные накладные
CREATE TABLE receipt_invoice (
    receipt_invoice_id SERIAL PRIMARY KEY,
    receipt_invoice_number VARCHAR(50) UNIQUE NOT NULL,
    receipt_invoice_date DATE DEFAULT CURRENT_DATE,
    purchase_order_id INTEGER REFERENCES purchase_order(purchase_order_id) ON DELETE SET NULL,
    storekeeper_id INTEGER NOT NULL REFERENCES storekeeper(storekeeper_id),
    receipt_invoice_status VARCHAR(30) DEFAULT 'POSTED' CHECK (receipt_invoice_status IN ('DRAFT', 'POSTED', 'CANCELLED')),
    actual_amount DECIMAL(14,2),
    receipt_invoice_created_at TIMESTAMP DEFAULT NOW()
);

-- Документы выдачи
CREATE TABLE issuance_document (
    issuance_document_id SERIAL PRIMARY KEY,
    inventory_item_id INTEGER NOT NULL REFERENCES inventory_item(inventory_item_id) ON DELETE RESTRICT,
    athlete_id INTEGER NOT NULL REFERENCES athlete(athlete_id) ON DELETE RESTRICT,
    storekeeper_id INTEGER NOT NULL REFERENCES storekeeper(storekeeper_id),
    issuance_date DATE NOT NULL,
    planned_return_date DATE,
    actual_return_date DATE,
    issuance_document_status VARCHAR(30) NOT NULL DEFAULT 'ACTIVE' CHECK (issuance_document_status IN ('ACTIVE', 'RETURNED', 'OVERDUE', 'EXTENDED')),
    condition_on_issue VARCHAR(50) DEFAULT 'NEW',
    condition_on_return VARCHAR(50),
    issuance_document_notes TEXT,
    issuance_document_created_at TIMESTAMP DEFAULT NOW()
);

-- Журнал операций (аудит)
CREATE TABLE operation_log (
    operation_log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES "user"(user_id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    details JSONB,
    ip_address INET,
    operation_log_created_at TIMESTAMP DEFAULT NOW()
);