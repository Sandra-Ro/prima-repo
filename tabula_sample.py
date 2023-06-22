iimport tabula as tb
import glob
myfile = 'H:/Работа/Python/Ejegodnik_2021.pdf'
mytable = tb.read_pdf(myfile, pages=75, relative_area=True, area=[9, 3, 64, 98], stream=True, columns=())
print(mytable[0].head(19))
tb.convert_into('H:/Работа/Python/Ejegodnik_2021.pdf', 'H:/Работа/Python/Ejegodnik_2021.csv', pages='75', relative_area=True, area=[9, 3, 64, 98], stream=True, columns=())
#mytable[0].to_csv('H:/Работа/Python/Ejegodnik_2021-1.csv')
