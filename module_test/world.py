# filename : world.py

import hello

from hello import Hello

def main() :
    print("This is the test of test() in hello.py: ")
    hello.test()

    print("This is the test of main() in hello.py: ")
    hello.main()

    print("This is the test of class Hello in hello.py: ")
    tmp = hello.Hello()
    tmp.show_string()

    print("This is the test of class Hello via \"from hello import Hello\"")
    tmp = Hello()
    tmp.show_string()


if __name__ == "__main__" :
    main()
