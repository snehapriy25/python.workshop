storage = []
num_items = int(input("Enter number of items: "))

for i in range(num_items):
    item = input(f"Enter item {i+1}: ")
    storage.append(item)

print("Initial storage:", storage)
search_item = input("Enter item to deliver: ")

if search_item in storage:
    print("Your item is delivered.")
    storage.remove(search_item)
else:
    print("Item not available.")

print("Remaining storage:", storage)
