from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu


def docum():
    doc = DocxTemplate(r'C:\Users\PRAVEENKUMAR\Desktop\Documents.docx')

    screen_1 = InlineImage(doc,'p.png',Inches(6))

    context = {'name' : input("Enter Document Name"),
               'screen1':screen_1,
               'name2' : input("2nd Screen name"),
               'screen2':screen_1

               }

    doc.render(context)

    doc.save(r'C:\Users\PRAVEENKUMAR\Desktop\document.docx')

