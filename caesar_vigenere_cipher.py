import string

letters_lower = string.ascii_lowercase

encoded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

offset = 10

decoded_message = ''

for character in encoded_message:
    if character in letters_lower:
        new_character = letters_lower[(letters_lower.index(character) + offset) % 26]
        decoded_message += new_character
    else:
        decoded_message += character

print(decoded_message)
print('\n')


decoded_message2 = 'caesar cipher is superb, bro. people would be confused if we sent these types of messages to them. haha!'

encoded_message2 = ''

for character in decoded_message2:
  if character in letters_lower:
    new_character = letters_lower[(letters_lower.index(character) - 10) % 26]
    encoded_message2 += new_character
  else:
    encoded_message2 += character
  
print(encoded_message2)
print('\n')


def caesar_encode(message, offset):
  encoded_message = ''
  for character in message:
    if character in letters_lower:
      new_character = letters_lower[(letters_lower.index(character) + offset) % 26]
      encoded_message += new_character
    else:
      encoded_message += character
  
  return encoded_message


def caesar_decode(message, offset):
  decoded_message = ''
  for character in message:
    if character in letters_lower:
      new_character = letters_lower[(letters_lower.index(character) + offset) % 26]
      decoded_message += new_character
    else:
      decoded_message += character
  
  return decoded_message

print(caesar_decode('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.', 10))
print('\n')

print(caesar_decode('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14))
print('\n')

print(caesar_decode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", 7))
print('\n')

encoded_message3 = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!'
keyword = 'friends'

keyword_phrase = ''

index = 0
for character in encoded_message3:

  if character in letters_lower:
    keyword_phrase += keyword[index % len(keyword)]
    index += 1
  else:
    keyword_phrase += character

decoded_message3 = ''

for character1, character2 in zip(encoded_message3, keyword_phrase):
  index1 = letters_lower.find(character1)
  index2 = letters_lower.find(character2)
  new_index = (index1 + index2) % 26

  if character1 in letters_lower:
    decoded_message3 += letters_lower[new_index]
  else:
    decoded_message3 += character1

print(decoded_message3)
print('\n')

def vigenere_encode(message, keyword):
  keyword_phrase = ''
  index = 0
  for character in message:
    if character in letters_lower:
      keyword_phrase += keyword[index % len(keyword)]
      index += 1
    else:
      keyword_phrase += character

  encoded_message = ''

  for character1, character2 in zip(message, keyword_phrase):
    index1 = letters_lower.find(character1)
    index2 = letters_lower.find(character2)
    new_index = (index1 - index2) % 26

    if character1 in letters_lower:
      encoded_message += letters_lower[new_index]
    else:
      encoded_message += character1

  return encoded_message

print(vigenere_encode(decoded_message3, 'friends'))