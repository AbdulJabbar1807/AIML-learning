import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("I'm " + sys.argv[1]) # type: ignore