import json
import os

file_name = "data.json"

# Завантаження існуючих даних
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
else:
    data = []

# Отримання списку імен користувачів
existing_names = [entry["name"] for entry in data if "name" in entry]

# Функція для введення нового користувача
def get_user_grades():
    while True:
        try:
            user_name = input("Enter your name: ").strip().capitalize()
            if not user_name:
                raise ValueError("Name cannot be empty")
            if user_name in existing_names:
                raise ValueError("This name already exists in the database")

            user_grades = input("Enter your grades (space-separated): ").strip()
            grades_str_list = user_grades.split()

            if not grades_str_list:
                raise ValueError("You must enter at least one grade")

            grades = []
            for g in grades_str_list:
                grade = float(g)
                if not (0 <= grade <= 100):
                    raise ValueError(f"Grade '{grade}' is out of allowed range (0–100)")
                grades.append(grade)

            return {"name": user_name, "grades": grades}

        except ValueError as e:
            print("Error:", e)
            print("Please try again.")

# Отримання нових даних
new_data = get_user_grades()
data.append(new_data)

# Збереження у файл
with open(file_name, "w") as file:
    json.dump(data, file, indent=4)

print(f"Data for {new_data['name']} saved successfully.")
