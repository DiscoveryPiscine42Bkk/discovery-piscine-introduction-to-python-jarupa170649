def famous_births(figures):
    
    sorted_figures = sorted(figures.values(), key=lambda person: int(person["date_of_birth"]))
    
    for person in sorted_figures:
        print(f'{person["name"]} is a great scientist born in {person["date_of_birth"]}.')

scientists = {
    "a": { "name": "A", "date_of_birth": "2000" },
    "b": { "name": "B", "date_of_birth": "1999" },
    "c": { "name": "C", "date_of_birth": "999" },
    "d": { "name": "D", "date_of_birth": "2025" }
}

famous_births(scientists)