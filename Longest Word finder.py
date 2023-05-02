# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:30:36 2023

@author: laure
"""

if __name__ == "__main__":
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do \ eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad \ minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex \ ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate \ velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat \ cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id \ est laborum."
    longestWord = ""
    currentWord = ""
    for char in text:
        if char.isalpha():
            currentWord = currentWord + char
        else:
            if len(currentWord) > len(longestWord):
                longestWord = currentWord
            currentWord = ""
    print("The longest word is " + str(longestWord) + " (" + str(len(longestWord)) + " characters)")
            

