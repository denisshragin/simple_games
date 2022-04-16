import random

NUM_DIGITS = 3
MAX_GUESS = 10

def get_secret_number():
	# Return a string of NUM_DIGITS all different characters
	numbers = list(range(10))
	random.shuffle(numbers)
	secret_number = ''
	for i in range(NUM_DIGITS):
		secret_number += str(numbers[i])
	return secret_number

def get_clues(guess, secret_number):
	# Return a string containing Pico/Fermi/Bagels indices
	if guess == secret_number:
		return 'You found it !'

	clues = []
	for i in range(len(guess)):
		if guess[i] == secret_number[i]:
			clues.append('Fermi')
		elif guess[i] in secret_number:
			clues.append('Pico')
	if len(clues) == 0:
		return 'Bagels'

	clues.sort()
	return ' '.join(clues)

def is_only_digits(number):
	# Return True if the string content only a chiffres
	if number == ' ':
		return False

	for i in number:
		if i not in '1 2 3 4 5 6 7 8 9 0'.split():
			return False

	return True


print("I'm thinking of a number of {NUM_DIGITS} digits. Try to guess it !".format(NUM_DIGITS=NUM_DIGITS))
print("The clues I give are the following...")
print("When I say:                It means:")
print("            Bagels                     No number is incorrect.")
print("            Pico                       A number is correct but misplaced.")
print("            Fermi                      A number is correct and well placed.")

while True:
	secret_number = get_secret_number()
	print(f"You get {MAX_GUESS} tries.")

	guess_taken = 1
	while guess_taken <= MAX_GUESS:
		guess = ''
		while len(guess) != NUM_DIGITS or not is_only_digits(guess):
			print(f"Try #{guess_taken} : ")
			guess = input()

		print(get_clues(guess, secret_number))
		guess_taken +=1

		if guess == secret_number:
			break
		if guess_taken > MAX_GUESS:
			print(f"You're out of tries!", "The answer is {secret_number}. ")

	print("Do you want to play again (Yes or No)?")
	if not input().lower().startswith('y'):
		break