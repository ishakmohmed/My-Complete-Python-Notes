# working with PDFs

import PyPDF2

with open("file.pdf", "rb") as file:
  # its important to read the pdf in binary, thus the "rb" as second arg
  reader = PyPDF2.PdfFileReader(file)
  print(reader.numPages)
  page = reader.getPage(0)
  page.rotateClockwise(90)
  # ^ this just rotates it in memory

  writer = PyPDF2.PdfFileWriter()
  writer.addPage(page) 
  # there's also insertPage(), insertBlankPage(), etc

with open("rotated.pdf", "wb") as output:
  writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names:
  merger.append(file_name)
merger.write("combined(file doesn't need to exist).pdf")