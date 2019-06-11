import csv, json

li = []
with open('am_tran_time.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for origin, destiny, values, longdest, latdest, longorig, latorig in reader:
        if( origin.isdigit()):
            if int(origin) < 2:
                li.append({
                   "o": origin,
                   "d": destiny,
                   "v": values,
                   "op": [latorig, longorig],
                   "dp": [latdest, longdest],
                })
with open("outfile_10.json", "w") as f:
    json.dump(li, f)
