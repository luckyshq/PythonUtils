from HTMLParser import HTMLParser

FOLDER_NAME = "Lately"

class MyHTMLParser(HTMLParser):
    a_text = False
    h3_text = False

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.start_deal = False
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
                    print("###" + " " + "[" + data + "]" + "(" + self.address + ")\n\n")
        if self.h3_text:
            if len(data) == 0:
                pass
            else:
                if data == FOLDER_NAME:
                    self.start_deal = True




if __name__ == "__main__":
    htmlFile = open("WeeklyReportDecoder/bookmarks.html", "r")
    html_code = htmlFile.read()
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    htmlFile.close()
