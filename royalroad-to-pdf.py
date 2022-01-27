import pdfkit
from requests_html import HTMLSession
from PyPDF2 import PdfFileMerger, PdfFileReader
from os.path import isfile

link_to_book = "https://www.royalroad.com/fiction/26294/he-who-fights-with-monsters"
final_name = 'monsters'

session = HTMLSession()

def get_links():
    page = session.get(link_to_book)
    table = page.html.find('tbody', first=True)
    rows = (table.find('tr'))
    # This ignores the preview chapters
    # rows = rows[14:]
    # print(rows)

    links = []
    for row in rows:
        links.extend(list(row.absolute_links))
    
    # print(links)
    return links

def create_chapter_pdfs(links):
    chapters = []
    for link in links:
        page = session.get(link)

        html = '''<head><meta charset="utf-8"/></head>\n'''
        chapter_title = page.html.find('title', first=True).text
        chapter_title = chapter_title.replace(" - He Who Fights With Monsters | Royal Road", "")
        html += f"<h1 style='text-align: center;'>{chapter_title}</h1>\n"
        html +=  page.html.find('.chapter-content', first=True).html

        pdfkit.from_string(html, f'chapters/{chapter_title}.pdf')
        
        chapters.append(chapter_title)
    return chapters

def merge_pdfs(chapters):
    merger = PdfFileMerger()

    if isfile('cover.pdf'):
        merger.append('cover.pdf')

    page_num = 1

    print(chapters)
    for file in chapters:
        path = f'chapters/{file}'

        pdf = PdfFileReader(open(f'chapters/{file}','rb'))
        num_pages = pdf.getNumPages()

        merger.addBookmark(file[:-4], page_num)
        page_num += num_pages

        merger.append(path)
    
    merger.write(f"{final_name}.pdf")
    merger.close()

if __name__ == '__main__':
    chapters = create_chapter_pdfs(get_links())
    merge_pdfs(chapters)