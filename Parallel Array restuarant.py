rest_name = ("mcdonalds", "chickfila", "chipotle", "cookout") 
food_name = ("burger", "chickennuggs", "bowls", "milkshake")

print("availible restuarants and their food options")
for i in range(len(rest_name)):
    print(f"{rest_name[i]}: {food_name[i]}")