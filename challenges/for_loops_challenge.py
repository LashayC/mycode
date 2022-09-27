#!/usr/bin/env python3

classinfo = {
    "all": [
        {
            "name": "Aaron",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Alexandra",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Alice",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Angela",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Ayrat",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Blake",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Shape of: A Giant Shark",
        },
        {
            "name": "Brandon",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Carl",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Transformation",
        },
        {
            "name": "Chris",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Pyrokinesis",
        },
        {
            "name": "Christian",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Deepak",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Explosive Shouts",
        },
        {
            "name": "Dennis",
            "skill level": "great",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Felicia",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Zoolingualism",
        },
        {
            "name": "Gabriel",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Height Manipulation",
        },
        {
            "name": "Julian",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Hydrokinesis",
        },
        {
            "name": "Kelly",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Lashay",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Stretchy",
        },
        {
            "name": "Nabin",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Steel Skin",
        },
        {
            "name": "Pratibha",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Teleportation",
        },
        {
            "name": "Quentin",
            "skill level": "remarkable",
            "spirit animal": "Lynx",
            "super power": "Polyglot",
        },
        {
            "name": "Will",
            "skill level": "super",
            "spirit animal": "Fox",
            "super power": "Eat Anything",
        },
    ]
}

# Find name in dictionary an d print first name

print('my first name is: ' + classinfo["all"][16]["name"])

# Print sentence 
print(f'My name is {classinfo["all"][16]["name"]}, my spriit animal is {classinfo["all"][16]["spirit animal"]}, my skills are {classinfo["all"][16]["skill level"]}, and my super power is {classinfo["all"][16]["super power"]}')

# Loop through entire class and output for everytone
for students in classinfo["all"]:
    print(f'{students["name"]}, a {students["skill level"]} {students["spirit animal"]} of a programmer, possesses a {students["super power"]} factor for moonlighting as a superhero!\n')
