from localspelling.gb_us import DICTIONARY
from localspelling.util import get_lookup_dictionaries

lookups = get_lookup_dictionaries(DICTIONARY)


def convert_spelling(test_text: str, target_locale: str) -> str:
    """
    Localises a string to British or American spelling, conserving case.

    Please note this function converts only spelling variants such as US "honour" vs UK "honor".
    It does not localise vocabulary such as "pavement" vs "sidewalk" or "aubergine" vs "eggplant".

    It also does not localise spellings where there is more than one correct conversion, such as US "program",
    which corresponds to both "programme" and "program" in British spelling.

    :param test_text:  The input text that you want to localise.
    :param target_locale: The alpha-2 code for the target locale. "us" or "gb".
    :return: The text localised to the target locale
    """
    if type(target_locale) is not str:
        raise Exception("Provide locale as string")
    target_locale = target_locale.lower()
    if target_locale not in lookups:
        raise Exception("Unknown locale " + str(target_locale))

    regex_lookup = lookups[target_locale][0]
    dict_lookup = lookups[target_locale][1]

    output = ""
    last_index = 0
    for m in regex_lookup.finditer(test_text):
        word = m.group(0)
        lookup = word.lower()

        result = dict_lookup.get(lookup, lookup)
        if word == word.upper():
            result = result.upper()
        elif word[0] == word[0].upper():
            result = result.capitalize()

        output += test_text[last_index:m.start(0)] + result

        last_index = m.end(0)
    if last_index < len(test_text):
        output += test_text[last_index:len(test_text)]
    return output
