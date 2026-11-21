
def get_minor(arr: list):
    minor = arr[0]
    minor_indice: int = 0
    
    for book in range(1, len(arr)):
        if arr[book].get("pages") < minor.get("pages"):
            minor = arr[book]
            minor_indice = book
    
    return minor_indice

def get_major(arr: list):
    major = arr[0]
    major_indice: int = 0
    
    for book in range(1, len(arr)):
        if arr[book].get("pages") > major.get("pages"):
            major = arr[book]
            major_indice = book
    
    return major_indice

def sort(arr: list, order: int):
    arr = arr.copy()
    new_arr: list = []
    
    for _ in range(len(arr)):
        if order == 1:
            minor = get_minor(arr)
            new_arr.append(arr.pop(minor))
        else:
            major = get_major(arr)
            new_arr.append(arr.pop(major))
    
    return new_arr