import json

# კლასი, რომელიც აღწერს წიგნის ობიექტს
class Book:
    def __init__(self, title, author, year, id):
        # ინიციალიზაცია: სათაური, ავტორი, გამოშვების წელი და უნიკალური ID
        self.title = title
        self.author = author
        self.year = year
        self.id = id

    def __str__(self):
        # ობიექტის ტექსტური წარმოდგენა
        return f"'{self.title}' by {self.author} ({self.year}) [ISBN: {self.id}]"

    def to_dict(self):
        # წიგნის მონაცემების გარდაქმნა ლექსიკონად (dictionary) ფორმატში
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'id': self.id
        }

    @classmethod
    def from_dict(cls, data):
        # ლექსიკონიდან (dictionary) მონაცემების გამოყენებით წიგნის ობიექტის შექმნა
        return cls(data['title'], data['author'], data['year'], data['id'])


# კლასი, რომელიც მართავს ბიბლიოთეკას
class Library:
    def __init__(self, filename='library.json'):
        # ინიციალიზაცია: ცარიელი წიგნების სია და ფაილის სახელი
        self.books = []
        self.filename = filename
        self.load_books()  # ბიბლიოთეკის ჩატვირთვა ფაილიდან

    def add_book(self, book):
        # წიგნის დამატება ბიბლიოთეკაში, დუბლიკატების შემოწმებით ID-ის მიხედვით
        if any(existing_book.id == book.id for existing_book in self.books):
            print(f"Book with ID '{book.id}' already exists in the library.")
            return
        
        self.books.append(book)  # ახალი წიგნის დამატება სიაში
        self.save_books()  # სიაში ცვლილებების შენახვა ფაილში
        print(f"Book '{book.title}' added to the library.")

    def save_books(self):
        # წიგნების მონაცემების შენახვა JSON ფაილში
        with open(self.filename, 'w') as json_file:
            json.dump([book.to_dict() for book in self.books], json_file, indent=4)
        print('Library saved to file.')

    def load_books(self):
        # წიგნების მონაცემების ჩატვირთვა JSON ფაილიდან
        try:
            with open(self.filename, 'r') as json_file:
                self.books = [Book.from_dict(data) for data in json.load(json_file)]
            print('Library loaded from file.')
        except FileNotFoundError:
            # თუ ფაილი არ არსებობს, იწყება ცარიელი ბიბლიოთეკით
            print('Library file does not exist. Starting with an empty library.')

    def list_books(self):
        # ბიბლიოთეკაში არსებული ყველა წიგნის ჩვენება
        if not self.books:
            print('No books in the library.')
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def search_books(self, title):
        # წიგნების ძებნა სათაურის მიხედვით
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print(f"Found {len(results)} book(s) matching '{title}':")
            for book in results:
                print(f"  - {book}")
        else:
            print(f"No books found with title containing '{title}'.")

    def delete_book(self, id):
        # წიგნის წაშლა ID-ის მიხედვით
        for book in self.books:
            if book.id == id:
                self.books.remove(book)  # წიგნის წაშლა სიიდან
                self.save_books()  # ცვლილებების შენახვა
                print(f"Book '{book.title}' deleted.")
                return
        print(f"No book found with ISBN '{id}'.")


# კლასი, რომელიც მართავს ბიბლიოთეკის მენიუს და ფუნქციებს
class BookManager:
    def __init__(self):
        self.library = Library()  # ბიბლიოთეკის ობიექტის ინიციალიზაცია
        # მენიუს ოფციების დაკავშირება შესაბამის ფუნქციებთან
        self.menu_options = {
            '1': self.add_book,
            '2': self.library.list_books,
            '3': self.search_book,
            '4': self.delete_book,
            '5': self.exit_program
        }

    def display_menu(self):
        # მენიუს სექციის ჩვენება
        print("\n" + "-" * 30)
        print('\n--- Book Management System ---')
        print('1. Add a new book')
        print('2. List all books')
        print('3. Search for a book by title')
        print('4. Delete a book by ID')
        print('5. Exit')
        print("-" * 30)

    def run(self):
        # პროგრამის ძირითადი ციკლი
        while True:
            self.display_menu()  # მენიუს ჩვენება
            choice = input('Choose an option: ')  # მომხმარებლის არჩევანის მიღება
            action = self.menu_options.get(choice)  # შესაბამისი ფუნქციის მიღება
            if action:
                action()
            else:
                print('Invalid option. Please try again.')

    def add_book(self):
        # ახალი წიგნის დამატების პროცესი
        title = input('Enter Book Title: ')
        author = input('Enter Book Author: ')
        year = input('Enter Book Year: ')
        id = input('Enter Book ID: ')
        book = Book(title, author, year, id)  # ახალი წიგნის ობიექტის შექმნა
        self.library.add_book(book)

    def search_book(self):
        # წიგნის ძებნის პროცესი სათაურის მიხედვით
        title = input('Enter title to search: ')
        self.library.search_books(title)

    def delete_book(self):
        # წიგნის წაშლის პროცესი ID-ის მიხედვით
        id = input('Enter ID of the book to delete: ')
        self.library.delete_book(id)

    def exit_program(self):
        # პროგრამის დასრულების ფუნქცია
        print('Exiting the program. Goodbye!')
        exit()


# პროგრამის გაშვება, როცა იგი მთავარი სკრიპტია
if __name__ == '__main__':
    app = BookManager()  # აპლიკაციის ობიექტის შექმნა
    app.run()  # აპლიკაციის გაშვება
