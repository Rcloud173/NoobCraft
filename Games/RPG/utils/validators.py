def validate_name(name):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    return None


def validate_stats(strength, intelligence, charisma):
    stats = [strength, intelligence, charisma]

    if not all(type(stat) is int for stat in stats):
        return "All stats should be integers"
    if not all(1 <= stat <= 4 for stat in stats):
        return "Each stat must be between 1 and 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"
    return None
