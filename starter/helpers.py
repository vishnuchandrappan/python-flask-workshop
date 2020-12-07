def snakeCase(value):
    temp = value.lower()
    temp = temp.split(' ')
    return '-'.join(temp)
