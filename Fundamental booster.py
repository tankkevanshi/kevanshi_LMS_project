# Fundamental Booster-Interactive personal data collector.

#======Welcome======

print ("="*40)

print ("Welcome to the Interctive peronal data collector!")

print ("\n This will collect your personal information.")

print ("\ perform some calculation,and show you data type deatils.")

print ("\n let's get started!!!")

# ======= Collect informetion section======

print ("="*50)

name= input ("please Enter your name:")

age_str = (input ("please Enter your age:"))

age=int(age_str)

height_str = input ("please Enter your height in meters:")

height = float (height_str)

fav_num_str = input ("please Enter your favrioute number:")

fav_num = int (fav_num_str)

# ======= data processing ======

print ("\n" + "=" * 50)

print ("processing your data........")

print ("=",50)

# calculate birth year

cur_year = 2026

birth_year = cur_year-age

print ("birth_year",birth_year)

# calculate height to centimeter
height_cm = height * 100

# perform some arithmetic opration

sum_value = age* fav_num

product_value = age* fav_num

# Type conversion

height_as_int = int (height)

age_as_float = float (age)

age_as_string = str(age)

# Display result

print ("/n"+"="*50)

print ("Thank you" you here is the information we collected;")

print ("="*50)

# Display each variabble with its type and memory address

print (f"\n "variable Deatils:")

print (f"name: {name}" type:{type(name)}")


