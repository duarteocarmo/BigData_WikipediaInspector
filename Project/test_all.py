from P1_time_string import hms_string
from P1_Pattern_Match_RE import find_match_from_string
import time

# define paths
path_save_indexer = '/Users/duarteocarmo/Desktop/bigdata/wiki_index.json'
path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'
path_found = '/Users/duarteocarmo/Desktop/bigdata/a_pages.txt'
pattern_path = '/Users/duarteocarmo/Desktop/bigdata/{}.txt'


# patterns for query
pattern1 = '"cat" [0, 16] "are" [2, 6] "to"'
pattern2 = '"or" [6, 7] "or" [2, 6] "or"'
pattern3 = '"when" [6, 7] "republic" [2, 6] "along"'
patterns = [pattern1, pattern2, pattern3]

# start match counter
pattern_counter = 0

# find matches
for pattern in patterns:

    pattern_counter += 1
    match_counter = 0
    matches = []
    start_time = time.time()

    # open master text file and look for match in each line
    with open(path_master_file) as infile:

        for line in infile:

            match = find_match_from_string(pattern, line)

            # if match exists, append to matches
            if len(match) != 0:
                match_counter += 1
                matches.append(match)

    elapsed_time = time.time() - start_time

    print 'Writing pattern {}.'.format(pattern_counter)

    # open text file to write results and write them
    with open(pattern_path.format(pattern_counter), 'a') as the_file:
        the_file.write('\nFor the pattern {} we found {} matches in {}:\n'.format(pattern, match_counter,
                                                                                  hms_string(elapsed_time)))
        for match in matches:
            the_file.write("%s\n" % match)
