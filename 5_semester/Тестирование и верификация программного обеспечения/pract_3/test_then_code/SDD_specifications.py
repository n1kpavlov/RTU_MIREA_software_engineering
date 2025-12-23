# Метаданные треков
TRACK_METADATA = [
    {
        "title": "Конь",
        "artist": "Любэ",
        "genre": "Фолк-рок",
        "year": 1994,
        "duration": 218
    },
    {
        "title": "А зори здесь тихие", 
        "artist": "Любэ",
        "genre": "Русская эстрада",
        "year": 2015,
        "duration": 214
    },
    {
        "title": "Кукла колдуна",
        "artist": "Король и Шут", 
        "genre": "Фолк-рок",
        "year": 1998,
        "duration": 203
    },
    {
        "title": "Кукла",
        "artist": "Иванушки International",
        "genre": "Поп", 
        "year": 1997,
        "duration": 314
    }
]

# Ожидаемые результаты поиска
SEARCH_RESULTS = [
    {
        "search_type": "by_title",
        "query": "Конь",
        "expected_titles": ["Конь"]
    },
    {
        "search_type": "by_title",
        "query": "Кукла", 
        "expected_titles": ["Кукла колдуна", "Кукла"]
    },
    {
        "search_type": "by_title",
        "query": "а зори здесь тихие",
        "expected_titles": ["А зори здесь тихие"]
    },
    {
        "search_type": "by_artist",
        "query": "Король и Шут",
        "expected_titles": ["Кукла колдуна"]
    },
    {
        "search_type": "by_artist", 
        "query": "Любэ",
        "expected_titles": ["Конь", "А зори здесь тихие"]
    },
    {
        "search_type": "by_genre",
        "query": "Поп",
        "expected_titles": ["Кукла"]
    },
    {
        "search_type": "by_genre",
        "query": "Фолк-рок", 
        "expected_titles": ["Конь", "Кукла колдуна"]
    }
]