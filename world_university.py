## import modules
## pip install pymysql
import sqlite3
import pandas as pd

connection = sqlite3.connect("world_university.db")
cursor = connection.cursor()
print("Connect to SQLite database")

# create a new table for world_university.csv
# table = "CREATE TABLE world_university2 (world_rank INTEGER PRIMARY KEY, institution TEXT, country TEXT, national_rank INTEGER, quality_of_education INTEGER, alumni_employment INTEGER, quality_of_faculty INTEGER, publications INTEGER, influence INTEGER, citations INTEGER, patents INTEGER, score INTEGER, teaching INTEGER, international INTEGER, research INTEGER, total_score INTEGER, num_students INTEGER, student_staff_ratio INTEGER, international_students INTEGER)"

# exercute and query data using the cursor
# cursor.execute(table)

# load world university data into the table
world_university1 = pd.read_csv("world_university2.csv")

# insert data into the table
world_university1.to_sql(
    "world_university2", connection, if_exists="replace", index=False
)

# quickly overview the data
select_query = "SELECT * FROM world_university2"
for all_info in cursor.execute(select_query):
    print(all_info)

cursor.execute(select_query).fetchmany(size=5)

# query1: Which five universities have the highest total score in United States?
query1 = """SELECT institution, total_score
         FROM world_university2
         WHERE country = 'USA' 
         ORDER BY total_score DESC 
         LIMIT 5;"""
UStop5_university_highest_total_score = cursor.execute(query1).fetchall()

# result 1
print("#" * 45)
print("The highest total score in top 5 universities in US :")
for i in UStop5_university_highest_total_score:
    print(i)

# query2: which five universities have the lowest international students ratio in United Kingdom?
query2 = """SELECT institution, international_students
         FROM world_university2
         WHERE country = 'United Kingdom'
         ORDER BY international_students ASC
         LIMIT 5;"""
UKlowest5_university_lowest_international_students_ratio = cursor.execute(
    query2
).fetchall()

# result 2
print("#" * 45)
print("The lowest international students ratio in top 5 universities in UK :")
for k in UKlowest5_university_lowest_international_students_ratio:
    print(k)

# query3: which five universities have the highest rank of publications in United States?
query3 = """SELECT Distinct institution, publications
            FROM world_university2
            WHERE country = 'USA'
            ORDER BY publications ASC
            LIMIT 5;"""
UStop5_university_highest_rank_publications = cursor.execute(query3).fetchall()

# result 3
print("#" * 45)
print("The highest rank of publications in top 5 universities in US :")
for j in UStop5_university_highest_rank_publications:
    print(j)

# query4: which top 3 universities have the highest teaching scores in United States?
query4 = """SELECT Distinct institution, teaching
            FROM world_university2
            WHERE country = 'USA'
            ORDER BY teaching DESC
            LIMIT 3;"""
UStop3_university_highest_teaching_scores = cursor.execute(query4).fetchall()

# result 4
print("#" * 45)
print("The highest teaching scores in top 3 universities in US :")
for m in UStop3_university_highest_teaching_scores:
    print(m)


# query5: which top 5 universities have the highest rank of quality of education and quality of faculty both in the United States?
query5 = """SELECT Distinct institution, quality_of_education, quality_of_faculty
            FROM world_university2
            WHERE country = 'USA'
            ORDER BY quality_of_education ASC, quality_of_faculty ASC
            LIMIT 5;"""
UStop5_university_highest_rank_quality_of_education_quality_of_faculty = cursor.execute(
    query5
).fetchall()

# result 5
print("#" * 45)
print(
    "The highest rank of quality of education and quality of faculty in top 5 universities in US :"
)
for n in UStop5_university_highest_rank_quality_of_education_quality_of_faculty:
    print(n)

## close the connection
connection.close()
