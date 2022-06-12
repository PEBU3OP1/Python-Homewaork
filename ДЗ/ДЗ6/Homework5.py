
def get_info_from_file(filename):
    data = open(filename, 'r')
    list_from_data = data.read()
    list_from_data = list(map(str, list_from_data.split()))
    data.close()
    return list_from_data
