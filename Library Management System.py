# Project: Library Management System
# Goal: Practice OOP concepts including inheritance, encapsulation, properties, class methods, and polymorphism

from datetime import date, timedelta
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    _total_items = 0

    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year
        self._is_borrowed = False
        LibraryItem._total_items += 1

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def is_borrowed(self):
        return self._is_borrowed

    @classmethod
    def total_items(cls):
        return cls._total_items

    @abstractmethod
    def loan_duration(self):
        pass

    def borrow(self):
        if self._is_borrowed:
            raise ValueError(f"'{self._title}' is already borrowed.")
        self._is_borrowed = True
        return date.today() + timedelta(days=self.loan_duration())

    def return_item(self):
        if not self._is_borrowed:
            raise ValueError(f"'{self._title}' was not borrowed.")
        self._is_borrowed = False

    def __repr__(self):
        status = "borrowed" if self._is_borrowed else "available"
        return f"[{self.__class__.__name__}] '{self._title}' by {self._author} ({self._year}) — {status}"


class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    def loan_duration(self):
        return 21

    def summary(self):
        return f"Book: {self._title}, {self._pages} pages, by {self._author}"


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self._issue = issue

    @property
    def issue(self):
        return self._issue

    def loan_duration(self):
        return 7

    def summary(self):
        return f"Magazine: {self._title}, Issue #{self._issue}"


class DVD(LibraryItem):
    def __init__(self, title, author, year, duration_minutes):
        super().__init__(title, author, year)
        self._duration = duration_minutes

    @property
    def duration(self):
        return self._duration

    def loan_duration(self):
        return 5

    def summary(self):
        return f"DVD: {self._title}, {self._duration} min"


class Member:
    _member_count = 0

    def __init__(self, name, email):
        Member._member_count += 1
        self._id = Member._member_count
        self._name = name
        self._email = email
        self._borrowed_items = []

    @property
    def name(self):
        return self._name

    @property
    def member_id(self):
        return self._id

    @property
    def borrowed_items(self):
        return list(self._borrowed_items)

    def borrow_item(self, item):
        due_date = item.borrow()
        self._borrowed_items.append((item, due_date))
        return due_date

    def return_item(self, item):
        for entry in self._borrowed_items:
            if entry[0] is item:
                item.return_item()
                self._borrowed_items.remove(entry)
                return
        raise ValueError(f"{self._name} does not have '{item.title}' borrowed.")

    @classmethod
    def total_members(cls):
        return cls._member_count

    def __repr__(self):
        return f"Member #{self._id}: {self._name} ({self._email}) | Borrowed: {len(self._borrowed_items)}"


class Library:
    def __init__(self, name):
        self._name = name
        self._catalog = []
        self._members = []

    def add_item(self, item):
        self._catalog.append(item)

    def register_member(self, member):
        self._members.append(member)

    def search(self, keyword):
        keyword = keyword.lower()
        return [item for item in self._catalog if keyword in item.title.lower() or keyword in item.author.lower()]

    def available_items(self):
        return [item for item in self._catalog if not item.is_borrowed]

    def report(self):
        print(f"\n{'=' * 40}")
        print(f"  Library: {self._name}")
        print(f"  Total items: {LibraryItem.total_items()}")
        print(f"  Available: {len(self.available_items())}")
        print(f"  Members: {Member.total_members()}")
        print(f"{'=' * 40}")
        for item in self._catalog:
            print(f"  {item}")
        print()


lib = Library("Alexandria Public Library")

b1 = Book("The Pragmatic Programmer", "David Thomas", 1999, 352)
b2 = Book("Clean Code", "Robert Martin", 2008, 464)
m1 = Magazine("National Geographic", "Various", 2024, 312)
d1 = DVD("Inception", "Christopher Nolan", 2010, 148)

for item in [b1, b2, m1, d1]:
    lib.add_item(item)

alice = Member("Alice Johnson", "alice@example.com")
bob = Member("Bob Smith", "bob@example.com")

lib.register_member(alice)
lib.register_member(bob)

due = alice.borrow_item(b1)
print(f"{alice.name} borrowed '{b1.title}', due: {due}")

due = bob.borrow_item(m1)
print(f"{bob.name} borrowed '{m1.title}', due: {due}")

lib.report()

alice.return_item(b1)
print(f"'{b1.title}' returned by {alice.name}")

results = lib.search("code")
print(f"\nSearch results for 'code':")
for r in results:
    print(f"  → {r.summary()}")