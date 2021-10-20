avengers = {'captain':['shield', 'hammer'], 'ironman':'suit',
    'black widow':'elegance', 'thor':'hammer'}

xmen = ['magneto', 'mystique', 'wolverine']

marvel = {'ave':avengers, 'xmen':xmen}

print("marvel =", marvel)
print("----")
print("marvel['ave'] =", marvel['ave'])
print("----")
print("marvel['ave'] =", marvel['ave']['captain'])
print("----")
print("marvel['ave'][1] =", marvel['ave']['captain'][1])
print("----")
print("marvel['ave'][1][1] =", marvel['ave']['captain'][1][1])
print("----")
