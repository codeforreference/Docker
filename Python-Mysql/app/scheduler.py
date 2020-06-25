import time 
import runpy

def scheduler():
    runpy.run_path("/app/app.py")
 
while True:
    scheduler()
    time.sleep(60)