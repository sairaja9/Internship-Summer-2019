import json

with open('decision_point_1.json') as json_file:
    data = json.load(json_file)
    for item in data:
        print(item["name"] + "\t" + "N/A" + "\t" + "N/A" + "\t" + "N/A" + "\t" + item["BOT Marines"] + "\t" + item["TOP Marines"] + "\t" + item["BOT Banelings"] + "\t" + item["TOP Banelings"] + "\t" + item["BOT Immortals"] + "\t" + ["TOP Immortals"])