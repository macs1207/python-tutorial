from bs4 import BeautifulSoup

html = """
        <!DOCTYPE html>
        <html>
            <body>
                <h1>My First Heading</h1>
                <div class="content">My first paragraph.</div>
            </body>
        </html>
        """

dom = BeautifulSoup(html, 'lxml')
print(dom.select(".content")[0].text)