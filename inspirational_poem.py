#Indexes
poem = "Where am I?"

print(poem[-6])

#the first character in an index is always 0

#Slicing
poem_2 = "Where am I?"

print(poem_2[:4])
print(poem_2[4:])

#Putting the colon before the character you want includes everything up to, excluding that character.
#but if you put the colon after the character, it will include that character and everything that comes after
#Number on left of colon, inclusive. Number on right of the colon, exclusive.

poem_3 = "Where am I?"

print(poem_3[6:-3])

#or you can do

name = "Payton Dison"

start_of_last = 7

print(name[start_of_last:start_of_last+2])