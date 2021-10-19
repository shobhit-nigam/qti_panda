germany = ['bayern', 'dortmund']
england = ['southampton', 'fulham']
spain = ['barca', 'Real madrid', 'sevilla', germany, 'Valencia', 'atletico']

print("spain =", spain)
print("germany =", germany)
print("-----")
spain[3][0] = 'wolfsberg'
print("spain =", spain)
print("germany =", germany)

# error
spain[3][0][0] = 'W'
