

def create_alphabet(language):
    if language == "en":
        abc = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        return abc
    elif language == "ru":
        abc = [chr(x) for x in range(ord('А'), ord('Я') + 1)]
        return abc
    elif language == "fr":
        abc = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        return abc
    elif language == "sp":
        abc = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        return abc
    elif language == "ge":
        abc = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        return abc
    elif language == "it":
        abc = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        return abc
    elif language == "po":
        abc = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        return abc
    elif language == "du":
        abc = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        return abc
    elif language == "ch":
        abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
        return abc
    elif language == "ja":
        abc = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ',
               'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ',
               'ロ', 'ワ', 'ヲ', 'ン']
        return abc
    else:
        raise ValueError("Unsupported language")
