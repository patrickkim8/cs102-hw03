import sys
from typing import List

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    # TODO: Fill in the actual logic here!
    with open(sys.argv[1]) as s:
        for line in s:
            value = line.split(",")

            y = 0
            for i in value:
                x = float(i)
                y = x + y
                z = y / len(value)
            print(f"{z}")





if __name__ == "__main__":
    main()
