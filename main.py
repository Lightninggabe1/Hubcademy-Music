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
