'''
FUNC:M_1n29_3_1_1_4
PDB:1n29
EC:3.1.1.4
RESI:gly,his,asp,ca
LOCI:a-29,47,91,125;
'''
import motifFunctions as cmd
HIS_GLY = { 
	'distances':
		[[9.89, 10.59, 10.6, 9.61], [9.8, 10.35, 10.34, 9.53], [8.81, 9.3, 9.38, 8.75], [10.93, 11.37, 11.26, 10.52], [9.48, 9.79, 9.81, 9.34], [10.71, 11.01, 10.92, 10.37]],
	'comparisons':
		[[('CB', 'HIS', 'O', 'GLY', 9.89), ('CB', 'HIS', 'C', 'GLY', 10.59), ('CB', 'HIS', 'CA', 'GLY', 10.6), ('CB', 'HIS', 'N', 'GLY', 9.61)], [('CG', 'HIS', 'O', 'GLY', 9.8), ('CG', 'HIS', 'C', 'GLY', 10.35), ('CG', 'HIS', 'CA', 'GLY', 10.34), ('CG', 'HIS', 'N', 'GLY', 9.53)], [('ND1', 'HIS', 'O', 'GLY', 8.81), ('ND1', 'HIS', 'C', 'GLY', 9.3), ('ND1', 'HIS', 'CA', 'GLY', 9.38), ('ND1', 'HIS', 'N', 'GLY', 8.75)], [('CD2', 'HIS', 'O', 'GLY', 10.93), ('CD2', 'HIS', 'C', 'GLY', 11.37), ('CD2', 'HIS', 'CA', 'GLY', 11.26), ('CD2', 'HIS', 'N', 'GLY', 10.52)], [('CE1', 'HIS', 'O', 'GLY', 9.48), ('CE1', 'HIS', 'C', 'GLY', 9.79), ('CE1', 'HIS', 'CA', 'GLY', 9.81), ('CE1', 'HIS', 'N', 'GLY', 9.34)], [('NE2', 'HIS', 'O', 'GLY', 10.71), ('NE2', 'HIS', 'C', 'GLY', 11.01), ('NE2', 'HIS', 'CA', 'GLY', 10.92), ('NE2', 'HIS', 'N', 'GLY', 10.37)]]}
HIS_ASP = { 
	'distances':
		[[9.67, 9.47, 8.42, 10.55], [8.37, 8.03, 6.95, 9.06], [8.55, 7.92, 6.77, 8.79], [7.03, 6.84, 5.85, 7.96], [7.44, 6.67, 5.53, 7.48], [6.36, 5.84, 4.76, 6.85]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.67), ('CB', 'HIS', 'CG', 'ASP', 9.47), ('CB', 'HIS', 'OD1', 'ASP', 8.42), ('CB', 'HIS', 'OD2', 'ASP', 10.55)], [('CG', 'HIS', 'CB', 'ASP', 8.37), ('CG', 'HIS', 'CG', 'ASP', 8.03), ('CG', 'HIS', 'OD1', 'ASP', 6.95), ('CG', 'HIS', 'OD2', 'ASP', 9.06)], [('ND1', 'HIS', 'CB', 'ASP', 8.55), ('ND1', 'HIS', 'CG', 'ASP', 7.92), ('ND1', 'HIS', 'OD1', 'ASP', 6.77), ('ND1', 'HIS', 'OD2', 'ASP', 8.79)], [('CD2', 'HIS', 'CB', 'ASP', 7.03), ('CD2', 'HIS', 'CG', 'ASP', 6.84), ('CD2', 'HIS', 'OD1', 'ASP', 5.85), ('CD2', 'HIS', 'OD2', 'ASP', 7.96)], [('CE1', 'HIS', 'CB', 'ASP', 7.44), ('CE1', 'HIS', 'CG', 'ASP', 6.67), ('CE1', 'HIS', 'OD1', 'ASP', 5.53), ('CE1', 'HIS', 'OD2', 'ASP', 7.48)], [('NE2', 'HIS', 'CB', 'ASP', 6.36), ('NE2', 'HIS', 'CG', 'ASP', 5.84), ('NE2', 'HIS', 'OD1', 'ASP', 4.76), ('NE2', 'HIS', 'OD2', 'ASP', 6.85)]]}
GLY_CA = { 
	'distances':
		[[4.24], [5.46], [6.41], [6.04]],
	'comparisons':
		[[('O', 'GLY', 'CA', 'CA', 4.24)], [('C', 'GLY', 'CA', 'CA', 5.46)], [('CA', 'GLY', 'CA', 'CA', 6.41)], [('N', 'GLY', 'CA', 'CA', 6.04)]]}
ASP_CA = { 
	'distances':
		[[14.6], [13.78], [12.67], [14.36]],
	'comparisons':
		[[('CB', 'ASP', 'CA', 'CA', 14.6)], [('CG', 'ASP', 'CA', 'CA', 13.78)], [('OD1', 'ASP', 'CA', 'CA', 12.67)], [('OD2', 'ASP', 'CA', 'CA', 14.36)]]}
ASP_GLY = { 
	'distances':
		[[14.52, 14.56, 14.23, 13.83], [13.63, 13.65, 13.44, 13.17], [12.66, 12.76, 12.65, 12.35], [14.05, 13.97, 13.78, 13.65]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 14.52), ('CB', 'ASP', 'C', 'GLY', 14.56), ('CB', 'ASP', 'CA', 'GLY', 14.23), ('CB', 'ASP', 'N', 'GLY', 13.83)], [('CG', 'ASP', 'O', 'GLY', 13.63), ('CG', 'ASP', 'C', 'GLY', 13.65), ('CG', 'ASP', 'CA', 'GLY', 13.44), ('CG', 'ASP', 'N', 'GLY', 13.17)], [('OD1', 'ASP', 'O', 'GLY', 12.66), ('OD1', 'ASP', 'C', 'GLY', 12.76), ('OD1', 'ASP', 'CA', 'GLY', 12.65), ('OD1', 'ASP', 'N', 'GLY', 12.35)], [('OD2', 'ASP', 'O', 'GLY', 14.05), ('OD2', 'ASP', 'C', 'GLY', 13.97), ('OD2', 'ASP', 'CA', 'GLY', 13.78), ('OD2', 'ASP', 'N', 'GLY', 13.65)]]}
HIS_CA = { 
	'distances':
		[[8.83], [9.08], [8.28], [10.38], [9.24], [10.42]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 8.83)], [('CG', 'HIS', 'CA', 'CA', 9.08)], [('ND1', 'HIS', 'CA', 'CA', 8.28)], [('CD2', 'HIS', 'CA', 'CA', 10.38)], [('CE1', 'HIS', 'CA', 'CA', 9.24)], [('NE2', 'HIS', 'CA', 'CA', 10.42)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_GLY, d, 'M_1n29_3_1_1_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'M_1n29_3_1_1_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_CA, d, 'M_1n29_3_1_1_4')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_CA, d, 'M_1n29_3_1_1_4')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_GLY, d, 'M_1n29_3_1_1_4')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_CA, d, 'M_1n29_3_1_1_4')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_GLY' :  match1,
		'HIS_ASP' :  match2,
		'GLY_CA' :  match3,
		'ASP_CA' :  match4,
		'ASP_GLY' :  match5,
		'HIS_CA' :  match6}