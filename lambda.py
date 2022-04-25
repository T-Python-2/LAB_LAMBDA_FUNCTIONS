
## Given the following list, using a lambda function , filter the list to include only names starting in "Kh" and "Mo".

myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filtered_list = list(filter(lambda x :x.startswith("Kh") or x.startswith("Mo")  , myList ))

print(filtered_list)