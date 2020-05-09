from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer


fp = open("Text-searchable.pdf", 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)

if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

rsrcmgr = PDFResourceManager()
device = PDFDevice(rsrcmgr)
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

file_w=open("Testing.txt", 'w')
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()

def parse_obj(lt_objs):
    words=[]
    for obj in lt_objs:
        
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            
            for line in obj:
                if isinstance(line, pdfminer.layout.LTTextLineHorizontal):
##                    print(line)
                    text = ""
                    for char in line:
#                        pos=0
                        a=char.__repr__()
                        b=char.get_text().encode("UTF-8")
                        string = a[8:40].rstrip(" matri")
                        print("Co-ords: {}".format(string))
                        print("text: "+b)
                        if b==" ":
                            text=text+" "
                            val2 = string.split(",")
                            if val2[0] == "' '>":
                                pass
                            else:
                                start_coord = []
                                end_coord = []
                                new = []
                                for i in range(len(val2)):
                                    if i==0:
                                        start_coord.append(float(val2[i]))
                                        end_coord.append(float(val2[i])+2.45)
                                    else:
                                        start_coord.append(float(val2[i]))
                                        end_coord.append(float(val2[i]))
                                new.append(end_coord[0])
                                new.append(end_coord[1])
                                
                                new.append(start_coord[0])
                                new.append(start_coord[2])
                                
                            print("start:", start_coord)
                            print("end:", end_coord)

                            print("\nfinal:", new)
                        elif b=="\n":
                            words.append(text)
                        else:
                            text = text+b
    print(words)
            
parse_obj(layout._objs)
