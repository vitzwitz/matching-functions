'''
FUNC:M_2qf7_6_4_1_1
PDB:2qf7
EC:6.4.1.1
RESI:asp,asp,zn,mg,mg
LOCI:a-549,655,1157;b-1156,1157;
'''
import motifFunctions as cmd
ASP_ZN = { 
	'distances':
		[[16.58], [17.53], [17.9], [17.92], [6.48], [5.15], [5.42], [4.21]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZN', 16.58)], [('CG', 'ASP', 'ZN', 'ZN', 17.53)], [('OD1', 'ASP', 'ZN', 'ZN', 17.9)], [('OD2', 'ASP', 'ZN', 'ZN', 17.92)], [('CB', 'ASP', 'ZN', 'ZN', 6.48)], [('CG', 'ASP', 'ZN', 'ZN', 5.15)], [('OD1', 'ASP', 'ZN', 'ZN', 5.42)], [('OD2', 'ASP', 'ZN', 'ZN', 4.21)]]}
ZN_ASPI = { 
	'distances':
		[6.48, 5.15, 5.42, 4.21],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'ASPI', 6.48), ('ZN', 'ZN', 'CG', 'ASPI', 5.15), ('ZN', 'ZN', 'OD1', 'ASPI', 5.42), ('ZN', 'ZN', 'OD2', 'ASPI', 4.21)]}
ASP_ASP = { 
	'distances':
		[[19.8, 18.78, 18.5, 18.36], [20.79, 19.71, 19.35, 19.33], [20.97, 19.92, 19.5, 19.62], [21.36, 20.23, 19.85, 19.8], [19.8, 20.79, 20.97, 21.36], [18.78, 19.71, 19.92, 20.23], [18.5, 19.35, 19.5, 19.85], [18.36, 19.33, 19.62, 19.8]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 19.8), ('CB', 'ASP', 'CG', 'ASP', 18.78), ('CB', 'ASP', 'OD1', 'ASP', 18.5), ('CB', 'ASP', 'OD2', 'ASP', 18.36)], [('CG', 'ASP', 'CB', 'ASP', 20.79), ('CG', 'ASP', 'CG', 'ASP', 19.71), ('CG', 'ASP', 'OD1', 'ASP', 19.35), ('CG', 'ASP', 'OD2', 'ASP', 19.33)], [('OD1', 'ASP', 'CB', 'ASP', 20.97), ('OD1', 'ASP', 'CG', 'ASP', 19.92), ('OD1', 'ASP', 'OD1', 'ASP', 19.5), ('OD1', 'ASP', 'OD2', 'ASP', 19.62)], [('OD2', 'ASP', 'CB', 'ASP', 21.36), ('OD2', 'ASP', 'CG', 'ASP', 20.23), ('OD2', 'ASP', 'OD1', 'ASP', 19.85), ('OD2', 'ASP', 'OD2', 'ASP', 19.8)], [('CB', 'ASP', 'CB', 'ASP', 19.8), ('CB', 'ASP', 'CG', 'ASP', 20.79), ('CB', 'ASP', 'OD1', 'ASP', 20.97), ('CB', 'ASP', 'OD2', 'ASP', 21.36)], [('CG', 'ASP', 'CB', 'ASP', 18.78), ('CG', 'ASP', 'CG', 'ASP', 19.71), ('CG', 'ASP', 'OD1', 'ASP', 19.92), ('CG', 'ASP', 'OD2', 'ASP', 20.23)], [('OD1', 'ASP', 'CB', 'ASP', 18.5), ('OD1', 'ASP', 'CG', 'ASP', 19.35), ('OD1', 'ASP', 'OD1', 'ASP', 19.5), ('OD1', 'ASP', 'OD2', 'ASP', 19.85)], [('OD2', 'ASP', 'CB', 'ASP', 18.36), ('OD2', 'ASP', 'CG', 'ASP', 19.33), ('OD2', 'ASP', 'OD1', 'ASP', 19.62), ('OD2', 'ASP', 'OD2', 'ASP', 19.8)]]}
MG_MG = { 
	'distances':
		[5.85, 5.85],
	'comparisons':
		[('MG', 'MG', 'MG', 'MG', 5.85), ('MG', 'MG', 'MG', 'MG', 5.85)]}
ASP_MG = { 
	'distances':
		[[82.29], [83.37], [83.09], [84.45], [79.53], [80.64], [80.4], [81.7], [68.44], [69.97], [70.45], [70.69], [65.48], [67.02], [67.54], [67.71]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 82.29)], [('CG', 'ASP', 'MG', 'MG', 83.37)], [('OD1', 'ASP', 'MG', 'MG', 83.09)], [('OD2', 'ASP', 'MG', 'MG', 84.45)], [('CB', 'ASP', 'MG', 'MG', 79.53)], [('CG', 'ASP', 'MG', 'MG', 80.64)], [('OD1', 'ASP', 'MG', 'MG', 80.4)], [('OD2', 'ASP', 'MG', 'MG', 81.7)], [('CB', 'ASP', 'MG', 'MG', 68.44)], [('CG', 'ASP', 'MG', 'MG', 69.97)], [('OD1', 'ASP', 'MG', 'MG', 70.45)], [('OD2', 'ASP', 'MG', 'MG', 70.69)], [('CB', 'ASP', 'MG', 'MG', 65.48)], [('CG', 'ASP', 'MG', 'MG', 67.02)], [('OD1', 'ASP', 'MG', 'MG', 67.54)], [('OD2', 'ASP', 'MG', 'MG', 67.71)]]}
MG_ASPI = { 
	'distances':
		[68.44, 69.97, 70.45, 70.69, 65.48, 67.02, 67.54, 67.71],
	'comparisons':
		[('MG', 'MG', 'CB', 'ASPI', 68.44), ('MG', 'MG', 'CG', 'ASPI', 69.97), ('MG', 'MG', 'OD1', 'ASPI', 70.45), ('MG', 'MG', 'OD2', 'ASPI', 70.69), ('MG', 'MG', 'CB', 'ASPI', 65.48), ('MG', 'MG', 'CG', 'ASPI', 67.02), ('MG', 'MG', 'OD1', 'ASPI', 67.54), ('MG', 'MG', 'OD2', 'ASPI', 67.71)]}
ZN_MG = { 
	'distances':
		[72.8, 69.81],
	'comparisons':
		[('ZN', 'ZN', 'MG', 'MG', 72.8), ('ZN', 'ZN', 'MG', 'MG', 69.81)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ZN, d, 'M_2qf7_6_4_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ZN_ASPI, d, 'M_2qf7_6_4_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASP, d, 'M_2qf7_6_4_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(MG_MG, d, 'M_2qf7_6_4_1_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_MG, d, 'M_2qf7_6_4_1_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(MG_ASPI, d, 'M_2qf7_6_4_1_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ZN_MG, d, 'M_2qf7_6_4_1_1')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ZN' :  match1,
		'ZN_ASPI' :  match2,
		'ASP_ASP' :  match3,
		'MG_MG' :  match4,
		'ASP_MG' :  match5,
		'MG_ASPI' :  match6,
		'ZN_MG' :  match7}