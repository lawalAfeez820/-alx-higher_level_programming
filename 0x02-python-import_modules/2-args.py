#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    length = len(argv) - 1

    if length == 0:
          print("0 arguments.")
    else:
        print(f"{length} arguments:")
        argv = argv[1:]
        for i,j in enumerate(argv):
            print(f"{i + 1}: {j}")
