'''
FUNC:A_1azw_3_4_11_5
PDB:1azw
EC:3.4.11.5
RESI:ser,asp,his
LOCI:a-110,266,294;
'''
import motifFunctions as cmd
ASP_SER = { 
	'distances':
		[[11.67, 11.38], [10.18, 9.85], [9.9, 9.38], [9.44, 9.28]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.67), ('CB', 'ASP', 'OG', 'SER', 11.38)], [('CG', 'ASP', 'CB', 'SER', 10.18), ('CG', 'ASP', 'OG', 'SER', 9.85)], [('OD1', 'ASP', 'CB', 'SER', 9.9), ('OD1', 'ASP', 'OG', 'SER', 9.38)], [('OD2', 'ASP', 'CB', 'SER', 9.44), ('OD2', 'ASP', 'OG', 'SER', 9.28)]]}
HIS_ASP = { 
	'distances':
		[[6.77, 5.76, 5.22, 6.04], [7.36, 6.04, 5.47, 5.99], [7.01, 5.56, 5.27, 5.14], [8.63, 7.26, 6.57, 7.17], [8.15, 6.65, 6.31, 6.1], [9.02, 7.54, 6.98, 7.2]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.77), ('CB', 'HIS', 'CG', 'ASP', 5.76), ('CB', 'HIS', 'OD1', 'ASP', 5.22), ('CB', 'HIS', 'OD2', 'ASP', 6.04)], [('CG', 'HIS', 'CB', 'ASP', 7.36), ('CG', 'HIS', 'CG', 'ASP', 6.04), ('CG', 'HIS', 'OD1', 'ASP', 5.47), ('CG', 'HIS', 'OD2', 'ASP', 5.99)], [('ND1', 'HIS', 'CB', 'ASP', 7.01), ('ND1', 'HIS', 'CG', 'ASP', 5.56), ('ND1', 'HIS', 'OD1', 'ASP', 5.27), ('ND1', 'HIS', 'OD2', 'ASP', 5.14)], [('CD2', 'HIS', 'CB', 'ASP', 8.63), ('CD2', 'HIS', 'CG', 'ASP', 7.26), ('CD2', 'HIS', 'OD1', 'ASP', 6.57), ('CD2', 'HIS', 'OD2', 'ASP', 7.17)], [('CE1', 'HIS', 'CB', 'ASP', 8.15), ('CE1', 'HIS', 'CG', 'ASP', 6.65), ('CE1', 'HIS', 'OD1', 'ASP', 6.31), ('CE1', 'HIS', 'OD2', 'ASP', 6.1)], [('NE2', 'HIS', 'CB', 'ASP', 9.02), ('NE2', 'HIS', 'CG', 'ASP', 7.54), ('NE2', 'HIS', 'OD1', 'ASP', 6.98), ('NE2', 'HIS', 'OD2', 'ASP', 7.2)]]}
HIS_SER = { 
	'distances':
		[[8.9, 8.46], [7.44, 6.98], [6.88, 6.59], [6.68, 6.04], [5.63, 5.31], [5.43, 4.79]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.9), ('CB', 'HIS', 'OG', 'SER', 8.46)], [('CG', 'HIS', 'CB', 'SER', 7.44), ('CG', 'HIS', 'OG', 'SER', 6.98)], [('ND1', 'HIS', 'CB', 'SER', 6.88), ('ND1', 'HIS', 'OG', 'SER', 6.59)], [('CD2', 'HIS', 'CB', 'SER', 6.68), ('CD2', 'HIS', 'OG', 'SER', 6.04)], [('CE1', 'HIS', 'CB', 'SER', 5.63), ('CE1', 'HIS', 'OG', 'SER', 5.31)], [('NE2', 'HIS', 'CB', 'SER', 5.43), ('NE2', 'HIS', 'OG', 'SER', 4.79)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_SER, d, 'A_1azw_3_4_11_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1azw_3_4_11_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_SER, d, 'A_1azw_3_4_11_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_SER' :  match1,
		'HIS_ASP' :  match2,
		'HIS_SER' :  match3}