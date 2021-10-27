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
# print("Сортировка по году")
# sorted_years = []
# for game in games:
# 		sorted_years.append(game["year"])
# sorted_years = sorted(sorted_years)
# print(sorted_years)
#
# games_sorted_by_year = []
# for year in sorted_years:
# 	for game in games:
# 		if int(game["year"]) == year:
# 			games_sorted_by_year.append(game)
# 			# print(x["name"])
# print(games_sorted_by_year)

#1.2
print("=====================================")
print("Сортировка по колличеству предложений")
sequels_games = []
for game in games:
		sequels_games.append(len(game["sequels"]))
sorted_sequels_games = sorted(sequels_games)
print(sorted_sequels_games)
counts_sequels = list(set(sorted_sequels_games))[::-1]
print(counts_sequels)

sorted_by_sequels = []
for i in counts_sequels:
	for x in games:
		if len(x["sequels"]) == i:
			sorted_by_sequels.append(x)
			# print(x["name"])
print(sorted_by_sequels)