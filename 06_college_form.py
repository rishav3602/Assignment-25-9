# Take user input (name, address, date of birth etc) to fill a
#  form for your college and print their email IDs

name = input("Enter your name: ")
address = input("Enter your address: ")
DoB = int(input("Enter your Dob: "))
fathers_name = input("Enter your father's name: ")
mothers_name = input("Enter your mother's name: ")
subject = input("Enter the subject: ")
print = (f"""
Name: {name}
Address: {address}
Date of birth: {DoB} 
Father's name: {fathers_name}
Mother's name: {mothers_name} 
Chosen subject: {subject}
""")
print(f"My email id is: {name}{address}@gmail.com")