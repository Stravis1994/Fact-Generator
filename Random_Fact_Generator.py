import requests
import json

def get_fact():
    response =  requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    content = response.text
    data = json.loads(content)
    return data["text"]

def get_fact_of_the_day():
    response =  requests.get("https://uselessfacts.jsph.pl/api/v2/facts/today")
    content = response.text
    data = json.loads(content)
    return data["text"]

print( '-'  * 50)
print( ' ' * 6 + "Welcome to the Random Fact Generator!")

while True:
    print( '-'  * 50)
    print(' ' * 20 + "Main Menu")
    print( '-'  * 50)
    print("1. Get the fact of the day.")
    print("2. Get up to 7 random facts.")
    print("3. Exit the program.")
    
    try:
        user_choice = int(input("Please enter your choice (1, 2, or 3): "))

    except ValueError:
        print("\nInvalid input. Please enter a number (1, 2, or 3).")
        continue
    if user_choice not in [1, 2, 3]:
        print("\nInvalid choice. Please enter 1, 2, or 3.")
        continue
    if user_choice == 1:
        print("\nFact of the day:")
        print(get_fact_of_the_day())
    elif user_choice == 2:
        number_of_facts = int(input("How many random facts would you like to know (1-7)? "))

        if number_of_facts <= 0:
            print("\nMinimum number of facts per execution is 1")
        elif number_of_facts > 7:
            print("\nMaximum number of facts per execution is 7")
        else:
            for i in range(number_of_facts):
                print(get_fact())
    elif user_choice == 3:
        print("\nThank you for using the Random Fact Generator. Goodbye!")
        break 