from dataclasses import dataclass, field
import itertools
from typing import Any, Self

counter_id = itertools.count(start=1)


@dataclass
class BookSchema:
    title: str
    author: str
    category: str
    year: int
    pages: int
    id: int = field(default_factory=lambda: next(counter_id))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            title=str(data["title"]),
            author=str(data["author"]),
            category=str(data["category"]),
            year=int(data["year"]),
            pages=int(data["pages"]),
        )
        
    @classmethod
    def to_dict(cls, data: Self) -> dict:
        book = {}
        book["id"] = data.id
        book["title"] = data.title
        book["author"] = data.author
        book["category"] = data.category
        book["year"] = data.year
        book["pages"] = data.pages
        return book
