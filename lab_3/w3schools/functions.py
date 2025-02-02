#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")



#function definitions cannot be empty, but if you for some reason have a functiondefinition with no content, put in the passstatement to avoid getting an error.
def myfunction():
    pass
