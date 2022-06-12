
def get_info_from_file(filename):
    data = open(filename, 'r')
    list_from_data = data.read()
    list_from_data = list(map(str, list_from_data.split()))
    data.close()
    return list_from_data

def polynomial(lst):
    x, y, z = [x for x in lst]
    polynom = f"{x} * (x ** 2) + {y} * (x) + {str(z)} = 0"
    return polynom

def working_with_files (filename, modif, info):
    with open(filename, modif) as data:
        data.write(str(info))