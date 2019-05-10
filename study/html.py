#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('starttag: <%s>' % tag)

    def handle_endtag(self, tag):
        print('endtag: </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('startendtag: <%s/>' % tag)

    def handle_data(self, data):
        print('data: ' + data + '1')

    def handle_comment(self, data):
        print('comment: <!--', data, '-->')

    def handle_entityref(self, name):
        print('entityref: &%s;' % name)

    def handle_charref(self, name):
        print('charref: &#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;&#1234;tutorial...<br>END</p>
</body></html>''')
