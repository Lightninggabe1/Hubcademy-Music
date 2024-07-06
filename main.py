#new_module: 'creating a set'
genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

survey_genres = set(['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin'])
print(survey_genres)

survey_abbreviated = {genre[0:3] for genre in genre_results}
print(survey_abbreviated)

#new_module 'creating a frozenset'
top_genres = ['rap', 'rock', 'pop']

# Write your code below!
frozen_top_genres = frozenset(top_genres)

#new_module: 'adding to a set'
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
tag1_set = set(song_data['Retro Words'])
thing = [user_tag_1,user_tag_2,user_tag_3]
tag1_set.update(thing)

song_data['Retro Words'] = tag1_set

#new_module 'removing from a set'
song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag2_set = set(song_data_users['Retro Words'])
tag2_set.remove('onion')
tag2_set.remove('helloworld')
tag2_set.remove('spam')
song_data_users['Retro Words'] = tag_set
print(song_data_users)

#new module: 'finding elements in a set'
allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag3_set = set(song_data_users['Retro Words'])
bad_tags = []
for tag in tag3_set:
  if tag not in allowed_tags:
    bad_tags.append(tag)

for etags in bad_tags:
  tag3_set.remove(etags)

song_data_users['Retro Words'] = tag3_set
#new module:'Set Union'
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
new_song_data = {}
for key, val in song_data.items():
  song_tag_set = set(val)
  user_tag_set = set(user_tag_data[key])
  new_song_data[key] = song_tag_set | user_tag_set


#new module: 'set intersection'

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
retrowordsset = set(user_recent_songs['Retro Words'])
lowkeyspaceset = set(user_recent_songs['Lowkey Space'])
tags_int = lowkeyspaceset & retrowordsset

recommended_songs = {}

for key,val in song_data.items():
  for tag in val:
    if tag in tags_int:
      if key not in user_recent_songs:
        recommended_songs[key] = val
  
 print(recommended_songs)     






#new_module: "Set Difference"

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!
user_liked_songset = set(user_liked_song['Back To Art'])
user_disliked_songset = set(user_disliked_song['Retro Words'])
tag_diff = user_liked_songset.difference(user_disliked_songset)

recommended_songs = {}
for key,val in song_data.items():
  for tag in val:
    if tag in tag_diff:
      if key not in user_liked_song and key not in user_disliked_song:
        recommended_songs[key] = val

print(recommended_songs)
