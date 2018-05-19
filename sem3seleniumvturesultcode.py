import math
from selenium import webdriver
chrome_path = r"C:\Users\Himanshu Poddar\Desktop\chromedriver.exe"

URL = "http://results.vtu.ac.in/vitaviresultcbcs/index.php"
j=1
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
        
file=open(r"C:\Users\Himanshu Poddar\Desktop\sgpavturesuhgj.txt","w")

while(j<=3):
    wd = webdriver.Chrome(chrome_path)
    wd.get(URL)
    usn = wd.find_element_by_name("usn")
    usn_input = "1PE16CS"+str(j).zfill(3)
    usn.send_keys(usn_input)
    inputs = wd.find_elements_by_xpath("//input")
    inputs[1].click()
    wd.switch_to_window(wd.window_handles[0])

    import bs4 as bs
    soup = bs.BeautifulSoup(wd.page_source.encode('utf-8'),'html.parser')
    x =  wd.find_elements_by_class_name("divTableCell")
    lista = []
    for y in x:
       lista.append(y.text)
    i=0
    
    try:
        new_list = []
        i=10
        while(i<=52):
            new_list.append(lista[i])
            i=i+6
        ar2=new_list
        k=0
        ar2 = [int(i) for i in ar2]
        while(k<len(ar2)):
            ar2[k] = func(ar2[k])
            k=k+1
        sm=((sum(ar2[0:6])*4)+(sum(ar2[6:8]))*2)/28
        file.write(usn_input)
        file.write(",")
        file.write(new_list[0])
        file.write(",")
        file.write(new_list[1])
        file.write(",")
        file.write(new_list[2])
        file.write(",")
        file.write(new_list[3])
        file.write(",")
        file.write(new_list[4])
        file.write(",")
        file.write(new_list[5])
        file.write(",")
        file.write(new_list[6])
        file.write(",")
        file.write(new_list[7])
        file.write(",")
        file.write(str(sm))
        file.write("\n")
        print(usn_input)
    except:
        print("error at",usn_input)

    wd.close()
    j=j+1
file.close()
