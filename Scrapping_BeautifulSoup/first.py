from urllib.request import Request, urlopen
from urllib.error import URLError , HTTPError
from bs4 import BeautifulSoup


# Copy your link here--
link="http://knit.ac.in/coe/ODD_2016/odx51fsp741g.asp"
# Link for result of IT 2014-18 3rd year


name = []
marks = []

# The code utilizes QueryString to generate all the Roll Numbers for the given range.
# The range should be changed manually for personal use.

import itertools as it
for rollno in it.chain(range(14601,14652),range(158602,158613)): # Chaining ranges for Regular and lateral students
    URL = link+"?rollno="+str(rollno)

    try:
        page= urlopen(URL)
    except URLError as e:
        if hasattr(e, 'reason'):
            print
            'We failed to reach a server.'
            print
            'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print
            'The server couldn\'t fulfill the request.'
            print
            'Error code: ', e.code
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
    else:
        soup = BeautifulSoup(page)
        all_tables=soup.table.findAll('table')

        if len(all_tables) > 2:   # checking condition for non-existent rollNo.
            name_table = all_tables[0]
            name_table_rows =  name_table.findAll('tr')
            # Getting Branch for confirmation. Some Students changed their branch after 1st Year.
            columns = name_table_rows[4].findAll('td')
            Branch_name = columns[1].string

            if Branch_name == "Information Technology" :
                print("Getting Result for Rollno:" + str(rollno))
                # Getting Student Name
                columns=name_table_rows[0].findAll('td')
                student_name=columns[1].string
                name.append(student_name)
                # Getting Marks
                marks_table = all_tables[4]
                rows=marks_table.findAll('tr')
                col=rows[2].findAll('td')
                marks_array=col[1].string.split("/")
                student_marks=marks_array[0]
                marks.append(student_marks)
            else:
                print("Rollno: " + str(rollno) + " Does not exist.")
        else:
            print("Rollno: " + str(rollno)+" Not found")

import pandas as pd
df=pd.DataFrame(name,columns=["Student_Name"])
df['Marks'] = marks
print(df)

df.to_csv('Result.csv')
