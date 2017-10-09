from P1_Extract_Page import getPage_from_article
from P1_Pattern_Match import get_all_matches
from P1_time_string import hms_string
import time

# define paths
path_save_indexer = '/Users/duarteocarmo/Desktop/bigdata/wiki_index.json'
path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'

# patterns for query
pattern1 = ["cat", (0, 10), "are", (2, 6), "to"]
pattern2 = ["or", (6, 7), "or", (2, 6), "or"]
pattern3 = ["when", (6, 7), "republic", (2, 6), "along"]
patterns = [pattern1, pattern2, pattern3]

# get necessary pages
page = getPage_from_article('Cat')

# start match counter
match_counter = 0

# loop over patterns
for pattern in patterns:

    start_time = time.time()
    found = []
    matches = get_all_matches(page, pattern)

    if len(matches) != 0:
        match_counter += len(matches)
        found.append(matches)

    elapsed_time = time.time() - start_time
    print '\nFor the pattern {} we found {} matches in {}:'.format(pattern, match_counter, hms_string(elapsed_time))
    print found
