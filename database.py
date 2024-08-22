import pymysql
import os

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="dynamocareers-dynamocareers.c.aivencloud.com",
  password=os.environ['DB_PASS'],
  read_timeout=timeout,
  port=25582,
  user= os.environ['DB_USER'],
  write_timeout=timeout,
)

def load_jobs_from_db():
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM jobs")
  result= cursor.fetchall()
  return result

def load_job_from_db(id):
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM jobs WHERE id = %(val)s", { 'val': id })
  result= cursor.fetchall()
  if len(result) == 0:
    return None
  else:
    return result

def add_application_to_db(job_id, data):
  cursor = connection.cursor()
  query = ("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
  cursor.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])

