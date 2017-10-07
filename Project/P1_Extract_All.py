import json
import linecache


# Extract text from XML dump file based on indexer
def getPage_from_all():

    # Get path of necessary files
    path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'

    print 'Getting Pages... '

    contents = ''

    # Loop over lines and return when its reached.
    with open(path_master_file) as infile:
        for line in infile:
                contents = contents + line

    print 'Got all Pages.'

    return contents


