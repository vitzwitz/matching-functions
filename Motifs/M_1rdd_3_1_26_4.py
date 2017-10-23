'''
FUNC:M_1rdd_3_1_26_4
PDB:1rdd
EC:3.1.26.4
RESI:his,mg
LOCI:a-124,300;
'''
import motifFunctions as cmd
HIS_MG = { 
	'distances':
		[[12.88], [14.06], [15.35], [14.21], [16.16], [15.55]],
	'comparisons':
		[[('CB', 'HIS', 'MG', 'MG', 12.88)], [('CG', 'HIS', 'MG', 'MG', 14.06)], [('ND1', 'HIS', 'MG', 'MG', 15.35)], [('CD2', 'HIS', 'MG', 'MG', 14.21)], [('CE1', 'HIS', 'MG', 'MG', 16.16)], [('NE2', 'HIS', 'MG', 'MG', 15.55)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_MG, d, 'M_1rdd_3_1_26_4')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_MG' :  match1}