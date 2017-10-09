def find_match_from_string(pattern, string):
    import re

    # get rid of unnecessary stuff
    pattern = pattern.replace('[', '.{')
    pattern = pattern.replace(']', '}')
    pattern = pattern.replace('"', '')
    pattern = pattern.replace(' ', '')

    # query regex
    matches = re.findall(r'(?=({}))'.format(pattern), string)

    return matches
