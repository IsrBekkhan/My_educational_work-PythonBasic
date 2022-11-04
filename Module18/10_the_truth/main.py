def cezar_decrypt(word):
    alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = 25
    decrypted_letters = []

    for letter in word:
        if letter.islower():
            decrypted_letters.append(alphabet_low[(alphabet_low.index(letter) + shift) % 26])
        elif letter.isupper():
            decrypted_letters.append(alphabet_up[(alphabet_up.index(letter) + shift) % 26])
        elif letter == '/':
            decrypted_letters.append(letter)
        elif letter == '(':
            decrypted_letters.append("'")
        elif letter == '+':
            decrypted_letters.append("*")
        elif letter == '.':
            decrypted_letters.append('-')
        elif letter == '"':
            decrypted_letters.append('!')

    return ''.join(decrypted_letters)

def letters_shift(word, step):
    shift = step % len(word)
    res = word[-shift:] + word[:-shift]

    return res


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm' \
       ' tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc' \
       ' ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft' \
       ' (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj' \
       ' Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg' \
       ' hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf' \
       ' zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug' \
       ' ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs' \
       ' boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb' \
       ' Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO' \
       ' bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()
decrypted_text = []
shifted_text = []

for word in text:
    decrypted_word = cezar_decrypt(word)
    decrypted_text.append(decrypted_word)
step = 3
for word in decrypted_text:
    shifted_word = letters_shift(word, step)
    if shifted_word.endswith('/'):
        step += 1
    shifted_text.append(shifted_word)

joined_text = ' '.join(shifted_text)
splited_text = joined_text.split('/')
joined_text_2 = '.\n'.join(splited_text)
print('Расшифрованный текст:\n', joined_text_2)

