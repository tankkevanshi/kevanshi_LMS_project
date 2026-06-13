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

print ( "Thank you! you here is the information we collected:")

print ("="*50)

# Display each variabble with its type and memory address

print (f"\n variable Deatils:")

print (f"name:{name} -> type:{type(name)} -> address:{id(name)} -> type:{type(height_as_int)}")

print (f"age:{age} -> type:{type(age)} -> address:{id(age)}")

print (f"height:{height} -> type:{type(height)} -> address:{id(height)}")

print (f"fav num:{fav_num} -> type:{type(fav_num)} -> address:{id(fav_num)}")

# ====== display conversion ========

print ("="*50)
print ("type conversion")
print ("="*50)
print ("\n height as integer:{height_as_int}")
print ("\n age as float : {age_as_float}")
print ("f\n Age as string : {age_as_strings}")

#======= Display opretion ==========

print ("="*50)

print ("calaculated result:")

print ("="*50)

print (f"\n your height in centimeter:{height_cm}")

print (f"Approximately : your birth year: {birth_year}")

print (f"\n sum of your age and favourite number: {sum_value}")

print (f"\n product of your age and favourite number : {product_value}")

# string connaction

greeting = "Hello ,"+ name +"!"

message = f" your favourite number is {fav_num}"

print (f" -> {greeting} ")

print (f" -> type : {type(greeting)}")

print (f" -> address : {id (greeting)}")

print (f" -> {message} ")

print (f" -> type : {type(message)}")

print (f" -> address : {id (message)}")

#======== summart table =========

print ("="*50)

print ("summary table:")

print ("="*50)

print (f"\n {'variable' : <20}{'value' : <20} {'type' : <25} {'id':<15}")

print (f"\n {'name':<20}{str (name):<20} {str(type(name)):<25} {id(name):<15}")

# ====== closing message =========

print ("="*50)

print ("Thank you using the personal data collector !!")

print ("="*50)

print ("\n you've successfully explore:")

print ("\n string, integer and print() functions")

print ("\n string , integer and float data types")

print ("\n atrithmetic opration")

print ("type ()and id() built-in functions!")

print ("string concatination")

print ("type casting")


