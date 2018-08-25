import os
import re
import sys


def links_in_directory(directory_path):
    os.chdir(directory_path)
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".py"):
            with open(os.path.abspath(file_name)) as f:
                file_data = f.read()
                links = re.findall(r'(https?://[^\s]+)', file_data)
                if links:
                    print(file_name)
                    print("\n".join(links)+"\n")


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        input_directory_path = argv[1]
        return links_in_directory(input_directory_path)
    except Exception as err:
        print(err, file = sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
