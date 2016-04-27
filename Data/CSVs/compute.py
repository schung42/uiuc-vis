import glob, os
os.chdir("CSVs")
for file in glob.glob("*.csv"):
    print(file)




# steve = open('../csvs/ethsexfa04.csv', 'r')
# print steve.read()
