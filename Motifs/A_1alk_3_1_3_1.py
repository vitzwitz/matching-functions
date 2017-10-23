'''
FUNC:A_1alk_3_1_3_1
PDB:1alk
EC:3.1.3.1
RESI:ser,arg
LOCI:a-102,166;
'''
import motifFunctions as cmd
SER_ARG = { 
	'distances':
		[[9.47, 9.57, 8.36, 7.63, 6.48, 6.03, 6.13], [10.72, 10.68, 9.4, 8.55, 7.28, 6.81, 6.77]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 9.47), ('CB', 'SER', 'CG', 'ARG', 9.57), ('CB', 'SER', 'CD', 'ARG', 8.36), ('CB', 'SER', 'NE', 'ARG', 7.63), ('CB', 'SER', 'CZ', 'ARG', 6.48), ('CB', 'SER', 'NH1', 'ARG', 6.03), ('CB', 'SER', 'NH2', 'ARG', 6.13)], [('OG', 'SER', 'CB', 'ARG', 10.72), ('OG', 'SER', 'CG', 'ARG', 10.68), ('OG', 'SER', 'CD', 'ARG', 9.4), ('OG', 'SER', 'NE', 'ARG', 8.55), ('OG', 'SER', 'CZ', 'ARG', 7.28), ('OG', 'SER', 'NH1', 'ARG', 6.81), ('OG', 'SER', 'NH2', 'ARG', 6.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_ARG, d, 'A_1alk_3_1_3_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_ARG' :  match1}