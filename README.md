# PythonUtils
常用Python脚本汇总

---

## WeeklyReportDecoder
通过Chrome导出的书签html文件直接生成Jekyll使用的技术周报md文件。

### 用法(使用python2)
1. 将导出的html文件命名为`bookmarks.html`，放到和`WeeklyReportDecoder.py`相同的目录下。
2. 在终端中使用`python WeeklyReportDecoder.py $1`来生成md文件， `$1`处为技术周报的期数。
3. 在outputs目录下就可以找到生成的md文件。

### py文件中参数说明
* **FOLDER_NAME** Chrome书签中放置要生成周报网址的文件夹名。e.g.,在我Chrome书签的Lately文件夹下放置的是需要生成周报的网址。
* **BLOG_TITLE_NAME** 要生成的Blog标题名称。（同时会对应生成md文件名）
* **BLOG_TITLE_CONTENT** Jekyll所需要的文件头，以及一些自定义预生成内容。

---
