#Print out the list of coin flips.
#Print out the first element of the list of your favourite colours.
#Output the sorted version of the list of your friends and family members' ages.

#Add a new baby (0 years old) to the list of your family's ages.

#Using the dictionary of movie information, access and print the year of one of the movies.

#If you haven't done so recently, now would be a good time to check that your code works and commit once it does.



#FAV Color
favourite_colors = ["red" , "yellow", "black", "purple"]
print(favourite_colors[0])

#Ages
age_fam = [17, 13, 15, 19, 10]
age_fam.append(0)
print(age_fam)


#flip coin lul

coin_flip = ["heads", "tails", "heads", "tails", "heads"]
print(coin_flip)


#movie
fav_movie = {
	'Kick Ass':"2015",
	'Dragon Ball Super Movie': '2018',	
	'A Movie': "2016",
}

print(fav_movie["Kick Ass"])


#Family Age
age_fam = {
'Ray': 17, 'Norman': 13, 'Conner': 15, 'Nash': 19, 'Emma': 10

}

sorted(age_fam.keys())
for age_fam in sorted(age_fam.items()):
	print(age_fam[0], ":", age_fam[1])








#cities

#cities_population = {
#	"Toronto": "2.81 million",
#	"Brampton": "520,911 thousand",
#	"Milton":"110,128 thousand"
#}

#print(cities_population["Toronto"])


#artist
#fav_artist = ["Billy Ray", "AMV", "The Rolling Stones"]
#print(fav_artist[2])


#Fav Words
#three_fav_words = {
#'cover me':'watch my six',
#'AYOL':'Are You Online',
#'Home': 'I wanna go Home'
#}
#print(three_fav_words['AYOL'])