
from add_book import addBook
from view_all_books import viewAllBooks
from display_option import displayOption
import os

while True:
  
    selectedOption = displayOption()
    os.system("cls")
   
    if selectedOption == "1":
        addBook()
    
    elif selectedOption == "2":
        viewAllBooks()
    
    elif selectedOption == "3":
        pass
    
    elif selectedOption == "4":
        pass
    
    elif selectedOption == "5":
        break
    
    else:
        print("\t\tInvaild Input! Please Try Again...")
    