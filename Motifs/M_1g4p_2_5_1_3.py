'''
FUNC:M_1g4p_2_5_1_3
PDB:1g4p
EC:2.5.1.3
RESI:ala,mg
LOCI:a-130,2003;
'''
import motifFunctions as cmd
ALA_MG = { 
	'distances':
		[8.47],
	'comparisons':
		[('CB', 'ALA', 'MG', 'MG', 8.47)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ALA_MG, d, 'M_1g4p_2_5_1_3')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ALA_MG' :  match1}