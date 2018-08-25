import os
import re
import sys

def links_in_directory(directory_path):
    try:
        os.chdir(directory_path)
    except FileNotFoundError:
        print(directory_path, " not found")
    else:
        for pyfile in os.listdir(directory_path):
            if pyfile.endswith(".py"):
                with open(os.path.abspath(pyfile)) as f:
                    lines = f.read()
                    if "http" in lines:
                        print(pyfile)
                        print("\n".join(re.findall(r'(https?://[^\s]+)', lines))+"\n")

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            input_directory_path = argv[1]
        except IndexError as ierr:
            raise ierr
        return links_in_directory(input_directory_path)
    except Exception as err:
        print(err, file = sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
