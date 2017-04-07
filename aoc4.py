from string import ascii_lowercase

def

def is_real(room):
    checksum = room[room.index('[')+1:room.index(']')]
    sector = room[room.rindex('-')+1:room.rindex('[')]
    name = room[:room.rindex('-')]

    letter_counts = {}
    for letter in name:
        if letter in ascii_lowercase and letter not in letter_counts:
            letter_counts[letter] = name.count(letter)

    letter_counts = sorted([(key, value) for (value, key) in letter_counts.items()], reverse=True)

    for v, k in letter_counts:
        #  if they are all the same


    import ipdb
    ipdb.set_trace()

is_real('aaaaa-bbb-z-y-x-123[abxyz]')