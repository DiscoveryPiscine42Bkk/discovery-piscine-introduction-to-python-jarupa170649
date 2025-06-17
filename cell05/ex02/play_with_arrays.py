original = [2, 8, 9, 48, 8, 22, -12, 2]

new = [num + 2 for num in original]
print( original )
flitered = [ num for num in new if num  > 5]
print( flitered )