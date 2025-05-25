def is_palindrome(word):
     if word.lower() == word[::-1].lower():
        return 1
     else:
        return 0
     

def get_user_input():
   return input ("Please input the word you wish to check: \n")

def main():
  word = get_user_input()
  result = is_palindrome(word)

  if result == 1:
     print("Your word is a palindrome")
  elif result == 0:
     print("Your word is not a palindrome")


if __name__ == '__main__':
   main()