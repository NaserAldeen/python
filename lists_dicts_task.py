counter = 1

skills = ["Python", "Java", "JavaScript", "C#", "Swift", "C++", "Git"]

cv = {}

name = input("Enter your name: ")
cv["name"] = name

age = input("Enter your age: ")
cv["age"] = int(age)

exp = input("How many years of experience do you have? ")
cv["experience"] = int(exp)

cv["skills"] = []

print("\nSkills:\n")
for skill in skills:
    print(str(counter) +"- "+ skill)
    counter += 1
    
skill_input = input("\nChoose a skill from above: ")
cv["skills"].append(skills[int(skill_input)-1])
sec_skill = input("Choose another skill from above: ")
cv["skills"].append(skills[int(sec_skill)-1])

if cv["age"] > 20 and cv["age"] < 45 and cv["experience"] > 1 and cv["skills"].count("Python")>0:
    print("You got accepted, "+cv["name"])
else:
    print("Sorry, we did not accept you")
      
