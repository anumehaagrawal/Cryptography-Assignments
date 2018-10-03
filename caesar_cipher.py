with open("caesar_cipher_text", "r") as f:
	data = f.readlines()
 
import operator
for line in data:
	words = line.split()
frequency={}
for i in words:
	for j in i:
		if j not in frequency.keys():
			frequency[str(j)]=1
		else:
			frequency[str(j)]=frequency[str(j)]+1
frequency=sorted(frequency.items(), key=operator.itemgetter(1))

print(frequency)
# Using frequency analysis compare the frequency of highest letter with english letter highest that is e
shift = 10

def shifttext(text, shift):
    a = ord('a')
    return ''.join(
        chr((ord(char) - a + shift) % 26 + a) if 'a' <= char <= 'z' else char
        for char in text.lower())
for line in data:
	print(shifttext(line,shift))