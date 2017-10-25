def reorderArrayWithEvenFirst(reorderedArray):
    next_even, next_odd = 0, len(reorderedArray) - 1

    while next_even < next_odd:
        if reorderedArray[next_even] % 2 == 0:
            next_even += 1
        else:
            reorderedArray[next_even], reorderedArray[next_odd] = reorderedArray[next_odd], reorderedArray[next_even]
            next_odd -= 1