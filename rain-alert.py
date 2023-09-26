from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()

lat = os.getenv("MY_LAT")
lon = os.getenv("MY_LONG")

owm_api_key = os.getenv("OWM_API_KEY")
twilio_acc_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
recipient_number = os.getenv("RECIPIENT_NUMBER")
my_twilio_number = os.getenv("MY_TWILIO_NUMBER")


response = requests.get(f"https://api.openweathermap.org/data/2.8/onecall?lat={lat}&lon={lon}&appid={owm_api_key}")
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("It's going to rain today. Remember to bring an Umbrella ☂️ and condition code is: ", condition_code)

    client = Client(twilio_acc_sid, twilio_auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an Umbrella ☂️",
            from_=my_twilio_number,
            to=recipient_number
        )

    print(message.status, " With SID: " + message.sid)

else:
    print("It won't rain and the condition code is: ", condition_code)
