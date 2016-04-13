#printfile.py

def print_file1(fname):
    f = open(fname, 'r')
    for line in f:
        #print(line, end = '')
        print(line)
    f.close()

def print_file2(fname):
    f = open(fname, 'r')
    print(f.read())
    f.close()
