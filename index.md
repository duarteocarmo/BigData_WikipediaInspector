## Welcome to my solution for Challenge 1. 

It was a long, tedious and lonely road but here it is. Instead of writting a report on share latex, I decided to make a website explaining my solution. Like this I can include code snippets, links to the repo and much more. 

*PS: I will also send a pdf file so that you can make sure I didn't change anything after the delivery date.* 

The solution has severall parts:

- Part 1: Cleaning an xml page.
- Part 2: Indexing the articles and storing the cleaned version. 
- Part 3: Accessing the cleaned files. 
- Part 4: Querying for a pattern. 
- Part 5: Testing and results. 

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
            
        number_of_lines += 1

    f.close()
```

After running this function, the console outputs the following message:

```shell
You parsed 17773690.0 articles and wrote 9575106.
Elapsed time: 2:04:17.77
It will take you: 0:38:20.97
There is coherence.
```

This indicates not only the number of articles that were parsed (with redirects), but also if there is coherence between the number of files indexed (without redirects) and written. (See more details in script.)

### Part 3: Accessing the cleaned files. 

Three different functions were designed for three needs: Getting a single line, getting multiple lines, and getting all lines. 

#### Getting a single line: 

In order to get a single line, the script simply looks for **the page name in the indexer file**, and consequently returns the corresponding line the 'master text file'.

Here's a portion of the script: 

```python
def getPage_from_article(articlename):

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

#### Getting multiple pages based on starting letter. 

In this type of problem, the script looks for all the articles names in the JSON indexer **that starts with a particular lette**r, and consequently stores the lines where these occur. 

Here's a portion of the function: 

```python
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
```

After this, we can save all of the lines that started with a particular letter to a particular text file, which was exactly what I did, by running the following script: 

```python
path_found = '/Users/duarteocarmo/Desktop/bigdata/a_pages.txt'

pages = getPage_from_articles_letter('A')

with open(path_found, 'w') as the_file:
    the_file.write(pages)
```

In this way, we keep all of the cleaned pages started by A in a text file so that we can query it.

#### Getting all pages. 

Since we already have stored all of the cleaned web pages, there is no need to 'fetch' anything in particular. 

### Part 4: Querying for a pattern. 

My first approach was to use regex, but for detecting overlapping matches it proved to be not the best solution. Therefore, I adopted the script provided by our teacher and 'adapted it' to return a list of the matches form a string. 

However, the script provided by the teacher seems to be very slow, therefore, I kept my original regex version of it. 

You can browse them:

- [Non regex teacher version](https://github.com/duarteocarmo/BigData_WikipediaInspector/blob/master/Project/P1_Pattern_Match.py)
- [Regex "me" version](https://github.com/duarteocarmo/BigData_WikipediaInspector/blob/master/Project/P1_Pattern_Match_RE.py)



### Part 5: Testing and results.

So that everything can be tested, 3 test files will be provided in the repo. Each one of them for a different situation described in Part 3. 

For every one of the tests that can be found in the GitHub page, the procedure is pretty much the same and is commented accordingly. This procedure consists of: defining the patterns for querying, getting pages, and looping over the patterns to find matches. All of the print statements "guide" the user, and the scripts are also commented. 

#### Querying a single page

In order to test in the 'Cat' page for example, and following the above methodology, the following script is produced:

```python
# define paths
path_save_indexer = '/Volumes/DUARTE OC/BIG DATA/wiki_index.json'
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
```

The code prints if run: 

```shell
Opening Indexer...
Indexer Open.
Fetching line...
Got line.

For the pattern ['cat', (0, 10), 'are', (2, 6), 'to'] we found 3 matches in 0:00:00.83:
[['cat care: how to', 'cats are [[lacto', 'cats are able to']]

For the pattern ['or', (6, 7), 'or', (2, 6), 'or'] we found 4 matches in 0:00:01.02:
[['orld record for']]

For the pattern ['when', (6, 7), 'republic', (2, 6), 'along'] we found 4 matches in 0:00:00.79:
[]
```

#### Querying all pages started in 'A'

When querying all of the pages started with A, two things change:

- We access the text file built before. 
- We also use regex to query instead of the function provided, you can see it on **P1_Pattern_Match_RE.py**, this is only for speed purposes. 

Here's a snippet of the script: 

```python
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
```



You can check the results in this [GIST](https://gist.github.com/duarteocarmo/36ac0ff01a880c3b37ee9da113d4e20a).  I found a bunch of matches for the first and second queries, but nothing for the third.

Here's also a snippet: 

```none
For the pattern "cat" [0, 16] "are" [2, 6] "to" we found the following matches in 0:00:38.24:
cations are used to
cations== arrays are used to
...
For the pattern "or" [6, 7] "or" [2, 6] "or" we found the following matches in 0:00:38.48:
ort network|wor
orting more tor
or governor |wor
...
For the pattern "when" [6, 7] "republic" [2, 6] "along" we found the following matches in 0:00:36.35:
```

#### Querying for the whole of Wikipedia

When querying the whole of Wikipedia, only this line changes, prompting all of wikipedia.

```python
# get necessary pages
pages = getPage_from_all()
```

This returns:

```shell

```

