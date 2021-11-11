def pars_planet(line: str):
    line = line.split('	')
    planet = {
        'name': line[0].strip() if line[0].strip() != 'NULL' else None,
        'climate': line[1].strip() if line[1].strip() != 'NULL' else None,
        'diameter': line[2].strip() if line[2].strip() != 'NULL' else None,
        'orbital_period': line[3].strip() if line[3].strip() != 'NULL' else None,
        'population': line[4].strip() if line[4].strip() != 'NULL' else None,
        'rotation_period': line[5].strip() if line[5].strip() != 'NULL' else None,
        'surface_water': line[6].strip() if line[6].strip() != 'NULL' else None,
        'terrain': line[7].strip() if line[7].strip() != 'NULL' else None,
    }
    return planet


def pars_people(line: str):
    line = line.split('	')
    people = {
        'name': line[0].strip() if line[0].strip() != 'NULL' else None,
        'birth_year': line[1].strip() if line[1].strip() != 'NULL' else None,
        'gender': line[2].strip() if line[2].strip() != 'NULL' else None,
        'eye_color': line[3].strip() if line[3].strip() != 'NULL' else None,
        'hair_color': line[4].strip() if line[4].strip() != 'NULL' else None,
        'height': line[5].strip() if line[5].strip() != 'NULL' else None,
        'mass': line[6].strip() if line[6].strip() != 'NULL' else None,
        'homeworld': line[7].strip() if line[7].strip() != 'NULL' else None,
    }
    return people