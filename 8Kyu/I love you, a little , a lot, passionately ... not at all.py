def how_much_i_love_you(nb_petals):
    petals = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    return petals[(nb_petals - 1) % 6]