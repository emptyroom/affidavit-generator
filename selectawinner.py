import random


f = open('test.txt', 'r')

# Generate two random numbers
random_number = random.randint(1, 8)
random_number2 = random.randint(1, 8)
random_number3 = random.randint(1, 8)
random_number4 = random.randint(1, 8)

print("Random numbers drawn are %r, %r, %r, and %r" % (random_number,
random_number2, random_number3, random_number4))

print('----------------------------------------------')

input("Press enter to select the winners")

winner = ''
winner1 = ''
winner2 = ''
winner3 = ''
winner4 = ''

for i in f.readlines():

    for x in i:
        winner += x
        if x == ',':
            break

    if winner[:-1] == str(random_number):

        winner1 = i

    elif winner[:-1] == str(random_number2):
        winner2 = i

    elif winner[:-1] == str(random_number3):
        winner3 = i

    elif winner[:-1] == str(random_number4):
        winner4 = i

    winner = ''

print("The winners are %s,  %s,  %s, %s"
    % (winner1, winner2, winner3, winner4))


f.close()
