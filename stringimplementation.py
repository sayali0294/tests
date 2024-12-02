string1 = "hello"
string2 = "world"

string1 +", " +string2
print(string1 +", " +string2)


String="sayali"
"String" + ">" +"concatenation"
print("String" + ">" +"concatenation")

string3= "I am a good student"
string3[0:4]
print(string3[0:4])

string3[5:12]
print(string3[5:12])

string4= "Sayali Punadikar"
string2[1:]
print(string4[1:])

string4[-1]
print(string4[-1])

string4[-4]
print(string4[-4])

string4[:-3]
print(string4[:-3])




s = "Sayali Punadikar"
s[7]
print(s[7])


s1= "I am a student"
print(len(s))
s1.replace('student', 'teacher')
print(s1.replace('student', 'teacher'))


address = "123 suhana apt, marathali, Bangalore"
address.replace("apt", "Apartment")
print(address.replace("apt", "Apartment"))


text = "hello, World"
text.lower()
text.title()
print(text.lower())
print(text.upper())
print(text.title())




text1 = "I am Is A Student"
text1.swapcase()
print(text1.swapcase())

text1.capitalize()
print(text1.capitalize())




#string searching

sentence = "I am a student at azad"
"am" in sentence


sentence = "I am a student at azad"
search_word = "am"

if search_word in sentence:
    print("The search word is present")
else:
    print("Not")


#string Comparison
str1 = "Hello"
str2 = "hello"


str1 == str2



names= ["Ajay",  "Nakula", "Bee"]
sorted(names)
print(sorted(names))  


#common string operation
input_str = "       sayali        "
input_str.strip()
print(input_str.strip())

csv_row="Apple       "
csv_row.strip()
print(csv_row.strip())


#string Splitting    

data = "Ajay, data science, teacher"
data
teacher_info  = data.split(',')
print(teacher_info)


#tell_me=len((input('Enter your Name: ').lstrip()))
#print(tell_me)



email = "ajay12345gmail.com"

if "@" in email:
    print("valid email")
else:
    print("Invalid")