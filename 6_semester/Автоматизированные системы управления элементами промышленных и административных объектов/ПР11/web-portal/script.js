// ==================== ТАБЫ В РАЗДЕЛЕ "РЕЗУЛЬТАТЫ" ====================

function showResultTab(tabName, btn) {
  document
    .querySelectorAll(".tab-btn")
    .forEach((b) => b.classList.remove("active"));
  document
    .querySelectorAll(".tab-content")
    .forEach((t) => t.classList.remove("active"));
  btn.classList.add("active");
  document.getElementById("tab-" + tabName).classList.add("active");
}

// ==================== СЛАЙДЕР ОТЗЫВОВ ====================

let slideIndex = 0;
let slideInterval;

function currentSlide(n) {
  slideIndex = n;
  updateSlider();
  resetAutoSlide();
}

function updateSlider() {
  document.querySelectorAll(".slide").forEach((slide, i) => {
    slide.classList.toggle("active", i === slideIndex);
  });
  document.querySelectorAll(".dot").forEach((dot, i) => {
    dot.classList.toggle("active", i === slideIndex);
  });
}

function autoSlide() {
  const totalSlides = document.querySelectorAll(".slide").length;
  slideIndex = (slideIndex + 1) % totalSlides;
  updateSlider();
}

function resetAutoSlide() {
  clearInterval(slideInterval);
  slideInterval = setInterval(autoSlide, 5000);
}

slideInterval = setInterval(autoSlide, 5000);

// ==================== ДАННЫЕ ДЛЯ ТАБЛИЦ ====================

const inventoryData = [
  {
    barcode: "SKI001-2024-001",
    name: "Лыжи Fischer Speedmax",
    category: "Лыжи",
    size: "190",
    status: "available",
  },
  {
    barcode: "SKI001-2024-003",
    name: "Лыжи Fischer Speedmax",
    category: "Лыжи",
    size: "200",
    status: "available",
  },
  {
    barcode: "SKI002-2024-001",
    name: "Лыжи Madshus Redline",
    category: "Лыжи",
    size: "192",
    status: "available",
  },
  {
    barcode: "BOOT001-2024-001",
    name: "Ботинки Salomon S/Lab",
    category: "Ботинки",
    size: "42",
    status: "available",
  },
  {
    barcode: "BOOT001-2024-003",
    name: "Ботинки Salomon S/Lab",
    category: "Ботинки",
    size: "44",
    status: "available",
  },
  {
    barcode: "POLE001-2024-001",
    name: "Палки Swix Triac",
    category: "Палки",
    size: "155",
    status: "available",
  },
  {
    barcode: "WAX001-2024-001",
    name: "Парафин Swix LF4",
    category: "Смазки",
    size: "—",
    status: "available",
  },
  {
    barcode: "WAX002-2024-001",
    name: "Парафин Swix HF6",
    category: "Смазки",
    size: "—",
    status: "available",
  },
];

const issuanceData = [
  {
    athlete: "Иванов Иван",
    item: "Лыжи Fischer Speedmax (195)",
    date: "01.12.2024",
    return: "30.03.2025",
    status: "active",
  },
  {
    athlete: "Петров Пётр",
    item: "Лыжи Fischer Speedmax (198)",
    date: "05.12.2024",
    return: "30.03.2025",
    status: "active",
  },
  {
    athlete: "Смирнова Анна",
    item: "Лыжи Madshus Redline (198)",
    date: "10.12.2024",
    return: "30.03.2025",
    status: "active",
  },
  {
    athlete: "Кузнецов Дмитрий",
    item: "Ботинки Salomon S/Lab (41)",
    date: "15.12.2024",
    return: "30.03.2025",
    status: "active",
  },
  {
    athlete: "Сидоров Сидор",
    item: "Лыжи Fischer Speedmax (200)",
    date: "01.10.2024",
    return: "01.11.2024",
    status: "overdue",
  },
];

const statusLabels = {
  available: "Доступен",
  active: "Активна",
  overdue: "Просрочена",
};

const statusClasses = {
  available: "status-available",
  active: "status-issued",
  overdue: "status-overdue",
};

function loadResultTables() {
  document.getElementById("result-inventory-tbody").innerHTML = inventoryData
    .map(
      (item) => `
        <tr>
            <td>${item.barcode}</td>
            <td>${item.name}</td>
            <td>${item.category}</td>
            <td>${item.size}</td>
            <td class="${statusClasses[item.status]}">${statusLabels[item.status]}</td>
        </tr>
    `,
    )
    .join("");

  document.getElementById("result-issuance-tbody").innerHTML = issuanceData
    .map(
      (item) => `
        <tr>
            <td>${item.athlete}</td>
            <td>${item.item}</td>
            <td>${item.date}</td>
            <td>${item.return}</td>
            <td class="${statusClasses[item.status]}">${statusLabels[item.status]}</td>
        </tr>
    `,
    )
    .join("");
}

document.addEventListener("DOMContentLoaded", loadResultTables);
