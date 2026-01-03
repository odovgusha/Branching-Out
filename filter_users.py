import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users
        if user.get("name", "").lower() == name.lower()
    ]

    for user in filtered_users:
        print(user)


def filter_users_by_age(min_age, max_age=None):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = []

    for user in users:
        age = user.get("age")

        if age is None:
            continue

        if age < min_age:
            continue

        if max_age is not None and age > max_age:
            continue

        filtered_users.append(user)

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (name / age): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        min_age = int(input("Enter minimum age: ").strip())
        max_age_input = input("Enter maximum age (or press Enter to skip): ").strip()

        if max_age_input:
            max_age = int(max_age_input)
        else:
            max_age = None

        filter_users_by_age(min_age, max_age)

    else:
        print("Filtering by that option is not yet supported.")

