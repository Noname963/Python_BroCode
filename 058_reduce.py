# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 vlaue remains
# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y,:x + y,letters)
print(word)