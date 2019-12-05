"""
8-6. City Names: Write a function called city_country() that takes in the name of a city
and its country .The function should return a string formatted like this:
     "Santiago, Chile"
Call your function with at least three city-country pairs, and print the value that’s returned .
"""

def city_country(city,country):
    """Return City and country name  seperated by a comma"""
    city_country = city + ',' + country
    return city_country.title()

pair1 = city_country("santiago","chile")
print(pair1)
pair2 = city_country("new delhi","india")
print(pair2)
pair3 = city_country("koyoto","japan")
print(pair3)
