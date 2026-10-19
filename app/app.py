import os
n=os.getenv("STUDENT_NAME","Bek"); s=os.getenv("STUDENT_SURNAME","Kadyrbekov")
g=os.getenv("STUDENT_GROUP","IT2-2306"); i=os.getenv("STUDENT_ID","35534")
print("================================")
print("DevOps Student Application")
print("================================")
print(f"Name: {n}\nSurname: {s}\nGroup: {g}\nStudent ID: {i}")
print("Application is running successfully!")
