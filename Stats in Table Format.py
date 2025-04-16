#import the Tabulate operation 

from tabulate import tabulate 


#Displaying the data set before organization in Taublate format



data = [
    ["Apr 11, 2025", "Rockets", "14", "4", "8", "1", "0"],
    ["Apr 9, 2025", "Mavericks", "27", "7", "3", "1", "0"],
    ["Apr 8, 2025", "Thunder", "28", "7", "3", "1", "0"],
    ["Apr 6, 2025", "Thunder", "19", "3", "7", "1", "0"],
    ["Mar 31, 2025", "Rockets", "16", "8", "4", "2", "2"]
]

#Header names of the categories


headers = ["Date", "Opponent", "Points", "Rebounds", "Assists", "Steals", "Blocks"]

#Format the table 

table = tabulate(data, headers=headers, tablefmt="grid")


print(table)