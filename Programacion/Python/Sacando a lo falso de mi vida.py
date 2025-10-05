my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
manipulated_list = my_list[:]

for i in range(len(manipulated_list) - 1, 0, -1):
    if manipulated_list[i] in manipulated_list[:i]:
        del manipulated_list[i]

print("La lista con elementos únicos: ", manipulated_list )

print("La lista original: ", my_list)

