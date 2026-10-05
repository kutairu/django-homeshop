# Уютный дом - интернет-магазин товаров для дома

Учебный проект на Django: три страницы (главная, каталог, «О нас»), общие header и footer,
навигация между страницами и фильтр каталога по категориям.

## Структура

```
homeshop/          — настройки проекта и главный urls.py
shop/              — приложение магазина
├── urls.py        — маршруты: /, /catalog/, /about/
├── views.py       — отображения страниц и список товаров
├── templates/shop — base.html (header, footer) и шаблоны страниц
└── static/shop    — стили
```

## Запуск

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Сайт откроется по адресу http://127.0.0.1:8000/
