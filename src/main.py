from database.database import Database
from helpers.raw_insert import generate_books
from helpers.idented_data import idented_data
from algorithms.linear_search import linear_search
from algorithms.category_filter import category_filter
from algorithms.selection_sort import sort
from algorithms.insertion_sort import insertion_sort
import random

def main():
    option = 0
    database = Database()
    books, categories, authors = generate_books(10)

    for book in books:
        database.insert(book)
        
    data = database.get()
    
    random.shuffle(data)
    
    while True:

        print("\n=========================")
        print("Escolha uma operação")
        print("=========================")
        print("1 - Ver livros da lista")
        print("2 - Busca Linear por titulo e autor O(n)")
        print("3 - Filtros por categoria")
        print("4 - Ordenação por seleção")
        print("5 - Inserção ordenada")
        print("8 - Saindo")
        print("=========================")
        option = int(input(f"Escolha: "))
        print("=========================\n")

        match option:
            case 1:
                idented_data(data)
            case 2:
                title = str(input("Qual titulo deseja buscar?\n"))
                author = str(input("Qual autor deseja buscar?\n"))

                if author not in authors:
                    print("Autor desconhecido ou nome digitado incorretamente!")
                    return False

                book = linear_search(data, title.strip(), author.strip())

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

                filtered_list = category_filter(data, category.strip())
                idented_data(filtered_list)

            case 4:
                print("Escolha a ordenação desejada:")
                print("1 - Desc")
                print("2 - Asc")
                print("=========================")
                order = int(input(f"Escolha: "))
                print("=========================\n")
                
                if order not in (1, 2):
                    print("Você escolheu uma opção invalida!")
                    return
                
                sorted_books = sort(data, order)
                idented_data(sorted_books)
                
            case 5:
                arr = insertion_sort(data)
                print(arr)
            case 8:
                print("Saindo")
                break
            case _:
                print("Opção invalida")


if __name__ == "__main__":
    main()
