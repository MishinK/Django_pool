#coding=utf8
#!/usr/bin/env python3

from local_lib import path

def main():
    dir = path.Path("dir")
    dir.mkdir_p()
    file = path.Path("dir/file").touch()
    file.write_text("Hello World!")
    print("File content: {0}".format(file.read_text()))

if __name__ == '__main__':
    main()