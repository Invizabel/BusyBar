## Busy Bar Smart Dashboard Project

#### HA (Home Assistant):
* Needs File editor installed on Home Assistant
* Settings > Apps > File editor > Open Web UI
* In "/homeassistant/configuration.yaml" at the bottom add the code from configurations.yaml
* In "/homeassistant/automations.yaml" at the bottom add the code from automations.yaml
* Save everything
* Now, Settings > Tools > Check configuration (Do not proceed if it fails, check your files/code) > Restart > Quick reload
* Note 1: Make sure you change the IP in configuration.yaml that you created to the LAN IP of your Busy Bar
* Note 2: It's a good idea to give your Busy Bar a static IP (check your routers help page for info on how to do this)
* Note 3: Example YAML file uses The National Weather Service integration in Home Assistant
* Note 4: To find an integration, go to Settings > Developer tools > States > filter by integration you want
* Note 5: Home Assistant supports Jinja templates

#### API (PC/Mac):
* ISS Tracker
* Current Time
* Current Forecast ie- sunny, cloudy, etc (United States only)
* Current Temperature (United States only)
* Current Wind Speed (United States only)

#### Notes:
* Supply your home location coordinates to get accurate weather

###### Todo:
* Add asynchronous GET requests to the various API features 
