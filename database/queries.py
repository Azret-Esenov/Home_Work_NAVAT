class Queries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone_number TEXT,
        visit_date DATE,
        food_rating INTEGER,
        cleanliness_rating INTEGER,
        extra_comments TEXT
    )
    """

    DROP_CATEGORIES_OF_DISHES = "DROP TABLE IF EXISTS categories_of_dishes"

    CREATE_CATEGORIES_OF_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS categories_of_dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """

    POPULATE_CATEGORIES_OF_DISHES = """
    INSERT INTO categories_of_dishes(name) VALUES 
    ('Плов'),
    ('Лагман'),
    ('Манты'),
    ('Бешбармак'),
    ('Чебуреки'),
    ('Баурсаки'),
    ('Чай'),
    ('Коктейли'),
    ('Салаты'),
    ('Десерты')
    """

    DROP_DISHES = "DROP TABLE IF EXISTS dishes"

    CREATE_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gram TEXT,
        price INTEGER,
        cover TEXT,
        dishes_id INTEGER,
        FOREIGN KEY(dishes_id) REFERENCES dishes(id)
    )
    """

    POPULATE_DISHES = """
    INSERT INTO dishes(name, gram, price, cover, dishes_id) VALUES
    ('Узбекский плов', '300 гр', 280, 'images/pilaf.jpg', 1),
    ('Азербайджанский плов','280 гр', 260, 'images/pilaf.jpg', 1),
    ('Классический лагман', '250 гр', 250, 'images/Lagman.jpg', 2),
    ('Лагман по-уйгурски', '260 гр', 260, 'images/Lagman.jpg', 2),
    ('Манты по-узбекски', '280 гр', 300, 'images/manti.jpg', 3),
    ('Манты с тыквой и мясом в мультиварке', '290 гр', 320, 'images/manti.jpg', 3),
    ('Классический бешбармак', '310 гр', 340, 'images/beshbarmak.jpg', 4),
    ('Бешбармак с курицей', '310 гр', 310, 'images/beshbarmak.jpg', 4),
    ('Чебуреки с мясным фаршем и луком', '80 гр', 90, 'images/cheburek.jpg', 5),
    ('Чебуреки с курицей', '70 гр', 80, 'images/cheburek.jpg', 5),
    ('Пышные баурсаки по-казахски', '100 гр', 90, 'images/baursaki.jpg', 6),
    ('Баурсаки на кефире без дрожжей', '100 гр', 90, 'images/baursaki.jpg', 6),
    ('Черный чай', '50 гр', 40, 'images/tea.jpg', 7),
    ('Зеленый чай', '50 гр', 50, 'images/tea.jpg', 7),
    ('Мохито', '30 гр', 150, 'images/koktel.jpg', 8),
    ('Космополитен', '40 гр', 170, 'images/koktel.jpg', 8),
    ('Салат Цезарь с курицей', '150 гр', 180, 'images/salat.jpg', 9),
    ('Салат Оливье', '200 гр', 200, 'images/salat.jpg', 9),
    ('Шоколадно-сметанный мусс', '110 гр', 210, 'images/desert.jpg', 10),
    ('Шоколадные маффины Брауни', '90 гр', 100, 'images/desert.jpg', 10)
    """