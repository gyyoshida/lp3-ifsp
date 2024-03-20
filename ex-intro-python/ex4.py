def is_codigo_valid(codigo: str):

    if len(codigo) != 7:
        return False
    if not f"{codigo[0]}{codigo[1]}" == "BR":
        return False
    if not int(codigo[2:6]):
        return False
    if not codigo[len(codigo) - 1] == "X":
        return False

    return True

