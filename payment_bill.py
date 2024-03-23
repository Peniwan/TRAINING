# Write a code to ask for person's details including name, age, phone number 
# and print out the user then save it into a list and push it to git hub
users_information = []
# ask user for information 
name = input("enter your name: ")
age = input("enter your age: ")
phone_number = input("enter your phone_number: ")

# output information back to user
print(f"person_name is {name}")
print(f"person_age is {age}")
print(f"phone_number is {phone_number}")

# save information in a list

user_details = [name, age, phone_number]
users_information.append(user_details)
print(user_details)
print(users_information)