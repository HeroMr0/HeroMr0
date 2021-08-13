import os
import sys
import time
from threading import Thread
import io

import BotAmino

from PIL import Image, ImageDraw, ImageFont


client = BotAmino.BotAmino()
print(f"Login as {client.profile.nickname=}, {client.authenticated=}")

maintenanceTime = 0
client.self_callable = True
client.wait = 1
client.prefix = "!"

@client.on_member_join_chat()
def main_chat(data):
    text = data.author
    img = Image.open("images/welcome.png")
    width, height = img.size
    font = ImageFont.truetype("images/fonts/beer_money_Regular.ttf", 250)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)
    draw.text(((width - w) / 2, (height - h) / 1.5), text=text, fill=(222, 49, 49, 1), font=font)
    img.save('images/w2.png')
    with open("images/w2.png", "rb") as w2:
        data.subClient.send_message(data.chatId, message="message", file=w2, fileType='image')
    with open("mp3/welcome.mp3", "rb") as aud:
        data.subClient.send_message(data.chatId, file=aud, fileType="audio")



client.launch(True)

print("Bot launched")


def maintenance():
    print("launch maintenance")
    maintenanceTime = 0
    while maintenanceTime < 500:
        maintenanceTime += 10
        time.sleep(10)
    os.execv(sys.executable, ["None", os.path.basename(sys.argv[0])])


Thread(target=maintenance).start()
