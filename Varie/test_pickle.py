import pickle



def main():
    data = ['one', 2, [3, 4, 5]]
 
    with open('data.dat', 'wb') as f:
        pickle.dump(data, f)

    objdump = None

    with open('data.dat', 'rb') as f:
        # Stores the now deserialized information into objdump
        objdump = pickle.load(f)

    print(objdump)

if __name__ == "__main__":
    main()