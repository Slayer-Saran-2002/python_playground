from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City", ["Kolkata", "Mumbai", "Delhi", "Patna", "Darjelling"])
table.align = "l"
table.add_column("Weather Temparature", [40, 40, 40, 40, 40])
print(table)
