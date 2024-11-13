
countries_and_capitals = {
    "Afghanistan": "Kabul",
    "Australia": "Cococ",
    "Brazil": "amazon",
    "Canada": "soco",
    "China": "Beijing",
    "Egypt": "Cairo",
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "United Kingdom": "London",
    "United States": "Washington"
}

print(countries_and_capitals)


print("................................................")
def add_country_capital(country, capital):
    
    if country in countries_and_capitals:
        print(f"The country '{country}' already exists with capital '{countries_and_capitals[country]}'.")
    else:
        countries_and_capitals[country] = capital
        print(f"Added: {country} - {capital}")


add_country_capital("Italy", "Rome")
add_country_capital("India", "Delhi")



print("................................................")
def search_capital(country):
   
    capital = countries_and_capitals.get(country)
    if capital:
        return f"The capital of {country} is {capital}."
    else:
        return f"Country '{country}' not found."


print(search_capital("India"))  #  The capital of India is New Delhi.
print(search_capital("Italy"))  #  Country 'Italy' not found.



print("................................................")
def display_countries_and_capitals():

    for country in sorted(countries_and_capitals.keys()):
        print(f"{country}: {countries_and_capitals[country]}")


display_countries_and_capitals()


print("................................................")
def update_capital(country, new_capital):
    
    if country in countries_and_capitals:
        countries_and_capitals[country] = new_capital
        print(f"Updated: The capital of {country} is now {new_capital}.")
        countries_and_capitals.update()
    else:
        print(f"Country '{country}' not found.")


update_capital("India", "Delhi")  
update_capital("Egypt", "jyro")  

print(countries_and_capitals)