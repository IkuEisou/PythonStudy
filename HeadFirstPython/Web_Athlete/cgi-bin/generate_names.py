import json, athletemodel, yate

names = athletemodel.get_names_from_store()
print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))
