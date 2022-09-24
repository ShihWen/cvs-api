from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    """
    Read parameters in section postgresql in database.ini.
    Return a parameter dictionary.
    """ 
    parser = ConfigParser()
    parser.read("database.ini")

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    return db

