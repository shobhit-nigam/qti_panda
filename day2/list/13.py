spain = ['barca', 'Real madrid', 'sevilla', 'Valencia', 'atletico']
listnum = [23, 78, 45, 84, 10, 23, 45, 67]

germany = ['bayern', 'dortmund']
england = ['southampton', 'fulham']

print("germany =", germany)
print("len of germany =", len(germany))
print("-----")
germany.append(spain)
print("germany =", germany)
print("len of germany =", len(germany))
print("-----")

print("england =", england)
print("len of england =", len(england))
print("-----")
england.extend(spain)
print("england =", england)
print("len of england =", len(england))
