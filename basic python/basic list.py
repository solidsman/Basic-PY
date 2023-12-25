print("|  WELCOME TO ANIMUS  |")

welcome = input("| Do u wana join  animu |(yes/no) : ")
if welcome == "yes":
    print("LOADING[||||||||||||||||||||||]")
else:
    quit()

def na_mes():
    na_me = ['Whats is your name: ', 'Whats your age: ', 'whats your skills: ']
    name_ans = []

    for question in na_me:
        name_ans.append(input(question))
        print("|YOUR DATA|")
        print(name_ans)

na_mes()

def next_2():
    details = ['whats your goal:  ', 'what your dream: ', 'whats your motive:  ']
    detail_ans = []

    for questions in details:
        detail_ans.append(input(questions))
        print("YOUR WAY")
        print(detail_ans)    

next_2()        

print("ADDDING |||||||||||||||||||||||||||||||||||||||||||||||")

num1 = input("enter your favoutite number:  ")
num2 = input("enter your favourite number:  ")
value = int(num1) + int(num2)
print(value)


print("SIMPILYFY|||||||||||||||||||||||||")



print("Starting numbers.............")

starting = float(input('write your favourite number: '))
ends = float(input('enter your age: '))
print(starting + ends)

print("Listing>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")

#listing

def mind_s():
    listing = ['anger level: ','hating level: ','sadness level: ','depression level: ','happinesss level: ']
    listing_a = []

    for questions in listing :
        listing_a.append(input(questions))
        print("Your Mind Level")
        print(listing_a)
mind_s()


def frd_s():
    frds = ['Whats your first friend name: ', 'Whats your second friend name: ','whats your third friend name: ']
    frds_a = []

    for questions in frds :
        frds_a.append(input(questions))
        frds_a.sort()
        print(frds_a)


frd_s()


print("Finding YOUR age diffrences.......................")

y1 = float(input("Enter your year of Birth date: "))
y2= float(input("Enter Date of this year: "))

dif = y2 - y1

print("Your Age difference: ", dif)

#midlibs

character = input("Enter your favourite inspirational character:  ")
hobby    = input("Enter your favourite Hobby:  ")

print("your favourite Hobby: " + hobby)
print("your Inspirational character: "+character)


def reverse_a():
    listed = ['Enter your favourite letter: ', 'Enter your favourite letter: ', 'Enter your favourite letter: ']
    listed_a = []
    for questions in listed :
        listed_a.append(input(questions))
        print("||||||||||")
        print(listed_a)
reverse_a()
















