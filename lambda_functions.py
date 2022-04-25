


namesList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]


filtered_list = list(filter(lambda element: element.startswith(("Kh","Mo")), namesList ))


print(filtered_list)
