import sys
from extract import clean_csv

def main():
    filename = "clean_results.csv"
    print(clean_csv(filename))

if __name__ == "__main__":
    sys.exit(main())