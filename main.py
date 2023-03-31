def Morse_Translator():
    if language == 'rus':
        morse_dict = morse_dict_rus
    else:
        morse_dict = morse_dict_eng
    if language == 'rus':
        text = input('Введите текст: ').upper()
    else:
        text = input('Enter the text: ').upper()
    morse_text = ''
    for char in text:
        if char == ' ':
            morse_text += '/'
        elif char in morse_dict:
            morse_text += morse_dict[char] + ' '
        else:
            morse_text += char
    if language == 'rus':
        print('Текст в азбуке Морзе: ' + morse_text)
        input()
    else:
        print('Morse code text: ' + morse_text)
        input()

def Morse_Decoder():
    if language == 'rus':
        morse_dict = morse_dec_rus
    else:
        morse_dict = morse_dec_eng
    if language == 'rus':
        morse_text = input('Введите код Морзе: ')
    else:
        morse_text = input('Enter the Morse code: ')
    text = ''
    for code in morse_text.split(' '):
        if code == '':
            text += ' '
        elif code in morse_dict:
            text += morse_dict[code]
        else:
            text += code
    if language == 'rus':
        print('Текст: ' + text)
        input()
    else:
        print('Text: ' + text)
        input()

morse_dict_eng = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}
morse_dict_rus = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}
morse_dec_eng = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' '}
morse_dec_rus = {'.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д', '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й', '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О', '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У', '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш', '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '..-..': 'Э', '..--': 'Ю', '.-.-': 'Я', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' '}

language = input('Select a language: English (eng) or Русский (rus)? ')
if language == 'rus':
    select = input('Выберите функцию Morse Code Translator (1) или Morse Code Decoder (2) ')
else:
    select = input('Select the function Morse Code Translator (1) or Morse Code Decoder (2) ')

if select == '1':
    Morse_Translator()
elif select == '2':
    Morse_Decoder()
else:
    if language == 'rus':
        print('Неизвестное значение')
        input()
    else:
        print('Unknown value')
        input()