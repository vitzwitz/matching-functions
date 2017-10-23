'''
FUNC:M_1it4_3_1_1_4
PDB:1it4
EC:3.1.1.4
RESI:his,asp,ca
LOCI:a-64,85,200;
'''
import motifFunctions as cmd
ASP_CA = { 
	'distances':
		[[14.09], [13.35], [12.16], [14.07]],
	'comparisons':
		[[('CB', 'ASP', 'CA', 'CA', 14.09)], [('CG', 'ASP', 'CA', 'CA', 13.35)], [('OD1', 'ASP', 'CA', 'CA', 12.16)], [('OD2', 'ASP', 'CA', 'CA', 14.07)]]}
HIS_CA = { 
	'distances':
		[[8.31], [8.44], [7.53], [9.72], [8.56], [9.82]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 8.31)], [('CG', 'HIS', 'CA', 'CA', 8.44)], [('ND1', 'HIS', 'CA', 'CA', 7.53)], [('CD2', 'HIS', 'CA', 'CA', 9.72)], [('CE1', 'HIS', 'CA', 'CA', 8.56)], [('NE2', 'HIS', 'CA', 'CA', 9.82)]]}
HIS_ASP = { 
	'distances':
		[[9.51, 9.38, 8.32, 10.5], [8.33, 8.02, 6.91, 9.09], [8.7, 8.11, 6.92, 9.03], [7.0, 6.78, 5.74, 7.91], [7.6, 6.86, 5.65, 7.71], [6.4, 5.84, 4.68, 6.85]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.51), ('CB', 'HIS', 'CG', 'ASP', 9.38), ('CB', 'HIS', 'OD1', 'ASP', 8.32), ('CB', 'HIS', 'OD2', 'ASP', 10.5)], [('CG', 'HIS', 'CB', 'ASP', 8.33), ('CG', 'HIS', 'CG', 'ASP', 8.02), ('CG', 'HIS', 'OD1', 'ASP', 6.91), ('CG', 'HIS', 'OD2', 'ASP', 9.09)], [('ND1', 'HIS', 'CB', 'ASP', 8.7), ('ND1', 'HIS', 'CG', 'ASP', 8.11), ('ND1', 'HIS', 'OD1', 'ASP', 6.92), ('ND1', 'HIS', 'OD2', 'ASP', 9.03)], [('CD2', 'HIS', 'CB', 'ASP', 7.0), ('CD2', 'HIS', 'CG', 'ASP', 6.78), ('CD2', 'HIS', 'OD1', 'ASP', 5.74), ('CD2', 'HIS', 'OD2', 'ASP', 7.91)], [('CE1', 'HIS', 'CB', 'ASP', 7.6), ('CE1', 'HIS', 'CG', 'ASP', 6.86), ('CE1', 'HIS', 'OD1', 'ASP', 5.65), ('CE1', 'HIS', 'OD2', 'ASP', 7.71)], [('NE2', 'HIS', 'CB', 'ASP', 6.4), ('NE2', 'HIS', 'CG', 'ASP', 5.84), ('NE2', 'HIS', 'OD1', 'ASP', 4.68), ('NE2', 'HIS', 'OD2', 'ASP', 6.85)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_CA, d, 'M_1it4_3_1_1_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_CA, d, 'M_1it4_3_1_1_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'M_1it4_3_1_1_4')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_CA' :  match1,
		'HIS_CA' :  match2,
		'HIS_ASP' :  match3}