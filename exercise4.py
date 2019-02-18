#Print out all of the ages of your friends/family that are less than 30 (or any number where some ages will not be printed!).
#Find and output the age of the oldest person in your friends/family list.
#Count how many times you flipped 'heads' using the coin flips list.
#You realize one of the performing artists in your list is no longer a favourite. Remove one of them from the list.
#Pick a city in your city population dictionary and change its population.








#Ages
ages = [17, 13, 15, 19, 10]
print(max(ages))

#flip coin lul

coin_flip = ["heads", "tails", "heads", "tails", "heads"]
print('The number of times "heads" is flipped is {}.'.format(coin_flip.count("heads")))




#artist

fav_artist = ["Billy Ray", "AMV", "The Rolling Stones"]

print(fav_artist[2])

#Fav Words
three_fav_words = {
'cover me':'watch my six',
'AYOL':'Are You Online',
'Home': 'I wanna go Home'
}
three_fav_words.pop('Home')
print(three_fav_words)


#cities

cities_population = {
	"Toronto": "2.81 million",
	"Brampton": "520,911 thousand",
	"Milton":"110,128 thousand"
}
cities_population["Toronto"] = "90 million"
print(cities_population)

#Family Age
age_fam = {
'Ray': 17, 
'Norman': 13, 
'Conner': 15, 
'Nash': 19, 
'Emma': 10

 }

for age in age_fam.values():
    if (int(age) < 16):
        print(age)