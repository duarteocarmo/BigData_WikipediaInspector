import json


# Extract text from XML dump file based on indexer
def getPage_from_article(articlename):

    # Get path of necessary files
    path_save_indexer = '/Users/duarteocarmo/Desktop/bigdata/wiki_index.json'
    path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'

    print 'Opening Indexer...'

    # Get indexer file
    with open(path_save_indexer) as file:
        wiki_indexer = json.load(file)

    print 'Indexer Open.'

    # Get line number
    index = wiki_indexer[articlename]

    print 'Fetching line...'

    current_line = 0

    # Loop over lines and return when its reached.
    with open(path_master_file) as infile:
        for line in infile:
            current_line += 1

            if current_line == index:
                final = line

    print 'Got line.'

    return final




