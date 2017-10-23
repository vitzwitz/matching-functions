'''
FUNC:A_1wd8_3_5_3_15
PDB:1wd8
EC:3.5.3.15
RESI:asp,his,asp,cys
LOCI:a-350,471,473,645;
'''
import motifFunctions as cmd
ASP_CYS = { 
	'distances':
		[[12.28, 10.76], [12.0, 10.35], [11.68, 10.04], [12.31, 10.58], [8.99, 8.9], [8.01, 8.28], [8.31, 8.74], [7.24, 7.71]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYS', 12.28), ('CB', 'ASP', 'SG', 'CYS', 10.76)], [('CG', 'ASP', 'CB', 'CYS', 12.0), ('CG', 'ASP', 'SG', 'CYS', 10.35)], [('OD1', 'ASP', 'CB', 'CYS', 11.68), ('OD1', 'ASP', 'SG', 'CYS', 10.04)], [('OD2', 'ASP', 'CB', 'CYS', 12.31), ('OD2', 'ASP', 'SG', 'CYS', 10.58)], [('CB', 'ASP', 'CB', 'CYS', 8.99), ('CB', 'ASP', 'SG', 'CYS', 8.9)], [('CG', 'ASP', 'CB', 'CYS', 8.01), ('CG', 'ASP', 'SG', 'CYS', 8.28)], [('OD1', 'ASP', 'CB', 'CYS', 8.31), ('OD1', 'ASP', 'SG', 'CYS', 8.74)], [('OD2', 'ASP', 'CB', 'CYS', 7.24), ('OD2', 'ASP', 'SG', 'CYS', 7.71)]]}
HIS_CYS = { 
	'distances':
		[[13.55, 12.59], [13.19, 12.43], [11.96, 11.29], [14.07, 13.45], [12.2, 11.74], [13.49, 13.04]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 13.55), ('CB', 'HIS', 'SG', 'CYS', 12.59)], [('CG', 'HIS', 'CB', 'CYS', 13.19), ('CG', 'HIS', 'SG', 'CYS', 12.43)], [('ND1', 'HIS', 'CB', 'CYS', 11.96), ('ND1', 'HIS', 'SG', 'CYS', 11.29)], [('CD2', 'HIS', 'CB', 'CYS', 14.07), ('CD2', 'HIS', 'SG', 'CYS', 13.45)], [('CE1', 'HIS', 'CB', 'CYS', 12.2), ('CE1', 'HIS', 'SG', 'CYS', 11.74)], [('NE2', 'HIS', 'CB', 'CYS', 13.49), ('NE2', 'HIS', 'SG', 'CYS', 13.04)]]}
CYS_ASPI = { 
	'distances':
		[[8.99, 8.01, 8.31, 7.24], [8.9, 8.28, 8.74, 7.71]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASPI', 8.99), ('CB', 'CYS', 'CG', 'ASPI', 8.01), ('CB', 'CYS', 'OD1', 'ASPI', 8.31), ('CB', 'CYS', 'OD2', 'ASPI', 7.24)], [('SG', 'CYS', 'CB', 'ASPI', 8.9), ('SG', 'CYS', 'CG', 'ASPI', 8.28), ('SG', 'CYS', 'OD1', 'ASPI', 8.74), ('SG', 'CYS', 'OD2', 'ASPI', 7.71)]]}
ASP_HIS = { 
	'distances':
		[[6.58, 7.61, 7.64, 8.92, 8.93, 9.61], [8.02, 8.94, 8.81, 10.26, 10.04, 10.84], [8.45, 9.17, 8.89, 10.45, 10.02, 10.89], [8.99, 10.01, 9.91, 11.34, 11.17, 11.96], [11.51, 10.67, 9.4, 11.15, 9.15, 10.28], [11.96, 11.07, 9.72, 11.52, 9.4, 10.56], [11.63, 10.61, 9.26, 10.94, 8.77, 9.88], [12.89, 12.07, 10.71, 12.59, 10.46, 11.66]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.58), ('CB', 'ASP', 'CG', 'HIS', 7.61), ('CB', 'ASP', 'ND1', 'HIS', 7.64), ('CB', 'ASP', 'CD2', 'HIS', 8.92), ('CB', 'ASP', 'CE1', 'HIS', 8.93), ('CB', 'ASP', 'NE2', 'HIS', 9.61)], [('CG', 'ASP', 'CB', 'HIS', 8.02), ('CG', 'ASP', 'CG', 'HIS', 8.94), ('CG', 'ASP', 'ND1', 'HIS', 8.81), ('CG', 'ASP', 'CD2', 'HIS', 10.26), ('CG', 'ASP', 'CE1', 'HIS', 10.04), ('CG', 'ASP', 'NE2', 'HIS', 10.84)], [('OD1', 'ASP', 'CB', 'HIS', 8.45), ('OD1', 'ASP', 'CG', 'HIS', 9.17), ('OD1', 'ASP', 'ND1', 'HIS', 8.89), ('OD1', 'ASP', 'CD2', 'HIS', 10.45), ('OD1', 'ASP', 'CE1', 'HIS', 10.02), ('OD1', 'ASP', 'NE2', 'HIS', 10.89)], [('OD2', 'ASP', 'CB', 'HIS', 8.99), ('OD2', 'ASP', 'CG', 'HIS', 10.01), ('OD2', 'ASP', 'ND1', 'HIS', 9.91), ('OD2', 'ASP', 'CD2', 'HIS', 11.34), ('OD2', 'ASP', 'CE1', 'HIS', 11.17), ('OD2', 'ASP', 'NE2', 'HIS', 11.96)], [('CB', 'ASP', 'CB', 'HIS', 11.51), ('CB', 'ASP', 'CG', 'HIS', 10.67), ('CB', 'ASP', 'ND1', 'HIS', 9.4), ('CB', 'ASP', 'CD2', 'HIS', 11.15), ('CB', 'ASP', 'CE1', 'HIS', 9.15), ('CB', 'ASP', 'NE2', 'HIS', 10.28)], [('CG', 'ASP', 'CB', 'HIS', 11.96), ('CG', 'ASP', 'CG', 'HIS', 11.07), ('CG', 'ASP', 'ND1', 'HIS', 9.72), ('CG', 'ASP', 'CD2', 'HIS', 11.52), ('CG', 'ASP', 'CE1', 'HIS', 9.4), ('CG', 'ASP', 'NE2', 'HIS', 10.56)], [('OD1', 'ASP', 'CB', 'HIS', 11.63), ('OD1', 'ASP', 'CG', 'HIS', 10.61), ('OD1', 'ASP', 'ND1', 'HIS', 9.26), ('OD1', 'ASP', 'CD2', 'HIS', 10.94), ('OD1', 'ASP', 'CE1', 'HIS', 8.77), ('OD1', 'ASP', 'NE2', 'HIS', 9.88)], [('OD2', 'ASP', 'CB', 'HIS', 12.89), ('OD2', 'ASP', 'CG', 'HIS', 12.07), ('OD2', 'ASP', 'ND1', 'HIS', 10.71), ('OD2', 'ASP', 'CD2', 'HIS', 12.59), ('OD2', 'ASP', 'CE1', 'HIS', 10.46), ('OD2', 'ASP', 'NE2', 'HIS', 11.66)]]}
