from operator import ne


start_char = {"Kh","Mo"}

myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

new_list = list(filter( lambda x: ( x[0:2] in start_char ) , myList))

print(new_list)