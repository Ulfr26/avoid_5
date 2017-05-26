#!usr/bin/python

in_str = input("Input your symbols: ").split()
print("\n")

i = 0
j = 0
found_glyph = 0

for word in in_str:
    i += 1
    for char in word:
        j += 1
        if ord(char) == 69 or ord(char) == 101:
            print("A fifthglyph was found amongst your symbols at word " + str(i))
            found_glyph = 1

if found_glyph == 0:
    print("The fifthglyph was not found in your symbols.")
