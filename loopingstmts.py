#take a number from the user and check whether it is prime?
num = int(input("Enter a number: "))
if 0<= num <2:
    print('Not a prime')
elif num == 2:
    print("Prime number")
elif num >= 3:
    for num1 in range(2,num):
        if num%num1 == 0:
            print("Not a prime")
            break
    else:
        print("Prime number")

#take a string from the user and check contains only digits or not?
str_num = input("Enter a string: ")
if str_num.isdigit():
    print("Contains only digits")
else:
    print("Contains not only digits")
#take a string from the user and check contains only  alphabets or not?
str_alp = input("Enter a string: ")
if str_alp.isalpha():
    print("Contains only alphabets")
else:
    print("Contains not only alphabets")
#take a string from the user and check contains only  special chars or not?
str_spl = input("Enter a string: ")
if not str_spl.isdigit() and not str_spl.isalpha() and not str_spl.isalnum()  :
    print("Contains only special chars")
else:
    print("Contains not only special chars")
#take a string from the user and check contains only  capital letters or not?
str_cap = input("Enter a string: ")
if str_cap.isupper():
    print("Contains only upperletters")
else:
    print("Contains not only upperletters")
#take a string from the user and check contains only  small letters or not?
str_low = input("Enter a string")
if str_low.islower():
    print("Contains only smallletters")
else:
    print("Contains not only smallletters")
 #WAP to replace last n occurrence.
str_rep = "Python program needs so much practice"
n = int(input("In which occurence string need to be changed: "))
pattern = "o"
str_repl = "k"
str_chg =""
count_no = 0
if n<=str_rep.count(pattern):
    for i in str_rep:
        if i == pattern:
            count_no +=1
            if count_no == n:
                str_chg += str_repl
            else:
                str_chg += i
        else:
            str_chg += i 
    str_rep = str_chg
print(str_rep)
#WAP to check given string contains numbers or not. it should consider float numbers also.
s =input("Enter a string: ")
for i in s:
    if i.isnumeric():
        print("contains numbers")
        break
s1 = s.split('.',1)
if len(s1) ==2:
    if s1[0][-1].isnumeric() and s1[1][0].isnumeric():
        print("contains float")
#Convert the total string in to lower case. Without using lower() function.
str_lower = input("Enter a string: ")
if str_lower:
    str_lower = str_lower.casefold()
print(str_lower)
#Convert the total string in to upper case. Without using upper() function.
str_upper = input("Enter a string: ")
str_cover = ""
if str_upper:
    for i in str_upper:
        if i.islower():
            str_cover += i.swapcase()
        else:
            str_cover += i
print(str_cover)
#Show the below menu to the user until and until user select quit and display corresponding os message
#'''
#Menu:
#1. windows
#2. Linux
#3. Mac
#4. quit
#'''
while True:
    print("Menu:\n1. Windows\n2. Linux\n3. Mac\n4. quit")
    chs_opt = int(input("Select some number from Menu: "))
    if chs_opt == 4:
        break

#take a string from the user and check contains at least one digit or not?
str_dg = input("Enter a string: ")
for i in str_dg:
    if i.isdigit():
        print("It contains one or more digits")
        break
else:
    print("No digits here")
#19. take a string from the user and check contains at least one alphabets or not?
str_al = input("Enter a string: ")
for i in str_al:
    if i.isalpha():
        print("It contains one or more alphabets")
        break
else:
    print("No alphabets")
#20. take a string from the user and check contains at least one chars or not?
str_ch = input("Enter a string: ")
if str_ch:
    print("it contains character")
else:
    print("No char")
#21. take a string from the user and check contains at least one capital letter or not?
str_cp = input("Enter a string: ")
for i in str_cp:
    if i.isupper():
        print("It contains one or more capital letters")
        break
else:
    print("No capital letters")
#22. take a string from the user and check contains at least one small letter or not?
str_cl = input("Enter a string: ")
for i in str_cl:
    if i.islower():
        print("It contains one or more small letters")
        break
else:
    print("No small letters")
#Print the first 100 odd numbers
print(tuple(range(1,200,2)))
#Determine the factors of a number entered  by the user
num_fac = int(input("Enter number to get factor of it"))
print([num for num in range(1,num_fac) if num_fac%num == 0])
#Play a number guessing game (User enters a guess, you print YES or Higher or Lower). This should #continue until and until user gives a correct number or want to quit in the middle.
print("let's play guessing game")
num = 6
condition = True
while condition:
    num1 = int(input("Enter the number: "))
    if num1>num:
        print("you guessed higher")
    elif num1<num:
        print("you guessed lower")
    elif num1 == num:
        print("The numbers are equal, you guessed correctly")
        inp_msg = input("you want to play the game again yes or no?")
        if inp_msg.casefold() == 'yes':
            condition = True
        else:
            condition = False
    
#Take two numbers from the user a,b check whether a is divisible by b or not?
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(f"{a} is divisible by {b}") if int(a/b) else print(f"{a} is lesser than {b}") 
#Find the sum of all the multiples of 3 or 5 below 1000
print(sum([i for i in range(1000) if i%3 == 0 or i%5 ==0]))
#Write a program to find out big of two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(max(num1,num2))
#Write a program to find out biggest number in the given numbers.
list_of_numbers = [int(input("Enter the number: ")) for i in range(int(input("Enter how many numbers you want enter: ")))]
print(max(list_of_numbers))
#find out third occurrence of given substring
print("Python is not easy, it is easy only when you come compare with other programming languages")
str_main = "Python is not easy, it is easy only when you come compare with other programming languages as i know"
str_sub = input("Enter the substring: ")
print(str_main.replace(str_sub,'kys',2).find(str_sub))

