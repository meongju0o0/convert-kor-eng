import re

한글_사전 = {
    'ㄱ': 'r',
    'ㄴ': 's',
    'ㄷ': 'e',
    'ㄹ': 'f',
    'ㅁ': 'a',
    'ㅂ': 'q',
    'ㅅ': 't',
    'ㅇ': 'd',
    'ㅈ': 'w',
    'ㅊ': 'c',
    'ㅋ': 'z',
    'ㅁ': 'a',
    'ㅍ': 'v',
    'ㅎ': 'g',
    'ㅏ': 'l',
    'ㅑ': 'i',
    'ㅓ': 'j',
    'ㅕ': 'u',
    'ㅗ': 'h',
    'ㅛ': 'y',
    'ㅜ': 'n',
    'ㅠ': 'b',
    'ㅣ': 'l',
    'ㅐ': 'o',
    'ㅔ': 'p'
}


def decompose_kor(s):
    base = 44032
    cho_s = [
        'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
        'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]
    jung_s = [
        'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ',
        'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
    ]
    jong_s = [
        '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ',
        'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]

    result = []

    for c in s:
        if '가' <= c <= '힣':
            i = ord(c) - base
            cho_index = i // 588
            jung_index = (i - 588 * cho_index) // 28
            jong_index = i % 28

            result.append((cho_s[cho_index], jung_s[jung_index], jong_s[jong_index]))
        else:
            result.append(c)

    return result


def kor_to_eng():
    raise NotImplementedError


def eng_to_kor():
    raise NotImplementedError


if __name__ == '__main__':
    str_input = input()
    idx_list = re.finditer(kor_dict.keys(), str_input)
    for idx in idx_list:
        str_input.replace(str_input[idx], kor_dict[str_input[idx]])
    print(str_input)