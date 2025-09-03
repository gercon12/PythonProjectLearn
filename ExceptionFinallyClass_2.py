def process_file():
    try:
        f = open("C:\\Users\\DELL LATITUDE\\PycharmProjects\\PythonProjectLearn\\book.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()

process_file()