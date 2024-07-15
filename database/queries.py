class Queries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone_number TEXT,
        visit_date INTEGER,
        food_rating TEXT,
        cleanliness_rating INTEGER,
        extra_comments TEXT
    )
    """
