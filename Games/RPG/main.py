def create_character(name, strength, intelligence, charisma):
    # ---- Name validation ----
    if not isinstance(name, str):
        return "The character name should be a string"
    
    if name == "":
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    # ---- Stats validation ----
    stats = [strength, intelligence, charisma]
    
    if not all(type(stat) is int for stat in stats):
        return "All stats should be integers"
    
    if not all(stat >= 1 for stat in stats):
        return "All stats should be no less than 1"
    
    if not all(stat <= 4 for stat in stats):
        return "All stats should be no more than 4"
    
    if sum(stats) != 7:
        return "The character should start with 7 points"
    
    # ---- Output ----
    def stat_line(label, value):
        return label + " " + "●" * value + "○" * (10 - value)
    
    return (
        name + "\n" +
        stat_line("STR", strength) + "\n" +
        stat_line("INT", intelligence) + "\n" +
        stat_line("CHA", charisma)
    )


def createCharacterFromInput():
    name = input ("Enter character name: ")

    # stats input
    strength = int(input("Enter strength: "))
    intelligence = int(input("Enter intelligence: "))
    charisma = int(input("Enter charsima: "))

    return create_character(name, strength, intelligence,charisma)


result = createCharacterFromInput()
print(result)