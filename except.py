#except.py
def get_age():
    while True:
        try:
            n = int(input('How old are you?'))
            return n
        except ValueError:
            print('Please enter an integer value.')

def convert2int1(s,base):
    try:
        return int(s,base)
    except(ValueError, TypeError):
        return 'error'

def convert2int2(s,base):
    try:
        return int(s,base)
    except ValueError:
        return 'value error'
    except TypeError:
        return 'type error'

def convert2int3(s,base):
    try:
        return int(s,base)
    except:
        return 'error'

def invert(x):
    try:
        return 1/x
    except ZeroDivisionError:
        return 'error'
    finally:
        print('invert(%s) done' % x)

def printfile(fname):
    num = 1
    with open(fname, 'r') as f:
        for line in f:
            #print('%04d %s' % (num, line), end = '')
            print('{0:04} {1}'.format(num, line), end = '')
            num =num+1
            
