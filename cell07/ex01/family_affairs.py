def g(family):
    return list(filter(lambda name: family[name] == "pum", family.keys()))

dupont_family = {
    "pum": "pum",
    "g": "g",
    "m": "m",
    "jarupa": "pum",
    "intarit": "pum"
}

print(g(dupont_family))