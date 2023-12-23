import math

a_NORMA = 0.116
o_NORMA = 0.126
e_NORMA = 0.102
y_NORMA = 0.040
bI_NORMA = 0.024
u_NORMA = 0.077

def get_letters_interp(letters_sum, letter_NORMA, letters_count): 
    letter_pi = round(letters_sum / letters_count, 3)
    letter_sigma = round(math.sqrt(letter_NORMA*(1-letter_NORMA)/letters_count), 3)
    letter_ai = round((letter_pi-letter_NORMA)/letter_sigma, 3)
    return (letter_NORMA, letters_sum, letter_pi, letter_sigma, letter_ai)

def print_row(letters_name, letters_interp, letters_color):
    letter_NORMA, letters_sum, letter_pi, letter_sigma, letter_ai = letters_interp
    print(f'{letters_name} \t {letters_sum} \t {letter_pi} \t {letter_NORMA} \t {letter_sigma} \t\t {letter_ai} \t {letters_color}')

vowels = 'уеыаоэяиюё'
consonants = 'бвгджзйклмнпрстфхцчшщьъ'
letters_count = 0
letters = {}
letters_udarenie = {}

text = "И О'н к устА'м моИ'м принИ'к, \
И вЫ'рвал грЕ'шный мО'й язЫ'к,\
И празднослО'вный и лукА'вый,\
И жА'ло мУ'дрыя змеИ'\
В устА' замЕ'ршие моИ' ВложИ'л деснИ'цею кровА'вой.\
И О'н мнЕ' грУ'дь рассё'к мечО'м, И сЕ'рдце трЕ'петное вЫ'нул,\
И У'гль, пылА'ющий огнЁ'м, ВО' грУ'дь отвЕ'рстую водвИ'нул.\
 Как трУ'п в пустЫ'не Я' лежА'л,\
 И бО'га глА'с кО' мнЕ' воззвА'л:\
 'ВосстА'нь, прорО'к, и вИ'ждь, и внЕ'мли,\
 ИспО'лнись вО'лею моЕ'й\
 И, обходЯ' морЯ' и зЕ'мли, ГлагО'лом жгИ' сердцА' людЕ'й.'\
" 

# text = "Вы пО'мните,\
# ВЫ' всЁ', конЕ'чно, пО'мните,\
# КА'к Я' стоЯ'л,\
# ПриблИ'зившись к стенЕ',\
# ВзволнО'ванно ходИ'ли вЫ' пО' кО'мнате\
# И чтО'-то рЕ'зкое\
# В лицО' бросА'ли мнЕ'.\
# ВЫ' говорИ'ли:\
# НА'м порА' расстА'ться,\
# ЧтО' вА'с измУ'чила\
# МоЯ' шальнА'я жИ'знь,\
# ЧтО' вА'м порА' зА' дЕ'ло принимА'ться,\
# А мО'й удЕ'л —\
# КатИ'ться дА'льше, внИ'з."
lowered_text = text.lower()
for i, symb in enumerate(lowered_text):
    if symb in vowels or symb in consonants:
        letters[symb] = 1 if not symb in letters else letters[symb]+1
        letters_count += 1
    if symb == "'" and lowered_text[i-1] in vowels:
        letters_udarenie[lowered_text[i-1]] = 1 if not lowered_text[i-1] in letters_udarenie else letters_udarenie[lowered_text[i-1]]+1
        letters[lowered_text[i-1]] += 1


print('\t ni \t pi \t pin \t sigmai \t ai \t Цвет')
print_row('А+Я', get_letters_interp(letters['а']+letters['я'], a_NORMA, letters_count), 'Ярко-красный')
print_row('О+0.5Ё', get_letters_interp(letters['о']+0.5*letters['ё'], o_NORMA, letters_count), 'Белый, желтый')
print_row('Е+0.5Ё', get_letters_interp(letters['е']+0.5*letters['ё'], e_NORMA, letters_count), 'Желтый, зеленый')
print_row('У+Ю', get_letters_interp(letters['у']+letters['ю'], y_NORMA, letters_count), 'Темный сине-зеленый')
print_row('Ы', get_letters_interp(letters['ы'], bI_NORMA, letters_count), 'Черный, коричневый')
print_row('И+0.5Й', get_letters_interp(letters['и']+0.5*letters['й'], u_NORMA, letters_count), 'Синий')
