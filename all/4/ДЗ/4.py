# Профиль пользователя
me = {"name": "Egor",
      "my_artists": ["Bon Jovi", "Ben Nichols","Test"],
      "songs_for_me":[]
      }

# список песен
songs = [
        {"name": "Сгораю", "band":"Noise MC"},
        {"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"},
        {"artist":"Guns N' Roses", "name": "Civil War", "long": 7.42, "band":True, "album": "Use Your Illusion II"},
        {"artist":"Ben Nichols", "name": "The last pale light in the west", "long": 3.24, "band":False, "album": None},
        {"name": "Сгораю", "band":"Noise MC"},
        {"name": "", "band":"", "long": 8.42},
        {"artist":"Bon Jovi", "name": "The Distance", "long": 3.25, "band":True, "album": "Bounce"},
        {"artist":"Bon Jovi", "name": "Open All Night", "long": 3.26, "band":True, "album": "Bounce"},
        ]

me["songs_for_me"] = {}
print(me)

for i in range(len(songs)):
    for artist in me["my_artists"]:
        if songs[i].get("artist") == artist:
            # key = artist
            if type(me["songs_for_me"].get(artist)) == list:
                me["songs_for_me"][artist].append(songs[i])
            else:
                me["songs_for_me"][artist] = [songs[i]]
print(me)
