def leap(x):
    try:
        if (x%4) == 0:
            if ((x%100) == 0) and ((x%400) != 0):
                return False
            else:
                return True
        else:
            return False

    except TypeError:
        return
