#new_module: 'set review'

music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
my_tags = frozenset(['pop', 'electronic', "relaxing", 'slow', 'synth'])

frozen_tag_union = my_tags | music_tags

regular_tag_intersect = music_tags.intersection(my_tags)

frozen_tag_difference = my_tags - music_tags

regular_tag_sd = music_tags.symmetric_difference(my_tags)
