myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filtered_list = list(filter(lambda element: 'Kh' in element or 'Mo' in element , myList ))
print("the filtered list is :")
print(filtered_list)