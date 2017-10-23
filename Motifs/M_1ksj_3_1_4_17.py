'''
FUNC:M_1ksj_3_1_4_17
PDB:1ksj
EC:3.1.4.17
RESI:gln,mg
LOCI:a-70,205;
'''
import motifFunctions as cmd
GLN_MG = { 
	'distances':
		[[11.26], [10.04], [10.56], [11.79], [9.8]],
	'comparisons':
		[[('CB', 'GLN', 'MG', 'MG', 11.26)], [('CG', 'GLN', 'MG', 'MG', 10.04)], [('CD', 'GLN', 'MG', 'MG', 10.56)], [('OE1', 'GLN', 'MG', 'MG', 11.79)], [('NE2', 'GLN', 'MG', 'MG', 9.8)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_MG, d, 'M_1ksj_3_1_4_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_MG' :  match1}