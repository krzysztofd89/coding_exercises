def first_recurring_character(characters):
    if characters:
        previous_characters = set()

        for character in characters:
            if character not in previous_characters:
                previous_characters.add(character)
            else:
                return character
    return None