#find out nth occurrence of given substring
print("Python is not easy, it is easy only when you come compare with other programming languages")
str_main = "Python is not easy, it is easy only when you come compare with other programming languages as i know"
str_sub = input("Enter the substring: ")
n = int(input("Enter the number in which occurence u want to find"))
print(str_main.replace(str_sub,'kys',n).find(str_sub))
#Take some single digit numbers from the user and findout min, maximum, sum, average
a = [int(input("Enter number: ")) for i in range(int(input("Enter the number of input u want to provide: ")))]
print("minimum is:",min(a))
print("maximum is:",max(a))
print("sum is:",sum(a))
print("average is:",sum(a)/len(a))
#WAP> 10 -> 000010
s = "10"
print(s.zfill(6))
#100 ->  000100
s = "100"
print(s.zfill(6))
#1000 ->  001000
s = "1000"
print(s.zfill(6))
#2345678  ->  2345678
s = "2345678"
print(s.zfill(9))
#names  ="emp1,emp2,emp3,emp4" iterate through the employee names.
names = "emp1,emp2,emp3,emp4"
for i in names.split(','):
    print(i)
#Take actual string, source string, destination string. replce first nth occurrences of source string #with destination string of actual string.
act_str = input("Enter actually string: ")
source_str = input("Enter source string: ")
dest_str = input("Enter destinatin stirng: ")
n = int(input("Occurences"))
print(act_str.replace(source_str,dest_str,n))
#Take a two numbers from the user and do below menu driven operations
#1. addition
#2. multiples
#3.division
#4.sqrt
#5. pow    a**b
#6.subtraction
#After selection do the corresponding operation.
#Note: user may give int, or float numbers. You should check whether it is proper digits or not. I.e the user given string should be in the position to convert to float. Other wise show the “inproper string given” Error.
a,b = [input("Enter the number: "),input("Enter the number: ")]
if (not isinstance(a, str)) and (not isinstance(b,str)):
    print("sum is",a+b)
    print("multiple",a*b)
    print("division",a/b)
    print("sqrt values",a**0.5,b**0.5)
    print("a**b is",pow(a,b))
    print("substraction",a-b)
else:
    print("inproper string given”")
#Take numbers from the user and find out min, maximum, sum, average
#l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
# find out how many even numbers are there and how many odd numbers are there and 
print(len([i for i in l if l%2 == 0]))
print(len([i for i in l if not l%2 == 0]))
# how many positive numbers are there and how many negative numbers are there and 
print('length of positive numbers',len([i for i in l if i == abs(i)]))
print('length of negitive numbers',len([i for i in l if i != abs(i)]))
# how many prime numbers are there and how many perfect numbers are there and
prime_num = [2]
for i in l:
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime_num.append(j)
print("prime numbers are",len(prime_num))
perf_num = []
for k in l:
    facts = []
    for m in range(1,k):
        if k%m == 0:
            facts.append(m)
    if k == sum(facts):
        perf_num.append(k)
print("perfect numbers",perf_num)
# how many Armstrong numbers are there and how many palindrome numbers are there.
arm_num = [1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
arm_num_list = [j for j in arm_num if j == sum([pow(int(i),len(str(j))) for i in str(j)])]
print('armstrong numbers len',len(arm_num_list),arm_num_list)

l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
print('palindrome',len([i for i in l if i == int(str(i)[::-1])])) 
#Take a string from the user and find out how many digits are there,
str_dg1 = input("Enter a string: ")
print(len([i for i in str_dg1 if i.isdigit()])) 
# how many special symbols are there, how many small letters are there, 
str_dg1 = input("Enter a string: ")
print("no of symbols",len([i for i in str_dg1 if not i.isdigit() and not i.isnumeric() and not i.isalpha() and not i.isalnum()])) 
print("no of small letters",len([i for i in str_dg1 if i.islower()]))
# how many caps are there.
print("no of capital letters",len([i for i in str_dg1 if i.isupper()]))

#Take a char from the user and find out how many number of occurrences are there in given string
str_char = input("Enter a character: ")
print("no of occurrences",str_dg1.count(str_chr))
#Take a element from the user and find out how many times the  element occurred in given list
str_num1 = int(input("Enter a number: "))
print(l.count(str_num1))
#Take a element from the user and find out how many number of occurrences are there in given tuple
l=(1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4)
str_num1 = int(input("Enter a number: "))
print(l.count(str_num1))
#Reverse the string without effecting the special symbols. 
# It involves three variations. Write code for three variations.
#	1.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba
s="abc123,#$45def6%$^789$%^"
l = []
add = ""
for i in s[::-1]:
    if not i.isalnum():
        l.append(i)
    else:
        l = ''.join(l[::-1])
        if l:
            add += l
        add += i
        l = []
print(add) 
#	2.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^
s = 'abc123,#$45def6%$^789$%^'
s1 = [i for i in s[::-1] if i.isalnum()]
print(s1)
for k,i in enumerate(s):
    n = k
    if not i.isalnum():
        print(s.index(i,n),i)
        s1.insert(s.index(i,n),i)
        print(s1)
print(''.join(s1))
#	3.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^
s = '123,#$456%$^789$%^'
l = []
add = ""
for i in s:
    if i.isalnum():
        l.append(i)
    else:
        l = ''.join(l[::-1])
        if l:
            add += l
        add += i
        l = []
print(add) 
