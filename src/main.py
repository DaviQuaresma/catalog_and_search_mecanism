from database.database import Database
from helpers.raw_insert import generate_books

def main():
    print("teste")
    database = Database()
    
    books: list[dict] = generate_books(10)
    
    for book in books:
        database.insert(book)
    
    

if __name__ == "__main__":
    main()