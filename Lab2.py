import sys

def print_arguments():
    script_name = sys.argv[0]
    arguments = sys.argv[1:]

    print("Script Name:", script_name)
    print("Arguments:", arguments)

    # Print script name and arguments combined
    print("Script and Arguments:", script_name, *arguments)

print_arguments()
