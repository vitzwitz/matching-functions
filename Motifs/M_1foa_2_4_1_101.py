'''
FUNC:M_1foa_2_4_1_101
PDB:1foa
EC:2.4.1.101
RESI:asp,mn
LOCI:a-291;a-448;
'''
import motifFunctions as cmd
ASP_MN = { 
	'distances':
		[[13.0], [12.21], [11.35], [12.6]],
	'comparisons':
		[[('CB', 'ASP', 'MN', 'MN', 13.0)], [('CG', 'ASP', 'MN', 'MN', 12.21)], [('OD1', 'ASP', 'MN', 'MN', 11.35)], [('OD2', 'ASP', 'MN', 'MN', 12.6)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MN, d, 'M_1foa_2_4_1_101')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MN' :  match1}