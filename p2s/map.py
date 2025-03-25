import sys
import ast
import numpy as np


def main():
    if sys.stdin.isatty():
        print("No input provided. Please pipe data into this script.", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) < 2:
        print("No lambda provided. Please provide a lambda as an argument.", file=sys.stderr)
        sys.exit(1)

    tree = ast.parse(f"lambda {sys.argv[1]}", mode='eval')
    f = eval(compile(tree, filename='<ast>', mode='eval'))
    for x in sys.stdin:
        print(f(x[:-1]))
