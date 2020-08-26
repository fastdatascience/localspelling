import re


def get_regex_and_raw_word(term):
    clean_term = re.sub(r'\*', '', term)
    regex = clean_term
    if not term.startswith("*"):
        regex = r'\b' + regex
    if not term.endswith("*"):
        regex = regex + r'\b'
    return regex, clean_term


def get_lookup_dictionaries(resource_file):
    gb_to_us = {}
    us_to_gb = {}
    gb_regexes = set()
    us_regexes = set()
    for l in resource_file.split("\n"):
        gb, us = l.strip().split("\t")
        this_word_gb_regex, gb_word = get_regex_and_raw_word(gb)
        this_word_us_regex, us_word = get_regex_and_raw_word(us)
        gb_regexes.add(this_word_gb_regex)
        us_regexes.add(this_word_us_regex)
        gb_to_us[gb_word] = us_word
        us_to_gb[us_word] = gb_word

    gb_regex = re.compile("(?i)" + "|".join(gb_regexes))
    us_regex = re.compile("(?i)" + "|".join(us_regexes))

    lookups = {"us": (gb_regex, gb_to_us), "gb": (us_regex, us_to_gb)}

    return lookups
