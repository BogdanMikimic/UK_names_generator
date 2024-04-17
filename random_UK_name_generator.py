from random import randint, choice, sample


def generate_name(number_of_names: int = randint(1, 3), name_gender: str = choice(['m', 'f'])) -> str:
    """
    Generates random UK female and male names and surnames from external txt files.
    Each full name will contain a number of names (random between 1 and 3 by default) and one surname.
    By default, a name gender is randomly selected and all names in the full name will be chosen from the
    same gender.

    Parameters:
    number_of_names (int): number of names, optional (if not specified it chooses 1-3 names at random)
    name_gender (str): name gender, needs to be 'm' or 'f' ('M' or 'F' are also acceptable),optional
    (if not specified it will be 'm' or 'f' selected at random)

    Raises:
    ValueError: If name_gender is not string
    ValueError: If name_gender is not 'm' or 'f'
    ValueError: If number_of_names is not an integer
    ValueError: If number_of_names is negative or zero

    Returns:
    Generated name as string
    """
    # checks that number_of_names and name_gender arguments are provided correctly
    if type(name_gender) != str:
        raise ValueError(f'name_gender needs to be a string. You provided "{name_gender}" which is a {type(name_gender)}')
    elif name_gender.lower() != 'm' and name_gender.lower() != 'f':
        raise ValueError(f'name_gender expected to be "m" or "f". You provided "{name_gender}"')

    if type(number_of_names) != int:
        raise ValueError(f'number_of_names argument needs to be an integer. You provided {number_of_names} which is a {type(number_of_names)}')
    elif number_of_names <= 0:
        raise ValueError(f'number_of_names argument needs to be a positive integer, bigger then zero')

    # opens the files containing the surnames and names, extracts them as lists, and closes the files
    surnames_list = list()
    names_list = list()

    with open('names_lists/surnames.txt', 'r', encoding="UTF-8") as surnames_doc:
        for line in surnames_doc:
            surnames_list.append(line.strip())

    with open(f'names_lists/{name_gender}_names.txt', 'r', encoding='UTF-8') as names_doc:
        for line in names_doc:
            names_list.append(line.strip())

    # select and return a random name
    return f'{" ".join(sample(names_list, number_of_names))} {choice(surnames_list)}'

print (generate_name())


