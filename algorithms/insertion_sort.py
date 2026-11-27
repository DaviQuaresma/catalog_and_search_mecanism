from enums.order_by import OrderBy

def insertion_sort(unorder_data: list[dict], order_by: OrderBy):
    data = unorder_data.copy()
    n = len(data)
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        print(data[j])
        print(type(data[j]))
        
        while j >= 0 and data[j].get("id") > key.get("id"):
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data