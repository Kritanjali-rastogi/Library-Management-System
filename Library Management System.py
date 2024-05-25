class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def available_book(self):
        print ("The books present in this library are: ") 
        for books in self.book_list:
            print("\t" + books)

    def book_issue(self, book_name):
        if book_name in self.book_list:
            print(f"The book {book_name} has been issued to you. Please return in 30 days")
            self.book_list.remove(book_name)
            return True
               
        else:
            print(f"The book {book_name} is not available to borrow")
            return False

    def book_return(self, book_name):
        if book_name not in self.book_list:
            self.book_list.append(book_name)
            print(f"The book {book_name} has been returned. Thanks!")


class Student:
    def request_book(self):
        self.book = input("Enter the book you want to borrow: ")
        return self.book
    
    def return_book(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
    

central_library = Library(["Jango", "Angular", "Python", "Java", "Statistics", "ML", "AI"])
Student_1 = Student()

while True:
    
    welcome_message = '''===== Welcom to Central Library. Please choose one of the following:
    1. List all the books
    2. Request a book
    3. Return a book
    4. Exit the library'''

    print(welcome_message)

    user_input = int(input("Enter the required option (1/2/3/4):  "))

    if user_input ==1:
        central_library.available_book()

    elif user_input ==2:
        central_library.book_issue(Student_1.request_book())
    
    elif user_input ==3:
        central_library.book_return(Student_1.return_book())

    elif user_input ==4:
        print("Thanks for using the system")
        exit()

    else:
        print("You have entered the incorrect choice")