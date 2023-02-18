import re


def camel_to_snake(text):
    text = re.sub("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))", r" \1", text)
    text = text.title()
    if len(text) == 2:
        text = text.upper()
    # text = text.capitalize()
    # text = text.lower()
    return text
