import glob, os

filenames = []
os.chdir("CSVs")
for file in glob.glob("*.csv"):
    filenames.append(file)
print filenames


filenums = []
for i in filenames:
    steve = open('../csvs/' + i, 'r')
    # print steve.read()
    suffix = 0
    if(i[-8:-6]=='sp'):
        suffix = 1
    if(i[-8:-6]=='su'):
        suffix = 5
    if(i[-8:-6]=='fa'):
        suffix = 8
    prefix = 120000 + 10*int(i[-6:-4]) + suffix
    filenums.append(prefix)
print filenums

for i in range(len(filenames)):
    full = open('../csvs/' + filenames[i], 'r').read()
    num = filenums[i]
    for i in range(len(full)):
