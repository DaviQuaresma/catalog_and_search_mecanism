
# Busca linear de tempo de execução O(n) proposital
# Parametros titulo e autor

def linear_search(data: list[dict], title: str | None, author: str | None) -> None | dict:
    found = False
    
    for book in data:
        book_title = book.get("title")
        book_author = book.get("author")
        
        if book_title == title and book_author == author:
            found = True
            return book
            
        elif book_title == title or book_author == author:
            found = True
            return book
        
    if not found:
        print("Resultado não encontrado!")
        return None