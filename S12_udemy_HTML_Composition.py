class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title):
        super().__init__('title', 'This is my title')
        #self._title_tag = Tag(title)
        #self.contents = str(self._title_tag)


    def display(self, file=None):
        print('<head>')
        print(self)
        print('</head>')


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')   # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


#########################################
#
# HtmlDoc Class is Made From Instances of 3 Other Classes
#
# It is COMPOSED of OTHER CLASSES
#
#########################################

class HtmlDoc(object):

    #AGGREGATION
    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    #COMPOSITION
    #def __init__(self, title=None):
        # self._doc_type = DocType()
        # self._head = Head(title)
        # self._body = Body()


    def add_tag(self, name, contents):
        self._body.add_tag(name,contents)

    #DIsplay Delegated to other classes
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    # my_page = HtmlDoc("Adam\'s HTML Title")
    # my_page.add_tag('h1', 'Main Heading')
    # my_page.add_tag('h2', 'sub-heading')
    # my_page.add_tag('p', "This is a paragraph")
    # with open("test.html", "w") as test_doc:
    #     my_page.display(file=test_doc)
    #     #my_page.display()


    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', 'Unlike <strong>composition</strong>, aggregation uses existing instances'
                 'of objects to build up ANOTHER object.')
    new_body.add_tag('p', 'The composed object doesn\'t actually own the objects that it is composed of'
    ' - if it is destroyed, those objects continue to exist')

    new_doc_type = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_doc_type, new_header, new_body)
    with open("test3.html", "w") as test_doc:
        my_page.display(file=test_doc)


# give our document new content by switching it's body
# my_page._body = new_body
# with open("test2.html", "w") as test_doc:
#     my_page.display(file=test_doc)


