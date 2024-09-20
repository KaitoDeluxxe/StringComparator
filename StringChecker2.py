from difflib import SequenceMatcher
from colorama import Fore,Style
import os

def similar(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()*100

def main ():
    print('Would you like to keep opening this app?(Y/N)')
    z = input('Answer: ')
    answer = z.strip(" ")
    while (answer == 'Y' or 'y'):
     print("String Compare and Checker")
     x = input("Enter First String : ")
     y = input("Enter Second String : ")
     text1 = x.strip()
     text2 = y.strip()
     if text1 == text2:
        print("[INFO] The string is the same")
        print("[INFO] Similarity : ", end=" ")
        print(similar(text1,text2), "%")
        input("Press Enter to start over...")
        os.system('CLS')
     else:
        print("[INFO] The string is not the same")
        print("[INFO] Similarity : ", end=" ")
        print("%.2f"%similar(text1, text2) ,"%")
        input("Press Enter to start over...")
        os.system('CLS')

if __name__== "__main__":
    main()