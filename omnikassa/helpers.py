def data_to_str(data):
    values = []
    for key, value in data.items():
        values.append('{}={}'.format(key, value))
    return '|'.join(values)


def str_to_data(string):
    pairs = string.split('|')
    data = {}
    for p in pairs:
        key, value = p.split('=', 1)
        data[key] = value
    return data
