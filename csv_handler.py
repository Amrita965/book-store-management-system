
import csv

def CSV_Reader():
    file = open("books-collection.csv", "r")
    reader = csv.reader(file)
    return reader, file
    
def CSV_Writer(mode):
    file = open("books-collection.csv", mode, newline="")
    writer = csv.writer(file)
    return writer, file
