original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = [num + 2 for num in original_array]
print( original_array )
flitered_array = [ num for num in new_array if num  > 5]
print( flitered_array )