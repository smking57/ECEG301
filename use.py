import requests
import thingspeak
import time
import random
import csv
import json
import os


channel_id = "3573951"
writekey = "4P5XTGX9E940QLLU"
readkey = "RNLNRUZBHNWN27TJ"
csv_name = 'data.csv'

def send_data(field1_value):
    url = f"https://api.thingspeak.com/update?api_key={writekey}&field1={field1_value}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Data sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

def read_data():
    channel = thingspeak.Channel(id=channel_id, api_key=readkey)
    data = json.loads(channel.get_field_last(field="field1"))
    created_at = data["created_at"]
    entry_id = data["entry_id"]
    value = data["field1"]
    print(data)

    new_file = not os.path.exists(csv_name)
    with open(csv_name, "a", newline="") as file:
        writer = csv.writer(file)
        if new_file:
            writer.writerow(["created_at", "entry_id", "field1"])
        writer.writerow([created_at, entry_id, value])


""""
# Example: send simulated sensor data every 15 seconds
while True:
    temperature = random.randint(20, 30)
    humidity = random.randint(40, 60)
    send_data(temperature, humidity)
    time.sleep(15)
"""

send_data(670)

read_data()