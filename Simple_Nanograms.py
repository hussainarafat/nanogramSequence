def nanogram_sequence(binary_array):
    sequence = []
    counter = 0

    for num in binary_array:
        if num == 1:
            counter += 1
        elif counter > 0:
            sequence.append(counter)
            counter = 0

    if counter > 0:
        sequence.append(counter)

    return sequence
