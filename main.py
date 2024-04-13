import random

import functions as funcs
import data

# s1 = funcs.generate_sample(data.products_per_category, 5)
# s2 = funcs.generate_sample(data.regions, 5)

# rows = funcs.merge_sample([s1, s2], 5)
# print(*s1[0:5], sep="\n")
# print()
# print(*s2[0:5], sep="\n")
# print()
# print(*rows, sep="\n")

poss_val = [data.subscription_prices, data.products_per_category, data.regions, data.domains]
header = ["Subscription date","Subscription prices", "Product category", "Product name", "Region", "Country", "City", "Domain name"]
dataset = funcs.generate_dataset(poss_val, 20, header)
# print(dataset, sep="\n")
# Test
funcs.to_csv_file(dataset, "C:\\Users\\Novaz\\Documents\\Informatique\\Programmation\\MSI\\Dataset_Generator\\test.csv")
# Prod
dataset = funcs.generate_dataset(poss_val, 10000, header)
funcs.to_csv_file(dataset, "C:\\Users\\Novaz\\Documents\\Informatique\\Programmation\\MSI\\Dataset_Generator\\out.csv")

# t = funcs.generate_random_time("28/04/2008", "11/04/2024")
# print(t)