# Conditional Statements

# If else
age = 20

if age < 18:
    print("you're too young")
elif age == 18:
    print("you are over age")
else:
    print("you're old")
    
# Logical operators 
if age >= 18 and age < 65:
    print("you are an adult but not a senior")
    
if age > 18 or age < 20:
    print("your age is not between 18-20")
    

if age is not 18:
    print("you are not 18")