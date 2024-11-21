import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
special_char=['!','@','#','$','%','^','&','*','(',')','_','-','+','=']
print("Hello, Welcome to the password generator")
n_alphabets=int(input("How many alphabets would you like to have in your password \n"))
n_numbers=int(input("How many numbers would you like to have in your password \n"))
n_special_char=int(input("How many special characters would you like to have in your password \n"))

#THIS IS AN EASY LEVEL OF MAKING PASSWORD GENERATOR
#password= ""
#for char in range (0,n_alphabets):
#    password+=random.choice(alphabets)
#for char in range (0,n_numbers):
 #   password+=random.choice(numbers)
#for char in range (0,n_special_char):
 #   password+=random.choice(special_char)
#print(password)

#MAkING HARD LEVEL WE WILL INITIAlIZE THE PASSWORD WITH EMPTY LIST AND THEN APPEND THE ITEMS IN IT AND THEN SHUFFLE THE ORDER OF ITEMS IN IT AND FINALLY USE THE FOR LOOP TO GET THE STRING BACK..
password= []
for char in range (0,n_alphabets):
    password.append(random.choice(alphabets))
for char in range (0,n_numbers):
    password.append(random.choice(numbers))
for char in range (0,n_special_char):
    password.append(random.choice(special_char))
print(password)
random.shuffle(password) #used to change the order of items in the list
print(password)
passby=""
for char in password:
    passby += char
print(f"Your password is:{passby}")