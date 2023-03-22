### Morse Code Translator
Morse Code-Code-Translator is a program in the Python programming language that accepts text entered by the user and translates it into Morse code, replacing letters with their corresponding characters. When the program starts, the user is prompted to select the language of the text (English or Russian), and then enter the text itself.

The program uses dictionaries to translate letters into Morse code. Depending on the selected language, the program selects the appropriate dictionary. Russian Russian uses a dictionary containing the encoding of English letters and numbers, and for the Russian language - a dictionary with the encoding of Russian letters and numbers.

Then, the program iterates through each character of the entered text and, if the character is a letter or a number, replaces it with the corresponding Morse code sign using the appropriate dictionary. If the symbol is not a letter or a number, it remains unchanged.

At the end of the program, the translated text is displayed on the screen in Morse code format, where each character is replaced with its corresponding Morse code sign. Characters are separated by spaces, and words are separated by a "/" sign.
