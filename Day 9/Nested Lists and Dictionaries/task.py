# Simple dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# Print "Lille" from travel_log
# print(travel_log["France"][1])

# Nested lists
nested_list = ["A", "B", ["C", "D"]]

# Print "D"
print(nested_list[2][1])

# Print "Stuttgart" from travel_log
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])