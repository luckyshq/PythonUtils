#coding=utf-8

from HTMLParser import HTMLParser
from os import path,mkdir
import time
import sys

FOLDER_NAME = "Lately"
BLOG_VERSION_NUMBER = sys.argv[1]
BLOG_TITLE_NAME = "Luckyshq技术周报 （第" + BLOG_VERSION_NUMBER + "期）"
BLOG_TITLE_CONTENT = "---\n" \
                     + "layout: post\n" \
                     + "title: " + " " + BLOG_TITLE_NAME + "\n" \
                     + "date: " + "  " + time.strftime("%Y-%m-%d %X", time.localtime()) \
                     + "\ncategories: others" \
                     + "\n---" \
                     + "\n\n"
MARK_DOWN_FILE_ENDING = ".md"

class MyHTMLParser(HTMLParser):
    a_text = False
    h3_text = False

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.start_deal = False
        self.content = ""
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "h3":
            self.h3_text = True
            self.a_text = False
        else:
            if tag == "a":
                self.a_text = True
                self.h3_text = False
                if len(attrs) == 0:
                    pass
                else:
                    for (variable, value) in attrs:
                        if variable == "href":
                            if self.start_deal:
                                self.address = value
            else:
                self.h3_text = False
                self.a_text = False
    def handle_data(self, data):
        if self.a_text:
            if data == "\r\n            ":
                pass
            else:
                if data == "\r\n        ":
                    self.start_deal = False
                if self.start_deal:
                    self.content += "###" + " " + "[" + data + "]" + "(" + self.address + ")\n\n"
        if self.h3_text:
            if len(data) == 0:
                pass
            else:
                if data == FOLDER_NAME:
                    self.start_deal = True




if __name__ == "__main__":
    htmlFile = open(path.split(path.realpath(__file__))[0] + "/bookmarks.html", "r")
    if not path.exists(path.split(path.realpath(__file__))[0] + "/outputs"):
        mkdir(path.split(path.realpath(__file__))[0] + "/outputs")
    outFile = open(path.split(path.realpath(__file__))[0] + "/outputs/" + time.strftime("%Y-%m-%d", time.localtime()) + BLOG_TITLE_NAME + MARK_DOWN_FILE_ENDING, "w")
    html_code = htmlFile.read()
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    htmlFile.close()
    hp.content = BLOG_TITLE_CONTENT + hp.content
    outFile.write(hp.content)
