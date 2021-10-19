germany = ['bayern', 'dortmund']
england = ('southampton', 'fulham')
spain = ('barca', 'Real madrid', 'sevilla', germany, 'Valencia', 'atletico')

print("type of spain =", type(spain))
print("type of germany =", type(germany))
print("spain =", spain)
print("germany =", germany)
print("-----")

spain[3].append("wolfsburg")
print("spain =", spain)
print("germany =", germany)
print("-----")

# error
spain.append("cccc")
