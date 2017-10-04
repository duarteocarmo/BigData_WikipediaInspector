# Clean XML page and return only clean text.
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




