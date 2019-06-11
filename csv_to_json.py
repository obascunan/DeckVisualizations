import csv, json

li = []
with open('am_tran_time.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for origin, destiny, values, longdest, latdest, longorig, latorig in reader:
        if( origin.isdigit()):
            if int(origin) < 10:
                li.append({
                   "origin_id": origin,
                   "destiny_id": destiny,
                   "value": values,
                   "origin_pos": [latorig, longorig],
                   "desinity_pos": [latdest, longdest],
                })
with open("outfile_10.json", "w") as f:
    json.dump(li, f)
