#Find the sum total of the population in the dictionary of cities.
#Using your dictionary containing the names of your family and friends with their ages, print out one of two messages for each depending on their age. For example:
#Martha is old.
#Stewart is young.
#Holly is young.
#1Print out the last two colours in your list of favourite colours.
#1Increase by 1 the age of everyone in your list of ages. Print it out.
#Add two new colours to your list of favourite colours.



#FAV Color
favourite_colors = ["red" , "yellow", "black" ,"purple"]
print(favourite_colors[2:])
print(favourite_colors)


#Ages
age_fam = [17, 13, 15, 19, 10]

for age in age_fam:
	age += 1
	print(age)




#cities

cities_population = {
	"Toronto": "2.81 million",
	"Brampton": "520,911 thousand",
	"Milton":"110,128 thousand"
}

cities_population["Toronto"] = 2810000 
cities_population["Brampton"] = 520911
cities_population["Milton"] = 110128

population_total = 0
for cities, population in cities_population.items():
    population_total = population_total + population
print(population_total)






#Family Age

age_fam = {
'Ray': 34, 
'Norman': 25, 
'Conner': 14, 
'Nash': 11, 
'Emma': 7

 }

for fam, age in age_fam.items():
	if  age < 17:
		print("{} is young.".format(fam))

	elif age > 20:
		print("{} is old.".format(fam))