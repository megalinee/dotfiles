#!/usr/bin/python3
import requests
import json
import rofi_menu
import asyncio
from datetime import datetime
import os

#Preferences
lightOnSymbol = "󰌵"
lightOffSymbol = "󰌶"

#Hue API
hueRoomName = ""
hueIP = ""
hueUsername = ""


hueURL = 'https://' + hueIP + '/clip/v2/resource'

def GetRoom(roomName):
    jsonData = json.loads(requests.get(hueURL + "/room", headers={'hue-application-key': hueUsername},verify=False).content)
    rooms = jsonData["data"]
    for room in rooms:
        if room["metadata"]["name"] == roomName:
            return room
    
def GetAllRoomLights(room):
    deviceChildren = room["children"]
    lights = []
    for deviceChild in deviceChildren:
        device = json.loads(requests.get(hueURL + "/device/" + deviceChild["rid"], headers={'hue-application-key': hueUsername},verify=False).content)["data"][0]
        for service in device["services"]:
            if service["rtype"] == "light":
                lights.append(device)
    return lights

def GetRoomLightRID(room):
    for service in room["services"]:
        if service["rtype"] == "grouped_light":
            return service["rid"]
        
def GetLightRID(light):
    for service in light["services"]:
            if service["rtype"] == "light":
                return service["rid"]

def GetLightState(light):
    return json.loads(requests.get(hueURL + "/light/" + GetLightRID(light), headers={'hue-application-key': hueUsername},verify=False).content)["data"][0]

def SetRoomLights(room, brightness):
    roomLightRID = GetRoomLightRID(room)
    if brightness == 0:
        return requests.put(hueURL + "/grouped_light/" + roomLightRID, data = '{"on":{"on":false}}', headers={'hue-application-key': hueUsername},verify=False)
    requests.put(hueURL + "/grouped_light/" + roomLightRID, data = '{"on":{"on":true}}', headers={'hue-application-key': hueUsername},verify=False)
    return requests.put(hueURL + "/grouped_light/" + roomLightRID, data = '{"dimming":{"brightness":' + str(brightness) + '}}', headers={'hue-application-key': hueUsername},verify=False)

def SetLight(light, brightness):
    lightRID = GetLightRID(light)
    if brightness == 0:
        return requests.put(hueURL + "/light/" + lightRID, data = '{"on":{"on":false}}', headers={'hue-application-key': hueUsername},verify=False)
    requests.put(hueURL + "/light/" + lightRID, data = '{"on":{"on":true}}', headers={'hue-application-key': hueUsername},verify=False)
    return requests.put(hueURL + "/light/" + lightRID, data = '{"dimming":{"brightness":' + str(brightness) + '}}', headers={'hue-application-key': hueUsername},verify=False)

room = GetRoom(hueRoomName)

class OffAllLights(rofi_menu.Item):
    """Turn off all lights"""
    async def on_select(self, meta):
        SetRoomLights(room, 0)
    
class OnAllLights(rofi_menu.Item):
    """Turn on all lights"""
    async def on_select(self, meta):
        SetRoomLights(room, 100)
        
class ToggleLight(rofi_menu.Item):
    """Toggle light"""
    def setLight(self, light):
        self.light = light
        self.lightState = GetLightState(light)
    
    async def on_select(self,meta):
        SetLight(self.light, 0 if GetLightState(self.light)["on"]["on"] else 100)
        
    async def render(self, meta):
        return (lightOnSymbol if GetLightState(self.light)["on"]["on"] else lightOffSymbol) + " " + self.lightState["metadata"]["name"]


menu_items = [OnAllLights("Turn on all lights"),
        OffAllLights("Turn off all lights")]

for light in GetAllRoomLights(room):
    toggleLight = ToggleLight()
    toggleLight.setLight(light)
    menu_items.append(toggleLight)

main_menu = rofi_menu.Menu(
    prompt="menu",
    items=menu_items,
)


if __name__ == "__main__":
    rofi_menu.run(main_menu)