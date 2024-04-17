def get_status(wins):
    score = {'Bob':1, 'Anna':1}
    for i in wins:
        if i == 'Bob':
            score['Bob'] += 1
        else:
            score['Anna'] += 1
        if score['Bob'] >= 4 and score['Bob'] >= score['Anna'] + 2:
            return 'Bob Wins'
        elif score['Anna'] >= 4 and score['Anna'] >= score['Bob'] + 2:
            return 'Anna Wins'
        elif score['Bob'] == 3 and score['Anna'] == 3:
            return 'Deuce'
        elif score['Bob'] == 4 and score['Anna'] == 3:
            return 'Bob Advantage'
        elif score['Anna'] == 4 and score['Bob'] == 3:
            return 'Anna Advantage'
        else:
            return f"Bob {score['Bob']*15} Anna {score['Anna']*15}"



print(get_status((['Bob','Anna','Bob']))) #Bob 30 Anna 15
print(get_status((['Bob','Anna','Bob','Anna']))) #Deuce
print(get_status((['Bob','Anna','Bob','Anna','Bob']))) #Bob Advantage
print(get_status((['Bob','Anna','Bob','Anna','Bob','Anna']))) #Deuce
print(get_status((['Bob','Anna','Bob','Anna','Bob','Anna','Bob']))) #Bob Advantage
print(get_status((['Bob','Anna','Bob','Anna','Bob','Anna','Bob','Bob']))) #Bob Wins



#Belom Jadi :(