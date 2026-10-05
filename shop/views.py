from django.shortcuts import render

# Пока у магазина нет базы данных, товары хранятся в списке.
# Каждый товар: название, категория, цена, значок для карточки и короткое описание.
PRODUCTS = [
    {'name': 'Плед из хлопка «Утро»', 'category': 'Текстиль', 'price': 2490, 'icon': '🧶',
     'text': 'Мягкий плед 150×200 см, стирается в машинке.'},
    {'name': 'Набор полотенец «Лён»', 'category': 'Текстиль', 'price': 1890, 'icon': '🧺',
     'text': 'Три полотенца разного размера из льна и хлопка.'},
    {'name': 'Подушка декоративная', 'category': 'Текстиль', 'price': 990, 'icon': '🛋️',
     'text': 'Чехол на молнии, наполнитель — гипоаллергенное волокно.'},
    {'name': 'Сковорода с антипригарным покрытием', 'category': 'Кухня', 'price': 3290, 'icon': '🍳',
     'text': 'Диаметр 28 см, подходит для индукционных плит.'},
    {'name': 'Набор ножей «Шеф»', 'category': 'Кухня', 'price': 4590, 'icon': '🔪',
     'text': 'Пять ножей из нержавеющей стали и деревянная подставка.'},
    {'name': 'Заварочный чайник', 'category': 'Кухня', 'price': 1290, 'icon': '🫖',
     'text': 'Жаропрочное стекло, объём 1 литр, ситечко в комплекте.'},
    {'name': 'Ваза из керамики', 'category': 'Декор', 'price': 1590, 'icon': '🏺',
     'text': 'Матовая глазурь, высота 25 см.'},
    {'name': 'Ароматическая свеча «Хвоя»', 'category': 'Декор', 'price': 790, 'icon': '🕯️',
     'text': 'Соевый воск, горит около 40 часов.'},
    {'name': 'Настенные часы', 'category': 'Декор', 'price': 2190, 'icon': '🕰️',
     'text': 'Бесшумный механизм, диаметр 30 см.'},
    {'name': 'Корзина для хранения', 'category': 'Хранение', 'price': 1190, 'icon': '🧺',
     'text': 'Плетёная корзина из джута с ручками.'},
    {'name': 'Органайзер для ящика', 'category': 'Хранение', 'price': 690, 'icon': '🗃️',
     'text': 'Шесть отделений для мелочей и столовых приборов.'},
    {'name': 'Настольная лампа', 'category': 'Освещение', 'price': 2890, 'icon': '💡',
     'text': 'Тёплый свет, регулировка яркости касанием.'},
    {'name': 'Гирлянда «Огоньки»', 'category': 'Освещение', 'price': 890, 'icon': '✨',
     'text': 'Пять метров, 50 тёплых светодиодов, работает от USB.'},
]

CATEGORIES = ['Текстиль', 'Кухня', 'Декор', 'Хранение', 'Освещение']


def index(request):
    """Главная страница: приветственный блок, категории и популярные товары."""
    context = {
        'categories': CATEGORIES,
        'popular': PRODUCTS[:4],
    }
    return render(request, 'shop/index.html', context)


def catalog(request):
    """Каталог: все товары или товары одной категории (?category=Кухня)."""
    current = request.GET.get('category', '')
    if current in CATEGORIES:
        products = [p for p in PRODUCTS if p['category'] == current]
    else:
        current = ''
        products = PRODUCTS
    context = {
        'categories': CATEGORIES,
        'current': current,
        'products': products,
    }
    return render(request, 'shop/catalog.html', context)


def about(request):
    """Страница «О нас»."""
    return render(request, 'shop/about.html')
