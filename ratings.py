"""Restaurant rating lister."""
import sys
filename = sys.argv[1]
restaurant_ratings = {}

with open(filename) as file:
	for line in file:
		line = line.rstrip()
		info = line.split(":")

		#adds each line info to dictionary
		restaurant_ratings[info[0]] = int(info[1])

	#user input
	new_restaurant = input("What restaurant would you like to rate?")
	new_rating = input("Please rate your restaurant on a scale of 1 to 5, 5 is highest.")

	#add to dictionary
	restaurant_ratings[new_restaurant] = new_rating

	for restaurant, restaurant_rating in sorted(restaurant_ratings.items()):
		print(f"{restaurant} is rated at {restaurant_rating}")






