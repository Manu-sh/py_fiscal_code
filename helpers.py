from typing import Literal, Final
from comuni import COMUNI

def is_vowel(ch: str) -> bool:
    return ch.lower() in ['a', 'e', 'i', 'o', 'u']

def is_consonant(ch: str) -> bool:
    return (ch := ch.lower()).isalpha() and not is_vowel(ch)

def find_comuni(pattern: str) -> list[dict[str,str]]:
    pattern: str = pattern.upper()
    return [ { k : v } for k,v in COMUNI.items() if pattern in k ]
