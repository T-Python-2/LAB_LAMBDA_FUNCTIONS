## Given the following list, using a lambda function , filter the list to include only 
# names starting in "Kh" and "Mo".

myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filtered_list = list(filter(lambda name : name.startswith("Mo") or name.startswith("Kh"), myList))
print(filtered_list)