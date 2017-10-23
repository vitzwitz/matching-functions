'''
FUNC:P_1ga8_2_4_1_44
PDB:1ga8
EC:2.4.1.44
RESI:asp,asn,gln
LOCI:a-130,153,189;
'''
import motifFunctions as cmd
ASN_GLN = { 
	'distances':
		[[8.9, 7.71, 6.87, 5.97, 7.54], [8.64, 7.69, 6.66, 5.55, 7.35], [9.06, 8.28, 7.39, 6.19, 8.21], [8.29, 7.4, 6.13, 5.08, 6.55]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLN', 8.9), ('CB', 'ASN', 'CG', 'GLN', 7.71), ('CB', 'ASN', 'CD', 'GLN', 6.87), ('CB', 'ASN', 'OE1', 'GLN', 5.97), ('CB', 'ASN', 'NE2', 'GLN', 7.54)], [('CG', 'ASN', 'CB', 'GLN', 8.64), ('CG', 'ASN', 'CG', 'GLN', 7.69), ('CG', 'ASN', 'CD', 'GLN', 6.66), ('CG', 'ASN', 'OE1', 'GLN', 5.55), ('CG', 'ASN', 'NE2', 'GLN', 7.35)], [('OD1', 'ASN', 'CB', 'GLN', 9.06), ('OD1', 'ASN', 'CG', 'GLN', 8.28), ('OD1', 'ASN', 'CD', 'GLN', 7.39), ('OD1', 'ASN', 'OE1', 'GLN', 6.19), ('OD1', 'ASN', 'NE2', 'GLN', 8.21)], [('ND2', 'ASN', 'CB', 'GLN', 8.29), ('ND2', 'ASN', 'CG', 'GLN', 7.4), ('ND2', 'ASN', 'CD', 'GLN', 6.13), ('ND2', 'ASN', 'OE1', 'GLN', 5.08), ('ND2', 'ASN', 'NE2', 'GLN', 6.55)]]}
ASP_GLN = { 
	'distances':
		[[9.9, 8.46, 7.6, 7.51, 7.43], [9.66, 8.35, 7.22, 7.07, 6.84], [10.59, 9.35, 8.16, 8.07, 7.58], [8.74, 7.5, 6.24, 5.96, 5.97]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 9.9), ('CB', 'ASP', 'CG', 'GLN', 8.46), ('CB', 'ASP', 'CD', 'GLN', 7.6), ('CB', 'ASP', 'OE1', 'GLN', 7.51), ('CB', 'ASP', 'NE2', 'GLN', 7.43)], [('CG', 'ASP', 'CB', 'GLN', 9.66), ('CG', 'ASP', 'CG', 'GLN', 8.35), ('CG', 'ASP', 'CD', 'GLN', 7.22), ('CG', 'ASP', 'OE1', 'GLN', 7.07), ('CG', 'ASP', 'NE2', 'GLN', 6.84)], [('OD1', 'ASP', 'CB', 'GLN', 10.59), ('OD1', 'ASP', 'CG', 'GLN', 9.35), ('OD1', 'ASP', 'CD', 'GLN', 8.16), ('OD1', 'ASP', 'OE1', 'GLN', 8.07), ('OD1', 'ASP', 'NE2', 'GLN', 7.58)], [('OD2', 'ASP', 'CB', 'GLN', 8.74), ('OD2', 'ASP', 'CG', 'GLN', 7.5), ('OD2', 'ASP', 'CD', 'GLN', 6.24), ('OD2', 'ASP', 'OE1', 'GLN', 5.96), ('OD2', 'ASP', 'NE2', 'GLN', 5.97)]]}
ASP_ASN = { 
	'distances':
		[[6.05, 7.03, 8.22, 6.85], [6.15, 6.7, 7.92, 6.15], [7.26, 7.69, 8.87, 7.0], [5.49, 5.76, 6.97, 5.04]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 6.05), ('CB', 'ASP', 'CG', 'ASN', 7.03), ('CB', 'ASP', 'OD1', 'ASN', 8.22), ('CB', 'ASP', 'ND2', 'ASN', 6.85)], [('CG', 'ASP', 'CB', 'ASN', 6.15), ('CG', 'ASP', 'CG', 'ASN', 6.7), ('CG', 'ASP', 'OD1', 'ASN', 7.92), ('CG', 'ASP', 'ND2', 'ASN', 6.15)], [('OD1', 'ASP', 'CB', 'ASN', 7.26), ('OD1', 'ASP', 'CG', 'ASN', 7.69), ('OD1', 'ASP', 'OD1', 'ASN', 8.87), ('OD1', 'ASP', 'ND2', 'ASN', 7.0)], [('OD2', 'ASP', 'CB', 'ASN', 5.49), ('OD2', 'ASP', 'CG', 'ASN', 5.76), ('OD2', 'ASP', 'OD1', 'ASN', 6.97), ('OD2', 'ASP', 'ND2', 'ASN', 5.04)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLN, d, 'P_1ga8_2_4_1_44')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_GLN, d, 'P_1ga8_2_4_1_44')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASN, d, 'P_1ga8_2_4_1_44')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLN' :  match1,
		'ASP_GLN' :  match2,
		'ASP_ASN' :  match3}