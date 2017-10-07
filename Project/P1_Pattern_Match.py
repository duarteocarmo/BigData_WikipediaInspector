def get_matches_starting_at(data, pattern, index, starting_index, resulting_matches):
    sub_data = data[index:]

    P = pattern[0]

    if sub_data[:len(P)] == P:
        if len(pattern) == 1:
            resulting_matches.append((starting_index, index + len(P)))
        else:
            for new_index in range(pattern[1][0] + 1, pattern[1][1] + 2):
                get_matches_starting_at(data, pattern[2:], index + len(P) + new_index - 1, starting_index,
                                        resulting_matches)

        return resulting_matches
    else:
        return []


def get_all_matches(data, pattern):
    matches_found = []
    for index in range(len(data)):
        matches_at_index = get_matches_starting_at(data, pattern, index, index, [])
        matches_found += matches_at_index

    matches = set(matches_found)

    result = []

    for m in matches:
        result.append(data[m[0]:m[1]])

    return list(set(result))
