
import csv

def addBook():
    ISBN = input("\t\tEnter ISBN Number of The Book: ")
    title = input("\t\tEnter The Title of The Book: ")
    author = input("\t\tEnter The Author's Name (Separated by Space):")
    quantity = input("\t\tEnter The Quantity of This Book: ")
    price = input("\t\tEnter Price of The Book: ")
    
    data = [ISBN, title, author, quantity, price]
    
    with open("books-collection.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
        
    print("\n\t\tBook Added Successfully.")
        
    