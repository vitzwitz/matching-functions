'''
FUNC:A_1sca_3_4_21_62
PDB:1sca
EC:3.4.21.62
RESI:asp,his,ser
LOCI:a-32,64,221;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[8.74, 8.49], [7.3, 7.0], [7.01, 6.57], [6.38, 6.1], [5.82, 5.27], [5.29, 4.82]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.74), ('CB', 'HIS', 'OG', 'SER', 8.49)], [('CG', 'HIS', 'CB', 'SER', 7.3), ('CG', 'HIS', 'OG', 'SER', 7.0)], [('ND1', 'HIS', 'CB', 'SER', 7.01), ('ND1', 'HIS', 'OG', 'SER', 6.57)], [('CD2', 'HIS', 'CB', 'SER', 6.38), ('CD2', 'HIS', 'OG', 'SER', 6.1)], [('CE1', 'HIS', 'CB', 'SER', 5.82), ('CE1', 'HIS', 'OG', 'SER', 5.27)], [('NE2', 'HIS', 'CB', 'SER', 5.29), ('NE2', 'HIS', 'OG', 'SER', 4.82)]]}
ASP_HIS = { 
	'distances':
		[[8.16, 7.91, 6.76, 8.96, 7.33, 8.63], [6.99, 6.53, 5.3, 7.5, 5.82, 7.12], [5.88, 5.63, 4.6, 6.77, 5.49, 6.66], [7.33, 6.56, 5.25, 7.29, 5.37, 6.67]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.16), ('CB', 'ASP', 'CG', 'HIS', 7.91), ('CB', 'ASP', 'ND1', 'HIS', 6.76), ('CB', 'ASP', 'CD2', 'HIS', 8.96), ('CB', 'ASP', 'CE1', 'HIS', 7.33), ('CB', 'ASP', 'NE2', 'HIS', 8.63)], [('CG', 'ASP', 'CB', 'HIS', 6.99), ('CG', 'ASP', 'CG', 'HIS', 6.53), ('CG', 'ASP', 'ND1', 'HIS', 5.3), ('CG', 'ASP', 'CD2', 'HIS', 7.5), ('CG', 'ASP', 'CE1', 'HIS', 5.82), ('CG', 'ASP', 'NE2', 'HIS', 7.12)], [('OD1', 'ASP', 'CB', 'HIS', 5.88), ('OD1', 'ASP', 'CG', 'HIS', 5.63), ('OD1', 'ASP', 'ND1', 'HIS', 4.6), ('OD1', 'ASP', 'CD2', 'HIS', 6.77), ('OD1', 'ASP', 'CE1', 'HIS', 5.49), ('OD1', 'ASP', 'NE2', 'HIS', 6.66)], [('OD2', 'ASP', 'CB', 'HIS', 7.33), ('OD2', 'ASP', 'CG', 'HIS', 6.56), ('OD2', 'ASP', 'ND1', 'HIS', 5.25), ('OD2', 'ASP', 'CD2', 'HIS', 7.29), ('OD2', 'ASP', 'CE1', 'HIS', 5.37), ('OD2', 'ASP', 'NE2', 'HIS', 6.67)]]}
ASP_SER = { 
	'distances':
		[[10.41, 9.99], [8.99, 8.57], [9.08, 8.59], [8.03, 7.7]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 10.41), ('CB', 'ASP', 'OG', 'SER', 9.99)], [('CG', 'ASP', 'CB', 'SER', 8.99), ('CG', 'ASP', 'OG', 'SER', 8.57)], [('OD1', 'ASP', 'CB', 'SER', 9.08), ('OD1', 'ASP', 'OG', 'SER', 8.59)], [('OD2', 'ASP', 'CB', 'SER', 8.03), ('OD2', 'ASP', 'OG', 'SER', 7.7)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'A_1sca_3_4_21_62')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1sca_3_4_21_62')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SER, d, 'A_1sca_3_4_21_62')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'ASP_HIS' :  match2,
		'ASP_SER' :  match3}