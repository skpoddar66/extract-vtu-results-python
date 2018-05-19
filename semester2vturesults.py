import requests
import math
from bs4 import BeautifulSoup
x=0;
def func(x):
    if(x>=45 and x<50):
        return 5
    elif(x>=40 and x<45):
        return 4
    elif(x<40):
        return 0
    elif(x%10==0):
        return math.ceil(x/10)+1;
    elif(x%10!=0):
        return math.ceil(x/10)
    else:
        return 0
        
file=open("sgpavturesuhgj.txt","w")
i=1
while(i<187):
    url="http://results.vtu.ac.in/cbcs_17/result_page.php?usn=1pe16cs%03d"%i
    try:
     r=requests.get(url);
    except:
        try:
           r=requests.get(url);
        except:
            r=requests.get(url);
    soup=BeautifulSoup(r.content,"html.parser")
    table=soup.find('table',{'class':'table table-bordered'})
    arr=[]
    
    usn="1PE16CS%03d"%i
    #usn="1PE16CS012"
    print(usn)
    for row in table.findAll('td'):
      arr.append(row.text.strip())
    file.write(usn)
    file.write(",")
    file.write(arr[4])
    
    file.write(",")
    file.write(arr[10])
    file.write(",")
    file.write(arr[16])
    file.write(",")
    file.write(arr[22])
    file.write(",")
    file.write(arr[28])
    file.write(",")
    file.write(arr[34])
    file.write(",")
    file.write(arr[40])
    file.write(",")
    file.write(arr[46])
    
    ar2=[int(arr[4]),int(arr[10]),int(arr[16]),int(arr[22]),int(arr[28]),int(arr[34]),int(arr[40]),int(arr[46])]
    
    ar2=list(map(lambda x:func(x),ar2))
    sm=0
    sm=sum(ar2)
    sm=((sum(ar2[0:5])*4)+(sum(ar2[5:7]))*2)/24;
    file.write(","+str(sm));
    file.write("\n")
    print("\nCGPA="+str(sm)+"\n")            
         
    #print(arr[4]+" "+arr[10]+" "+arr[16]+" "+arr[22]+ " "+arr[28]+" "+arr[34]+" "+arr[40]+" "+arr[46])
    i=i+1
file.close()

