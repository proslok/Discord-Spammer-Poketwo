from webserver import keep_alive
import requests

channelID = 1032893966565249125
headers = {
    "authorization":
    "MTAzMjU2MTI4ODM0MzIxMjA0NA.GbdMAX.-TVcO7dBq5e8dZUxbsql_nhkqnFJuiJP3kUeFA"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
