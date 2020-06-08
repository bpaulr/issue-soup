HEX_CHARS = set(["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


def parse_hex(hex_str: str) -> str:
    hex_len = len(hex_str)
    if hex_len != 3 and hex_len != 6:
        raise IllegalHexArgumentException("Invalid supplied hex code length," + hex_str)
    multi = 2 if hex_len == 3 else 1
    new_hex = []
    for c in hex_str:
        if c.upper() not in HEX_CHARS:
            raise IllegalHexArgumentException("Invalid supplied hex code, " + hex_str)
        new_hex.append(c*multi)
    return '#' + ''.join(new_hex).upper()


class IllegalHexArgumentException(Exception):
    pass
