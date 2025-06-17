def average(grades):
    return sum(grades.values()) / len(grades)

class_B = {
    "a": 1,
    "b": 5,
    "c": 8,
    "d": 9
}

class_C = {
    "e": 20,
    "f": 15,
    "j": 10,
    "k": 12
}

print(f"Average for class B: {average(class_B)}.")
print(f"Average for class C: {average(class_C)}.")
