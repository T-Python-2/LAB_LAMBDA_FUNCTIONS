


#using a lambda function inside filter function

myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filtered_list = list(filter(lambda element : element.startswith("Kh") or element.startswith("Mo")  , myList ))

print(filtered_list)



