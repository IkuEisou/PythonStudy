#! /usr/local/bin/python3
import athletemodel, yate, glob

data_files = glob.glob('data/*.txt')
athletes = athletemodel.getAll()

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))

print(yate.para("Select an athlete from the list to work with:"))
print(yate.start_form("generate_timeing_data.py"))
for each_ath in athletes:
    print(yate.radio_button("which_athlete", athletes[each_ath].name))
print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html"}))
