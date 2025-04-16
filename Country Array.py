country_list = ['unitedstates', 'russia', 'china', 'australia', 'netherlands']
cities_list = ['Boston', 'Moscow', 'Beijing', 'Sydney', 'Amsterdam']
population_numbers = ['530000', '800000', '1000000', '600000', '700000']

print("Every countries major city and respective population:")

for i in range(len(country_list)):
    print(f"Country: {country_list[i]} City: {cities_list[i]} Population: {population_numbers[i]}")