import pandas as pd
import re

data = pd.read_csv('postings.csv')
len_data = len(data['job_skills'])

sk = []
jt = []
for i in range(0, len_data):
    skill = data['job_skills'][i]
    title = data['job_title'][i]
    sk.append(skill)
    jt.append(title)

skill_list = []
for s in sk:
    s = str(s)
    skills = s.split(',')
    skill_list.extend(skills)

sk_lst = []
for skill in skill_list:
    n = skill.replace(" ", "")
    n = n.replace("#", "")
    n = n.replace("*", "")
    n = n.replace(".", "")
    if n != 'nan':
        sk_lst.append(n)


job_list = []
delimiters = ['-', ',']
for j in jt:
    j = str(j)
    j = j.replace(".", "")
    j = j.replace("Sr", "Senior")
    j = j.replace("Jr", "Junior")
    jb = []
    for delimiter in delimiters:
        jobs = re.split(',|-', j)
        jb.extend(jobs)
    job_list.extend(jb)

job = []
for j in job_list:
    j = str(j)
    j = j.lstrip(' ')
    if j.__contains__('Data'):
        job.append(j)

senior = []
junior = []
engineer = []
analyst = []
scientist = []
big_data = []
for s in job:
    if s.__contains__('Senior'):
        senior.append(s)
    elif s.__contains__('Junior'):
        junior.append(s)
    elif s.__contains__('Engineer'):
        engineer.append(s)
    elif s.__contains__('Analyst'):
        analyst.append(s)
    elif s.__contains__('Scientist'):
        scientist.append(s)
    elif s.__contains__('Big Data'):
        big_data.append(s)


skill_count = pd.Series(sk_lst).value_counts()
#print(skill_count[0:20])

job_title_count = pd.Series(job).value_counts()
#print(job_title_count[:35])

job_countries_count = pd.Series(data['job_location']).value_counts()
print(job_countries_count)

search_countries_count = pd.Series(data['search_country']).value_counts()
print(search_countries_count)

job_level_count = pd.Series(data['job level']).value_counts()
print(job_level_count)

senior_positions = str(len(senior))
junior_positions = str(len(junior))
engineer_positions = str(len(engineer))
analyst_positions = str(len(analyst))
scientist_positions = str(len(scientist))
big_positions = str(len(big_data))
print("Senior positions: " + senior_positions)
print("Junior positions: " + junior_positions)
print("Engineer positions: " + engineer_positions)
print("Analyst positions: " + analyst_positions)
print("Scientist positions: " + scientist_positions)
print("Big Data positions: " + big_positions)
