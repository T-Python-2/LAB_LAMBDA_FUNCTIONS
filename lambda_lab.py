myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

start_letters1 = 'Mo'
start_letters2 = 'Kh'


filtered_list = list(filter(lambda element: element.startswith(start_letters1) or element.startswith(start_letters2), myList))

print("the filtered list is :")
print(filtered_list)