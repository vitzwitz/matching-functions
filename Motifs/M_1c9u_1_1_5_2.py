'''
FUNC:M_1c9u_1_1_5_2
PDB:1c9u
EC:1.1.5.2
RESI:his,asp,ca
LOCI:a-144,163,1003;
'''
import motifFunctions as cmd
ASP_CA = { 
	'distances':
		[[14.01], [12.6], [11.97], [12.25]],
	'comparisons':
		[[('CB', 'ASP', 'CA', 'CA', 14.01)], [('CG', 'ASP', 'CA', 'CA', 12.6)], [('OD1', 'ASP', 'CA', 'CA', 11.97)], [('OD2', 'ASP', 'CA', 'CA', 12.25)]]}
HIS_CA = { 
	'distances':
		[[11.25], [9.97], [9.72], [9.06], [8.67], [8.18]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 11.25)], [('CG', 'HIS', 'CA', 'CA', 9.97)], [('ND1', 'HIS', 'CA', 'CA', 9.72)], [('CD2', 'HIS', 'CA', 'CA', 9.06)], [('CE1', 'HIS', 'CA', 'CA', 8.67)], [('NE2', 'HIS', 'CA', 'CA', 8.18)]]}
HIS_ASP = { 
	'distances':
		[[7.58, 6.8, 5.56, 7.65], [8.08, 6.97, 5.76, 7.54], [7.49, 6.19, 5.1, 6.52], [9.36, 8.18, 7.01, 8.61], [8.55, 7.14, 6.2, 7.2], [9.59, 8.25, 7.21, 8.42]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.58), ('CB', 'HIS', 'CG', 'ASP', 6.8), ('CB', 'HIS', 'OD1', 'ASP', 5.56), ('CB', 'HIS', 'OD2', 'ASP', 7.65)], [('CG', 'HIS', 'CB', 'ASP', 8.08), ('CG', 'HIS', 'CG', 'ASP', 6.97), ('CG', 'HIS', 'OD1', 'ASP', 5.76), ('CG', 'HIS', 'OD2', 'ASP', 7.54)], [('ND1', 'HIS', 'CB', 'ASP', 7.49), ('ND1', 'HIS', 'CG', 'ASP', 6.19), ('ND1', 'HIS', 'OD1', 'ASP', 5.1), ('ND1', 'HIS', 'OD2', 'ASP', 6.52)], [('CD2', 'HIS', 'CB', 'ASP', 9.36), ('CD2', 'HIS', 'CG', 'ASP', 8.18), ('CD2', 'HIS', 'OD1', 'ASP', 7.01), ('CD2', 'HIS', 'OD2', 'ASP', 8.61)], [('CE1', 'HIS', 'CB', 'ASP', 8.55), ('CE1', 'HIS', 'CG', 'ASP', 7.14), ('CE1', 'HIS', 'OD1', 'ASP', 6.2), ('CE1', 'HIS', 'OD2', 'ASP', 7.2)], [('NE2', 'HIS', 'CB', 'ASP', 9.59), ('NE2', 'HIS', 'CG', 'ASP', 8.25), ('NE2', 'HIS', 'OD1', 'ASP', 7.21), ('NE2', 'HIS', 'OD2', 'ASP', 8.42)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_CA, d, 'M_1c9u_1_1_5_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_CA, d, 'M_1c9u_1_1_5_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'M_1c9u_1_1_5_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_CA' :  match1,
		'HIS_CA' :  match2,
		'HIS_ASP' :  match3}