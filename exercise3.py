#Print out the first two performing artists in that list.
#For each of your favourite movies, print out a sentence about when the movie was released. For example:
#Avatar came out in 2009.
#Mean Girls came out in 2004.
#The Matrix came out in 1999.
#Sort and reverse the list of ages of your family. Save it and print it to the screen.
#See if you can sort and reverse the list on one line!
#Add "Beauty and the Beast" movie to your dictionary of movies information, but with a twist: the movie was released both in 1991 and in 2017. Print it out.



#Ages
age_fam = [17, 13, 15, 19, 10]

age_fam.sort()
age_fam.reverse()
print(age_fam)

#artist

fav_artist = ["Billy Ray", "AMV", "The Rolling Stones"]

print(fav_artist[0] + ", " + fav_artist[1])


#movie
fav_movie = {
	'Kick Ass':"2015",
	'Dragon Ball Super Movie': '2018',	
	'A Movie': "2016",
}

fav_movie["Beauty and the Beast"] = "1991 and 2017"

print("Beauty and the Beast came out in.... {}.".format(fav_movie["Beauty and the Beast"]))

for movie, year_out in fav_movie.items():
    print("{} came out in {}".format(movie, year_out))