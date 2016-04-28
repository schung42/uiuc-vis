import csv, os, glob

grades = {

'Engineering': {

'CS': { 'overall': 0.0 },
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

'BADM': { 'overall': 0.0 },
'ACCY': { 'overall': 0.0 },
'FIN': { 'overall': 0.0 } },

'Fine and Applied Arts': {

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

'EPSY': { 'overall': 0.0 },
'SPED': { 'overall': 0.0 },
'CI': { 'overall': 0.0 } },

'Media': {

'ADV': { 'overall': 0.0 },
'MACS': { 'overall': 0.0 },
'JOUR': { 'overall': 0.0 },
'MDIA': { 'overall': 0.0 } },

'Applied Health Sciences': {

'CHLH': { 'overall': 0.0 },
'KIN': { 'overall': 0.0 },
'SHS': { 'overall': 0.0 },
'RST': { 'overall': 0.0 },
'IHLT': { 'overall': 0.0 } },

'Other': {

'LER': { 'overall': 0.0 },
'SOCW': { 'overall': 0.0 },
'BTW': { 'overall': 0.0 },
'PLPA': { 'overall': 0.0 },
'INFO': { 'overall': 0.0 },
'AFST': { 'overall': 0.0 } }}
#College data borrowed from https://courses.engr.illinois.edu/cs19920.05/sp20.016/discovery/gpa_of_every_course_at_illinois/?a=fbcs

def findmajor(grades, major):
	for college in list(grades):
		if major in college:
			return college[program]

def findclass(grades, num):
	for college in list(grades):
		for major in list(college):
			if num in major:
				return major[num]
				
#print grades
#For each file

filenames = []
os.chdir("grades")
for file in glob.glob("*.csv"):
    filenames.append(file)

x = findmajor(grades, 'CS')
print x