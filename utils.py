
smiles_atoms = {'Al', 'As', 'B', 'Br', 'C', 'Cl', 'F', 'I', 'K', 'Li', 'N',
    'Na', 'O', 'P', 'S', 'Se', 'Si', 'Te', 'se', 'te', 'c', 'n', 'o', 'p', 's'}




def readDetailsFromPdbLine(line):
    atom = line[0:6].replace(" ", '')
    atom_serial = line[6:11].replace(" ", '')
    atom_name = line[12:16].replace(" ", '')
    alternate_location = line[16].replace(" ", '')
    residue_name = line[17:20].replace(" ", '')
    chain_identifier = line[21].replace(" ", '')
    residue_sequence_number = line[22:26].replace(" ", '')
    code = line[26].replace(" ", '')
    x_coordinate = line[30:38].replace(" ", '')
    y_coordinate = line[38:46].replace(" ", '')
    z_coordinate = line[46:54].replace(" ", '')
    occupancy = line[54:60].replace(" ", '')
    temperature = line[60:66].replace(" ", '')
    segment_identifier = line[72:76].replace(" ", '')
    element_symbol = line[76:78].replace(" ", '')
    charge = line[78:80].replace(" ", '')

    return {
        'atom':atom,
        'atom_serial':atom_serial,
        'atom_name':atom_name,
        'alternate_location':alternate_location,
        'residue_name':residue_name,
        'chain_identifier':chain_identifier,
        'residue_sequence_number':residue_sequence_number,
        'code':code,
        'x_coordinate':x_coordinate,
        'y_coordinate':y_coordinate,
        'z_coordinate':z_coordinate,
        'occupancy':occupancy,
        'temperature':temperature,
        'segment_identifier':segment_identifier,
        'element_symbol':element_symbol,
        'charge': charge
    }

def getStringOfSize(value, size, left_justification = True):
    result = [' ']*size
    value = str(value)[0:size]
    spaces = size - len(value)
    if left_justification == True:
        result[0:size] = value + ' '*spaces
    else:
        result[0:size] = ' '*spaces + value
    
    return ''.join(result)


def getPdbLineFromDetails(
        atom = '',
        atom_serial = '',
        atom_name = '',
        alternate_location = '',
        residue_name = '',
        chain_identifier = '',
        residue_sequence_number = '',
        code = '',
        x_coordinate = '',
        y_coordinate = '',
        z_coordinate = '',
        occupancy = '',
        temperature = '',
        segment_identifier = '',
        element_symbol = '',
        charge = ''
    ):

    atom = getStringOfSize(atom, 6, True)
    atom_serial = getStringOfSize(atom_serial, 5, False)
    atom_name = getStringOfSize(atom_name, 4, False)
    alternate_location = getStringOfSize(alternate_location, 1, True)
    residue_name = getStringOfSize(residue_name, 3, False)
    chain_identifier = getStringOfSize(chain_identifier, 1, True)
    residue_sequence_number = getStringOfSize(residue_sequence_number, 4, False)
    code = getStringOfSize(code, 1, True)
    x_coordinate = getStringOfSize(x_coordinate, 8, False)
    y_coordinate = getStringOfSize(y_coordinate, 8, False)
    z_coordinate = getStringOfSize(z_coordinate, 8, False)
    occupancy = getStringOfSize(occupancy, 6, False)
    temperature = getStringOfSize(temperature, 6, False)
    segment_identifier = getStringOfSize(segment_identifier, 4, True)
    element_symbol = getStringOfSize(element_symbol, 2, False)
    charge = getStringOfSize(charge, 2, True)


    line = atom + atom_serial + ' ' + atom_name + alternate_location + residue_name + ' ' + chain_identifier + residue_sequence_number \
            + code + ' '*3 + x_coordinate + y_coordinate + z_coordinate + occupancy + temperature + ' '*6 + segment_identifier + element_symbol \
            + charge
    
    return line
    

    
def pdbqtToPdb(pdbqt):
    lines = pdbqt.split('\n')

    result = []
    for line in lines:
        if line.startsWith('ATOM') or line.startsWith('HETATM'):
            details = getPdbLineFromDetails(line)
            result.append(getPdbLineFromDetails(atom=details['atom'],
                                                atom_serial=details['atom_serial'],
                                                atom_name=details['atom_name'],
                                                x_coordinate=details['x_coordinate'],
                                                y_coordinate=details['y_coordinate'],
                                                z_coordinate=details['z_coordinate'],
                                                element_symbol=details['atom_name']
                                                )+ '\n')
    
    return ''.join(result)

