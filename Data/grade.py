import csv, os, glob

grades = {'overall': 0.0,

'Engineering': {
'overall': 0.0,
'CS': { 'overall': 0.0, '125': 7.9 },
'ECE': { 'overall': 0.0 },
'CEE': { 'overall': 0.0 },
'ME': { 'overall': 0.0 },
'TAM': { 'overall': 0.0 },
'MSE': { 'overall': 0.0 },
'AE': { 'overall': 0.0 },
'IE': { 'overall': 0.0 },
'NPRE': { 'overall': 0.0 },
'ENG': { 'overall': 0.0 },
'GE': { 'overall': 0.0 },
'BIOE': { 'overall': 0.0 },
'ABE': { 'overall': 0.0 }, },

'Liberal Arts and Sciences': {
'overall': 0.0,
'CHEM': { 'overall': 0.0 },
'MATH': { 'overall': 0.0 },
'ECON': { 'overall': 0.0 },
'PHYS': { 'overall': 0.0 },
'PSYC': { 'overall': 0.0 },
'MCB': { 'overall': 0.0 },
'STAT': { 'overall': 0.0 },
'CMN': { 'overall': 0.0 },
'ANTH': { 'overall': 0.0 },
'IB': { 'overall': 0.0 },
'PS': { 'overall': 0.0 },
'ATMS': { 'overall': 0.0 },
'ENGL': { 'overall': 0.0 },
'HIST': { 'overall': 0.0 },
'SOC': { 'overall': 0.0 },
'CLCV': { 'overall': 0.0 },
'ASTR': { 'overall': 0.0 },
'RLST': { 'overall': 0.0 },
'CHBE': { 'overall': 0.0 },
'PHIL': { 'overall': 0.0 },
'GEOL': { 'overall': 0.0 },
'LAS': { 'overall': 0.0 },
'GEOG': { 'overall': 0.0 },
'LING': { 'overall': 0.0 },
'EALC': { 'overall': 0.0 },
'GWS': { 'overall': 0.0 },
'FR': { 'overall': 0.0 },
'GLBL': { 'overall': 0.0 },
'LAST': { 'overall': 0.0 },
'GER': { 'overall': 0.0 },
'ARTH': { 'overall': 0.0 },
'ESE': { 'overall': 0.0 },
'LLS': { 'overall': 0.0 },
'SPAN': { 'overall': 0.0 },
'AFRO': { 'overall': 0.0 },
'SCAN': { 'overall': 0.0 },
'CWL': { 'overall': 0.0 },
'RHET': { 'overall': 0.0 },
'BIOC': { 'overall': 0.0 },
'KOR': { 'overall': 0.0 },
'ITAL': { 'overall': 0.0 },
'JAPN': { 'overall': 0.0 },
'SLAV': { 'overall': 0.0 },
'REES': { 'overall': 0.0 },
'CW': { 'overall': 0.0 }, },

'Agricultural, Consumer and Environmental Sciences': {
'overall': 0.0,
'ACE': { 'overall': 0.0 },
'FSHN': { 'overall': 0.0 },
'ANSC': { 'overall': 0.0 },
'NRES': { 'overall': 0.0 },
'CPSC': { 'overall': 0.0 },
'HDFS': { 'overall': 0.0 },
'HORT': { 'overall': 0.0 },
'TSM': { 'overall': 0.0 },
'AGED': { 'overall': 0.0 },
'AGCM': { 'overall': 0.0 } },

'Business': {
'overall': 0.0,
'BADM': { 'overall': 0.0 },
'ACCY': { 'overall': 0.0 },
'FIN': { 'overall': 0.0 } },

'Fine and Applied Arts': {
'overall': 0.0,
'MUS': { 'overall': 0.0 },
'ARCH': { 'overall': 0.0 },
'THEA': { 'overall': 0.0 },
'UP': { 'overall': 0.0 },
'ARTD': { 'overall': 0.0 },
'DANC': { 'overall': 0.0 },
'LA': { 'overall': 0.0 },
'ART': { 'overall': 0.0 },
'ARTF': { 'overall': 0.0 },
'ARTS': { 'overall': 0.0 } },

'Education': {
'overall': 0.0, 'overall': 0.0,
'EPSY': { 'overall': 0.0 },
'SPED': { 'overall': 0.0 },
'CI': { 'overall': 0.0 } },

'Media': {
'overall': 0.0,
'ADV': { 'overall': 0.0 },
'MACS': { 'overall': 0.0 },
'JOUR': { 'overall': 0.0 },
'MDIA': { 'overall': 0.0 } },

'Applied Health Sciences': {
'overall': 0.0,
'CHLH': { 'overall': 0.0 },
'KIN': { 'overall': 0.0 },
'SHS': { 'overall': 0.0 },
'RST': { 'overall': 0.0 },
'IHLT': { 'overall': 0.0 } },

'Other': {
'overall': 0.0,
'LER': { 'overall': 0.0 },
'SOCW': { 'overall': 0.0 },
'BTW': { 'overall': 0.0 },
'PLPA': { 'overall': 0.0 },
'INFO': { 'overall': 0.0 },
'AFST': { 'overall': 0.0 } }}
#College data borrowed from https://courses.engr.illinois.edu/cs19920.05/sp20.016/discovery/gpa_of_every_course_at_illinois/?a=fbcs

def findmajor(grades, major):
	for college in grades:
		if major in grades[college]:
			return grades[college][major]

def findclass(grades, major, num):
	maj = findmajor(grades, major)
	if num in maj:
		return maj[num]
	else 
		maj[num] = 'placeholder value'
		
#print grades
#For each file

filenames = []
os.chdir("grades")
for file in glob.glob("*.csv"):
    filenames.append(file)

#findmajor(grades, 'CS')
#findclass(grades, 'CS', '125')
#print x