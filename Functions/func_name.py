import re

def title_except_uppercase(s):
    words = s.split(' ')
    for i, word in enumerate(words):
        if word in ["to", "of", "at", "in", "from", "not"]:
            pass
        elif len(word) == 2:
            words[i] = word.upper()
        elif not word.isupper():
            words[i] = word.capitalize()
    return ' '.join(words)


def camel_to_snake(text):
    text = re.sub("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r" \1", text)
    text = title_except_uppercase(text)
    if len(text) == 2:
        text = text.upper()
    # text = text.capitalize()
    # text = text.lower()
    return text
