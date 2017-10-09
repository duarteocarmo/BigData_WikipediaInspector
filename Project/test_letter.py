from P1_time_string import hms_string
from P1_Pattern_Match_RE import find_match_from_string
import time

# define paths
path_save_indexer = '/Users/duarteocarmo/Desktop/bigdata/wiki_index.json'
path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'
path_found = '/Users/duarteocarmo/Desktop/bigdata/a_pages.txt'

# patterns for query
pattern1 = '"cat" [0, 16] "are" [2, 6] "to"'
pattern2 = '"or" [6, 7] "or" [2, 6] "or"'
pattern3 = '"when" [6, 7] "republic" [2, 6] "along"'
patterns = [pattern1, pattern2, pattern3]

# open file with articles
f = open(path_found, 'r')
pages = f.read()

# start match counter
match_counter = 0

# find matches
for pattern in patterns:
    start_time = time.time()
    a = find_match_from_string(pattern, pages)
    elapsed_time = time.time() - start_time
    print '\nFor the pattern {} we found the following matches in {}:'.format(pattern, hms_string(elapsed_time))
    for match in a:
        print match
