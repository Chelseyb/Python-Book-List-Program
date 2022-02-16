import pickle
import random
import sys
import csv

def print_menu():
    print("-------------------------------------------------------------------------------------")
    print("Welcome to the Python Booklist program!\n")
    print("This program allows you to write the title, author, genre and a summary of a book to a file.\nYou can then view your booklist and search the booklist by title!")
    print("-------------------------------------------------------------------------------------")
    print("1. Add to booklist")
    print("2. Search for an author in the booklist")
    print("3. Print the full booklist")
    print("4. Delete a book off the list by author")
    print("5. Quit")


    
    
def get_menu_choice():
    #  for a choice and check it
    while (True):
        try:
            choice = int(input("\nEnter your choice: "))
            if (choice < 1 or choice > 5):
                print("Please select a valid option.")
                continue
        except:
            print("Please enter a numeric value.")
        else:
            break

    return choice

def main():
    print_menu()
    choice = get_menu_choice()
    bookRank = 0
    i = 0
    fullBookList = []
    filename =open('booklist.csv')
    for i in filename:
            fullBookList.append(i.split(","))        
    
    #if the user picks 1 in the menu they are going to add a line in the csv file that has the title, author and genre of the book
    if choice == 1:
        bookToAdd = input("Enter the name of the book: ")
        authorName = input("Enter the author of the book: ")
        genreOfBook = input("Enter the genre of the book: ")
        summaryOfBook = input("Write a summary of the book so you will remeber what it's about: ")

               
        #add the book to the list and file
        with open('booklist.csv','a') as fileName:
            fullBookList.append([bookToAdd,authorName,genreOfBook,summaryOfBook])
            fileName.write(str(len(fullBookList))+",")
            fileName.write(str(bookToAdd)+",")
            fileName.write(str(authorName)+",")
            fileName.write(str(genreOfBook)+",")
            fileName.write(str(summaryOfBook)+"," +"\n")

        
        print(f"Your book called {bookToAdd} written by {authorName} was added to your list!")
        fileName.close()





      
    #option 2 allows the user to enter author of the book and print the book
    elif choice == 2:
        number = input("Enter the author you are looking for: ")

        

        #read csv, and split on "," the line
        filename = csv.reader(open('booklist.csv', "r"), delimiter=",")

        print(f"\nBooks by {number}")
        print("--------------")
        #loop through the csv list
        for row in filename:
            #if current rows 2nd value is equal to input, print that row

            if number == row[2]:
                 print (row)
        """
        this is not grabbing the right row
        filename = open('booklist.csv')
        bookNumber = 0
        test = False
        for i in filename:
            if test:
                #if you find the author print the books
                    if searchKey in i:
                        print("Books Found: "+ str(i))
            else:
                print("That author is not on your list")
 
            bookNumber +=1
        """
        

            
    elif choice == 3:
        #print the full booklist.csv file
        filename =open('booklist.csv')
        for i in filename:    
            print(i)

            
    elif choice == 4:
        #want to delete an entire row based off of the number/ author
        delKey = input("Enter author of the book you want to delete: ")
        for i in fullBookList:
            if i[2] == delKey:
                fullBookList.remove(i)
       #index won't work
       #if delKey.isdigit():
          #  fullBookList.pop(int(delKey)-1)
       # else:
         
        #read csv, and split on "," the line
        with open('booklist.csv', "w") as filenameDel:
    
            #loop through the csv list
            index = 1
            for row in fullBookList:
                #fix index when you delete a value 
                fullBookList[index -1][0] = str(index)

                #write the new values after something is del
                filenameDel.write(fullBookList[index - 1][0]+","+ fullBookList[index-1][1]+","+ fullBookList[index-1][2]+","+ fullBookList[index-1][3]+","+ fullBookList[index-1][4]+"\n")
                index +=1 
        
            print("Book was deleted from the list")

    elif choice == 5:
        sys.exit()
        
    play_again = input("\n Add another book? (y/n): ")
    if play_again.lower() == "y":
            main()

# Call main
main()
