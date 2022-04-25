myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

new_list = list(filter(lambda i : i.startswith("Kh") or i.startswith("Mo") , myList))
print(new_list) 