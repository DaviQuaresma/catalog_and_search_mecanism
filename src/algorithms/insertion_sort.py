def insertion_sort(unorder_data: list[dict]):
    data = unorder_data.copy()
    n = len(data)
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j].get("id") > key.get("id"): # pyright: ignore[reportOptionalOperand]
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data