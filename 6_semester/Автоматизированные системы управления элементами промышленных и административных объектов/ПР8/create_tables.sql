-- Базовая таблица пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(200) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    login VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(30) NOT NULL CHECK (role IN ('athlete', 'coach', 'storekeeper', 'purchase_manager', 'manager', 'accountant', 'administrator')),
    registration_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Справочник складов
CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    type VARCHAR(50) CHECK (type IN ('main', 'reserve', 'service'))
);

-- Тренеры
CREATE TABLE coaches (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    specialization VARCHAR(100),
    category VARCHAR(50)
);

-- Группы спортсменов
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    coach_id INTEGER REFERENCES coaches(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Спортсмены
CREATE TABLE athletes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    sports_category VARCHAR(50),
    birth_year INTEGER,
    group_id INTEGER REFERENCES groups(id) ON DELETE SET NULL,
    coach_id INTEGER REFERENCES coaches(id) ON DELETE SET NULL,
    has_active_debt BOOLEAN DEFAULT FALSE
);

-- Кладовщики
CREATE TABLE storekeepers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    warehouse_id INTEGER REFERENCES warehouses(id) ON DELETE SET NULL,
    certificate_number VARCHAR(50)
);

-- Менеджеры по закупкам
CREATE TABLE purchase_managers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    department VARCHAR(100)
);

-- Руководители
CREATE TABLE managers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    position VARCHAR(100),
    access_level INTEGER DEFAULT 1 CHECK (access_level BETWEEN 1 AND 3)
);

-- Бухгалтеры
CREATE TABLE accountants (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    section VARCHAR(100)
);

-- Администраторы
CREATE TABLE administrators (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    access_level VARCHAR(30) DEFAULT 'FULL' CHECK (access_level IN ('FULL', 'PARTIAL', 'READONLY'))
);

-- Номенклатура
CREATE TABLE nomenclature (
    id SERIAL PRIMARY KEY,
    article VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL CHECK (category IN ('skis', 'boots', 'poles', 'bindings', 'wax', 'accessories')),
    unit VARCHAR(20) NOT NULL DEFAULT 'pcs',
    standard_service_life INTEGER,
    min_stock_level INTEGER DEFAULT 0,
    manufacturer VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Поставщики
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    inn VARCHAR(12) UNIQUE NOT NULL,
    kpp VARCHAR(9),
    legal_address TEXT,
    contact_person VARCHAR(200),
    phone VARCHAR(20),
    email VARCHAR(100),
    rating DECIMAL(3,2) DEFAULT 0 CHECK (rating BETWEEN 0 AND 5),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Заявки на инвентарь
CREATE TABLE purchase_requests (
    id SERIAL PRIMARY KEY,
    number VARCHAR(50) UNIQUE NOT NULL,
    created_date TIMESTAMP DEFAULT NOW(),
    status VARCHAR(30) NOT NULL DEFAULT 'DRAFT' CHECK (status IN ('DRAFT', 'ON_APPROVAL', 'APPROVED', 'REJECTED')),
    author_id INTEGER NOT NULL REFERENCES users(id),
    approved_by INTEGER REFERENCES users(id),
    planned_amount DECIMAL(14,2),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Позиции заявок
CREATE TABLE purchase_request_items (
    id SERIAL PRIMARY KEY,
    request_id INTEGER NOT NULL REFERENCES purchase_requests(id) ON DELETE CASCADE,
    nomenclature_id INTEGER NOT NULL REFERENCES nomenclature(id) ON DELETE RESTRICT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    expected_price DECIMAL(12,2),
    priority VARCHAR(20) DEFAULT 'MEDIUM' CHECK (priority IN ('HIGH', 'MEDIUM', 'LOW'))
);

-- Заказы поставщикам
CREATE TABLE purchase_orders (
    id SERIAL PRIMARY KEY,
    number VARCHAR(50) UNIQUE NOT NULL,
    created_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(30) NOT NULL DEFAULT 'DRAFT' CHECK (status IN ('DRAFT', 'SENT', 'IN_TRANSIT', 'DELIVERED', 'CLOSED')),
    supplier_id INTEGER NOT NULL REFERENCES suppliers(id),
    manager_id INTEGER NOT NULL REFERENCES purchase_managers(id),
    total_amount DECIMAL(14,2),
    expected_delivery_date DATE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Единицы инвентаря
CREATE TABLE inventory_items (
    id SERIAL PRIMARY KEY,
    barcode VARCHAR(50) UNIQUE NOT NULL,
    nomenclature_id INTEGER NOT NULL REFERENCES nomenclature(id) ON DELETE RESTRICT,
    serial_number VARCHAR(100),
    status VARCHAR(30) NOT NULL DEFAULT 'AVAILABLE' CHECK (status IN ('AVAILABLE', 'RESERVED', 'ISSUED', 'UNDER_REPAIR', 'DEFECTIVE', 'WRITTEN_OFF')),
    warehouse_id INTEGER REFERENCES warehouses(id) ON DELETE SET NULL,
    receipt_date DATE,
    write_off_date DATE,
    purchase_cost DECIMAL(12,2),
    size VARCHAR(20),
    current_holder_id INTEGER REFERENCES athletes(id) ON DELETE SET NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Приходные накладные
CREATE TABLE receipt_invoices (
    id SERIAL PRIMARY KEY,
    number VARCHAR(50) UNIQUE NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    order_id INTEGER REFERENCES purchase_orders(id) ON DELETE SET NULL,
    storekeeper_id INTEGER NOT NULL REFERENCES storekeepers(id),
    status VARCHAR(30) DEFAULT 'POSTED' CHECK (status IN ('DRAFT', 'POSTED', 'CANCELLED')),
    actual_amount DECIMAL(14,2),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Документы выдачи
CREATE TABLE issuance_documents (
    id SERIAL PRIMARY KEY,
    inventory_item_id INTEGER NOT NULL REFERENCES inventory_items(id) ON DELETE RESTRICT,
    athlete_id INTEGER NOT NULL REFERENCES athletes(id) ON DELETE RESTRICT,
    storekeeper_id INTEGER NOT NULL REFERENCES storekeepers(id),
    issuance_date DATE NOT NULL,
    planned_return_date DATE,
    actual_return_date DATE,
    status VARCHAR(30) NOT NULL DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'RETURNED', 'OVERDUE', 'EXTENDED')),
    condition_on_issue VARCHAR(50) DEFAULT 'NEW',
    condition_on_return VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Журнал операций (аудит)
CREATE TABLE operation_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    details JSONB,
    ip_address INET,
    created_at TIMESTAMP DEFAULT NOW()
)