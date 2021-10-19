spain = ['barca', 'Real madrid', 'sevilla', 'Valencia', 'atletico']
germany = ['bayern', 'dortmund']
england = ['southampton', 'fulham']

bundesliga = germany
print("germany =", germany)
print("bundesliga =", bundesliga)
print("-----")
germany.insert(1, 'schalke')
germany.sort()
germany.append('wolfsburg')
print("germany =", germany)
print("bundesliga =", bundesliga)
