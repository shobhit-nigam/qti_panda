germany = ['bayern', 'dortmund']
england = ['southampton', 'fulham']
spain = ['barca', 'Real madrid', 'sevilla', 'Valencia', 'atletico', germany]

print("spain =", spain)
bundesliga = germany
print("germany =", germany)
print("bundesliga =", bundesliga)
print("-----")
germany.insert(1, 'schalke')
germany.sort()
germany.append('wolfsburg')
print("spain =", spain)
print("germany =", germany)
print("bundesliga =", bundesliga)
