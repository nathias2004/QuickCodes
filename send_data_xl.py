import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
style = xlwt.easyxf('font: bold 1')
sheet1.write(0, 0, 'QIDS',style) 
sheet1.write(0, 1, 'PARAPHRASES',style) 
sheet1.write(0, 2, 'BLEUSCORE',style) 
sheet1.write(0, 3, 'ROUGESCORE',style) 

start = 2

for i in range(0,1200):
	sheet1.write(start,0,i)
	for j in range(0,5):
		sheet1.write(start+j,1,j)
		sheet1.write(start+j,2,0)
		sheet1.write(start+j,3,0)
	start = start+5


  
wb.save('example.xls')