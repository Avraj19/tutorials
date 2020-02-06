# define the following keys using a dictionary

# beginning
# Middle
# End
# Hero/heroine

# populate the value of the key, with a story broken into beginning, middle, end.
# use your hero/heroine as well

# Print the story using by calling your dictionary key individually
# Interpolate
hero_name = input('Enter the name of your hero: ').strip().capitalize()

story_line_vol1 = {
    'Hero': hero_name,
    'Beginning': 'In the beginning there was our god',
    'Middle': 'Then came the universe with all its glory',
    'End': 'After millions of years of peace there was war, that threaten the universe.'
}

story_line_vol2 = {
    'Beginning': 'The war raged on',
    'Middle': 'God was captured by and week by his sister the darkness ',
    'End': hero_name + ', Sam, the devil, the angels and some witch teamed up to free god and defeated the darkness'
}

story_collection = {
    'vol1': story_line_vol1,
    'vol2': story_line_vol2
}

print(story_collection)
