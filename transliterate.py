phonetic_map = {
    'a': 'अ', 'aa': 'आ', 'i': 'इ', 'ee': 'ई', 'u': 'उ', 'uu': 'ऊ', 'ri': 'ऋ',
    'e': 'ए', 'ai': 'ऐ', 'o': 'ओ', 'au': 'औ', 'an': 'अं', 'ah': 'अः',
    'k': 'क', 'kh': 'ख', 'g': 'ग', 'gh': 'घ', 
    'ch': 'च', 'chh': 'छ', 'j': 'ज', 'jh': 'झ',
    't':'ट', 'th':'ठ', 'd':'ड', 'dh':'ढ', 'n':'ण',
    't': 'त', 'th': 'थ', 'd': 'द', 'dh': 'ध', 'n': 'न',
    'p': 'प', 'ph': 'फ', 'b': 'ब', 'bh': 'भ', 'm': 'म',
    'y': 'य', 'r': 'र', 'v': 'व', 'sh': 'श', 
    'shh': 'ष', 's': 'स', 'h': 'ह', 'l': 'ळ', 'ksh': 'क्ष', 'gy': 'ज्ञ', 'l': 'ल',
}

vowel_signs = {
    'a': '', 'aa': 'ा', 'i': 'ि', 'ee': 'ी', 'u': 'ु', 'uu': 'ू', 
    'e': 'े', 'ai': 'ै', 'o': 'ो', 'au': 'ौ', 'an': 'ं', 'ah': 'ः'
}

consonant_clusters = ['ch', 'gh', 'kh', 'jh', 'ph', 'th', 'dh', 'bh', 'sh', 'ma', 'la', 'pa']


def transliterate_word(word):
    # Break word into characters
    i = 0
    n = len(word)
    result = ''
    cons = ''
    
    while i < n:
        # Check for consonant clusters
        if i < n:
            if word[i:i+3] in phonetic_map:
                cons = word[i:i+3]
                i += 3
                print(f"3{i}a")
            elif word[i:i+2] in phonetic_map:
                cons = word[i:i+2]
                i += 2
                print(f"2{i}a")
            else:
                cons = word[i]
                i += 1
                print(f"1{i}a")

        # Check for vowel after the consonant
        if i < n and word[i] in vowel_signs:
            vowel = word[i]
            if i+1 < n:
                if word[i:i+2] in vowel_signs:
                    vowel = word[i:i+2]
                    i += 1
                    print(f"{i} a")
            i += 1
            print(f"2{i}b")
        else:
            vowel = 'a'  # default vowel sound
            # i += 1
            print(f'1{i}b')

        # Map consonant and vowel to Devanagari
        devanagari_cons = phonetic_map.get(cons, '')
        devanagari_vowel = vowel_signs.get(vowel, '')
        
        # Append to result
        result += devanagari_cons + devanagari_vowel

    return result

# def transliterate_word(word):
#     # Break word into characters
#     i = 0
#     n = len(word)
#     result = ''
    
#     while i < n:
#         # Check for consonant clusters
#         if i+1 < n and word[i:i+2] in consonant_clusters:
#             cons = word[i:i+2]
#             i += 2
#         else:
#             cons = word[i]
#             i += 1

#         # Check for vowel after the consonant
#         if i < n and word[i:i+2] in vowel_signs:
#             vowel = word[i:i+2]
#             i += 2
#         elif i < n and word[i] in vowel_signs:
#             vowel = word[i]
#             i += 1
#         else:
#             vowel = 'a'  # default vowel sound

#         # Map consonant and vowel to Devanagari
#         devanagari_cons = phonetic_map.get(cons, '')
#         devanagari_vowel = vowel_signs.get(vowel, '')
        
#         # Append to result
#         result += devanagari_cons + devanagari_vowel

#     return result



# def transliterate_word(word):
#     i = 0
#     n = len(word)
#     result = ''
    
#     while i < n:
#         # Handle consonants
#         cons = ''
#         if i+2 <= n and word[i:i+2] in phonetic_map:
#             cons = word[i:i+2]
#             i += 2
#         elif word[i] in phonetic_map:
#             cons = word[i]
#             i += 1
#         else:
#             i += 1  # Skip invalid characters
#             continue

#         # Handle vowels
#         vowel = ''
#         if i < n and word[i:i+2] in vowel_signs:
#             vowel = word[i:i+2]
#             i += 2
#         elif i < n and word[i] in vowel_signs:
#             vowel = word[i]
#             i += 1

#         # Map consonant and vowel to Devanagari
#         devanagari_cons = phonetic_map.get(cons, '')
#         devanagari_vowel = vowel_signs.get(vowel, '')

#         # Append to result
#         result += devanagari_cons + devanagari_vowel

#     return result

# # Example usage
# input_text = "mala pizza khaycha ahe"
# output_text = transliterate_text(input_text)
# print(f"Original: {input_text}")
# print(f"Transliterated: {output_text}")
