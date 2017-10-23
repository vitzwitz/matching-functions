'''
FUNC:Pab_1g9r_2_4_1_44
PDB:1g9r
EC:2.4.1.44
RESI:asp,asn,gln
LOCI:a-130,153,189;
'''
import motifFunctions as cmd
ASN_GLN = { 
	'distances':
		[[8.93, 7.68, 6.87, 5.98, 7.57], [8.67, 7.64, 6.63, 5.52, 7.31], [9.1, 8.24, 7.34, 6.14, 8.16], [8.3, 7.34, 6.07, 5.03, 6.49]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLN', 8.93), ('CB', 'ASN', 'CG', 'GLN', 7.68), ('CB', 'ASN', 'CD', 'GLN', 6.87), ('CB', 'ASN', 'OE1', 'GLN', 5.98), ('CB', 'ASN', 'NE2', 'GLN', 7.57)], [('CG', 'ASN', 'CB', 'GLN', 8.67), ('CG', 'ASN', 'CG', 'GLN', 7.64), ('CG', 'ASN', 'CD', 'GLN', 6.63), ('CG', 'ASN', 'OE1', 'GLN', 5.52), ('CG', 'ASN', 'NE2', 'GLN', 7.31)], [('OD1', 'ASN', 'CB', 'GLN', 9.1), ('OD1', 'ASN', 'CG', 'GLN', 8.24), ('OD1', 'ASN', 'CD', 'GLN', 7.34), ('OD1', 'ASN', 'OE1', 'GLN', 6.14), ('OD1', 'ASN', 'NE2', 'GLN', 8.16)], [('ND2', 'ASN', 'CB', 'GLN', 8.3), ('ND2', 'ASN', 'CG', 'GLN', 7.34), ('ND2', 'ASN', 'CD', 'GLN', 6.07), ('ND2', 'ASN', 'OE1', 'GLN', 5.03), ('ND2', 'ASN', 'NE2', 'GLN', 6.49)]]}
ASP_GLN = { 
	'distances':
		[[9.8, 8.37, 7.51, 7.38, 7.36], [9.71, 8.42, 7.27, 7.1, 6.91], [10.71, 9.48, 8.3, 8.19, 7.75], [8.83, 7.63, 6.35, 6.05, 6.04]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 9.8), ('CB', 'ASP', 'CG', 'GLN', 8.37), ('CB', 'ASP', 'CD', 'GLN', 7.51), ('CB', 'ASP', 'OE1', 'GLN', 7.38), ('CB', 'ASP', 'NE2', 'GLN', 7.36)], [('CG', 'ASP', 'CB', 'GLN', 9.71), ('CG', 'ASP', 'CG', 'GLN', 8.42), ('CG', 'ASP', 'CD', 'GLN', 7.27), ('CG', 'ASP', 'OE1', 'GLN', 7.1), ('CG', 'ASP', 'NE2', 'GLN', 6.91)], [('OD1', 'ASP', 'CB', 'GLN', 10.71), ('OD1', 'ASP', 'CG', 'GLN', 9.48), ('OD1', 'ASP', 'CD', 'GLN', 8.3), ('OD1', 'ASP', 'OE1', 'GLN', 8.19), ('OD1', 'ASP', 'NE2', 'GLN', 7.75)], [('OD2', 'ASP', 'CB', 'GLN', 8.83), ('OD2', 'ASP', 'CG', 'GLN', 7.63), ('OD2', 'ASP', 'CD', 'GLN', 6.35), ('OD2', 'ASP', 'OE1', 'GLN', 6.05), ('OD2', 'ASP', 'NE2', 'GLN', 6.04)]]}
ASP_ASN = { 
	'distances':
		[[5.93, 6.82, 8.01, 6.55], [6.21, 6.63, 7.83, 5.99], [7.34, 7.67, 8.84, 6.94], [5.7, 5.78, 6.96, 4.93]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 5.93), ('CB', 'ASP', 'CG', 'ASN', 6.82), ('CB', 'ASP', 'OD1', 'ASN', 8.01), ('CB', 'ASP', 'ND2', 'ASN', 6.55)], [('CG', 'ASP', 'CB', 'ASN', 6.21), ('CG', 'ASP', 'CG', 'ASN', 6.63), ('CG', 'ASP', 'OD1', 'ASN', 7.83), ('CG', 'ASP', 'ND2', 'ASN', 5.99)], [('OD1', 'ASP', 'CB', 'ASN', 7.34), ('OD1', 'ASP', 'CG', 'ASN', 7.67), ('OD1', 'ASP', 'OD1', 'ASN', 8.84), ('OD1', 'ASP', 'ND2', 'ASN', 6.94)], [('OD2', 'ASP', 'CB', 'ASN', 5.7), ('OD2', 'ASP', 'CG', 'ASN', 5.78), ('OD2', 'ASP', 'OD1', 'ASN', 6.96), ('OD2', 'ASP', 'ND2', 'ASN', 4.93)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLN, d, 'Pab_1g9r_2_4_1_44')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_GLN, d, 'Pab_1g9r_2_4_1_44')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASN, d, 'Pab_1g9r_2_4_1_44')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLN' :  match1,
		'ASP_GLN' :  match2,
		'ASP_ASN' :  match3}