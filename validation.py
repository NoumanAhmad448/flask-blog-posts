import re

def validate_alph_space(input):
    return re.search(r"[^a-zA-Z ]+", input)

def validate_html(input):
    return re.search(r"<.*?>", input)