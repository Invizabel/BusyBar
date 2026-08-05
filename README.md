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
* Now, Settings > Developer tools > Check configuration (Do not proceed if it fails, check your files/code) > Restart > Quick reload
* Note 1: Make sure you change the IP in rest_commands.yml that you created to the LAN IP of your Busy Bar
* Note 2: It's a good idea to give your Busy Bar a static IP (check your routers help page for info on how to do this)
* Note 3: Example YAML file uses The National Weather Service integration in Home Assistant
* Note 5: To find an integration, go to Settings > Developer tools > States > filter by integration you want
* Note 6: Home Assistant supports Jinja templates

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
