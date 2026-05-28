# Program to find contact number by name independent of any case from a dictionary.

contacts = [
    {"name": "Gopal", "phone": "987654"}, 
    {"name": "Gaurav", "phone": "876543"}, 
    {"name": "Dheeraj", "phone": "765432"}]
def find(n):
    for c in contacts:
        if c["name"].lower() == n.lower(): 
            return f"Found: {c['phone']}"
    return "Not found"

print(find(input("Search contact: ").strip()))
