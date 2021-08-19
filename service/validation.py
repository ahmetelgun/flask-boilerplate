def validate(objects, scheme):
    if len(objects) != len(scheme):
        return False

    if len(objects) == 0 and len(scheme) == 0:
        return True

    if len(objects) == 0 or len(scheme) == 0:
        return False

    for index, object in enumerate(objects):
        if type(object) != scheme[index]:
            return False

    return True
