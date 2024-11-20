# Solutions to OOP Exercises

## Exercise 1: Book Class Solution

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
    
    def read(self, pages_read):
        self.current_page = min(self.current_page + pages_read, self.pages)
        return f"Now on page {self.current_page} of {self.pages}"
    
    def bookmark(self):
        return f"Bookmarked at page {self.current_page}"
    
    def is_finished(self):
        return self.current_page >= self.pages

# Usage example:
book = Book("Python OOP", "John Doe", 200)
print(book.read(50))    # Now on page 50 of 200
print(book.bookmark())   # Bookmarked at page 50
print(book.is_finished()) # False
