const API = 'http://localhost:8000';
let searchTimeout;

// ==================== НАВИГАЦИЯ ====================

function showTab(name) {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('nav button').forEach(b => b.classList.remove('active'));
    document.getElementById('tab-' + name).classList.add('active');
    event.target.classList.add('active');

    const loaders = {
        dashboard: loadDashboard,
        athletes: loadAthletes,
        issuances: loadIssuances,
        inventory: loadInventory,
        statistics: loadStatistics,
    };
    if (loaders[name]) loaders[name]();
}

// ==================== ТОСТЫ ====================

function showToast(message, type) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast ${type}`;
    setTimeout(() => toast.className = 'toast hidden', 3000);
}

// ==================== ДАШБОРД ====================

async function loadDashboard() {
    const res = await fetch(`${API}/api/dashboard`);
    const d = await res.json();

    // KPI
    const kpiValues = [d.athletes_count, d.available_items, d.active_issuances, d.overdue_count, d.debtors];
    document.querySelectorAll('.kpi-value').forEach((el, i) => {
        el.textContent = kpiValues[i] ?? '—';
        el.classList.remove('skeleton');
    });

    // Категории
    const maxCat = Math.max(...d.categories.map(c => c.count), 1);
    document.getElementById('category-chart').innerHTML = d.categories.map(c => `
        <div class="chart-row">
            <span class="chart-label">${c.category}</span>
            <div class="chart-bar-wrapper">
                <div class="chart-bar" style="width:${(c.count / maxCat * 100).toFixed(0)}%"></div>
            </div>
            <span class="chart-value">${c.count}</span>
        </div>
    `).join('');

    // Последние выдачи
    document.getElementById('recent-issuances-tbody').innerHTML = d.recent_issuances.map(r => `
        <tr class="${r.effective_status === 'OVERDUE' ? 'row-danger' : ''}">
            <td>${r.athlete_name}</td>
            <td>${r.product_name}</td>
            <td>${r.issuance_date}</td>
            <td>${r.planned_return_date || '—'}</td>
            <td><span class="badge badge-${r.effective_status.toLowerCase()}">${r.effective_status}</span></td>
        </tr>
    `).join('');

    // Топ-должники
    document.getElementById('top-debtors-tbody').innerHTML = d.top_debtors.map(t => `
        <tr class="row-danger">
            <td>${t.athlete_name}</td>
            <td>${t.sports_category || '—'}</td>
            <td>${t.overdue_items}</td>
            <td>${t.max_days} дн.</td>
        </tr>
    `).join('');
}

// ==================== СПОРТСМЕНЫ ====================

function debounceSearch() {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(loadAthletes, 300);
}

async function loadAthletes() {
    const search = document.getElementById('athlete-search').value;
    const debt = document.getElementById('debt-filter').value;
    const res = await fetch(`${API}/api/athletes?search=${search}&has_debt=${debt}`);
    const data = await res.json();
    document.getElementById('athletes-tbody').innerHTML = data.map(a => `
        <tr class="${a.has_active_debt ? 'row-warning' : ''}">
            <td><strong>${a.full_name}</strong></td>
            <td>${a.sports_category || '—'}</td>
            <td>${a.birth_year || '—'}</td>
            <td>${a.group_name || '—'}</td>
            <td>${a.coach_name || '—'}</td>
            <td>${a.active_items}</td>
            <td>${a.has_active_debt ? '⚠️' : '✅'}</td>
            <td><button class="btn-sm" onclick="viewAthlete(${a.athlete_id})">👁️</button></td>
        </tr>
    `).join('');
}

async function viewAthlete(id) {
    const res = await fetch(`${API}/api/athletes/${id}`);
    if (!res.ok) return showToast('Спортсмен не найден', 'error');
    const a = await res.json();
    document.getElementById('athlete-modal').classList.remove('hidden');
    document.getElementById('athlete-detail').innerHTML = `
        <h3>${a.full_name}</h3>
        <div class="detail-grid">
            <div class="detail-item"><span class="detail-label">Email</span><span>${a.email || '—'}</span></div>
            <div class="detail-item"><span class="detail-label">Телефон</span><span>${a.phone || '—'}</span></div>
            <div class="detail-item"><span class="detail-label">Разряд</span><span>${a.sports_category || '—'}</span></div>
            <div class="detail-item"><span class="detail-label">Год рождения</span><span>${a.birth_year || '—'}</span></div>
            <div class="detail-item"><span class="detail-label">Группа</span><span>${a.group_name || '—'}</span></div>
            <div class="detail-item"><span class="detail-label">Тренер</span><span>${a.coach_name || '—'}</span></div>
            <div class="detail-item"><span class="detail-label">Активных выдач</span><span>${a.active_items}</span></div>
            <div class="detail-item"><span class="detail-label">Возвращено</span><span>${a.returned_items}</span></div>
            <div class="detail-item"><span class="detail-label">Статус</span><span class="${a.has_active_debt ? 'text-danger' : 'text-success'}">${a.has_active_debt ? '⚠️ Должник' : '✅ Без долгов'}</span></div>
        </div>
    `;
}

function closeAthleteModal() {
    document.getElementById('athlete-modal').classList.add('hidden');
}

// ==================== ВЫДАЧИ ====================

async function loadIssuances() {
    const filter = document.getElementById('issuance-filter').value;
    const res = await fetch(`${API}/api/issuance/active?filter_status=${filter}`);
    const data = await res.json();
    document.getElementById('issuances-tbody').innerHTML = data.map(d => `
        <tr class="${d.effective_status === 'OVERDUE' ? 'row-danger' : ''}">
            <td><strong>${d.athlete_name}</strong></td>
            <td>${d.product_name}</td>
            <td>${d.size || '—'}</td>
            <td>${d.issuance_date}</td>
            <td>${d.planned_return_date || '—'}</td>
            <td><span class="badge badge-${d.effective_status.toLowerCase()}">${d.effective_status === 'OVERDUE' ? `Просрочено (${d.days_overdue}д)` : 'Активна'}</span></td>
            <td><button class="btn-sm btn-return" onclick="returnInventory(${d.issuance_document_id})">↩</button></td>
        </tr>
    `).join('');
}

async function openIssueModal() {
    document.getElementById('issue-modal').classList.remove('hidden');
    const res = await fetch(`${API}/api/athletes`);
    const data = await res.json();
    document.getElementById('issue-athlete').innerHTML = '<option value="">— Выберите —</option>' +
        data.map(a => `<option value="${a.athlete_id}">${a.full_name} ${a.has_active_debt ? '⚠️' : ''}</option>`).join('');
    document.getElementById('issue-inventory').innerHTML = '<option value="">— Сначала выберите спортсмена —</option>';
}

function closeIssueModal() {
    document.getElementById('issue-modal').classList.add('hidden');
}

document.getElementById('issue-athlete').addEventListener('change', async function () {
    const res = await fetch(`${API}/api/inventory/available`);
    const data = await res.json();
    document.getElementById('issue-inventory').innerHTML = '<option value="">— Выберите —</option>' +
        data.map(i => `<option value="${i.inventory_item_id}">${i.barcode} — ${i.nomenclature_name} (${i.size || 'б/р'})</option>`).join('');
});

async function issueInventory() {
    const res = await fetch(`${API}/api/issuance/issue`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            athlete_id: parseInt(document.getElementById('issue-athlete').value),
            inventory_item_id: parseInt(document.getElementById('issue-inventory').value),
            planned_return_date: document.getElementById('issue-return-date').value,
        }),
    });
    const data = await res.json();
    showToast(data.message, data.status);
    if (data.status === 'success') {
        closeIssueModal();
        loadDashboard();
        loadAthletes();
        loadIssuances();
        loadInventory();
    }
}

async function returnInventory(id) {
    const res = await fetch(`${API}/api/issuance/return`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ issuance_id: id }),
    });
    const data = await res.json();
    showToast(data.message, data.status);
    loadDashboard();
    loadIssuances();
    loadInventory();
    loadAthletes();
}

// ==================== СКЛАД ====================

async function loadInventory() {
    const res = await fetch(`${API}/api/inventory/available`);
    const data = await res.json();
    document.getElementById('inventory-tbody').innerHTML = data.map(i => `
        <tr>
            <td>${i.barcode}</td>
            <td>${i.nomenclature_name}</td>
            <td>${i.nomenclature_category}</td>
            <td>${i.size || '—'}</td>
        </tr>
    `).join('');
}

// ==================== СТАТИСТИКА ====================

async function loadStatistics() {
    const res = await fetch(`${API}/api/inventory/statistics`);
    const data = await res.json();
    document.getElementById('stats-container').innerHTML = data.map(s => `
        <div class="stat-card">
            <h3>${s.nomenclature_category}</h3>
            <div class="stat-row">
                <span>Доступно:</span><span class="stat-available">${s.available}</span>
            </div>
            <div class="stat-row">
                <span>Выдано:</span><span class="stat-issued">${s.issued}</span>
            </div>
            <div class="stat-row">
                <span>Проблемы:</span><span class="stat-problems">${s.problems}</span>
            </div>
            <div class="stat-bar">
                <div class="stat-bar-available" style="width:${(s.available / s.total * 100).toFixed(0)}%"></div>
                <div class="stat-bar-issued" style="width:${(s.issued / s.total * 100).toFixed(0)}%"></div>
                <div class="stat-bar-problems" style="width:${(s.problems / s.total * 100).toFixed(0)}%"></div>
            </div>
        </div>
    `).join('');
}

// ==================== ИНИЦИАЛИЗАЦИЯ ====================

loadDashboard();