checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    checklist[index] = '√' + checklist[index]

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
	if function_code == "C" or function_code == "c":
		input_item = user_input("\u001b[33m Input item:")
		create(input_item)

	elif function_code == "R" or function_code == "r":
		item_index = user_input("Index Number: ")
		print(read(int(item_index)))
	elif function_code == "P" or function_code == "p":
		list_all_items()
	elif function_code == "Q" or function_code == "q":
		return False

	else:
		print("Unknown Option")
		return True

def test():
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    list_all_items()
test()
running = True

while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list and Q to quit: ")
    runner = select(selection)
