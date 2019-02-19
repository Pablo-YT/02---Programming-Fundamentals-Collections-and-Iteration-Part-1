#Output the message "I will not skateboard in the halls" 20 times.

#Create a list consisting of the above message. It should appear in the list 20 times.

#Create a list consisting of the numbers between 1 and 50.

#Use a for loop to find the sum of the numbers in the above list.

#Create a new list which has three of each number up to 50.

#Ie. [1, 1, 1, 2, 2, 2, 3, 3, 3, ... , 50, 50, 50] and so on, up to 50.
#Make a new list out all of the countries from the dictionary in Exercise 6 that are not islands. Print out both lists.

text = 0
while text < 20:
	print("I will not skateboard in the halls")
	text +=1


text_list = []
for n in range(0,20):
    text_list.append('I will not skateboard in the halls')
print(text_list)

	
a_list = list(range(1,51))

list_num = []
for number in range(1,51):
    list_num.append(number)
    list_num.append(number)
    list_num.append(number)

print(list_num)
