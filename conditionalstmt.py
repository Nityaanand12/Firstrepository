#7. Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor). Based on four inputs
#Decide whether there is sufficient buses or not and give solution for how many extra buses required.

Total_no_of_people = int(input("Enter no of people: "))
Total_no_of_buses = int(input("Enter no of buses: "))
no_of_seats_in_buses = int(input("Enter no of seats in buses: "))
adjust_factor = float(input("Enter no of people can adjust per seat: "))
Total_no_seats = Total_no_of_buses*no_of_seats_in_buses*adjust_factor
if Total_no_of_people > Total_no_seats:
    print("Buses are not sufficient")
    no_of_people_left = (Total_no_of_people - Total_no_seats)
    if no_of_people_left > no_of_seats_in_buses:
        buses_required = no_of_people_left/no_of_seats_in_buses
        if buses_required != round(buses_required):
            buses_required = round(buses_required)+1
            print(f"{buses_required} buses are required")
        else:
            print(f"{buses_required} buses are required")
    else:
        print("One extra bus is required")
else:
    print("buses are sufficient")

#Take number from the user decide whether it is even or odd.

num = int(input("Enter number to check whether it even or odd: "))
if num%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#take number from the user decide whether it is positive number or negative number
num = int(input("Enter a number to check whether it is positive or negitive"))
if num == abs(num):
    print("Number is positive")
else:
    print("Number is negitive")

#take a string from the user print the length. if the user not given anything then show an error message
str1 = input("Enter a string")
print(len(str1))
if not len(str1):
    print("Error Message;: please Enter some string")

#code to perform mathematical operations. take two numbers from the user: 1. add, 2. sub, 3. mul, 4.div, 5.quit
num1 = int(input("Enter a number to do some mathematical operations"))
num2 = int(input("Enter a number to do some mathematical operations"))
print("addition of two number is:",num1+num2)
print("substraction of two number is:",num1-num2)
print("multiplication of two number is:",num1*num2)
print("division of two number is:",num1/num2)
#print(sys.exit() or sys.quit())

#118. show the menu:
   		# 1. kids
    	#	2. Men's
   		# 3. Women's
        #Show the corresponding message based on the selection. Mention error message if he enter >3.

print("below is the menu, please choose one of them")
print("Menu: \n1.kids\n2.Men's\n3.Women's")
selected_option = int(input("please choose any option from the above Menu"))
if selected_option:
    if selected_option == 1:
        print("you are seleted for kids, go to the first floor")
    elif selected_option == 2:
        print("you are seleted the Men's place, go to the second floor")
    elif selected_option == 3:
        print("you are seleted the Women's place, go to the Third floor")
    elif selected_option > 3:
        print("Error Message: you have not selected correct number from the given Menu")
    else: pass
else:
    print("Not choosen item from the Menu")

# write a program to check given substring is there in actual string or not?
#example: act="python is a pure object oriented programing language"
#check whether “pure” is there in act or not.
#Note: Use in operator

pattern = input("Enter a word to check if it is in original string or not")
orginal_string = "python is a pure object oriented programing language"
if pattern in orginal_string:
    print("your word is in orginal string")
else:
    print("Not found")

#Take three numbers from the user and decide which is big
num_1, num_2, num_3 = [int(input("please enter the number: ")) for i in range(3)]
if num_1>num_2 and num_1>num_3:
    print("The big number is:",num_1)
elif num_2>num_3:
    print("The big number is:",num_2)
else:
    print("The big number is:",num_3)

# Take age and gender from the user and decide whether he is eligible for marriage in India or not.
#Age criteria: men age>22, women>18
age = int(input("Enter your age to check whether your are eligible for marriage in India: "))
gender = input("Enter your gender male or female: ")
if gender == "male" and age>=22:
    print("you are eligible for the marriage")
elif gender == "female" and age>=18:
    print("you are eligible for the marriage")
else:
    print("you are not eligible for the marriage")

#Take an age  and gender from the user: and mention that what he/she can do in india.
age = int(input("Enter your age: "))
gender = input("Enter your gender male or female: ")
if (age < 18 and gender == "female") or (age<22 and gender=="male"):
    print("you can continue with studies")
elif gender == "female" and age>=18:
    print("you can continue studies or if you wish, you can do the marriage because you are eligible for marriage")
elif gender == "male" and age>=22:
    print("you can continue studies or if you wish, you can do the marriage because you are eligible for marriage")
else:
    print("No comments")

#conditions
#       1. Theatre: 5 for men 7 for women
#    	2. Voting system: 18 for men and women
#    	3. Marriage in india: 23 for men and for women >21
#    	4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for women
#       5. For driving licence: (min:18, max:60) for men and women
#Eligibility:
#  	    1. theatre
#		2.  Voting system
#		3.  Marriage in india
#		4.  For govt obs
#		5. For driving licence:
#Enter an option:
#	Gender:
#		1. men
#		2. women
#Enter an option:
#Enter an age of person:

print("Gender:\n    1.male\n    2.female")
gender_opt = input("Enter an option for gender from above gender list")
age = int(input("Enter your age as well"))
if gender_opt == 1:
    if age > 5: print("you are eligible to go to theater")
    if age > 18: print("you are eligible to vote")
    if age > 23: print("you are eligible for marriage")
    if 32<age>18: print("you are eligible to get govt jobs")
    if 60<age>18: print("you are eligible to get driving license")
elif gender_opt == 2:
    if age > 7: print("you are eligible to go to theater")
    if age > 18: print("you are eligible to vote")
    if age > 21: print("you are eligible for marriage")
    if 34<age>18: print("you are eligible to get govt jobs")
    if 60<age>18: print("you are eligible to get driving license")
else:
    print("Not selected shown genders")

#operating systems:
#	1.windows
#	2.android
#	3.mac
#Enter an option:

#If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
#If the user enters 2 then show "Goto second floor and buy adroid mobiles"
#If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
#If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3"


print("operating systems:\n   1.windows\n   2.android\n   3.mac")
selected_option = input("Enter an option")
if selected_option == 1:
    print("Goto first floor and buy windows laptop or mobile")
elif selected_option == 2:
    print("Goto second floor and buy adroid mobiles")
elif selected_option == 3:
    print("Goto third floor and buy mac laptop or iphones")
else:
    print("There is only three floors, please select 1 or 2 or 3")


#Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.
age = int(input("Enter your age: "))
if age<1:
    print("you are a baby")
elif 1<age<3:
    print("you are toddler")
elif age<18:
    print("you are child")
elif 10<age<19:
    print("you are teenager")
elif age<60:
    print("you are old codger")
#Take two number a,b from the user and check whether a is divisible by b or not
a = int(input("Enter a number"))
b = int(input("Enter a number"))
if a%b == 0:
    print('it is divisible')
else:
    print("Not divisible")