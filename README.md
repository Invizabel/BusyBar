## Busy Bar Smart Dashboard Project

#### HA (Home Assistant):
* WIP
* Needs File editor installed on Home Assistant
* Settings > Apps > File editor > Open Web UI
* Create a folder titled "BusyBar" in the "/homeassistant/" directory
* Then create files called "automations.yaml" and "rest_commands.yaml" and copy and paste the relevant code
* Then, in "/homeassistant/configuration.yaml" at the bottom add:
```
rest_command: !include BusyBar/rest_commands.yaml
automation: !include BusyBar/automations.yaml
```
* Save everything
* Now, Settings > Developer tools > Check configuration (Do not proceed if it fails, check your files/code) > Restart > Restart Home Assistant

#### Features:
* ISS Tracker
* Current Time
* Current Forecast ie- sunny, cloudy, etc (United States only)
* Current Temperature (United States only)
* Current Wind Speed (United States only)

#### Notes:
* Supply your home location coordinates to get accurate weather

###### Todo:
* Add asynchronous GET requests to the various API features 
