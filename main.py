import smtplib
import datetime as dt
import random

my_email = "sample@gmail.com"
password = "pass"

now = dt.datetime.now()
day_of_week = now.weekday()

def sent_mail(motivation_massage: str):
    """Docstring

    :param motivation_massage
    """

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="destination_email@gmail.com",
            msg=f"Subject:Moc, energia...\n\n {motivation_massage}"
        )


if day_of_week == 0:
    with open("quotes.txt", "r") as file:
        quotes_list = file.readlines()
    motivation_massage = random.choice(quotes_list)
    sent_mail(motivation_massage)


















