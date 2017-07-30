# count Vowel in the string.

vowels = 'AEIOU'
dict = {}.fromkeys(vowels, 0)
string = raw_input("Enter String : ")

for i in string.upper():
	if i in dict:
		dict[i] += 1
		
print (dict)
