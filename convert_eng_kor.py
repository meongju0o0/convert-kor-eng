import re

kor_dict = {
    'ㄱ': 'r', 'ㄴ': 's', 'ㄷ': 'e', 'ㄹ': 'f',
    'ㅁ': 'a', 'ㅂ': 'q', 'ㅅ': 't', 'ㅇ': 'd',
    'ㅈ': 'w', 'ㅊ': 'c', 'ㅋ': 'z', 'ㅌ': 'x',
    'ㅍ': 'v', 'ㅎ': 'g',
    'ㅏ': 'k', 'ㅑ': 'i', 'ㅓ': 'j', 'ㅕ': 'u',
    'ㅗ': 'h', 'ㅛ': 'y', 'ㅜ': 'n', 'ㅠ': 'b',
    'ㅡ': 'm', 'ㅣ': 'l', 'ㅐ': 'o', 'ㅔ': 'p'
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
            cho_idx = i // 588
            jung_idx = (i - 588 * cho_idx) // 28
            jong_idx = i % 28
            result.extend((cho_s[cho_idx], jung_s[jung_idx], jong_s[jong_idx]))
        else:
            result.extend(c)

    return result


def kor_to_eng(str_input):
    idx_list = re.finditer(kor_dict.keys(), str_input)
    for idx in idx_list:
        kor_to_change = str_input[idx]
        str_input.replace(kor_to_change, kor_dict[kor_to_change])
    print(str_input)


def eng_to_kor():
    raise NotImplementedError


if __name__ == '__main__':
    str_input = input()
    kor_to_eng(str_input)