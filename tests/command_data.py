from city_info.city import City

all_raw_lines = (
    'ID, City, Country,Population\n'
    '1. Tokyo, Japan - 32,450,000\n'
    '6. Jakarta. Indonesia - 18,900,000\n'
    '7. Sao Paulo; Brazil - 18,850,000\n'
    '14. Moscow, Russian Fed. - 15,000,000\n'
)

cities = [
    City(id=1, name='Tokyo', country='Japan', population=32450000),
    City(id=6, name='Jakarta.', country='Indonesia', population=18900000),
    City(id=7, name='Sao Paulo', country='Brazil', population=18850000),
    City(id=14, name='Moscow', country='Russian Fed.', population=15000000)
]
