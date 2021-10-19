germany = ('bayern', 'dortmund')
england = ('southampton', 'fulham')
spain = ('barca', 'Real madrid', 'sevilla', germany, 'Valencia', 'atletico')

print("type of spain =", type(spain))
print("spain =", spain)
print("germany =", germany)
print("-----")

# error
england[1]="man city"
print("spain =", spain)
print("germany =", germany)
