from PIL import Image, ImageDraw
import os
import requests
import json
response = requests.get('https://flunkey.in/restaurant.json?id=5').json()
# print(response['Categories'])
# with open('data.json','w') as f:
#     json.dump(response.json(),f)
filename = "img01.png"
image = Image.new(mode="RGB",size = (200,len(response['Categories'][0]['Food']*20)),color =(73, 109, 137))
text = ''
if response['Categories'][0]['Name'] == "Soups":
    # print(response['Categories'][0]['Food'])
    for i in response['Categories'][0]['Food']:
        print(i["Name"])
        info = i["Name"]
        text += f"\n{info}"
    print(text)     
    draw = ImageDraw.Draw(image)
    draw.text((20,20),text,fill=(255,255,0))
image.save(filename)
os.system(filename)