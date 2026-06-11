
from datetime import datetime, timedelta

# =====================================
# Global Data Structures
# =====================================

books = []
users = {}
borrow_records = []
blocked_users = set()

ADMIN = "admin"
USER = "user"


# =====================================
# Helper Functions
# =====================================

def find_book(book_id):
    for book in books:
        if book["book_id"] == book_id:
            return book
    return None


def validate_book_number(book_id):

    if not books:
        return book_id == 1

    max_book_id = max(book["book_id"] for book in books)

    return book_id == max_book_id + 1


def login():

    user_id = int(input("Enter User ID: "))

    if user_id not in users:
        print("User not found")
        return None

    return user_id


def is_admin(user_id):
    return users[user_id]["role"] == ADMIN


def is_user(user_id):
    return users[user_id]["role"] == USER


# =====================================
# User Management
# =====================================

def add_user():

    user_id = int(input("Enter User ID: "))
    name = input("Enter Name: ")

    role = input(
        "Enter Role (admin/user): "
    ).lower()

    if role not in [ADMIN, USER]:
        print("Invalid role")
        return

    users[user_id] = {
        "user_id": user_id,
        "name": name,
        "role": role
    }

    print("User added successfully")


# =====================================
# Admin Functions
# =====================================

def add_book(logged_in_user):

    if not is_admin(logged_in_user):
        print(
            "Access Denied. Only Admin can add books."
        )
        return

    book_id = int(input("Book ID: "))

    if not validate_book_number(book_id):
        print(
            "Book numbering must be sequential."
        )
        return

    title = input("Book Title: ")
    author = input("Author: ")

    collection = input(
        "Collection Name (blank if none): "
    ).strip()

    volume_no = None

    if collection:
        volume_no = int(
            input("Volume Number: ")
        )

    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "collection": collection,
        "volume_no": volume_no,
        "available": True
    })

    print("Book added successfully.")


def remove_book(logged_in_user):

    if not is_admin(logged_in_user):
        print(
            "Access Denied. Only Admin can remove books."
        )
        return

    book_id = int(input("Book ID: "))

    book = find_book(book_id)

    if not book:
        print("Book not found")
        return

    if not book["available"]:
        print(
            "Cannot remove issued book."
        )
        return

    books.remove(book)

    print("Book removed successfully.")


def clear_book_entry(logged_in_user):

    if not is_admin(logged_in_user):
        print(
            "Access Denied. Only Admin can clear entries."
        )
        return

    book_id = int(input("Book ID: "))

    book = find_book(book_id)

    if not book:
        print("Book not found")
        return

    books.remove(book)

    global borrow_records

    borrow_records = [
        record
        for record in borrow_records
        if book_id not in record["book_ids"]
    ]

    print("Book entry cleared.")


def view_borrowed_books(logged_in_user):

    if not is_admin(logged_in_user):
        print(
            "Access Denied. Only Admin can view borrowed books."
        )
        return

    print("\nBorrowed Books")

    found = False

    for record in borrow_records:

        if record["return_date"] is None:

            found = True

            due_date = (
                record["issue_date"]
                + timedelta(days=14)
            )

            for bid in record["book_ids"]:

                book = find_book(bid)

                print(
                    f"{bid:<10}"
                    f"{book['title']:<25}"
                    f"{record['user_name']:<15}"
                    f"{record['issue_date'].date()}"
                    f"    "
                    f"{due_date.date()}"
                )

    if not found:
        print("No borrowed books.")


# =====================================
# User Search Functions
# =====================================

def view_available_books():

    print("\nAvailable Books")

    for book in books:

        if book["available"]:

            print(
                book["book_id"],
                "-",
                book["title"],
                "-",
                book["author"]
            )


def search_book_by_title(logged_in_user):

    if not is_user(logged_in_user):
        print(
            "Only Users can search books."
        )
        return

    keyword = input(
        "Enter title/substring: "
    ).lower()

    found = False

    for book in books:

        if keyword in book["title"].lower():

            found = True

            print(
                book["book_id"],
                book["title"],
                book["author"]
            )

    if not found:
        print("No books found.")


def search_book_by_author(logged_in_user):

    if not is_user(logged_in_user):
        print(
            "Only Users can search books."
        )
        return

    author = input(
        "Enter author name: "
    ).lower()

    found = False

    for book in books:

        if book["author"].lower() == author:

            found = True

            print(
                book["book_id"],
                book["title"]
            )

    if not found:
        print("No books found.")

# =====================================
# USER OPERATIONS
# =====================================

from datetime import datetime, timedelta


def receive_book(logged_in_user):

    if not is_user(logged_in_user):
        print("Access Denied. Only Users can borrow books.")
        return

    if logged_in_user in blocked_users:
        print("User is blocked.")
        return

    view_available_books()

    book_id = int(input("Enter Book ID: "))

    book = find_book(book_id)

    if not book:
        print("Book not found.")
        return

    if not book["available"]:
        print("Book unavailable.")
        return

    if book["collection"]:
        print(
            "This book belongs to a collection. "
            "Issue the collection instead."
        )
        return

    book["available"] = False

    borrow_records.append({
        "user_id": logged_in_user,
        "user_name": users[logged_in_user]["name"],
        "book_ids": [book_id],
        "issue_date": datetime.now(),
        "return_date": None
    })

    print("Book issued successfully.")


