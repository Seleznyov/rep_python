games = [
		{"name": "Fallout",
		"sequels":["Fallout 2", "Fallout: Tactics", "Fallout. Brotherhood of the steel"],
		"studio": "Black Isle",
		"year": 1997},
		{"name": "Dragon Age: Origin",
		"sequels":["Dragon Age 2", "Dragon Age 3"],
		"studio": "Bioware",
		"year":2009},
		{"name": "Cyberpunk 2077",
		"sequels":[],
		"studio": "CD Project",
		"year": 2020},
		{"name": "Death Stranding",
		"sequels":[],
		"studio":"Kodjima Production",
		"year":2018},
		{"name": "Deus Ex",
		"sequels":["Deus Ex: Invisible War", "Deus Ex: Human Revolution", "Deus Ex: Mankind Divided"],
		"studio":"ION Storm",
		"year":2000},
		]

# 1.1
print("Сортировка по году")
val = []
for i in range(len(games)):
		val.append(games[i]["year"])
new_val = sorted(val)
# print(new_val)
for i in new_val:
	for x in games:
		if int(x["year"]) == i:
			print(x["name"])

#1.2
print("=====================================")
print("Сортировка по колличеству продложений")
val2 = []
for i in range(len(games)):
		val2.append(len(games[i]["sequels"]))
val3 = sorted(val2)

zzz = list(set(val3))[::-1]
# print(zzz)
for i in zzz:
	for x in games:
		if len(x["sequels"]) == i:
			print(x["name"])
