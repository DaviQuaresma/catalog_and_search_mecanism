from database.database import Database
from helpers.raw_insert import generate_books
from helpers.idented_data import idented_data
from algorithms.linear_search import linear_search

def main():
    option = 0
    database = Database()
    books: list[dict] = generate_books(10)
    
    for book in books:
        database.insert(book)
    
    while True:
        
        print("\n=========================")
        print("Escolha uma operação")
        print("=========================")
        print("1 - Ver livros da lista")
        print("2 - Busca Linear por titulo e autor O(n)")
        print("3 - Busca Linear por titulo e autor O(n)")
        print("4 - Busca Linear por titulo e autor O(n)")
        print("=========================")
        option = int(input(f"Escolha: "))
        print("=========================\n")
    
        match option:
            case 1:
               idented_data(books)
            case 2:
                title = input("Qual titulo deseja buscar?\n")
                author = input("Qual autor deseja buscar?\n")
                
                book = linear_search(books, title.strip(), author.strip())
                
                if book:
                    print("-" * 40)
                    for key, value in book.items():
                        print(f"{key} => {value}")
                    print("-" * 40)
                    
            case 3:
                print("Saindo")
                break
            case _:
                print("Opção invalida")
            

if __name__ == "__main__":
    main()