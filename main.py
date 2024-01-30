import pandas as pd
import smtplib
from datetime import datetime
import random

with open('login.txt') as login:
    content = login.readlines()
    MY_EMAIL = content[0].strip()
    MY_PASSWORD = content[1].strip()


today_tuple = (datetime.now().month, datetime.now().day)

df = pd.read_csv('birthdays.csv')
birthdays_dict = {(row.month, row.day): row for (index, row) in df.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday! \n\n{contents}"
            )