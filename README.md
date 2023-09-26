# Rain Alert Script

## Overview

The Rain Alert Script is a Python script that utilizes Twilio's SMS API and OpenWeather's API to provide rain alerts. It checks the weather forecast and sends an SMS notification if rain is expected within a specified timeframe.

## Features

- Receive SMS alerts about upcoming rain.
- Customizable location and time window for rain alerts.
- Utilizes Twilio's SMS service for reliable notifications.
**NOTE**: *Twilio's free service involve some bounus credits, which you can use to send SMS. However, it will eventually run out and thereafter you might want to pay for their extra services*
- Utilizes OpenWeather's API for weather data.

## Requirements

- Python 3.x
- Twilio API credentials
- OpenWeather API key

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python packages:
3. Set up a Twilio account and obtain your Account SID, Auth Token, and Twilio phone number. Also get hold of a phone number to send the rain alert SMS to.
4. Sign up for an OpenWeather API key.
5. Create a `.env` file with your Twilio, OpenWeather API credentials, coordinates, phone number as environment variables.
6. Keep in mind that the time in which the script checks is 6AM to 6PM (12hrs for usual office hours). If it does rain 
within this time window, the alert will be sent. You can check out OpenWeather's API doc [here](https://openweathermap.org/api/one-call-3) on how it works
7. Run the `rain_alert_script.py` file.

## Configuration

You can customize the following variables in `config.py`:

- `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio authentication token.
- `RECIPIENT_NUMBER`: Number to which the alert should go to.
- `MY_TWILIO_NUMBER`: Your Twilio phone number(Number from which the alert is sent from).
- `OPENWEATHER_API_KEY`: Your OpenWeather API key.
- `MY_LAT`,`MY_LONG` : The location for which you want to receive rain alerts (latitude and Longitude).

## Acknowledgments

- [Twilio](https://www.twilio.com/) for their SMS service.
- [OpenWeather](https://openweathermap.org/) for providing weather data.

## Contributing

If you'd like to contribute, please fork the repository and create a pull request. Please make sure to update tests as appropriate.

## Support

If you encounter any issues or have suggestions, please [open an issue](https://github.com/muhzinkhan/rain-alert/issues).

## Roadmap

- [ ] Add support for multiple locations and customizable time windows.
- [ ] Implement additional notification methods (e.g., email).
- [ ] Create a web interface for easy setup and configuration.

## Authors

- [Muhsin Khan](https://github.com/muhzinkhan)

## Disclaimer

This script is provided as-is, without any warranty or guarantee of any kind. Use at your own risk.
