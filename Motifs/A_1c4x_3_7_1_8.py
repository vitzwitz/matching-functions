'''
FUNC:A_1c4x_3_7_1_8
PDB:1c4x
EC:3.7.1.8
RESI:ser,asp,his
LOCI:a-110,235,263;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[8.91, 9.03], [7.46, 7.55], [7.02, 7.13], [6.59, 6.6], [5.78, 5.84], [5.39, 5.36]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.91), ('CB', 'HIS', 'OG', 'SER', 9.03)], [('CG', 'HIS', 'CB', 'SER', 7.46), ('CG', 'HIS', 'OG', 'SER', 7.55)], [('ND1', 'HIS', 'CB', 'SER', 7.02), ('ND1', 'HIS', 'OG', 'SER', 7.13)], [('CD2', 'HIS', 'CB', 'SER', 6.59), ('CD2', 'HIS', 'OG', 'SER', 6.6)], [('CE1', 'HIS', 'CB', 'SER', 5.78), ('CE1', 'HIS', 'OG', 'SER', 5.84)], [('NE2', 'HIS', 'CB', 'SER', 5.39), ('NE2', 'HIS', 'OG', 'SER', 5.36)]]}
ASP_HIS = { 
	'distances':
		[[6.75, 7.23, 6.7, 8.54, 7.83, 8.83], [5.76, 5.94, 5.29, 7.19, 6.37, 7.38], [5.33, 5.55, 5.15, 6.72, 6.22, 7.04], [5.94, 5.75, 4.77, 6.9, 5.69, 6.84]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.75), ('CB', 'ASP', 'CG', 'HIS', 7.23), ('CB', 'ASP', 'ND1', 'HIS', 6.7), ('CB', 'ASP', 'CD2', 'HIS', 8.54), ('CB', 'ASP', 'CE1', 'HIS', 7.83), ('CB', 'ASP', 'NE2', 'HIS', 8.83)], [('CG', 'ASP', 'CB', 'HIS', 5.76), ('CG', 'ASP', 'CG', 'HIS', 5.94), ('CG', 'ASP', 'ND1', 'HIS', 5.29), ('CG', 'ASP', 'CD2', 'HIS', 7.19), ('CG', 'ASP', 'CE1', 'HIS', 6.37), ('CG', 'ASP', 'NE2', 'HIS', 7.38)], [('OD1', 'ASP', 'CB', 'HIS', 5.33), ('OD1', 'ASP', 'CG', 'HIS', 5.55), ('OD1', 'ASP', 'ND1', 'HIS', 5.15), ('OD1', 'ASP', 'CD2', 'HIS', 6.72), ('OD1', 'ASP', 'CE1', 'HIS', 6.22), ('OD1', 'ASP', 'NE2', 'HIS', 7.04)], [('OD2', 'ASP', 'CB', 'HIS', 5.94), ('OD2', 'ASP', 'CG', 'HIS', 5.75), ('OD2', 'ASP', 'ND1', 'HIS', 4.77), ('OD2', 'ASP', 'CD2', 'HIS', 6.9), ('OD2', 'ASP', 'CE1', 'HIS', 5.69), ('OD2', 'ASP', 'NE2', 'HIS', 6.84)]]}
ASP_SER = { 
	'distances':
		[[11.45, 11.57], [10.05, 10.09], [9.98, 9.84], [9.16, 9.33]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.45), ('CB', 'ASP', 'OG', 'SER', 11.57)], [('CG', 'ASP', 'CB', 'SER', 10.05), ('CG', 'ASP', 'OG', 'SER', 10.09)], [('OD1', 'ASP', 'CB', 'SER', 9.98), ('OD1', 'ASP', 'OG', 'SER', 9.84)], [('OD2', 'ASP', 'CB', 'SER', 9.16), ('OD2', 'ASP', 'OG', 'SER', 9.33)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'A_1c4x_3_7_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1c4x_3_7_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SER, d, 'A_1c4x_3_7_1_8')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'ASP_HIS' :  match2,
		'ASP_SER' :  match3}