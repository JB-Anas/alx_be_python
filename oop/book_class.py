
# book_class.py

class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.

        :param title: The title of the book (str).
        :param author: The author of the book (str).
        :param year: The publication year of the book (int).
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        String representation of the Book instance.

        :return: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.

        :return: A string that recreates the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor for the Book instance.

        Prints a message when the instance is deleted.
        """
        print(f"Deleting {self.title}")
