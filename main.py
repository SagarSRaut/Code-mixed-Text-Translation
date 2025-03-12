from tokenization import tokenize
from transliterate import transliterate_word
# from phonetics import phonetic_map, vowel_signs, consonant_clusters


def transliterate_text(text):
    tokens = tokenize(text)
    transliterated_tokens = [transliterate_word(token) for token in tokens]
    return ' '.join(transliterated_tokens)

# Example usage
input_text = "maza jevan jhal ahe."
output_text = transliterate_text(input_text)
# print(f"Original: {input_text}")
# print(f"Transliterated: {output_text.encode('utf-8').decode('utf-8')}")

# Write the result to a file with UTF-8 encoding
with open('transliterated_output.txt', 'w', encoding='utf-8') as file:
    file.write(f"Original: {input_text}\n")
    file.write(f"Transliterated: {output_text}\n")

print("Transliteration completed. Check the transliterated_output.txt file.")