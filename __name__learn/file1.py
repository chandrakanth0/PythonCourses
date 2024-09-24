def main():
    print("this file1's function is ececuted because you directly run the file")

def other():
    print("this file1's function is executed becaue you run this from other python file")


if __name__ == '__main__':
    main()

else:
    other()