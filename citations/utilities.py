def dc_alpha_counter(number):
    """
    Provides a counter using alphanumeric letters from 1-703, e.g.
    a, b, c, ..., aa, ab, ..., zz
    """
    if number > 703:
        raise ValueError("The alpha_counter function can only count up to zz, or 703")
    if number <= 26:
        return "{0}".format(chr(number + 96))
    return "{0}{1}".format(chr(96 + (number - 1) / 26), alpha_counter((26 if number == 0 else number) % 26))
