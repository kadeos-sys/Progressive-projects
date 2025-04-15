
#Defining the data list into respective categories 

fake_names = ["Alvin", "Chris", "Jacob", "Kade", "Nate"]
image_weight = ["132", "186", "196", "201", "250"]
fav_num = ["68", "96", "57", "76", "23"]
location = ["Charlotte", "Dallas", "Tampa", "NewYork", "Boston"]


#Displaying / Accessing the data 

for i in range(len(fake_names)):
    print(f"Name: {fake_names[i]}  Weight: {image_weight[i]} Favorite Number: {fav_num[i]}, Location: {location[i]}")