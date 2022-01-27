# RoyalRoad-To-PDF
Gets a story and makes a pdf

## Intended Purpose

1. Use this to create a pdf out of a story from royal road
2. Use calibre to convert into MOBI
3. Send to reading device

## Installation

* Download repository

```
pip install -r requirements.txt
```

This utilises pdfkit, which uses wkhtmltopdf.

* For Ubuntu:

```
sudo apt-get install wkhtmltopdf
```

## Usage

* Edit royalroad-to-pdf.py and change *link_to_book* to chosen story
* Change *final_name*
* To have a cover, download an intended image and convert it to pdf (https://jpg2pdf.com/). Place the pdf in same folder as the script and rename it to cover.pdf
* Run royalroad-to-pdf.py
