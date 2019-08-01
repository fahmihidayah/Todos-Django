

def get_parameter(argument, key, default):
    if key in argument:
        value = argument[key]
        return value
    else:
        return default