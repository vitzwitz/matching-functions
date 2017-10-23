'''
FUNC:M_2toh_1_14_16_2
PDB:2toh
EC:1.14.16.2
RESI:his,ser,fe
LOCI:a-331,395;a-501;
'''
import motifFunctions as cmd
HIS_FE = { 
	'distances':
		[[7.7], [6.26], [6.18], [5.14], [5.04], [4.11]],
	'comparisons':
		[[('CB', 'HIS', 'FE', 'FE', 7.7)], [('CG', 'HIS', 'FE', 'FE', 6.26)], [('ND1', 'HIS', 'FE', 'FE', 6.18)], [('CD2', 'HIS', 'FE', 'FE', 5.14)], [('CE1', 'HIS', 'FE', 'FE', 5.04)], [('NE2', 'HIS', 'FE', 'FE', 4.11)]]}
SER_FE = { 
	'distances':
		[[9.67], [8.78]],
	'comparisons':
		[[('CB', 'SER', 'FE', 'FE', 9.67)], [('OG', 'SER', 'FE', 'FE', 8.78)]]}
SER_HIS = { 
	'distances':
		[[6.09, 6.29, 5.64, 7.54, 6.69, 7.71], [5.97, 5.79, 4.82, 6.94, 5.74, 6.89]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 6.09), ('CB', 'SER', 'CG', 'HIS', 6.29), ('CB', 'SER', 'ND1', 'HIS', 5.64), ('CB', 'SER', 'CD2', 'HIS', 7.54), ('CB', 'SER', 'CE1', 'HIS', 6.69), ('CB', 'SER', 'NE2', 'HIS', 7.71)], [('OG', 'SER', 'CB', 'HIS', 5.97), ('OG', 'SER', 'CG', 'HIS', 5.79), ('OG', 'SER', 'ND1', 'HIS', 4.82), ('OG', 'SER', 'CD2', 'HIS', 6.94), ('OG', 'SER', 'CE1', 'HIS', 5.74), ('OG', 'SER', 'NE2', 'HIS', 6.89)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_FE, d, 'M_2toh_1_14_16_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_FE, d, 'M_2toh_1_14_16_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_HIS, d, 'M_2toh_1_14_16_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_FE' :  match1,
		'SER_FE' :  match2,
		'SER_HIS' :  match3}