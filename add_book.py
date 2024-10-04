
from csv_handler import CSV_Writer 

def addBook():
    
    ISBN = input("\t\tEnter ISBN Number of The Book: ")
    title = input("\t\tEnter The Title of The Book: ")
    author = input("\t\tEnter The Author's Name (Separated by Space):")
    quantity = input("\t\tEnter The Quantity of This Book: ")
    price = input("\t\tEnter Price of The Book: ")
    
    data = [ISBN, title, author, quantity, price]
    
    writer, file = CSV_Writer("a")
    writer.writerow(data)
    file.close()
        
    print("\n\t\tBook Added Successfully.")
        
    