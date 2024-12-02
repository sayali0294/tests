#1
n=0
if n> 0:
        print('The number is positive.')
if n< 0:
        print('The number is negative.')
else:
        print("The number is zero.")


#2
n=5
if n%2==0:
    print('The number is even')
else:
    print('The number is odd')


#3
marks=44
if 100>marks>90:
    print('grade is A')
elif 89>marks>70:
    print('grade is B')
elif 69>marks>50:
    print('grade is C')
else:
    print("grade is F")


#4
num=65
if num % 3 == 0 and num % 5 == 0:
        print('The number is divisible by both 3 and 5.')
if num % 3 == 0:
        print('The number is divisible by 3.')
if num % 5 == 0:
        print('The number is divisible by 5.')
else:
        print('The number is not divisible by 3 or 5.')

#5
num1=78
num2=52
if num1<num2:
      print(f"smaller number is {num1}")
if num2<num1:
      print(f"smaller number is {num2}")
else:
      print(f"both numbers are equal")


#6
num1=34
num2=78
num3=88
if num1> num2:
 if num1> num3:
        largest=num1
 else:
        largest=num3
else:
    if num2> num3:
        largest=num2
    else:
        largest=num3
        print(f"the largest number is {largest}")


#7
year=1978
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#8
temp=22
if temp <15:
        print('cold')
elif 15<temp<30:
        print('Warm')
else:
        temp>30
        print('Hot')

#9
str="b"
char="AEIOUaeiou"
if str in char:
        print('vowels')
else:
        print('consonant')


#10
age = 30
if age < 18:
    print('You are not eligible to drive.')
else:
    18 <= age
    print('You are eligible to drive.')


#11
s1=0
s2=1
s3=0

if (s1+s2)>s3 and (s1+s3)>s2 and (s2+s3)>s1:
  print('can form a triangle')
else:
  print('can not form a triangle')

#12
salary=5000000
if salary<=500000:
        print('the tax rate is 5%')
elif 500001<salary<1000000:
        print('the tax rate is 10%')
else:
     salary > 1000001
     print('the tax rate is 20%')

#13
age=55
if 0< age < 12:
        print('person is child') 
elif 13< age < 19:
        print('person is teen')
elif 20< age < 59:
        print('person is Adult')
else:
      60< age
      print('person is senior')


#14
num=8
if (num%2==0) and (num>10):
        print(f"the {num} is divisible by 2 and greater than 10")

else:
        print(f"{num}is not divisible by 2 or greater than 10")


#15
num=1
if(num<5) or (num>20):
    print(f"the {num}is less than 5 or greater than 20")
else:
    print(f"the {num}is  neither less than 5 nor greater than 20")



#16
usage=121
if usage<=100:
  print(f"the electricity bill is{usage*5} for{usage} units.")
elif 101<usage<200:
  print(f"the electricity bill is{usage*10} for{usage} units.")
else:
    usage<200
    print(f"the electricity bill is{usage*20} for{usage} units.")


   
#17
Month="March"
if Month=="December" or Month=="January"or Month=="February":
        print('Season is winter')
if Month=="March" or Month=="April"or Month=="May":
        print('Season is Spring')
if Month=="June" or Month=="July"or Month=="August":
        print('Season is Summer')
else:
        print('season is Auntum')

#18
pcount=8
pw='12345678'
if pcount==8:
        if '@' in 'pw':
                print('strong password')
        else:
                print('@ required in password') 
else:
        ('atleast 8 character required')       




#19
BMI=18
if 18.5>BMI:
 print('Underweight')

elif 18.5<BMI<24.9:
        print('Normal')
elif 25<BMI<29.9:
        print('Overweight')
else:
         30<BMI
         print('obese')

#20
Name="A"
if Name>="A" and Name<="z":
        print('Alphabet')
elif Name>="0" and Name<="9":
        print('Digit')
else:
        print('special Character')  


