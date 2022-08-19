#!/usr/bin/env python3
import sys
import string
from pathlib import Path

# How long each word in words.txt should be
NUM_CHARS = 5


def is_ascii(s):
    '''Return True if entire word uses ASCII characters.'''
    return all(ord(c) < 128 for c in s)


if __name__ == "__main__":
    # Set up the files needed.
    RAW_WORDS_FILE = Path('raw_words.txt')
    WORDS_FILE = Path('words.txt')

    # Read the raw words list
    if not RAW_WORDS_FILE.exists():
        print(f"Could not find {RAW_WORDS_FILE} file")
        sys.exit(1)
    with RAW_WORDS_FILE.open() as f:
        raw_words = f.read().splitlines()

    skip_list = [
        'abbés', 'blasé', 'fêtes', 'króna', 'outré', 'passé', 'roués', 'éclat'
    ]

    words = []
    for word in raw_words:
        # 1. Must be NUM_CHARS chars
        # 2. Must not contain apostrophe
        # 3. Must not be a proper noun i.e. start with capital letter
        # 4. Must not be in the above skip list
        if len(word) == NUM_CHARS and \
           "'" not in word and \
           word[0] not in string.ascii_uppercase and \
           word not in skip_list:
            words.append(word)

    WORDS_FILE.unlink(missing_ok=True)
    WORDS_FILE.write_text('\n'.join(words))
