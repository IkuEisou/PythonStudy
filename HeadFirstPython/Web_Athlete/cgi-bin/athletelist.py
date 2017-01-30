
class AthleteList(list):
    def __init__(self, a_name, a_dob, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def prtAth(self):
        print(self.name + '\'s times are: ' + str(self))

    def prtTop3(self):
         print(self.name + '\'s fastest times are: ' + str(self[0:3]))
         
    def top3(self):
        return(self[0:3])