def return_book(logged_in_user):

    if not is_user(logged_in_user):
        print("Access Denied. Only Users can return books.")
        return

    book_id = int(input("Enter Book ID: "))

    for record in borrow_records:

        if (
            record["user_id"] == logged_in_user
            and book_id in record["book_ids"]
            and record["return_date"] is None
        ):

            record["return_date"] = datetime.now()

            book = find_book(book_id)

            if book:
                book["available"] = True

            days = (
                record["return_date"]
                - record["issue_date"]
            ).days

            if days > 14:
                blocked_users.add(logged_in_user)

                print(
                    "Returned after 14 days."
                )
                print(
                    "User has been blocked."
                )
            else:
                print("Book returned successfully.")

            return

    print("No active borrow record found.")


# =====================================
# COLLECTION OPERATIONS
# =====================================

def issue_collection(logged_in_user):

    if not is_user(logged_in_user):
        print("Only Users can issue collections.")
        return

    if logged_in_user in blocked_users:
        print("User is blocked.")
        return

    collection_name = input(
        "Collection Name: "
    ).strip()

    collection_books = []

    for book in books:

        if (
            book["collection"]
            == collection_name
        ):
            collection_books.append(book)

    if not collection_books:
        print("Collection not found.")
        return

    for book in collection_books:

        if not book["available"]:

            print(
                "Entire collection is not available."
            )
            return

    for book in collection_books:
        book["available"] = False

    borrow_records.append({
        "user_id": logged_in_user,
        "user_name": users[logged_in_user]["name"],
        "book_ids": [
            book["book_id"]
            for book in collection_books
        ],
        "issue_date": datetime.now(),
        "return_date": None
    })

    print(
        "Collection issued successfully."
    )


def return_collection(logged_in_user):

    if not is_user(logged_in_user):
        print("Only Users can return collections.")
        return

    collection_name = input(
        "Collection Name: "
    ).strip()

    collection_ids = []

    for book in books:

        if (
            book["collection"]
            == collection_name
        ):
            collection_ids.append(
                book["book_id"]
            )

    if not collection_ids:
        print("Collection not found.")
        return

    for record in borrow_records:

        if (
            record["user_id"] == logged_in_user
            and set(record["book_ids"])
            == set(collection_ids)
            and record["return_date"] is None
        ):

            record["return_date"] = (
                datetime.now()
            )

            for book_id in collection_ids:

                book = find_book(book_id)

                if book:
                    book["available"] = True

            days = (
                record["return_date"]
                - record["issue_date"]
            ).days

            if days > 14:

                blocked_users.add(
                    logged_in_user
                )

                print(
                    "Collection returned late."
                )
                print(
                    "User blocked."
                )

            else:
                print(
                    "Collection returned."
                )

            return

    print("No active collection record found.")


# =====================================
# MENUS
# =====================================

def admin_menu(logged_in_user):

    while True:

        print("\n===== ADMIN MENU =====")

        print("1. Add Book")
        print("2. Remove Book")
        print("3. Clear Book Entry")
        print("4. View Borrowed Books")
        print("5. Logout")

        choice = input("Choice: ")

        if choice == "1":
            add_book(logged_in_user)

        elif choice == "2":
            remove_book(logged_in_user)

        elif choice == "3":
            clear_book_entry(
                logged_in_user
            )

        elif choice == "4":
            view_borrowed_books(
                logged_in_user
            )

        elif choice == "5":
            break

        else:
            print("Invalid choice")


def user_menu(logged_in_user):

    while True:

        print("\n===== USER MENU =====")

        print("1. View Available Books")
        print("2. Search Book By Title")
        print("3. Search Book By Author")
        print("4. Receive Book")
        print("5. Return Book")
        print("6. Issue Collection")
        print("7. Return Collection")
        print("8. Logout")

        choice = input("Choice: ")

        if choice == "1":
            view_available_books()

        elif choice == "2":
            search_book_by_title(
                logged_in_user
            )

        elif choice == "3":
            search_book_by_author(
                logged_in_user
            )

        elif choice == "4":
            receive_book(
                logged_in_user
            )

        elif choice == "5":
            return_book(
                logged_in_user
            )

        elif choice == "6":
            issue_collection(
                logged_in_user
            )

        elif choice == "7":
            return_collection(
                logged_in_user
            )

        elif choice == "8":
            break

        else:
            print("Invalid choice")


# =====================================
# MAIN PROGRAM
# =====================================

while True:

    print("\n===== LIBRARY SYSTEM =====")

    print("1. Add User")
    print("2. Login")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        add_user()

    elif choice == "2":

        logged_in_user = login()

        if logged_in_user is None:
            continue

        role = users[
            logged_in_user
        ]["role"]

        if role == ADMIN:
            admin_menu(
                logged_in_user
            )

        elif role == USER:
            user_menu(
                logged_in_user
            )

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")


