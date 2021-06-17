empty_list = []
#               0           1           2               3           4       5       6           7               8           9
city_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(city_list)

three_cities = city_list[0:2]
print(three_cities)

city_list[0] = "San Francisco"
print(city_list[0]) 
city_list[2] = "Brooklyn"
print(city_list[2])
city_list[7] = "Hollywood"
print(city_list[7]) 
city_list[5] = "Tampa"
print(city_list[5]) 

#                   1       2       3       4           5       6       7       8           9           10
operator_list = ["Ash", "Jager", "Wamai", "Bandit", "Blitz", "Kaid", "Sledge", "Ela", "Thermite", "Mozzie"]
print(operator_list)
print(operator_list[0])
print(operator_list[6])
print(operator_list[8])
print(operator_list[10])

operator_lists = operator_list
print(operator_lists[1:10])