ASP_ASP = { 
	'distances':
		[[11.46, 12.07, 12.27, 12.65], [11.45, 12.11, 12.48, 12.56], [10.6, 11.38, 11.86, 11.83], [12.43, 13.02, 13.43, 13.38], [11.46, 11.45, 10.6, 12.43], [12.07, 12.11, 11.38, 13.02], [12.27, 12.48, 11.86, 13.43], [12.65, 12.56, 11.83, 13.38]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.46), ('CB', 'ASP', 'CG', 'ASP', 12.07), ('CB', 'ASP', 'OD1', 'ASP', 12.27), ('CB', 'ASP', 'OD2', 'ASP', 12.65)], [('CG', 'ASP', 'CB', 'ASP', 11.45), ('CG', 'ASP', 'CG', 'ASP', 12.11), ('CG', 'ASP', 'OD1', 'ASP', 12.48), ('CG', 'ASP', 'OD2', 'ASP', 12.56)], [('OD1', 'ASP', 'CB', 'ASP', 10.6), ('OD1', 'ASP', 'CG', 'ASP', 11.38), ('OD1', 'ASP', 'OD1', 'ASP', 11.86), ('OD1', 'ASP', 'OD2', 'ASP', 11.83)], [('OD2', 'ASP', 'CB', 'ASP', 12.43), ('OD2', 'ASP', 'CG', 'ASP', 13.02), ('OD2', 'ASP', 'OD1', 'ASP', 13.43), ('OD2', 'ASP', 'OD2', 'ASP', 13.38)], [('CB', 'ASP', 'CB', 'ASP', 11.46), ('CB', 'ASP', 'CG', 'ASP', 11.45), ('CB', 'ASP', 'OD1', 'ASP', 10.6), ('CB', 'ASP', 'OD2', 'ASP', 12.43)], [('CG', 'ASP', 'CB', 'ASP', 12.07), ('CG', 'ASP', 'CG', 'ASP', 12.11), ('CG', 'ASP', 'OD1', 'ASP', 11.38), ('CG', 'ASP', 'OD2', 'ASP', 13.02)], [('OD1', 'ASP', 'CB', 'ASP', 12.27), ('OD1', 'ASP', 'CG', 'ASP', 12.48), ('OD1', 'ASP', 'OD1', 'ASP', 11.86), ('OD1', 'ASP', 'OD2', 'ASP', 13.43)], [('OD2', 'ASP', 'CB', 'ASP', 12.65), ('OD2', 'ASP', 'CG', 'ASP', 12.56), ('OD2', 'ASP', 'OD1', 'ASP', 11.83), ('OD2', 'ASP', 'OD2', 'ASP', 13.38)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_CYS, d, 'A_1wd8_3_5_3_15')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_CYS, d, 'A_1wd8_3_5_3_15')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_ASPI, d, 'A_1wd8_3_5_3_15')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_HIS, d, 'A_1wd8_3_5_3_15')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_ASP, d, 'A_1wd8_3_5_3_15')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_CYS' :  match1,
		'HIS_CYS' :  match2,
		'CYS_ASPI' :  match3,
		'ASP_HIS' :  match4,
		'ASP_ASP' :  match5}