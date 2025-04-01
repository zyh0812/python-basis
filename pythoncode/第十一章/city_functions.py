def country_city(city,country,population=''):
    if population:
        return f"{city.title()}, {country.title()}-population {population}"
    else:
        return f"{city.title()}, {country.title()}"