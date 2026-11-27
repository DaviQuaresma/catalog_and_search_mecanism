import random

def generate_books(qtd: int):
    books: list[dict] = []
    
    categories: list = ["Didatico", "Matematica", "Engenharia"]
    authors: list = ["Albert Wenstein", "Nikolas Tesla", "Leonardo Da vinci"]
    
    for b in range(qtd):
        book = {}
        book["title"] = f"Book-{b}"
        book["author"] = random.choice(authors)
        book["category"] = random.choice(categories)
        book["year"] = random.randint(2000, 2026)
        book["pages"] = random.randint(100, 600)
        books.append(book)
    
    return books, categories, authors


    
    
    