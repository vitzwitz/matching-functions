'''
FUNC:M_1qlh_1_1_1_1
PDB:1qlh
EC:1.1.1.1
RESI:ser,his,zn,zn
LOCI:a-48,51,375,376;
'''
import motifFunctions as cmd
HIS_ZN = { 
	'distances':
		[[11.25], [11.02], [10.15], [11.81], [10.49], [11.49], [25.96], [26.38], [25.54], [27.63], [26.3], [27.56]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 11.25)], [('CG', 'HIS', 'ZN', 'ZN', 11.02)], [('ND1', 'HIS', 'ZN', 'ZN', 10.15)], [('CD2', 'HIS', 'ZN', 'ZN', 11.81)], [('CE1', 'HIS', 'ZN', 'ZN', 10.49)], [('NE2', 'HIS', 'ZN', 'ZN', 11.49)], [('CB', 'HIS', 'ZN', 'ZN', 25.96)], [('CG', 'HIS', 'ZN', 'ZN', 26.38)], [('ND1', 'HIS', 'ZN', 'ZN', 25.54)], [('CD2', 'HIS', 'ZN', 'ZN', 27.63)], [('CE1', 'HIS', 'ZN', 'ZN', 26.3)], [('NE2', 'HIS', 'ZN', 'ZN', 27.56)]]}
ZN_ZN = { 
	'distances':
		[21.35, 21.35],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 21.35), ('ZN', 'ZN', 'ZN', 'ZN', 21.35)]}
SER_ZN = { 
	'distances':
		[[6.04], [5.85], [22.5], [22.21]],
	'comparisons':
		[[('CB', 'SER', 'ZN', 'ZN', 6.04)], [('OG', 'SER', 'ZN', 'ZN', 5.85)], [('CB', 'SER', 'ZN', 'ZN', 22.5)], [('OG', 'SER', 'ZN', 'ZN', 22.21)]]}
SER_HIS = { 
	'distances':
		[[7.28, 7.28, 6.59, 8.3, 7.35, 8.32], [7.8, 7.5, 6.51, 8.44, 7.03, 8.17]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 7.28), ('CB', 'SER', 'CG', 'HIS', 7.28), ('CB', 'SER', 'ND1', 'HIS', 6.59), ('CB', 'SER', 'CD2', 'HIS', 8.3), ('CB', 'SER', 'CE1', 'HIS', 7.35), ('CB', 'SER', 'NE2', 'HIS', 8.32)], [('OG', 'SER', 'CB', 'HIS', 7.8), ('OG', 'SER', 'CG', 'HIS', 7.5), ('OG', 'SER', 'ND1', 'HIS', 6.51), ('OG', 'SER', 'CD2', 'HIS', 8.44), ('OG', 'SER', 'CE1', 'HIS', 7.03), ('OG', 'SER', 'NE2', 'HIS', 8.17)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ZN, d, 'M_1qlh_1_1_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ZN_ZN, d, 'M_1qlh_1_1_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_ZN, d, 'M_1qlh_1_1_1_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_HIS, d, 'M_1qlh_1_1_1_1')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ZN' :  match1,
		'ZN_ZN' :  match2,
		'SER_ZN' :  match3,
		'SER_HIS' :  match4}