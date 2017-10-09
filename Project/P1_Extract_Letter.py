import json
import linecache


# Extract text from XML dump file based on indexer
def getPage_from_articles_letter(letter):

    letter_lowercase = letter.lower()

    # Get path of necessary files
    path_save_indexer = '/Users/duarteocarmo/Desktop/bigdata/wiki_index.json'
    path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'

    print 'Opening Indexer'

    with open(path_save_indexer) as file:
        wiki_indexer = json.load(file)

    print 'Indexer Open'

    indexes = []

    articles_count = 0

    for article in wiki_indexer.keys():
        article_lowercase = article.lower()
        if article_lowercase.startswith(letter_lowercase):
            indexes.append(wiki_indexer[article])
            articles_count += 1

    indexes = sorted(indexes)

    print 'Getting Pages...'

    current_line = 0
    contents = ''

    for index in indexes:
        text = linecache.getline(path_master_file, index)
        contents = contents + text
        articles_count -= 1

    print 'Got Pages with {}'.format(letter)

    return contents

