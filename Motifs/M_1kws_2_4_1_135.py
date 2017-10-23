'''
FUNC:M_1kws_2_4_1_135
PDB:1kws
EC:2.4.1.135
RESI:glu,mn
LOCI:a-281,500;
'''
import motifFunctions as cmd
GLU_MN = { 
	'distances':
		[[15.24], [13.74], [12.93], [13.63], [11.7]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 15.24)], [('CG', 'GLU', 'MN', 'MN', 13.74)], [('CD', 'GLU', 'MN', 'MN', 12.93)], [('OE1', 'GLU', 'MN', 'MN', 13.63)], [('OE2', 'GLU', 'MN', 'MN', 11.7)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_MN, d, 'M_1kws_2_4_1_135')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_MN' :  match1}