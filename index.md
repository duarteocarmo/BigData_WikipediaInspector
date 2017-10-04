## Welcome to my solution for the first challenge, aka: 'WIKI_DESTROYER'

As you might have noticed by know, in this website I will try to explain a little bit how my solution works. 

Thanks for taking the time. This was hard, and I did it alone: bad idea. Here we go. 

### Part 1: Indexing and Cleaning at the same time. 

So, once I decompressed the bz2 file, I got a **huge** xml file that I could not even open. To tackle this, I managed to get an idea of what it looked like. 

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

```python
import re
import json
import time
from P1_time_string import hms_string
from P1_Clean_Page import cleanPage



# Get path of necessary files
path_xml = '/Users/duarteocarmo/Desktop/bigdata/enwiki-20170820-pages-articles-multistream.xml'
path_save_indexer = '/Volumes/DUARTE OC/BIG DATA/wiki_index.json'
path_master_file = '/Users/duarteocarmo/Desktop/bigdata/articles.txt'


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

# number of lines confirm
with open(path_master_file) as f:
    numberoflinesintext = sum(1 for _ in f)


# test json
with open(path_save_indexer) as file:
    wiki_indexer = json.load(file)

if numberoflinesintext == len(wiki_indexer):
    print 'There is coherence.'


```
### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/duarteocarmo/WIKIPEDIA/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
