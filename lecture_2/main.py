def generate_profile(age):
    age = int(age)
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >=20:
        return "Adult"
    return None


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
from datetime import datetime
current_year =  datetime.now().year
current_age = current_year - birth_year
list_of_hobbies = []
stop_word = "Stop"

while True:
    user_input = input("Enter a favorite hobby or type 'stop' to finish: ")
    if user_input.lower() == stop_word.lower():
        break
    else:
        list_of_hobbies.append(user_input)

life_stage = generate_profile(current_age)
user_profile = {'Name': user_name, 'Age': current_age, 'Life Stage': life_stage, 'Hobbies': list_of_hobbies}

print('\n' + '-'*3)
print("Profile Summary:")
print("Name:", user_profile['Name'])
print("Age:", user_profile['Age'])
print("Life Stage:", user_profile['Life Stage'])

if not user_profile['Hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite hobbies: ({len(user_profile['Hobbies'])}):")
    for hobby in user_profile['Hobbies']:
        print(f" - {hobby}")

print('-'*3)