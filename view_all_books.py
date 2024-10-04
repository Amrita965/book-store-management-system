
import csv

def viewAllBooks():
    
    width = 20
    
    print("\t\tAll Books")
    print("\t\t============\n")
    print(f"\t\t{'ISBN'.ljust(width)}{'Title'.ljust(width)}{'Author'.ljust(width)}{'Quantity'.ljust(width)}{'Price'.ljust(width)}")
    print("\t\t======================================================================================")
    
    with open("books-collection.csv", "r") as file:
        reader = csv.reader(file)
        
        for record in list(reader):
            print(f"\t\t{record[0].ljust(width)}{record[1].ljust(width)}{record[2].ljust(width)}{record[3].ljust(width)}{record[4].ljust(width)}")
            print("\t\t--------------------------------------------------------------------------------------")