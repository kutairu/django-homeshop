// Скрипты магазина «Уютный дом»: корзина, всплывающие сообщения и кнопка «Наверх».
// Подключается в base.html атрибутом defer, поэтому выполняется после загрузки разметки.

const CART_KEY = 'homeshop-cart';

// Корзина хранится в localStorage браузера, чтобы не обнуляться при переходе между страницами.
// Формат: { "Название товара": количество }
function loadCart() {
    try {
        return JSON.parse(localStorage.getItem(CART_KEY)) || {};
    } catch {
        return {};
    }
}

function saveCart(cart) {
    try {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
    } catch {
        // браузер запретил хранение — корзина проживёт до перехода на другую страницу
    }
}

function cartTotal(cart) {
    return Object.values(cart).reduce((sum, count) => sum + count, 0);
}

// Обновляет число на значке корзины в шапке
function updateCartCount() {
    const counter = document.getElementById('cart-count');
    if (counter) {
        counter.textContent = cartTotal(loadCart());
    }
}

// Всплывающее сообщение внизу экрана
let toastTimer;
function showToast(message) {
    const toast = document.getElementById('toast');
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('toast--visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('toast--visible'), 2200);
}

// Кнопки «В корзину» на карточках товаров
function initCartButtons() {
    document.querySelectorAll('.js-add-to-cart').forEach((button) => {
        button.addEventListener('click', () => {
            const name = button.dataset.name;
            const cart = loadCart();
            cart[name] = (cart[name] || 0) + 1;
            saveCart(cart);
            updateCartCount();
            showToast(`Добавлено в корзину: ${name}`);

            // кнопка на секунду показывает, что товар добавлен
            button.textContent = 'Добавлено ✓';
            button.classList.add('btn--done');
            setTimeout(() => {
                button.textContent = 'В корзину';
                button.classList.remove('btn--done');
            }, 1200);
        });
    });
}

// Кнопка «Наверх» появляется после прокрутки на 400 пикселей
function initToTop() {
    const button = document.getElementById('to-top');
    if (!button) return;
    window.addEventListener('scroll', () => {
        button.classList.toggle('to-top--visible', window.scrollY > 400);
    });
    button.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

updateCartCount();
initCartButtons();
initToTop();
