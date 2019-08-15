import json

with open('.\Data Converter\decision_point_1.json') as json_file:
    data = json.load(json_file)
    for key, value in data:
        filename = value['name']
        BOTMarines = value['BOT Marines']
    print(filename + '\t' + 'N/A' + '\t' + 'BOTMarines')
    
    # for name in data:
    #     print(data['name'])
    #     for name in data['name']:
    #         print (data['name'['name']])
        #print(item[1] + '\t' + 'N/A' + '\t' + 'N/A' + '\t' + 'N/A' + '\t' + item[3] + '\t' + item[4] + '\t' + item[5] + '\t' + item[6] + '\t' + item[7] + '\t' + [8])