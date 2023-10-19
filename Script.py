import datetime
import json
import mysql.connector
from plyer import notification
import pyttsx3
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'passkey=00',
    'database': 'devops',
}
BIRTHDAYS_FILE = 'birthdays.json'
def load_birthdays():
    try:
        with open(BIRTHDAYS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def schedule_notifications():
    today = datetime.date.today()
    birthdays = load_birthdays()

    for birthday, name in birthdays.items():
        month, day = map(int, birthday.split())
        birthday_date = datetime.date(today.year, month, day)
        days_until_birthday = (birthday_date - today).days

        if days_until_birthday == 0:
            message = f"Today is {name}'s birthday! 🎉"
            notification.notify(
                title='Birthday Notification',
                message=message,
                app_icon="C:\\Users\\Arnav\\OneDrive\\Documents\\cake.ico",
                app_name='Birthday Reminder',
                timeout=10,
            )
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
i=0
while(i<2):
    schedule_notifications()
    i+=1
speak("Birthday notification")
