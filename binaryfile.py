#binaryfile.py
import pickle
def is_gif(fname):
    f = open(fname, 'br')
    first4 = tuple(f.read(4))
    return first4 == (0x47, 0x49, 0x46, 0x38)

def make_pickled_file():
    grades = {'alan' : [4,8,10,10],
              'tom' : [7,7,7,8],
              'dan' : [5,None,7,7],
              'may' : [10,8,10,10]}
    outfile = open('grades.dat', 'wb')
    pickle.dump(grades, outfile)

def get_pickled_data():
    infile = open('grades.dat', 'rb')
    grades = pickle.load(infile)
    return grades
