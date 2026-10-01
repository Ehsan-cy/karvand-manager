import json
options = ["Add member", "Show members", "Edit member", "Delete member","Show report", "Exit"]

for number, option in enumerate(options, start=1):
    print(f"{number}) {option}")

user = {}

choice = input("Select from menu: ")

if choice == "6":
    print("Exiting the program.")
    exit()

if choice == "1":
    #add new member
    print("Adding a new member...")
    
    user = {"full_name": input("full_name: ").split(" "),
            "email": input("email: "),
            "city": input("city: "),
            "education": input("education: "),
            "skills": input("skills: ").split(","),
            }
    with open("karvands.json", "a",encoding="utf-8") as file:
            json.dump(user, file, indent=4)
    
    print(f"{user['full_name'][0]} added successfully!")

elif choice == "2":
    #show members
    with open("karvands.json", "r", encoding="utf-8") as file :
        user = json.load(file)
    if user:
        print("Member Details:")
        print(f"Full Name: {' '.join(user.get('full_name', []))}")
        print(f"Email: {user.get('email', 'N/A')}")
        print(f"City: {user.get('city', 'N/A')}")
        print(f"Education: {user.get('education', 'N/A')}")
        print(f"Skills: {', '.join(user.get('skills', []))}")
    else:
        print("No members found.")
    

elif choice == "3":
    #edit member
    with open("karvands.json", "r") as file:
        user = json.load(file)
    edit_name = input("Enter the full name of the member to edit: ")
    
    if edit_name in user['full_name']:
        new_email = input("Enter new email: ")
        new_city = input("Enter new city: ")
        new_education = input("Enter new education: ")
        new_skills = input("Enter new skills: ").split(",")
        
        user['email'] = new_email
        user['city'] = new_city
        user['education'] = new_education
        user['skills'] = new_skills
        with open("karvands.json", "a",encoding="utf-8") as file:
                json.dump(user, file, indent=4)
        
        print(f"{edit_name} updated successfully!")
    else:
        print(f"No member found with the name {edit_name}.")

elif choice == "4":
    #delete member
    with open("karvands.json", "r",encoding="utf-8") as file:
            json.dump(user, file)
    delete_name = input("Enter the full name of the member to delete: ")
    
    if delete_name in user['full_name']:
        user.clear()
        with open("karvands.json", "a",encoding="utf-8") as file:
                json.dump(user, file, indent=4)
        print(f"{delete_name} deleted successfully!")
    else:
        print(f"No member found with the name {delete_name}.")
elif choice == "5":
    #show report
    with open("karvands.json", "r",encoding="utf-8") as file:
        user = json.load(file)
    print("Member Report:")
    print(f"Full Name: {' '.join(user.get('full_name', []))}")
    print(f"Email: {user.get('email', 'N/A')}")
    print(f"City: {user.get('city', 'N/A')}")
    print(f"Education: {user.get('education', 'N/A')}")
    print(f"Skills: {', '.join(user.get('skills', []))}")

else:
    print("Invalid choice. Please select a valid option from the menu.")



    








    
    


