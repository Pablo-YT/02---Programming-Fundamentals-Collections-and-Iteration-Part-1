#You want to add up your expenses for the year. Create a list of numbers (integers or floats) that represents your expenses, eg:

#[250, 7.95, 30.95, 16.50]

#Add up the numbers and output the result.

#Put this code into a method. The method should take a list as an argument and return the sum of the expenses in the list. Call the method twice with different lists

expenses = [250, 7.86, 32, 19.78]

#print(sum(expenses))

def list_expense(expenses):
	return (sum(expenses))



print(list_expense(expenses))