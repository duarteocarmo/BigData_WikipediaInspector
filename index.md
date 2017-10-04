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

The **multistream.xml** (64GB = goodbye hardrive.) is a separation of all of the articles into their xml format. Therefore, before getting all of the articles, I decided to make a function that takes the **xml page of an article**, and only returns the contents of the contents of the **text** tag. Sometimes, the page has absolutely nothing inside it (I don't know how/why) therefore, when this happens, it returns '#redirect'. You'll see why in the next part. 

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

The second part….

