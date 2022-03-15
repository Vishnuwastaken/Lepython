list = ["Dude", "Guy", "Person"]
for i in range(len(list)):
    print(f"Hello {list[i]}, Welcome to Dinner!")

# dream forgot his mod folder at home
list.remove("Guy")
print("\nUnfortunately, Guy forgot his mod folder at home.\n")

for i in range(len(list)):
    print(f"Hello {list[i]}, Welcome to Dinner!")

print("\nA bigger table has been found! Automatically inviting Dude's friends!\n")
list.insert(1, "Mark")
list.insert(2, "Jeff")
list.append('Bob')

for i in range(len(list)):
    print(f"Hello {list[i]}, Welcome to Dinner!")

print("\nAll of the tables just broke! We are sorry to inform you but only 1 table remains...")

while len(list) > 2:
    list.pop()
for i in range(len(list)):
    print(f"{list[i]}, You have a seat.")

print("\nNevermind, the last table JUST broke.")

while len(list) != 0:
    list.pop()
for i in range(len(list)):
    print(list)
print("Go Home.")
