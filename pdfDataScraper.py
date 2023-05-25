import pypdf;
pdfFileObj = open('copd2012to2014.pdf', 'rb')
pdfReader = pypdf.PdfReader(pdfFileObj)
print(len(pdfReader.pages))#prints number of pages in the pdf
#change year for each year 
currDate="2014"

totalText = '';
for i in pdfReader.pages:
    totalText+=i.extract_text()
    #i represents a pageObj
totalTxtArr= totalText.split(" ") 
for i in range(0,len(totalTxtArr)):
    currstr= totalTxtArr[i]
    if currstr.endswith(currDate): #detects cell in the matrix with a date
        countyName= totalTxtArr[i+1]
        n=0
        for j in range(2,5):
            n+=1
            if totalTxtArr[i+j].isnumeric(): 
                break #accounts for multiple word county names
            countyName+= totalTxtArr[i+j]
        print(currDate +" "+ countyName + " "+totalTxtArr[i+n+15])
        

    
        
