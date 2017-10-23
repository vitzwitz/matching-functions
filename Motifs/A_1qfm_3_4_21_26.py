'''
FUNC:A_1qfm_3_4_21_26
PDB:1qfm
EC:3.4.21.26
RESI:ser,asp,his
LOCI:a-554,641,680;
'''
import motifFunctions as cmd
ASP_SER = { 
	'distances':
		[[11.35, 10.95], [9.9, 9.45], [9.83, 9.19], [8.99, 8.7]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.35), ('CB', 'ASP', 'OG', 'SER', 10.95)], [('CG', 'ASP', 'CB', 'SER', 9.9), ('CG', 'ASP', 'OG', 'SER', 9.45)], [('OD1', 'ASP', 'CB', 'SER', 9.83), ('OD1', 'ASP', 'OG', 'SER', 9.19)], [('OD2', 'ASP', 'CB', 'SER', 8.99), ('OD2', 'ASP', 'OG', 'SER', 8.7)]]}
HIS_ASP = { 
	'distances':
		[[6.77, 5.72, 5.3, 5.83], [7.29, 5.95, 5.56, 5.7], [6.8, 5.33, 5.17, 4.78], [8.61, 7.22, 6.74, 6.88], [7.93, 6.43, 6.24, 5.74], [8.91, 7.43, 7.06, 6.87]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.77), ('CB', 'HIS', 'CG', 'ASP', 5.72), ('CB', 'HIS', 'OD1', 'ASP', 5.3), ('CB', 'HIS', 'OD2', 'ASP', 5.83)], [('CG', 'HIS', 'CB', 'ASP', 7.29), ('CG', 'HIS', 'CG', 'ASP', 5.95), ('CG', 'HIS', 'OD1', 'ASP', 5.56), ('CG', 'HIS', 'OD2', 'ASP', 5.7)], [('ND1', 'HIS', 'CB', 'ASP', 6.8), ('ND1', 'HIS', 'CG', 'ASP', 5.33), ('ND1', 'HIS', 'OD1', 'ASP', 5.17), ('ND1', 'HIS', 'OD2', 'ASP', 4.78)], [('CD2', 'HIS', 'CB', 'ASP', 8.61), ('CD2', 'HIS', 'CG', 'ASP', 7.22), ('CD2', 'HIS', 'OD1', 'ASP', 6.74), ('CD2', 'HIS', 'OD2', 'ASP', 6.88)], [('CE1', 'HIS', 'CB', 'ASP', 7.93), ('CE1', 'HIS', 'CG', 'ASP', 6.43), ('CE1', 'HIS', 'OD1', 'ASP', 6.24), ('CE1', 'HIS', 'OD2', 'ASP', 5.74)], [('NE2', 'HIS', 'CB', 'ASP', 8.91), ('NE2', 'HIS', 'CG', 'ASP', 7.43), ('NE2', 'HIS', 'OD1', 'ASP', 7.06), ('NE2', 'HIS', 'OD2', 'ASP', 6.87)]]}
HIS_SER = { 
	'distances':
		[[8.95, 8.57], [7.48, 7.08], [6.91, 6.52], [6.7, 6.28], [5.65, 5.21], [5.44, 4.96]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.95), ('CB', 'HIS', 'OG', 'SER', 8.57)], [('CG', 'HIS', 'CB', 'SER', 7.48), ('CG', 'HIS', 'OG', 'SER', 7.08)], [('ND1', 'HIS', 'CB', 'SER', 6.91), ('ND1', 'HIS', 'OG', 'SER', 6.52)], [('CD2', 'HIS', 'CB', 'SER', 6.7), ('CD2', 'HIS', 'OG', 'SER', 6.28)], [('CE1', 'HIS', 'CB', 'SER', 5.65), ('CE1', 'HIS', 'OG', 'SER', 5.21)], [('NE2', 'HIS', 'CB', 'SER', 5.44), ('NE2', 'HIS', 'OG', 'SER', 4.96)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_SER, d, 'A_1qfm_3_4_21_26')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1qfm_3_4_21_26')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_SER, d, 'A_1qfm_3_4_21_26')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_SER' :  match1,
		'HIS_ASP' :  match2,
		'HIS_SER' :  match3}