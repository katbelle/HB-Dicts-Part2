"""Restaurant rating lister."""
import sys
filename = sys.argv[1]
restaurant_ratings = {}

with open(filename) as file:
	for line in file:
		line = line.rstrip()
		info = line.split(":")
		# how do I put this in restaurant ratings? 
		
		restaurant_ratings[info[0]] = int(info[1])
	# print(sorted(restaurant_ratings))
	
	sorted_lst = sorted(restaurant_ratings)
	
	for restaurant_name in sorted_lst:
		print(f"{restaurant_name} is rated at {restaurant_ratings[restaurant_name]}")
		# if restaurant_name == restaurant_ratings[restaurant_name]:
		# 	print("YAY")
		# else:
		# 	print("Nay")

	# for entry in restaurant_ratings.items():
	# 	print(f"{entry[0]} is rated at {entry[1]}")


