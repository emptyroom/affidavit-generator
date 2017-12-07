import random


f = open('test.txt', 'r')

# print(file)


random_number = random.randint(1, 100)
random_number2 = random.randint(1, 100)


print("Random numbers drawn are %r and %r" % (random_number, random_number2))
print('----------------------------------------------')

winner = ''
winner1 = ''
winner2 = ''

for i in f.readlines():

	for x in i:
		winner += x
		if x == ',':
			break

	if winner[:-1] == str(random_number):
		winner1 = i
		
				
	elif winner[:-1] == str(random_number2):
		winner2 = i

	
	winner = ''		
				
print("The winners are %s and %s" %(winner1,winner2))


f.close()



