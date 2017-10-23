'''
FUNC:A_1tah_3_1_1_3
PDB:1tah
EC:3.1.1.3
RESI:ser,asp,his
LOCI:a-87,263,285;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[9.06, 8.35], [7.57, 6.88], [7.07, 6.49], [6.72, 5.95], [5.8, 5.22], [5.48, 4.72]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 9.06), ('CB', 'HIS', 'OG', 'SER', 8.35)], [('CG', 'HIS', 'CB', 'SER', 7.57), ('CG', 'HIS', 'OG', 'SER', 6.88)], [('ND1', 'HIS', 'CB', 'SER', 7.07), ('ND1', 'HIS', 'OG', 'SER', 6.49)], [('CD2', 'HIS', 'CB', 'SER', 6.72), ('CD2', 'HIS', 'OG', 'SER', 5.95)], [('CE1', 'HIS', 'CB', 'SER', 5.8), ('CE1', 'HIS', 'OG', 'SER', 5.22)], [('NE2', 'HIS', 'CB', 'SER', 5.48), ('NE2', 'HIS', 'OG', 'SER', 4.72)]]}
ASP_HIS = { 
	'distances':
		[[6.13, 6.86, 6.61, 8.2, 7.83, 8.66], [5.57, 5.89, 5.39, 7.16, 6.52, 7.43], [5.45, 5.71, 5.36, 6.85, 6.39, 7.16], [5.87, 5.8, 4.94, 7.0, 5.92, 7.02]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.13), ('CB', 'ASP', 'CG', 'HIS', 6.86), ('CB', 'ASP', 'ND1', 'HIS', 6.61), ('CB', 'ASP', 'CD2', 'HIS', 8.2), ('CB', 'ASP', 'CE1', 'HIS', 7.83), ('CB', 'ASP', 'NE2', 'HIS', 8.66)], [('CG', 'ASP', 'CB', 'HIS', 5.57), ('CG', 'ASP', 'CG', 'HIS', 5.89), ('CG', 'ASP', 'ND1', 'HIS', 5.39), ('CG', 'ASP', 'CD2', 'HIS', 7.16), ('CG', 'ASP', 'CE1', 'HIS', 6.52), ('CG', 'ASP', 'NE2', 'HIS', 7.43)], [('OD1', 'ASP', 'CB', 'HIS', 5.45), ('OD1', 'ASP', 'CG', 'HIS', 5.71), ('OD1', 'ASP', 'ND1', 'HIS', 5.36), ('OD1', 'ASP', 'CD2', 'HIS', 6.85), ('OD1', 'ASP', 'CE1', 'HIS', 6.39), ('OD1', 'ASP', 'NE2', 'HIS', 7.16)], [('OD2', 'ASP', 'CB', 'HIS', 5.87), ('OD2', 'ASP', 'CG', 'HIS', 5.8), ('OD2', 'ASP', 'ND1', 'HIS', 4.94), ('OD2', 'ASP', 'CD2', 'HIS', 7.0), ('OD2', 'ASP', 'CE1', 'HIS', 5.92), ('OD2', 'ASP', 'NE2', 'HIS', 7.02)]]}
ASP_SER = { 
	'distances':
		[[11.58, 11.0], [10.25, 9.63], [10.11, 9.3], [9.49, 9.04]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.58), ('CB', 'ASP', 'OG', 'SER', 11.0)], [('CG', 'ASP', 'CB', 'SER', 10.25), ('CG', 'ASP', 'OG', 'SER', 9.63)], [('OD1', 'ASP', 'CB', 'SER', 10.11), ('OD1', 'ASP', 'OG', 'SER', 9.3)], [('OD2', 'ASP', 'CB', 'SER', 9.49), ('OD2', 'ASP', 'OG', 'SER', 9.04)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'A_1tah_3_1_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1tah_3_1_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SER, d, 'A_1tah_3_1_1_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'ASP_HIS' :  match2,
		'ASP_SER' :  match3}