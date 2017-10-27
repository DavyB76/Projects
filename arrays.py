def reorderArrayWithEvenFirst(reorderedArray):
    next_even, next_odd = 0, len(reorderedArray) - 1

    while next_even < next_odd:
        if reorderedArray[next_even] % 2 == 0:
            next_even += 1
        else:
            reorderedArray[next_even], reorderedArray[next_odd] = reorderedArray[next_odd], reorderedArray[next_even]
            next_odd -= 1


def transform_string_to_list_using_for(symbols):
    returnSeq = []

    for symbol in symbols:
        returnSeq.append(ord(symbol))

    return returnSeq


def transform_string_to_list_using_listcomp(symbols):
    return [ord(symbol) for symbol in symbols]


def generate_cartesian_product_list_from_two_lists(color_list, size_list):
    cartesian_product_list = [(color, size) for color in color_list
                                            for size in size_list]

    return cartesian_product_list