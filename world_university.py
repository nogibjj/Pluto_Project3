## import modules
## pip install psycopg2
import psycopg2
connection = psycopg2.connect("world_university.db")
cursor = connection.cursor()
print("Connect to PostgreSQL")
# create a new table for world_university.csv
table = "CREATE TABLE world_university_info (world_rank INTEGER PRIMARY KEY, institution TEXT, country TEXT, national_rank INTEGER, quality_of_education INTEGER, alumni_employment INTEGER, quality_of_faculty INTEGER, publications INTEGER, influence INTEGER, citations INTEGER, patents INTEGER, score INTEGER, teaching INTEGER, international INTEGER, research INTEGER, citations INTEGER, total_score INTEGER, num_students INTEGER, student_staff_ratio INTEGER, international_students INTEGER)"
cursor = connection.cursor() 
cursor.execute(table)
connection.commit()




