import spacy
import PyPDF2

nlp = spacy.load('en_core_web_lg')


def return_ents(doc):
    d = {}
    if doc.ents:
        for ent in doc.ents:
            d[ent.text] = ent.label_ + ' - ' + str(spacy.explain(ent.label_))
        return d
    else:
        return {'message': 'No named entities found.'}


def extract_file():
    text = ''
    file = open("test.pdf", mode="rb")
    pdf_reader = PyPDF2.PdfFileReader(file)
    for i in range(pdf_reader.numPages):
        page = pdf_reader.getPage(i)
        text = text + page.extract_text()

    doc = nlp(text)
    return return_ents(doc)


