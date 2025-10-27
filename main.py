from stats import count_words, count_chars, print_report
import sys

def get_book_text(path):
    book = open(path, 'r')
    content = book.read()
    return content

def main():
   print(sys.argv)
   if len(sys.argv)<2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    
   __path__ = sys.argv[1]
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {__path__}...")
   print("----------- Word Count ----------")
   print(f"Found {count_words(get_book_text(__path__))} total words")
   print("--------- Character Count -------")
   print_report(count_chars(get_book_text(__path__)))
   print("============= END ===============")

if __name__=="__main__":
    main()