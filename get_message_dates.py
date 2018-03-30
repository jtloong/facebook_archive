from bs4 import BeautifulSoup
import glob, csv
file_names = glob.glob("messages/*.html")
message_dates = []
message_dates.append('time')
for file_name in file_names:
    print(file_name)
    f = open(file_name, 'r').read()
    soup = BeautifulSoup(f, 'lxml')
    times = soup.findAll("span", { "class" : "meta" })
    times = [str(i)[19:-7] for i in times]
    message_dates.append(times)

with open("analysis/message_dates.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(message_dates)
