'''
FUNC:A_1bmt_2_1_1_13
PDB:1bmt
EC:2.1.1.13
RESI:asp,his,ser
LOCI:a-757,759,810;
'''
import motifFunctions as cmd
SER_HIS = { 
	'distances':
		[[10.34, 10.39, 9.6, 11.42, 10.28, 11.38], [9.45, 9.43, 8.54, 10.49, 9.24, 10.41]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 10.34), ('CB', 'SER', 'CG', 'HIS', 10.39), ('CB', 'SER', 'ND1', 'HIS', 9.6), ('CB', 'SER', 'CD2', 'HIS', 11.42), ('CB', 'SER', 'CE1', 'HIS', 10.28), ('CB', 'SER', 'NE2', 'HIS', 11.38)], [('OG', 'SER', 'CB', 'HIS', 9.45), ('OG', 'SER', 'CG', 'HIS', 9.43), ('OG', 'SER', 'ND1', 'HIS', 8.54), ('OG', 'SER', 'CD2', 'HIS', 10.49), ('OG', 'SER', 'CE1', 'HIS', 9.24), ('OG', 'SER', 'NE2', 'HIS', 10.41)]]}
ASP_HIS = { 
	'distances':
		[[7.65, 7.9, 7.16, 9.18, 8.2, 9.36], [6.54, 6.68, 5.95, 7.93, 7.01, 8.12], [5.49, 5.55, 4.85, 6.82, 6.01, 7.07], [7.0, 7.08, 6.37, 8.23, 7.29, 8.37]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.65), ('CB', 'ASP', 'CG', 'HIS', 7.9), ('CB', 'ASP', 'ND1', 'HIS', 7.16), ('CB', 'ASP', 'CD2', 'HIS', 9.18), ('CB', 'ASP', 'CE1', 'HIS', 8.2), ('CB', 'ASP', 'NE2', 'HIS', 9.36)], [('CG', 'ASP', 'CB', 'HIS', 6.54), ('CG', 'ASP', 'CG', 'HIS', 6.68), ('CG', 'ASP', 'ND1', 'HIS', 5.95), ('CG', 'ASP', 'CD2', 'HIS', 7.93), ('CG', 'ASP', 'CE1', 'HIS', 7.01), ('CG', 'ASP', 'NE2', 'HIS', 8.12)], [('OD1', 'ASP', 'CB', 'HIS', 5.49), ('OD1', 'ASP', 'CG', 'HIS', 5.55), ('OD1', 'ASP', 'ND1', 'HIS', 4.85), ('OD1', 'ASP', 'CD2', 'HIS', 6.82), ('OD1', 'ASP', 'CE1', 'HIS', 6.01), ('OD1', 'ASP', 'NE2', 'HIS', 7.07)], [('OD2', 'ASP', 'CB', 'HIS', 7.0), ('OD2', 'ASP', 'CG', 'HIS', 7.08), ('OD2', 'ASP', 'ND1', 'HIS', 6.37), ('OD2', 'ASP', 'CD2', 'HIS', 8.23), ('OD2', 'ASP', 'CE1', 'HIS', 7.29), ('OD2', 'ASP', 'NE2', 'HIS', 8.37)]]}
ASP_SER = { 
	'distances':
		[[6.47, 5.26], [6.38, 5.21], [7.53, 6.37], [5.43, 4.45]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 6.47), ('CB', 'ASP', 'OG', 'SER', 5.26)], [('CG', 'ASP', 'CB', 'SER', 6.38), ('CG', 'ASP', 'OG', 'SER', 5.21)], [('OD1', 'ASP', 'CB', 'SER', 7.53), ('OD1', 'ASP', 'OG', 'SER', 6.37)], [('OD2', 'ASP', 'CB', 'SER', 5.43), ('OD2', 'ASP', 'OG', 'SER', 4.45)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_HIS, d, 'A_1bmt_2_1_1_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1bmt_2_1_1_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SER, d, 'A_1bmt_2_1_1_13')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_HIS' :  match1,
		'ASP_HIS' :  match2,
		'ASP_SER' :  match3}