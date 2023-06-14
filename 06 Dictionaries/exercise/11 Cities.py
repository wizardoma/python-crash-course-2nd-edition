# Make a dictionary called cities. Use the names of three cities as keys in your
# dictionary. Create a dictionary of information about each city and include the country that the
# city is in, its approximate population, and one fact about that city. The keys for each city’s
# dictionary should be something like country, population, and fact. Print the name of each
# city and all of the information you have stored about it.

cities = {
    "lagos": {
        "population": "15 million",
        "country": "Nigeria",
        "fact": "Lagos was the former capital of Nigeria and the most populous city in west africa"
    },

      "abuja": {
        "population": "4 million",
        "country": "Nigeria",
        "fact": "Abuja is the capital of Nigeria"
    },

      "new york city": {
        "population": "10 million",
        "country": "USA",
        "fact": "This is the city that has the costliest accomodation in the United States of America"
    },
}


for city, details in cities.items():
    print(f"Let's talk about {city}")
    print(f"{city} is a city in {details['country']}, it has a population of {details['population']}. This is a fact about it \n {details['fact']}")