alphabet: list[str] = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ы", "ъ", "э", "ю", "я"]

def decipher_word(word_for_decipher: str) -> list[str]:
    """
    Decipher given word by Caesar's cipher.
    """
    words_after_decipher: list[str] = []
    
    for number in range(1, len(alphabet)):
        words_after_decipher.append(get_decifer_word_by_number_shift(word_for_decipher, number))

    return words_after_decipher


def clean_word(word: str) -> str:
    """
    Replace symbols and get lower.
    """
    word = word.lower()
    symbols_for_replace = (("ё", "е"), ("й", "и"))
    
    for symbol in symbols_for_replace:
        if symbol[0] in word:
            word = word.replace(symbol[0], symbol[1])
    return word

def get_decifer_word_by_number_shift(word_for_decipher, number):
    word_symbols = []
    
    for symbol in clean_word(word_for_decipher):
        
        symbol_index = alphabet.index(symbol)
        next_symbol_index = symbol_index + number
        
        if next_symbol_index > len(alphabet) - 1:
            next_symbol_index = next_symbol_index - len(alphabet) 
        
        word_symbols.append(alphabet[next_symbol_index])
        
    return "".join(word_symbols)
    

                                       
            
            
            
            
        
    
