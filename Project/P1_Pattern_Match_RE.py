def find_match_from_string(pattern, string):
    import re

    pattern = pattern.replace('[', '.{')
    pattern = pattern.replace(']', '}')
    pattern = pattern.replace('"', '')
    pattern = pattern.replace(' ', '')

    matches = re.findall(r'(?=({}))'.format(pattern), string)

    return matches
