# Formats and displays a student profile summary using dictionary data mapping.


name   = input("Enter your name: ")
age    = input("Enter your age: ")
city   = input("Enter your city: ")
favouriteSubject   = input("Enter your Favourite Subject: ")
targetRole   = input("Enter your Target Role: ")


student= {
    'Name' : name,
    'Age' : age,
    'City' : city,
    'Favourite Subject' : favouriteSubject,
    'Target Role' : targetRole ,
}

print()
print(f"Hi! My name is {student['Name'].title()} and I am {student['Age']} years old.")
print(f"I'm from {student['City'].title()}.")
print(f"My favourite subject is {favouriteSubject}.")
print(f"My target role is to be {targetRole.title()}")
