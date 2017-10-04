import json
import xml.etree.ElementTree as ET
from P1_Wikipedia_Indexer import path_xml, path_save_indexer

# Extract text from XML dump file based on indexer
def getPage_from_article(articlename):

    print 'Opening Indexer'

    with open(path_save_indexer) as file:
        wiki_indexer = json.load(file)

    print 'Indexer Open'

    indexes = wiki_indexer[articlename]

    print 'The indexes are the following:', indexes

    content = ''

    print 'Opening Xml'

    fp = open(path_xmLfile)

    for i, line in enumerate(fp):

        if i >= indexes[0] - 2:
            content = content + line

        if i == indexes[1] - 2:
            break

    print 'Got Page'

    return content

# Extract text from XML dump file based on indexer
def getPage_from_articles_letter(letter):

    print 'Opening Indexer'

    with open(path_save_indexer) as file:
        wiki_indexer = json.load(file)

    print 'Indexer Open'

    indexes = []

    for article in wiki_indexer.keys():

        if article.startswith(letter):
            indexes.append(wiki_indexer[article])

    print 'Opening Xml'

    fp = open(path_xmLfile)

    contents = []

    for pair in indexes:

        content = ''

        for i, line in enumerate(fp):

            if i >= pair[0] - 2:
                content = content + line

            if i == pair[1] - 2:
                contents.append(content)
                break

    print 'Got Page'

    return contents


# Extract text from XML dump file based on indexer
def getPage_from_all():

    print 'Opening Indexer'

    with open(path_save_indexer) as file:
        wiki_indexer = json.load(file)

    print 'Indexer Open'

    print 'Opening Xml'

    fp = open(path_xmLfile)

    contents = []

    for item in wiki_indexer.values():

        content = ''

        for i, line in enumerate(fp):

            if i >= item[0] - 2:
                content = content + line

            if i == item[1] - 2:
                contents.append(content)
                break

    print 'Got Page'

    return contents

# Clean XML page and return only clean text.
def cleanPage(xmlpage):

    print 'Cleaning Page'

    tree = ET.fromstring(xmlpage)

    for node in tree.iter():
        if node.tag == 'text':
            text = node.text

    text = text.replace('\n', ' ').replace('\r', '')
    text = text.lower()

    print 'Finished cleaning'

    return text












