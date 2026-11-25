from .schema import BookSchema
from typing import Any

class Database:
    
    def __init__(self):
        self.database: dict[int, BookSchema] = {}
        pass


    def get(self) -> list[dict]:
        data = list(self.database.values())
        final_list = []
        
        for book in data:
            new_book = BookSchema.to_dict(book)
            final_list.append(new_book)
        
        return final_list
    

    def insert(self, data: dict[str, Any]) -> bool:
        try:
            new_book = BookSchema.from_dict(data)
            self.database[new_book.id] = new_book 
            
            return True
        except Exception as e:
            print(f"Error on insert: \n {e}")
            
            return False
        
    def find(self, id: int) -> BookSchema | None:
        return self.database.get(id)
            
    def update(self, data: dict[str, Any], id: int) -> bool:
        try:
            book = self.find(id)
            
            if book:
                new_book = BookSchema.from_dict(data)
                self.database[book.id] = new_book
                return True
            
            return False
        except Exception as e:
            print(f"Error on update: \n {e}")
            
            return False

    def delete(self, id: int) -> bool:
        try:
            book = self.find(id)
            
            if book:
                self.database.pop(id)
                return True
                
            return False
        except Exception as e:
            print(f"Error on find: \n {e}")
            return False