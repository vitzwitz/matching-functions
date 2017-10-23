'''
FUNC:P_1ak9_3_4_21_62
PDB:1ak9
EC:3.4.21.62
RESI:asp,his,ser
LOCI:a-32,64,221;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[8.64, 8.58], [7.24, 7.12], [6.85, 6.61], [6.4, 6.27], [5.67, 5.31], [5.26, 4.97]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.64), ('CB', 'HIS', 'OG', 'SER', 8.58)], [('CG', 'HIS', 'CB', 'SER', 7.24), ('CG', 'HIS', 'OG', 'SER', 7.12)], [('ND1', 'HIS', 'CB', 'SER', 6.85), ('ND1', 'HIS', 'OG', 'SER', 6.61)], [('CD2', 'HIS', 'CB', 'SER', 6.4), ('CD2', 'HIS', 'OG', 'SER', 6.27)], [('CE1', 'HIS', 'CB', 'SER', 5.67), ('CE1', 'HIS', 'OG', 'SER', 5.31)], [('NE2', 'HIS', 'CB', 'SER', 5.26), ('NE2', 'HIS', 'OG', 'SER', 4.97)]]}
ASP_HIS = { 
	'distances':
		[[8.09, 7.87, 6.78, 8.96, 7.45, 8.72], [6.82, 6.41, 5.26, 7.45, 5.93, 7.19], [5.8, 5.6, 4.69, 6.77, 5.66, 6.78], [7.15, 6.44, 5.15, 7.26, 5.46, 6.75]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.09), ('CB', 'ASP', 'CG', 'HIS', 7.87), ('CB', 'ASP', 'ND1', 'HIS', 6.78), ('CB', 'ASP', 'CD2', 'HIS', 8.96), ('CB', 'ASP', 'CE1', 'HIS', 7.45), ('CB', 'ASP', 'NE2', 'HIS', 8.72)], [('CG', 'ASP', 'CB', 'HIS', 6.82), ('CG', 'ASP', 'CG', 'HIS', 6.41), ('CG', 'ASP', 'ND1', 'HIS', 5.26), ('CG', 'ASP', 'CD2', 'HIS', 7.45), ('CG', 'ASP', 'CE1', 'HIS', 5.93), ('CG', 'ASP', 'NE2', 'HIS', 7.19)], [('OD1', 'ASP', 'CB', 'HIS', 5.8), ('OD1', 'ASP', 'CG', 'HIS', 5.6), ('OD1', 'ASP', 'ND1', 'HIS', 4.69), ('OD1', 'ASP', 'CD2', 'HIS', 6.77), ('OD1', 'ASP', 'CE1', 'HIS', 5.66), ('OD1', 'ASP', 'NE2', 'HIS', 6.78)], [('OD2', 'ASP', 'CB', 'HIS', 7.15), ('OD2', 'ASP', 'CG', 'HIS', 6.44), ('OD2', 'ASP', 'ND1', 'HIS', 5.15), ('OD2', 'ASP', 'CD2', 'HIS', 7.26), ('OD2', 'ASP', 'CE1', 'HIS', 5.46), ('OD2', 'ASP', 'NE2', 'HIS', 6.75)]]}
ASP_SER = { 
	'distances':
		[[10.38, 10.11], [8.99, 8.73], [9.11, 8.79], [8.05, 7.87]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 10.38), ('CB', 'ASP', 'OG', 'SER', 10.11)], [('CG', 'ASP', 'CB', 'SER', 8.99), ('CG', 'ASP', 'OG', 'SER', 8.73)], [('OD1', 'ASP', 'CB', 'SER', 9.11), ('OD1', 'ASP', 'OG', 'SER', 8.79)], [('OD2', 'ASP', 'CB', 'SER', 8.05), ('OD2', 'ASP', 'OG', 'SER', 7.87)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'P_1ak9_3_4_21_62')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'P_1ak9_3_4_21_62')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SER, d, 'P_1ak9_3_4_21_62')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'ASP_HIS' :  match2,
		'ASP_SER' :  match3}