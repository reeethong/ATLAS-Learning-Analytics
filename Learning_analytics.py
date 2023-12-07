'''To run code, 
1) on microsoft teams, navigate to excel sheet file
2) Press the arrow down and click "Sync"
3) Login to onedrive
4) Navigate and find path to xlsx file
5) update URL on line 14 , May need to change backslashes to double backslashes
Dependencies:
1) pip install pandas
2) pip install openpyxl
'''


import pandas as pd
url = "D:\\Nanyang Technological University\\NTU Imperial Student-Led Project on Learning Analytics - General\\NTU Student Analytics Survey.xlsx"
df = pd.read_excel(url)
columnlist = list(df.columns)
# for i in columnlist:
#     print(i)
#     print("\n")
df = df[["ID","Year of Study", "School", "I have read and understood the instructions.", \
        "1.\xa0\xa0\xa0\xa0\xa0I keep track of my own learning data (e.g. tracking hours spent on a module per week, strengths and weakness in terms of course topics).2",\
        "2.\xa0\xa0\xa0\xa0 It is important to keep track and analyse my own learning data.2",\
        "3.\xa0\xa0\xa0\xa0 I will adjust my study habits or learning strategies based on insights from learning analytics.2",\
        "Would you like to elaborate on your ratings?2", \
        "1.\xa0\xa0\xa0\xa0 I know that the university has put in place a student data governance policy in line with PDPC.2",\
        "2.\xa0 \xa0 \xa0The university should ask for my explicit consent for learning analytics projects if it involves any identifiable data about me (e.g., name, ethnicity, age, and gender).2",\
        "3.\xa0\xa0\xa0\xa0 I am comfortable with the idea of NTU collecting data on my learning behaviours and performances to improve teaching and learning.2",\
        "4.\xa0\xa0\xa0\xa0 It is important to me that I can opt out of the collection of my learning data for my professors and tutors. 2",\
        "5.\xa0\xa0\xa0\xa0 It is important to me that I can opt out of the collection of my learning data to be used by myself.2",\
        "Would you like to raise any further privacy concerns that NTU should address with learning analytics?2",\
        "Do you have any further suggestions or comments on how you would like to be supported by learning analytics?",\
        "1.\xa0\xa0\xa0\xa0 The university should regularly update me about my learning progress based on the analysis of my educational data.3",\
        "2.\xa0 \xa0The learning analytics service should show how my learning progress compares to the course learning outcomes.3",\
        "3.\xa0\xa0\xa0\xa0 I expect the teaching staff to act (i.e. support me) if the analytics show that I am at-risk of failing, underperforming or needs improvement in my learning.3",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU. a. Early AleRT for Learning Intervention (EARLI): A predictive AI project to detect and support at-risk students...",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU. b. Course Analytics Dashboard for Students (CADS): A personalised learning analytics project that provides facul...",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU.\xa0c. NTU AI Learning Assistant (NALA): Customised Gen-AI tutoring chatbot to guide students based on faculty curat...",\
        "4.\xa0\xa0\xa0\xa0 I feel that the following project could potentially benefit students in NTU.\xa0d. Skills and Course Advising for Learning Excellence (SCALE): A course and co-curricular recommendation AI proj...",\
]]

df.drop(df[df['I have read and understood the instructions.'] != 'Yes'].index, inplace=True)

STEM_Schools = [
"CCEB",	
"CEE",
"COE",
"EEE",
"MSE",
"MAE",
"REP",
"SBS",
"SCSE",
"SPMS",
"SSM"	
]
num_STEM_Schools = 8 + 10 + 5 + 21 + 4 + 12 + 4 + 11 + 22 + 13 + 2 
#Science,tech,engineering,maths
non_STEM_Schools = ["ADM","ASE", "SOH", "WKWSCI", "NBS", "NIE", "LKCSoM", "SSS"]
num_Non_STEM_Schools = 5 + 1 + 15 + 1 + 22 + 3 + 2 + 6
# print(df["ID"].head(20))
print(num_STEM_Schools, num_Non_STEM_Schools)