p_phrase = "was it a car or a cat I saw"
r_phrase = ''
for char in p_phrase:
    r_phrase = char + r_phrase

if p_phrase == r_phrase:
    print("string is reversible")

else:
    print("string is not reversible")