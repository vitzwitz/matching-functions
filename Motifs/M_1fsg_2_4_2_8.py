'''
FUNC:M_1fsg_2_4_2_8
PDB:1fsg
EC:2.4.2.8
RESI:mg,mg
LOCI:a-301,302;
'''
import motifFunctions as cmd
MG_MG = { 
	'distances':
		[7.2, 7.2],
	'comparisons':
		[('MG', 'MG', 'MG', 'MG', 7.2), ('MG', 'MG', 'MG', 'MG', 7.2)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MG_MG, d, 'M_1fsg_2_4_2_8')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MG_MG' :  match1}