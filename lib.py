# library.py

library = {
    "books": [
        {"title": "The Great Gatsby", "author": "Fitzgerald", "available": True},
        {"title": "1984", "author": "Orwell", "available": True},
        {"title": "Mockingbird", "author": "Lee", "available": True}
    ],
    "borrowed": []
}


def show_books():
    print("\n📚 AVAILABLE BOOKS:")
    for i, book in enumerate(library["books"]):
        if book["available"]:
            print(f"{i + 1}. {book['title']} by {book['author']}")


def borrow():
    show_books()
    choice = int(input("Enter book number to borrow: ")) - 1
    if library["books"][choice]["available"] and len(library["borrowed"]) < 2:
        library["books"][choice]["available"] = False
        library["borrowed"].append(library["books"][choice]["title"])
        print(f"✅ Borrowed {library['books'][choice]['title']}!")
    else:
        print("❌ Can't borrow (not available or already have 2 books)")


def return_book():
    if not library["borrowed"]:
        print("No books to return")
        return
    print("\nYour books:")
    for i, book in enumerate(library["borrowed"]):
        print(f"{i + 1}. {book}")
    choice = int(input("Enter number to return: ")) - 1
    for book in library["books"]:
        if book["title"] == library["borrowed"][choice]:
            book["available"] = True
    library["borrowed"].pop(choice)
    print("✅ Book returned!")


def main():
    while True:
        print("\n" + "=" * 30)
        print("1. Show Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Choose (1-4): ")

        if choice == "1":
            show_books()
        elif choice == "2":
            borrow()
        elif choice == "3":
            return_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()