

def idented_data(data: list[dict]):
    for book in data:
        for key, value in book.items():
            print(f"{key} => {value}")
        print("-" * 40)
    