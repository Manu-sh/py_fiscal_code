from helpers import find_comuni, is_consonant, is_vowel

# accetta il nome del comune e ritorna il codice catastale (gestisce solo comuni italiani)
# es. fc_comune('Firenze') -> 'D612'
def fc_comune(pattern: str) -> str:
    matches: list[dict[str,str]] = find_comuni(pattern)
    assert len(matches) == 1
    return list( matches[0].values() )[0].strip()

# ritorna le 3 cifre relative al cognome (gestisce 1 solo cognome, nella realtà il codice fiscale ne può contemplare più di 1)
def fc_surname(surname: str) -> str:
    surname = sorted(surname, key=is_consonant, reverse=True)
    surname += ['X', 'X', 'X']
    return ''.join(surname[0:3]).upper()

# ritorna le 3 cifre relative al nome (gestisce 1 solo nome, nella realtà il codice fiscale ne può contemplare più di 1)
def fc_name(name: str) -> str:
    name = sorted(name, key=is_consonant, reverse=True)

    if len(name) <= 3:
        name += ['X', 'X', 'X']
        return ''.join(name[0:3]).upper()

    name = name[0:3] if not is_consonant(name[3]) else [name[0], name[2], name[3]]
    return ''.join(name).upper()


"""
Lettera  Mese
A  gennaio   L  luglio
B  febbraio  M  agosto
C  marzo     P  settembre
D  aprile    R  ottobre
E  maggio    S  novembre
H  giugno    T  dicembre
"""

# ritorna la lettera associata al mese di nascita
# es fc_birth_month(1) -> 'A'
def fc_birth_month(month_no: int) -> str:
    HMAP: Final[list[str]] = ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'M', 'P', 'R', 'S', 'T']
    assert month_no >= 1 and month_no <= 12
    return HMAP[month_no - 1]

# ritorna le ultime 2 cifre dell'anno 
# es. fc_birth_year(2001) -> '01'
def fc_birth_year(year_no: int) -> str:
    return ''.join( str(year_no)[-2:] )

# codifica il giorno di nascita se tale numero ha meno di 2 cifre viene usato '0' come pad 
# es. fc_birth_day(1, 'M') -> '01'
def fc_birth_day(day_no: int, sex: str) -> str:
    assert day_no <= 31 and day_no > 0
    assert sex in ['m', 'M', 'f', 'F']

    if sex in ['f', 'F']:
        day_no += 40

    return f'{day_no:02d}'

# dati i 15 caratteri alfanumerici che compongono il codice fiscale calcola il sedicesimo ed ultimo carattere che funge da carattere di controllo
def fc_cin(fiscal_code: str) -> str:

    ODD_ENCODE: Final[dict[str,int]] = {
        '0': 1,  '1': 0,  '2': 5,  '3': 7,  '4': 9,  '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
        'A': 1,  'B': 0,  'C': 5,  'D': 7,  'E': 9,  'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21, 
        'K': 2,  'L': 4,  'M': 18, 'N': 20, 'O': 11, 'P': 3,  'Q': 6,  'R': 8,  'S': 12, 'T': 14,
        'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23 
    }

    EVEN_ENCODE: Final[dict[str,int]] = {
        '0': 0,  '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 0,  'B': 1,  'C': 2,  'D': 3,  'E': 4,  'F': 5,  'G': 6,  'H': 7,  'I': 8,  'J': 9, 
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }

    ENCODE: Final[list[dict]] = [EVEN_ENCODE, ODD_ENCODE]

    assert len(fiscal_code) == 15

    cin_sum: int = 0
    for idx, ch in enumerate(fiscal_code):
        cin_sum += ENCODE[ (idx + 1) & 1 ][ch] # +1 perché gli array partono da 0

    return chr( cin_sum % 26 + ord('A') )


def fiscal_code(first_name: str, last_name: str, year: int, month: int, day: int, sex: Literal['M', 'F'], comune: str) -> str:
    fiscal_code_15: str = fc_surname(last_name) + fc_name(first_name) + fc_birth_year(year) + fc_birth_month(month) + fc_birth_day(day, sex='M') + fc_comune(comune)
    return fiscal_code_15 + fc_cin(fiscal_code_15)


print('Nazione: Italia')
sex: Literal['M', 'F'] = input('Sesso (M/F): ')
first_name: str        = input('Nome: ')
last_name:  str        = input('Cognome: ')

day, month, year       = map(int, input('Data di nascita (G/M/YYYY): ').split('/'))
comune: str            = input('Comune di nascita: ')

print(
    fiscal_code(
        last_name=last_name, first_name=first_name, 
        day=day, month=month, year=year, 
        comune=comune, sex=sex
    )
)
