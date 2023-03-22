import random


def lucky():
    global people, name
    choice = str(input('Do you want to use the "Who is lucky?" feature? '
                       'Write Yes/No:\n'))
    while True:
        if choice == "Yes":
            lucky_one = random.choice(list(people.keys()))
            people.pop(lucky_one)
            print(f"\n{lucky_one} is the lucky one!")
            shared = total / len(people)
            people = {name: round(shared, 2) for name in people}
            people[lucky_one] = 0
            print(people)
            break
        elif choice == "No":
            print('\nNo one is going to be lucky\n')
            shared = total / len(people)
            people = {name: round(shared, 2) for name in people}
            print(people)
            break


amount = int(input("Enter the number of friends joining (including you):\n"))
people = {}
if amount > 0:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(amount):
        name = str(input())
        people[name] = 0
    total = float(input("\nEnter the total bill value:\n"))
    lucky()
else:
    print("No one is joining for the party")
