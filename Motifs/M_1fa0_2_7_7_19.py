'''
FUNC:M_1fa0_2_7_7_19
PDB:1fa0
EC:2.7.7.19
RESI:lys,mn,mn
LOCI:a-215,600,601;
'''
import motifFunctions as cmd
LYS_MN = { 
	'distances':
		[[16.49], [15.68], [14.81], [13.62], [12.82], [13.77], [12.96], [11.93], [10.74], [10.18]],
	'comparisons':
		[[('CB', 'LYS', 'MN', 'MN', 16.49)], [('CG', 'LYS', 'MN', 'MN', 15.68)], [('CD', 'LYS', 'MN', 'MN', 14.81)], [('CE', 'LYS', 'MN', 'MN', 13.62)], [('NZ', 'LYS', 'MN', 'MN', 12.82)], [('CB', 'LYS', 'MN', 'MN', 13.77)], [('CG', 'LYS', 'MN', 'MN', 12.96)], [('CD', 'LYS', 'MN', 'MN', 11.93)], [('CE', 'LYS', 'MN', 'MN', 10.74)], [('NZ', 'LYS', 'MN', 'MN', 10.18)]]}
MN_MN = { 
	'distances':
		[5.28, 5.28],
	'comparisons':
		[('MN', 'MN', 'MN', 'MN', 5.28), ('MN', 'MN', 'MN', 'MN', 5.28)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_MN, d, 'M_1fa0_2_7_7_19')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(MN_MN, d, 'M_1fa0_2_7_7_19')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_MN' :  match1,
		'MN_MN' :  match2}