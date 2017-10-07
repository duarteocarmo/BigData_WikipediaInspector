## Welcome to my solution for Challenge 1. 

It was a long, tedious and lonely road but here it is (I think). Instead of writting a report on share latex, I decided to make a website explaining my solution. Like this I can include code snippets, links to the repo and much more. 

PS: I will also send and markdown file so that you can make sure I didn't change anything after the delivery date. 

The solution has severall parts:

- Part 1: Cleaning an xml page.
- Part 2: Indexing the articles and storing the cleaned version. 
- Part 3: Accessing the cleaned files. 
- Part 4: Querying for a pattern. 
- Part 5: Testing. 

I'm gonna try to make this as simple as possible! So hold tight. 

### Part 1: Cleaning an XML page. 

The **multistream.xml** (64GB = goodbye hardrive.) is a separation of all of the articles into their xml format. Therefore, before getting all of the articles, I decided to make a function that takes the **xml page of an article**, and only returns the contents of the contents of the **text** tag. 

Sometimes, the page has absolutely nothing inside it (I don't know how/why) therefore, when this happens, it returns '#redirect'. You'll see why in the next part. 

You can find my cleanPage function [here](https://github.com/duarteocarmo/WIKIPEDIA/blob/master/Project/P1_Clean_Page.py).

Here is a snippet of the function: 

```python
def cleanPage(xmlpage):
    import xml.etree.ElementTree as ET
    
    tree = ET.fromstring(xmlpage)
    
    for node in tree.iter():
        if node.tag == 'text':
            text = node.text
            if text is None:
                return '#redirect'
            else:
                text = text.replace('\n', ' ').replace('\r', '')
                text = text.lower()

                return text
```

### Part 2: Indexing the articles and storing their clean version. 

The indexing and cleaning were done all at once. 

First, the index file is a JSON file called **wiki_index.json**, in there, a dictionary is stored. This dictionary contains as keys the names of the articles and as values of lines in a text file. 

The text file, **articles.txt**, contains all of the articles. Every cleaned article is stored in a line. 

Therefore, if the dictonnary has: 

```
{'Cat':2345}
```

This means that the cleaned article corresponding to the title **Cat** is stored in the line nº2345 of the **articles.txt** file. 

The file that does this is can be found [here](https://github.com/duarteocarmo/WIKIPEDIA/blob/master/Project/P1_Wikipedia_Indexer.py). 

Anyways, here is a snippet of the most relevant part: 

```python
# Important variables to define
total_pages = 5483785.00
number_of_lines = 0
number_of_articles = 0.0
files_written = 0
page_detected = 0

# create a dictionary to store indexes of lines of each article
wiki_index = {}

# start timer
start_time = time.time()

# loop over all lines of the xml dump
with open(path_xml) as infile:
    f = open(path_master_file, 'w')

    for line in infile:

        # if <page> tag detected, get line number
        if '<page>' in line:

            contents = line
            page_detected = 1

        # if page is detected keep adding lines to contents
        if page_detected == 1:
            contents += line

        # detect and store article name
        if '<title>' in line:

            match = re.search(r'>(.*)<', line)
            if match:
                title = match.group()[1:-1]

        # if </page> tag detected, store values of important lines in dictionary
        if '</page>' in line:

            contents += line
            number_of_articles += 1.0
            clean = cleanPage(contents).encode('utf-8')

            # if page is not a redirect, store to indexer and write to text file
            if clean.startswith('#redirect') is False:
                files_written += 1
                wiki_index[title] = files_written
                f.write(clean + '\n')

            page_detected = 0

        # test setting
        # if files_written == 220600:
        #     break

        number_of_lines += 1

    f.close()

# finish timer and get prediction on total time.
elapsed_time = time.time() - start_time
elapsed_for_total = total_pages * (elapsed_time / number_of_articles)

# Inform user
print 'You parsed {} articles and wrote {}.'.format(number_of_articles, files_written)
print 'Elapsed time: {}'.format(hms_string(elapsed_time))
print 'It will take you: {}'.format(hms_string(elapsed_for_total))

# Save dictionary to JSON file.
with open(path_save_indexer, 'w') as file:
    file.write(json.dumps(wiki_index))
```

After running this function, the console outputs the following message:

```shell
You parsed 17773690.0 articles and wrote 9575106.
Elapsed time: 2:04:17.77
It will take you: 0:38:20.97
There is coherence.
```

This indicates not only the number of articles that were parsed (without redirects), but also if there is coherence between the number of files indexed and written. (See more details in script.)

### Part 3: Accessing the cleaned files. 

Three different functions were designed for three needs: Getting a single line, getting multiple lines, and getting all lines. 

#### Getting a single line: 

In order to get a single line, the script simply looks for the page name in the indexer file, and consequently returns the corresponding line the 'master text file'.

Here's a portion of the script: 

```python
# Extract text from XML dump file based on indexer
def getPage_from_article(articlename):

    # Get path of necessary files
    path_save_indexer = '/Volumes/DUARTE OC/BIG DATA/wiki_index.json'
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
```

Don't forget that you can access the full code here. 







### Part 4: Querying for a pattern. 

