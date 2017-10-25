def process_parity(input_nb):
    num_bits = 0
    while input_nb:
        num_bits ^= input_nb & 1
        input_nb >>= 1
    return num_bits