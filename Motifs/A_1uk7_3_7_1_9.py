'''
FUNC:A_1uk7_3_7_1_9
PDB:1uk7
EC:3.7.1.9
RESI:ala,asp,his
LOCI:a-103,224,252;
'''
import motifFunctions as cmd
HIS_ALA = { 
	'distances':
		[[8.88], [7.44], [6.91], [6.72], [5.73], [5.54]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ALA', 8.88)], [('CG', 'HIS', 'CB', 'ALA', 7.44)], [('ND1', 'HIS', 'CB', 'ALA', 6.91)], [('CD2', 'HIS', 'CB', 'ALA', 6.72)], [('CE1', 'HIS', 'CB', 'ALA', 5.73)], [('NE2', 'HIS', 'CB', 'ALA', 5.54)]]}
HIS_ASP = { 
	'distances':
		[[6.91, 5.81, 5.47, 5.79], [7.26, 5.88, 5.51, 5.59], [6.68, 5.21, 5.1, 4.62], [8.49, 7.05, 6.53, 6.73], [7.7, 6.2, 5.99, 5.55], [8.69, 7.18, 6.75, 6.68]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.91), ('CB', 'HIS', 'CG', 'ASP', 5.81), ('CB', 'HIS', 'OD1', 'ASP', 5.47), ('CB', 'HIS', 'OD2', 'ASP', 5.79)], [('CG', 'HIS', 'CB', 'ASP', 7.26), ('CG', 'HIS', 'CG', 'ASP', 5.88), ('CG', 'HIS', 'OD1', 'ASP', 5.51), ('CG', 'HIS', 'OD2', 'ASP', 5.59)], [('ND1', 'HIS', 'CB', 'ASP', 6.68), ('ND1', 'HIS', 'CG', 'ASP', 5.21), ('ND1', 'HIS', 'OD1', 'ASP', 5.1), ('ND1', 'HIS', 'OD2', 'ASP', 4.62)], [('CD2', 'HIS', 'CB', 'ASP', 8.49), ('CD2', 'HIS', 'CG', 'ASP', 7.05), ('CD2', 'HIS', 'OD1', 'ASP', 6.53), ('CD2', 'HIS', 'OD2', 'ASP', 6.73)], [('CE1', 'HIS', 'CB', 'ASP', 7.7), ('CE1', 'HIS', 'CG', 'ASP', 6.2), ('CE1', 'HIS', 'OD1', 'ASP', 5.99), ('CE1', 'HIS', 'OD2', 'ASP', 5.55)], [('NE2', 'HIS', 'CB', 'ASP', 8.69), ('NE2', 'HIS', 'CG', 'ASP', 7.18), ('NE2', 'HIS', 'OD1', 'ASP', 6.75), ('NE2', 'HIS', 'OD2', 'ASP', 6.68)]]}
ASP_ALA = { 
	'distances':
		[[11.19], [9.76], [9.68], [8.87]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ALA', 11.19)], [('CG', 'ASP', 'CB', 'ALA', 9.76)], [('OD1', 'ASP', 'CB', 'ALA', 9.68)], [('OD2', 'ASP', 'CB', 'ALA', 8.87)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ALA, d, 'A_1uk7_3_7_1_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1uk7_3_7_1_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ALA, d, 'A_1uk7_3_7_1_9')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ALA' :  match1,
		'HIS_ASP' :  match2,
		'ASP_ALA' :  match3}