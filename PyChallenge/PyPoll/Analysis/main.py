import os 
import csv

inputfile = os.path.join("Resources","election_data.csv")
outputfile = os.path.join("Analysis","analysis.txt")

totalvote = 0
candiatelist = []
candiatevotes = {}

winner = ""
winnervotes = 0

with open (inputfile) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        totalvote = totalvote + 1 
        candiatename = row[2]
        if candiatename not in candiatelist: 
            candiatelist.append(candiatename)
            candiatevotes[candiatename] = 0
        candiatevotes[candiatename] = candiatevotes[candiatename] + 1

with open (outputfile, "w") as textfile:
    for candiate in candiatevotes:
        votes = candiatevotes[candiate]
        if votes > winnervotes:
            winnervotes = votes
            winner = candiate
    summary = "Winning Candiate"
    textfile.write(summary)
    print(summary)

    
