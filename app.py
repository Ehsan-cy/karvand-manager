import json
import os

path = r"D:\Maktab_sharif\CW\karvand-manager\data\karvands.json"

# make folder if not exist
os.makedirs(os.path.dirname(path), exist_ok=True)

if not os.path.exists(path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump( {"karvands": []},file,ensure_ascii=False, indent=2)

while True:
    e = input(
        "1. add member\n"
        "2. show members\n"
        "3. search with ID\n"
        "4. search by skill\n"
        "5. edit member\n"
        "6. delete a member\n"
        "7. exit\n"
        "Please select: "
    ).lower()

    if e == "1" or e == "add":
        # read prior data from file
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        karvands = data["karvands"]

        name = input("Please enter your name: ").strip()
        if name in [karvand["name"] for karvand in karvands]:
            print("This name already exists. Please choose a different name.")
            continue
        email = input("Please enter your email: ").strip()
        city = input("Please enter your city: ").strip()
        degree = input("Please enter your degree: ").strip()
        field = input("Please enter your field of study: ").strip()

        skills = []

        while True:
            skill_name = input("Please enter a skill name: ").strip()
            skill_level = input("Please enter the skill level: ").strip()

            while True:
                try:
                    score = int(input("Please rate your skill from 0 to 100: "))
                    if 0 <= score <= 100:
                        break
                    print("Score must be between 0 and 100.")
                except ValueError:
                    print("Please enter a number.")

            skills.append({
                "name": skill_name,
                "level": skill_level,
                "score": score
            })

            more = input("Do you want to add another skill? (yes/no): ").lower()
            if more != "yes":
                break

        # make ID
        if len(karvands) == 0:
            karvand_id = 1
        else:
            karvand_id = max(
                karvand["id"] for karvand in karvands
            ) + 1

        karvand = {
            "id": karvand_id,
            "name": name,
            "email": email,
            "city": city,
            "education": {
                "degree": degree,
                "field": field
            },
            "skills": skills
        }

        karvands.append(karvand)

        # save data to file
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print("Member added successfully.")

    elif e == "2" or e == "show":
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            karvands = data["karvands"]

            if len(karvands) == 0:
                print("There are no members.")
            else:
                for karvand in karvands:
                    print("ID:", karvand["id"])
                    print("Name:", karvand["name"])
                    print("Email:", karvand["email"])
                    print("City:", karvand["city"])
                    print("Degree:", karvand["education"]["degree"])
                    print("Field:", karvand["education"]["field"])
                    print("Skills:")

                    for skill in karvand["skills"]:
                        print(skill["name"], "| Level:", skill["level"], "| Score:", skill["score"])

           