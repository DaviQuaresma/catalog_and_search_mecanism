

def category_filter(books: list[dict], filter: str) -> list[dict]:
    
    result: list[dict] = []
    
    for book in books:
        if book.get("category") == filter:
            result.append(book)
    
    return result