class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("this users email has been updated")

    def __repr__(self):
        return "User {}, email: {}, + books read : {}".format(
            self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self,book,rating= 0):
        self.books.update({book:rating})

    def get_average_rating(self):
        total = 0
        for i in self.books.values():
            if type(i) == 'int':
              total += i
        return total/len(self.books)

# grayson = User('Grayson A Walker','gaw3aa@virginia.edu')
# tom  = User('Grayson A Walker','gaw3aa@virginia.edu')

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("this books ISBN has been updated.")

    def add_rating(self,rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    
    def get_average_rating(self):
        total = 0
        divisor = 1
        if len(self.ratings)>1:
            divisor = len(self.ratings)
        for i in self.ratings:
            total += i
        return total/(divisor)

    def __hash__(self):
        return hash((self.title, self.isbn))

# dharma_bums = Book("Dharma Bums",69)
# dharma_bum = Book("Dharma Bums",420)
# dharma_bums.add_rating(2)
# dharma_bums.add_rating(4)

class Fiction(Book):
    def __init__(self,title,isbn,author):
        super().__init__(title,isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title,self.author)

class Non_Fiction(Book):
    def __init__(self,title,isbn,subject,level):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title,level=self.level,subject=self.subject)

# ulysses = Fiction("Ulysses",1234,"Joyce")
# superforecasting = Non_Fiction("Superforecasting",1234,"Statistics","intermed")

# grayson.read_book('dharma_bums',3)
# grayson.read_book('dharma',4)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def __repr__(self):
        return "Users: {users}\n\nBooks: {books}".format(users=len(self.users),books=len(self.books))

    def __eq__(self, diff):
        return self.users == diff.users and self.books == diff.books
    
    def create_book(self,title,isbn):
        return Book(title,isbn)

    def create_novel(self,title,author,isbn):
        return Fiction(title,isbn,author)

    def create_non_fiction(self,title,isbn,subject,level):
        return Non_Fiction(title,isbn,subject,level)

    def add_book_to_user(self,book,email,rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book,rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self,name,email,user_books=None):
        user = User(name,email)
        self.users[email] = user
        if user_books != None:
            for i in user_books:
                self.add_book_to_user(i,email)
                print(i)

    def print_catalog(self):
        for i in self.books.keys():
            print(i)

    def print_users(self):
        for i in self.users.values():
            print(i)

    def most_read_book(self):
        max_book = None 
        max_book_value = 0
        for book,value in self.books.items():
            if value > max_book_value:
                max_book = book
                max_book_value = value
        return max_book

    def most_positive_user(self):
        highest_avg_rating = 0
        highest_name = None

        for user in self.users.values():
            my_avg = user.get_average_rating()
            if  my_avg > highest_avg_rating:
                highest_avg_rating = my_avg
                highest_name = user.name

        return ("Most positive user is {name} with average rating of {rating}".format(name=highest_name, rating=highest_avg_rating))

    def highest_rated_book(self):
        max_avg = 0
        max_book = ''
        for i,value in self.books.items():
           avg = i.get_average_rating()
           if avg > max_avg:
               max_avg = avg
               max_book = i
        return max_book

    def get_most_read_book(self):
        high_read_count = 0
        high_read_name = None
        for book in self.books.keys():
            if self.books[book] > high_read_count:
                high_read_count = self.books[book]
                high_read_name = book.title

        return ("Book with highest read count is {name}".format(name=high_read_name))

    
tom_book = TomeRater()
tom_book.add_user("Grayson","gaw3aa@",["Lolita","Last Exit","Ulysses"])
