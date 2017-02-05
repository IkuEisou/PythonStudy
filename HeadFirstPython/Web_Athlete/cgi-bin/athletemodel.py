import pickle, glob
from athletelist import AthleteList

def get_coach_data(file):
    try:
        with open(file) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as ferr:
        print("File Error：" + str(ferr))
        return None

def _sanitize(time_str):
    if ':' in time_str:
        splitter = ':'
    elif '-' in time_str:
        splitter = '-'
    else:
        return time_str
    (mins,secs) = time_str.split(splitter)
    return mins + '.' + secs

def sanitize(reclist):
    cleanl = set([_sanitize(t) for t in reclist])
    return sorted(cleanl)

def crt_athlete(data):
    a = AthleteList(data.pop(0), data.pop(0), sanitize(data))
    return a

def getAll():
    data_files = glob.glob('data/*.txt')
    #print(data_files)
    all_ath = {}
    for each_f in data_files:
        data = get_coach_data(each_f)
        ath = crt_athlete(data)
        all_ath[ath.name] = ath
    return all_ath
            
def put2store(fileName='athletes.pickle'):
    try:
        with open(fileName, 'wb') as athf:
            pickle.dump(getAll(), athf)
    except IOError as ioerr:
        print('File err(put2store):' + str(ioerr))

def get_from_store(fileName='athletes.pickle'):
    try:
        with open(fileName, 'rb') as athf:
           all_athletes = pickle.load(athf)
##        for each_ath in all_athletes:
##            print(all_athletes[each_ath].name + ' '
##                  + all_athletes[each_ath].dob)
        return all_athletes
    except IOError as ioerr:
        print('File err(get_from_store):' + str(ioerr))
        return None

def get_names_from_store():
    athletes = get_from_store()
    response = [athletes[each_ath].name for each_ath in athletes]
    return(response)
##put2store()
##get_from_store()
