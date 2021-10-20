avengers = {'captain':['shield', 'hammer'], 'ironman':'suit',
    'black widow':'elegance', 'thor':'hammer'}

dc = {'wonder woman':'lasso', 'batman':'rich', 'flash':'fast'}

superhero = avengers.copy()

superhero.update(dc)

print(superhero)

# error
avengers + dc
