import pypdf;
currDate="2019"
pdfFileObj = open('pqi_summary_v2020_'+currDate+'.pdf', 'rb')
pdfReader = pypdf.PdfReader(pdfFileObj)
print(len(pdfReader.pages))#prints number of pages in the pdf

totalText = '';
for i in pdfReader.pages:
    totalText+=i.extract_text()
    #i represents a pageObj
totalTxtArr= totalText.split(" ") 
print(totalTxtArr)
for i in range(0,len(totalTxtArr)):
    currstr= totalTxtArr[i]
    if '\n' in currstr and i<(len(totalTxtArr)-12): #detects cell in the matrix with a date
        countyName= currstr[currstr.index('\n')+1:]
        n=-1
        for j in range(1,4):
            n+=1
            if totalTxtArr[i+j].isnumeric(): 
                break #accounts for multiple word county names
            countyName+= totalTxtArr[i+j]
        print(currDate +" "+ countyName + " "+totalTxtArr[i+n+11])
        

    
        
