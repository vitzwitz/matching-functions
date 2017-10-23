'''
FUNC:A_1ysc_3_4_16_5
PDB:1ysc
EC:3.4.16.5
RESI:ser,asp,his
LOCI:a-146,338,397;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[8.53, 9.36], [7.07, 7.92], [6.59, 7.66], [6.31, 6.93], [5.32, 6.39], [5.04, 5.79]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.53), ('CB', 'HIS', 'OG', 'SER', 9.36)], [('CG', 'HIS', 'CB', 'SER', 7.07), ('CG', 'HIS', 'OG', 'SER', 7.92)], [('ND1', 'HIS', 'CB', 'SER', 6.59), ('ND1', 'HIS', 'OG', 'SER', 7.66)], [('CD2', 'HIS', 'CB', 'SER', 6.31), ('CD2', 'HIS', 'OG', 'SER', 6.93)], [('CE1', 'HIS', 'CB', 'SER', 5.32), ('CE1', 'HIS', 'OG', 'SER', 6.39)], [('NE2', 'HIS', 'CB', 'SER', 5.04), ('NE2', 'HIS', 'OG', 'SER', 5.79)]]}
ASP_HIS = { 
	'distances':
		[[6.26, 7.0, 6.66, 8.35, 7.9, 8.79], [5.61, 6.04, 5.51, 7.36, 6.7, 7.66], [5.38, 5.86, 5.52, 7.1, 6.68, 7.49], [5.86, 5.86, 4.97, 7.09, 5.99, 7.12]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.26), ('CB', 'ASP', 'CG', 'HIS', 7.0), ('CB', 'ASP', 'ND1', 'HIS', 6.66), ('CB', 'ASP', 'CD2', 'HIS', 8.35), ('CB', 'ASP', 'CE1', 'HIS', 7.9), ('CB', 'ASP', 'NE2', 'HIS', 8.79)], [('CG', 'ASP', 'CB', 'HIS', 5.61), ('CG', 'ASP', 'CG', 'HIS', 6.04), ('CG', 'ASP', 'ND1', 'HIS', 5.51), ('CG', 'ASP', 'CD2', 'HIS', 7.36), ('CG', 'ASP', 'CE1', 'HIS', 6.7), ('CG', 'ASP', 'NE2', 'HIS', 7.66)], [('OD1', 'ASP', 'CB', 'HIS', 5.38), ('OD1', 'ASP', 'CG', 'HIS', 5.86), ('OD1', 'ASP', 'ND1', 'HIS', 5.52), ('OD1', 'ASP', 'CD2', 'HIS', 7.1), ('OD1', 'ASP', 'CE1', 'HIS', 6.68), ('OD1', 'ASP', 'NE2', 'HIS', 7.49)], [('OD2', 'ASP', 'CB', 'HIS', 5.86), ('OD2', 'ASP', 'CG', 'HIS', 5.86), ('OD2', 'ASP', 'ND1', 'HIS', 4.97), ('OD2', 'ASP', 'CD2', 'HIS', 7.09), ('OD2', 'ASP', 'CE1', 'HIS', 5.99), ('OD2', 'ASP', 'NE2', 'HIS', 7.12)]]}
ASP_SER = { 
	'distances':
		[[11.08, 12.27], [9.92, 11.08], [9.97, 11.0], [9.02, 10.27]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.08), ('CB', 'ASP', 'OG', 'SER', 12.27)], [('CG', 'ASP', 'CB', 'SER', 9.92), ('CG', 'ASP', 'OG', 'SER', 11.08)], [('OD1', 'ASP', 'CB', 'SER', 9.97), ('OD1', 'ASP', 'OG', 'SER', 11.0)], [('OD2', 'ASP', 'CB', 'SER', 9.02), ('OD2', 'ASP', 'OG', 'SER', 10.27)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'A_1ysc_3_4_16_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1ysc_3_4_16_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SER, d, 'A_1ysc_3_4_16_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'ASP_HIS' :  match2,
		'ASP_SER' :  match3}