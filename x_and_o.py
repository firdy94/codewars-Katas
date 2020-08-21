def xo(s: str) -> bool:
    s_lower = s.lower()
    num_x = s.count('x')
    num_o = s.count('o')

    return num_x == num_o
