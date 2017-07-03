import sys, getopt

ifile = ""
ofile = ""

myopts, args = getopt.getopt(sys.argv[1:], "i:o")


# o == option
# a == argument passed to the option

for o, a in myopts:
    if o =="-i":
        ifile = a
    elif o == "-o":
        ofile = a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])

print("Input file : %s and output file: %s " % (ifile, ofile))
