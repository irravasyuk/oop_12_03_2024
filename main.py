# Завдання 3
# Створіть клас Book з атрибутами title (назва
# книги), author (автор) та genre (жанр). Додайте метод
# display_info, який виведе інформацію про книгу у
# вигляді "Назва: {title}, Автор: {author}, Жанр: {genre}".

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def information(self):
        print(f"Назва: {self.title},\nАвтор: {self.author},\nЖанр: {self.genre}")

book1 = Book("12 правил життя", "Джордана Пітерсон", "допоможи собі сам")
book1.information()
