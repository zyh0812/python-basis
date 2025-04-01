from city_functions import country_city

def test_city_conuntry():
    city_country = country_city('santiago','chile')
    assert city_country == 'Santiago, Chile'

def test_city_country_population():
    city_country_population = country_city('santiago','chile','500000')
    assert city_country_population == 'Santiago, Chile-population 500000'