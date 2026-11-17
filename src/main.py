from database.database import Database
from helpers.raw_insert import generate_books
from helpers.idented_data import idented_data
from algorithms.linear_search import linear_search
from algorithms.category_filter import category_filter


def main():
    option = 0
    database = Database()
    books, categories, authors = generate_books(10)

    for book in books:
        database.insert(book)

    while True:

        print("\n=========================")
        print("Escolha uma operação")
        print("=========================")
        print("1 - Ver livros da lista")
        print("2 - Busca Linear por titulo e autor O(n)")
        print("3 - Filtros por categoria")
        print("4 - Ordenação por seleção")
        print("8 - Saindo")
        print("=========================")
        option = int(input(f"Escolha: "))
        print("=========================\n")

        match option:
            case 1:
                idented_data(books)
            case 2:
                title = str(input("Qual titulo deseja buscar?\n"))
                author = str(input("Qual autor deseja buscar?\n"))

                if author not in authors:
                    print("Autor desconhecido ou nome digitado incorretamente!")
                    return False

                book = linear_search(books, title.strip(), author.strip())

                if book:
                    print("-" * 40)
                    for key, value in book.items():
                        print(f"{key} => {value}")
                    print("-" * 40)

            case 3:
                category = str(input("Qual categoria você deseja visualizar?\n"))

                if category not in categories:
                    print("Categoria desconhecida ou digitada incorretamente!")
                    return False

                filtered_list = category_filter(books, category.strip())
                
                if filtered_list:
                    print("-" * 40)
                    for book in filtered_list:
                        for key, value in book.items():
                            print(f"{key} => {value}")
                        print("-" * 40)

            case 4:
                    
            case 8:
                print("Saindo")
                break
            case _:
                print("Opção invalida")


if __name__ == "__main__":
    main()
