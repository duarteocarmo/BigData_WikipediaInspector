import json


# Extract text from XML dump file based on indexer
def getPage_from_articles_letter(letter):

    letter_lowercase = letter.lower()

    # Get path of necessary files
    path_save_indexer = '/Volumes/DUARTE OC/BIG DATA/wiki_index.json'
    path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'

    print 'Opening Indexer'

    with open(path_save_indexer) as file:
        wiki_indexer = json.load(file)

    print 'Indexer Open'

    indexes = []

    for article in wiki_indexer.keys():
        article_lowercase = article.lower()

        if article_lowercase.startswith(letter_lowercase):
            indexes.append(wiki_indexer[article])

    print 'Getting Pages...'

    current_line = 0
    contents = ''

    # Loop over lines and return when its reached.
    with open(path_master_file) as infile:
        for line in infile:
            current_line += 1

            if current_line in indexes:
                contents = contents + line

    print 'Got Pages with {}'.format(letter)

    return contents
