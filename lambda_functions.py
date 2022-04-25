#LAB_LAMBDA_FUNCTIONS


#list of names to be filtered
names_list = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

#filtered list, using the lambda function.
filtered_list = list(filter(lambda word: word.startswith("Kh") or word.startswith("Mo"),names_list))

#print the filtered list
print(filtered_list)