import glob
import sys
import re


def links_in_directory(directory_path):
    prev = -1
    for file_name in sorted(glob.glob(directory_path + "/unit*.py")):
        cur = (re.search(r'[\d]+', file_name.replace(directory_path, "")).group())
        with open(file_name) as f:
            file_data = f.read()
            links = re.findall(r'(https?://[^\s]+)', file_data)
            if links and prev != cur:
                print("\nUnit " + cur)
                prev = cur
            if links:
                print("\n".join(links))


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
