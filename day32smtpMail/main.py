import smtplib
import datetime as dt
import pandas
import random

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

now = dt.datetime.now()
today= (now.month,now.day)

if today in birthdays_dict.keys():
          file_path= f"letter_templates/letter_{random.randint(1,3)}.txt"
          with open(file_path) as file:
              letter=file.read()
              new_letter=letter.replace("[NAME]",birthdays_dict[today]["name"])

my_email = "zyxwvuts941@gmail.com"
password ="******************"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs= birthdays_dict[today]["email"],
                        msg=f"subject:Happy Birthday!!\n\n {new_letter} ")









