
from csv_handler import CSV_Writer, CSV_Reader

def deleteBook():
    
    ISBN = input("\t\tEnter The ISBN Number of The Book:")
    
    isFound = False
    
    reader, file = CSV_Reader()
    rows = list(reader)
    file.close()
        
    for row in rows:
        if row[0] == ISBN:
            rows.remove(row)
            writer, file = CSV_Writer("w")
            writer.writerows(rows)
            file.close()
            isFound = True
            print(f"\t\tBook {row[1]} has been deleted successfully.")
            return
            
    if isFound == False:
        print("\t\tBook not found.")