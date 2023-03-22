# Defining dictionaries for translating letters into Morse code
morse_dict_eng = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
morse_dict_rus = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}

# User's request for the input text language
language = input('Select a language: English (eng) or Русский (rus)? ')

# Defining a dictionary for the selected language
if language == 'rus':
    morse_dict = morse_dict_rus
else:
    morse_dict = morse_dict_eng

# Request for a text to be translated into Morse code
if language == 'rus':
    text = input('Введите текст: ').upper()
else:
    text = input('Enter the text: ').upper()

# We translate the text into Morse code, replacing the letters with their corresponding signs
morse_text = ''
for char in text:
    if char == ' ':
        morse_text += '/'
    elif char in morse_dict:
        morse_text += morse_dict[char] + ' '
    else:
        morse_text += char

# Output the result
if language == 'rus':
    print('Текст в азбуке Морзе: ' + morse_text)
else:
    print('Morse code text: ' + morse_text)