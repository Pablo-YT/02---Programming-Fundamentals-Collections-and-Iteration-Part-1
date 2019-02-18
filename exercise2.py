#Print out the last element of the list of your favourite colours.
#Note: do this in a way that would still work for a list of any size!

#Add a new city to the dictionary of cities and population.
#Reverse the list of coin flips and save it.
#Print out the population of one of the cities.
#Print out a sentence about each item in the list of performing artists. For example:
#I think Pearl Jam is great.
#I think Lady Gaga is great.
#I think Pink Floyd is great.




#FAV Color
favourite_colors = ["red" , "yellow", "black", "purple"]
print(favourite_colors[-1])


#flip coin lul

coin_flip = ["heads", "tails", "heads", "tails", "heads", "tails"]

coin_flip.reverse()

print(coin_flip)

#artist

fav_artist = ["Billy Ray", "AMV", "The Rolling Stones"]

print("I think {}, {} and {} are great".format(fav_artist[0],fav_artist[1],fav_artist[2]))


#cities

cities_population = {
	"Toronto": "2.81 million",
	"Brampton": "520,911 thousand",
	"Milton":"110,128 thousand"
}

cities_population["Tokyo"] = "9.2 million"

print(cities_population["Tokyo"])





#Ages
#age_fam = [17, 13, 15, 19, 10]

#print(age_fam[0])



#Fav Words
#three_fav_words = {
#'cover me':'watch my six',
#'AYOL':'Are You Online',
#'Home': 'I wanna go Home'
#}
#print(three_fav_words['AYOL'])

#movie
#fav_movie = {
#	'Kick Ass':"2015",
#	'Dragon Ball Super Movie': '2018',	
#	'A Movie': "2016",
#}

#print(fav_movie["Kick Ass"])



#Family Age
#age_fam = {
#'Ray': 17, 'Norman': 13, 'Conner': 15, 'Nash': 19, 'Emma': 10

# }
#print(age_fam['Ray'])