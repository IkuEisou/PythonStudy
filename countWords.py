#countWords.py
import re
def fenci(s):
    p = re.compile(r'\w+')
    return p.findall(s)

def countChars(fname):
    file = open(fname, 'r')
    counter = 0
    for line in file:
        counter += len(line)
    return counter

def countWords(fname):
    d = getWords(fname)
    return sum(d[k] for k in d)

def countLines(fname):
    file = open(fname, 'r')
    counter = 0
    for line in file:
        counter += 1
    return counter

def getWords(fname):
    file = open(fname, 'r')
    d = {}
    for line in file:
        s = fenci(line)
        for word in s:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d

def listWords(fname):
    d = getWords(fname)
    lst = []
    for k in d:
        pair = (d[k], k)
        lst.append(pair)
    lst.sort()
    lst.reverse()
    return lst

def print_file_stats(fname):
    """
     Print statistics for the given file.
    """

    print("The file '%s' has: " % fname)
    print("  %4s characters" % countChars(fname))
    print("  %4s words" % countWords(fname))
    print("  %4s lines" % countLines(fname))
    print("\nThe top 10 most frequent words are:")
    lst = listWords(fname)
    i = 1
    for count, word in lst[:10]:
        print('%2s. %4s %s' % (i, count, word))
        i += 1
