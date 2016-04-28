import glob, os

filenames = []
os.chdir("CSVs")
for file in glob.glob("*.csv"):
    filenames.append(file)
print filenames

fout = open("../out2.csv", "a")

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

print "time to create a new list!"
unclean_array = []
for i in range(len(filenames)):
    full = open('../csvs/' + filenames[i], 'r').read()
    num = filenums[i]
    for i in range(len(full)):
        if (full[i:i+6] == str(num)):
            for j in range(2000):
                if(full[i+j:i+j+6] == str(num)):
                    if(full[i+2:i+6]!= ',,,,'):
                        unclean_array.append(full[i:i+j-1])
                        print full[i:i+j-1]
                        fout.write(full[i:i+j-1])
                if(j == 1999):
                    if(full[i+2:i+6]!= ',,,,'):
                        unclean_array.append(full[i:i+2000])
                        print full[i:i+2000]
                        fout.write(full[i:i+2000])
print "up to date"

# print "array finished"
# array_of_arrays = []
# for i in unclean_array:
#     newarr = []
#     oldcommaindex = 0
#     for j in range(len(i)):
#         if(i[j] == ','):
#             newarr.append(i[oldcommaindex:j])
#             oldcommaindex = j+1
#         array_of_arrays.append(newarr)
#     print newarr
