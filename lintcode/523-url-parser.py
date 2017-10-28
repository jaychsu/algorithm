import re

class HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    def parseUrls(self, content):
        # r'': use raw string
        # [=\s]+: this block should contain `=` or blank, and at least one char here
        # ["\']: this block should contain `"` or `'`
        # [^"\'>\s]*: this block should contain any chars until `"`, `'`, `>`, or blank appears
        links = re.findall(r'href[=\s]+["\']([^"\'>\s]*)', content, re.I)
        return [link for link in links if link and not link.startswith('#')]
