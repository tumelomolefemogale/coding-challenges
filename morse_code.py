'''Given a Morse code string, return the decoded message.
Letters are separated by a single space
Words are separated by three spaces'''

morse_letter_dic = {'.-': 'A', '-.': 'N', '-...': 'B', '---': 'O',
'-.-.': 'C', '.--.': 'P', '-..': 'D', '--.-': 'Q',
'.': 'E', '.-.': 'R', '..-.': 'F', '...': 'S',
'--.':	'G', '-': 'T', '....': 'H', '..-': 'U',
'..': 'I', '...-': 'V', '.---': 'J', '.--': 'W',
'-.-': 'K', '-..-': 'X', '.-..': 'L', '-.--': 'Y',
'--': 'M', '--..': 'Z'}


def decode_morse(morse):
    morse_list_split = morse.split(' ')
    morse_list = []

    for element in morse_list_split:
        if element == '':
            morse_list.append(' ')
        else:
            morse_list.append(element)

    letters_list = []

    for element in morse_list:
        if element == ' ':
            letters_list.append(element)
        else:
            letters_list.append(morse_letter_dic[element])

    print(''.join(letters_list))


print(decode_morse("--.."))
print(decode_morse("... --- ..."))
print(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--."))
print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."))
print(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --."))
