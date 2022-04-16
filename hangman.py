import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  0   |
      |
      |
     ===''', '''
  +---+
  0   |
  |   |
      |
     ===''', '''
  +---+
  0   |
 /|   |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
 /    |
     ===''', '''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']

words = 'aigle babouin baleine belette blaireau bouc canard \
		 canari castor cerf chameau chat cheval chien chouette \
		 cigogne cobra cochon corbeau corneille couleuvre \
		 couyote crapaud crotale cygne dauphin dindon dromadaire \
		 faucon fourmi furet gorille grenouille hibou \
		 hippopotame lama lapin lion loup mouton mule mygale \
		 oie otarie ours palourde panda paresseux perroquet \
		 phoque pigeon poisson puma putois python rat renard \
		 renne requin salamandre saumon singe souris taupe \
		 tigre tortue truite '.split()

def get_random_word(word_list):
	# Retourne un mot au hasard parmi ceux d'une liste.
	word_index = random.randint(0, len(word_list) - 1)
	return word_list[word_index]

def display_board(missed_letters, correct_letters, secret_word):
	print(HANGMAN_PICS[len(missed_letters)])
	print("------------------------------------------------------------------------")

	print("Mauvaises lettres :", end = ' ')
	for letter in missed_letters:
		print(letter, end=' ')
	print()

	blanks = '_' * len(secret_word)
	#Remplace les tirets par les lettres correctement devinees.
	for i in range(len(secret_word)):
		if secret_word[i] in correct_letters:
			blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
	#Affiche le mot secret avec des espaces entre les lettres.
	for letter in blanks:
		print(letter, end = " ")
	print()

def get_guess(already_guessed):
	# Affiche la lettre saisie per le joueur. S'assure qu'il s'agit d'un unique lettre et de rien d'autre.
	while True:
		print("Propose une lettre.")
		guess = input()
		guess = guess.lower()
		if len(guess) !=1:
			print("Propose une seule lettre STP.")
		elif guess in already_guessed:
			print("Tu as déjà demandé cette lettre.")
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print("Propose une lettre STP.")
		else:
			return guess

def play_again():
	# Retourne True si le joueur veut recommencer, False sinon.
	print("Veux-tu rejouer (oui ou non) ?")
	return input().lower().startswith('o')

print("P E N D U")
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
	display_board(missed_letters, correct_letters, secret_word)

	# Invite le joueur a proposer une lettre
	guess = get_guess(missed_letters + correct_letters)

	if guess in secret_word:
		correct_letters = correct_letters + guess

		# Verifie si le joueur a gagné.
		found_all_letters = True
		for i in range(len(secret_word)):
			if secret_word[i] not in correct_letters:
				found_all_letters = False
				break
		if found_all_letters:
			print("Oui! Le mot secret est " + secret_word.upper() + '! Tu a gagné!')
			game_is_done = True
	else:
		missed_letters = missed_letters + guess

		#Vérifie si le joueur a perdu.
		if len(missed_letters) == len(HANGMAN_PICS) - 1:
			display_board(missed_letters, correct_letters, secret_word)
			print(('Tu as epuisé tous tes essais ! \nAprès ' + str(len(missed_letters)) + ' mauvaises lettres et ' + str(len(correct_letters)) +
			 ' lettres exactes, le mot secret était "' + secret_word + '".'))
			game_is_done = True

# Demande au joueur s'il veut recommencer (seulement si la partie est finie

	if game_is_done:
		if play_again():
			missed_letters = ''
			correct_letters = ''
			game_is_done = False
			secret_word = get_random_word(words)
		else:
			break
