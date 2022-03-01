from larousse_api import larousse

def main():

    

    # Print the array containing all defintions of "Fromage"
    print(larousse.get_definitions("Fromage"))

if __name__ == "__main__":
    main()