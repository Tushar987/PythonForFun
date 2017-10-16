import urllib.request as req
from bs4 import BeautifulSoup


link="http://knit.ac.in/coe/ODD_2016/odx51fsp741g.asp"
name=[]
marks=[]

for rollno in range(14601,14651):
    result = link+"?rollno="+str(rollno)

    page= req.urlopen(result)

    soup = BeautifulSoup(page)
    # print(soup.prettify())

    all_tables=soup.table.findAll('table')
    # for table in all_tables:
    #     print(table.prettify())

    if len(all_tables)>2:# checking condition for non-existent rollNo.
        print("Getting Result for Rollno:"+ str(rollno))
        name_table=all_tables[0]
        marks_table=all_tables[4]

        # Getting Student Name
        columns=name_table.tr.findAll('td')
        student_name=columns[1].string
        name.append(student_name)

        # Getting Marks
        rows=marks_table.findAll('tr')
        col=rows[2].findAll('td')
        marks_array=col[1].string.split("/")
        student_marks=marks_array[0]
        marks.append(student_marks)
    else:
        print("Rollno: "+ str(rollno)+"Not found")

import pandas as pd

df=pd.DataFrame(name,columns=["Student_Name"])
# print(marks)
# print(len(name))
df['Marks']=marks
print(df)

df.to_csv('Result.csv')