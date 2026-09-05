"""Complete reference solutions for the Cipher exercise family."""

from __future__ import annotations

from string import ascii_uppercase


def transpose_cipher(message: str, rows: int, columns: int) -> str:
    """Fill a matrix row-major and read it column-major.

    ``len(message)`` is guaranteed to equal ``rows * columns``. Preserve all
    spaces and punctuation.
    """
    return "".join(message[row * columns + column] for column in range(columns) for row in range(rows))


def encrypt_with_key(message: str, key: str) -> str:
    """Encrypt with a keyed substitution alphabet.

    Scan ``key`` case-insensitively, keeping each letter's first occurrence.
    The key contains all 26 letters. Align that alphabet with A-Z, preserve
    message-letter case, and leave nonletters unchanged.
    """
    keyed_alphabet: list[str] = []
    seen: set[str] = set()
    for character in key:
        upper = character.upper()
        if upper in ascii_uppercase and upper not in seen:
            seen.add(upper)
            keyed_alphabet.append(upper)

    substitution = dict(zip(ascii_uppercase, keyed_alphabet))
    encrypted: list[str] = []
    for character in message:
        replacement = substitution.get(character.upper())
        if replacement is None:
            encrypted.append(character)
        elif character.islower():
            encrypted.append(replacement.lower())
        else:
            encrypted.append(replacement)
    return "".join(encrypted)


def possible_decryptions(dictionary: list[str], ciphertext: str) -> list[str]:
    """Return words compatible with some 1-to-26 tokenization of ciphertext.

    Tokens have one or two digits, no leading zero, and values 1 through 26.
    Equal letters map to equal numbers and different letters map to different
    numbers. Preserve dictionary order and return each word once.
    """

    def matches(word: str) -> bool:
        normalized = word.upper()

        def search(
            letter_index: int,
            digit_index: int,
            letter_to_number: dict[str, int],
            used_numbers: set[int],
        ) -> bool:
            if letter_index == len(normalized):
                return digit_index == len(ciphertext)
            if digit_index >= len(ciphertext) or ciphertext[digit_index] == "0":
                return False

            letter = normalized[letter_index]
            for width in (1, 2):
                end = digit_index + width
                if end > len(ciphertext):
                    continue
                number = int(ciphertext[digit_index:end])
                if not 1 <= number <= 26:
                    continue
                assigned = letter_to_number.get(letter)
                if assigned is not None and assigned != number:
                    continue
                if assigned is None and number in used_numbers:
                    continue

                if assigned is None:
                    letter_to_number[letter] = number
                    used_numbers.add(number)
                if search(letter_index + 1, end, letter_to_number, used_numbers):
                    return True
                if assigned is None:
                    del letter_to_number[letter]
                    used_numbers.remove(number)
            return False

        return search(0, 0, {}, set())

    result: list[str] = []
    seen_words: set[str] = set()
    for word in dictionary:
        if word not in seen_words and matches(word):
            seen_words.add(word)
            result.append(word)
    return result
