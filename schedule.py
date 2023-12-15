from apscheduler.schedulers.blocking import BlockingScheduler
import os
from datetime import datetime

def clean_qrcode_files():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}]::INFO:: cleaning qr code png files..")
    os.system("rm -f app/qrcode/*")

scheduler = BlockingScheduler()
scheduler.add_job(clean_qrcode_files, 'interval', hours=8)
scheduler.start()