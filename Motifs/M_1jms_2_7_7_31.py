'''
FUNC:M_1jms_2_7_7_31
PDB:1jms
EC:2.7.7.31
RESI:asp,mg
LOCI:a-434,701;
'''
import motifFunctions as cmd
ASP_MG = { 
	'distances':
		[[5.91], [5.41], [6.46], [4.35]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 5.91)], [('CG', 'ASP', 'MG', 'MG', 5.41)], [('OD1', 'ASP', 'MG', 'MG', 6.46)], [('OD2', 'ASP', 'MG', 'MG', 4.35)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MG, d, 'M_1jms_2_7_7_31')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MG' :  match1}