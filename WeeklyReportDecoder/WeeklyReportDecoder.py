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
                     + "\n## 新闻\n\n\n\n" \
                     + "## 编程\n\n\n\n" \
                     + "## Android开发\n\n\n\n" \
                     + "## 设计\n\n\n\n"
MARK_DOWN_FILE_ENDING = ".md"

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.start_deal = False
        self.content = ""
        self.a_text = False
        self.h3_text = False

    def handle_starttag(self, tag, attrs):
        if tag == "h3":
            self.h3_text = True
            self.a_text = False
            return

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
            return

        self.a_text = False
        self.h3_text = False

    def handle_data(self, data):
        if self.a_text:
            if data == "\r\n            " or data == "\r\n        ":
                pass
            else:
                if self.start_deal:
                    self.content += "###" + " " + "[" + data + "]" + "(" + self.address + ")\n\n" \
                                    + "##### \n\n"
        if self.h3_text:
            if len(data) == 0:
                pass
            else:
                if data == FOLDER_NAME:
                    self.start_deal = True

    def handle_endtag(self, tag):
        if tag == "dl":
            self.start_deal = False


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
    print(hp.content)
    outFile.close()
