import csv

with open('data/convertcsv.csv', newline='') as csvfile:
  with open('data/metrovisazoho.csv', 'w+') as csvout:
    writer = csv.writer(csvout, lineterminator='\n')
    cs = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(cs, None)  # skip the first row from the reader, the old header
    writer.writerow(['Date-dd/MM/YY', 'Withdrawals', 'Deposits', 'Payee', 'Description', 'Reference Number']) # write new header
    for line in cs:
        if line[0] == '':
            print (''.join(line) +' was eliminated')
        else:
            writer.writerow((line[0],line[4],line[5],'',line[3],line[2]))
