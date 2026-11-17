

def idented_data(data: list[dict]):
    
    for book in data:
        print("-----------------------------")
        for key, value in book.items():
            print(f"{key} => {value}")
    