'''
FUNC:M_1dqs_4_6_1_3
PDB:1dqs
EC:4.6.1.3
RESI:his,zn
LOCI:a-275,402;
'''
import motifFunctions as cmd
HIS_ZN = { 
	'distances':
		[[10.16], [8.87], [8.55], [8.03], [7.56], [7.13]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 10.16)], [('CG', 'HIS', 'ZN', 'ZN', 8.87)], [('ND1', 'HIS', 'ZN', 'ZN', 8.55)], [('CD2', 'HIS', 'ZN', 'ZN', 8.03)], [('CE1', 'HIS', 'ZN', 'ZN', 7.56)], [('NE2', 'HIS', 'ZN', 'ZN', 7.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ZN, d, 'M_1dqs_4_6_1_3')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ZN' :  match1}