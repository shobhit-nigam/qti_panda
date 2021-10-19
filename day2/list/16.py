germany = ['bayern', 'dortmund']
england = ['southampton', 'fulham']
spain = ['barca', 'Real madrid', 'sevilla', 'Valencia', 'atletico', germany.copy()]

print("spain =", spain)
bundesliga = germany.copy()
print("germany =", germany)
print("bundesliga =", bundesliga)
print("-----")
germany.insert(1, 'schalke')
germany.sort()
germany.append('wolfsburg')
print("spain =", spain)
print("germany =", germany)
print("bundesliga =", bundesliga)

# spain.insert(spain)
