'''
FUNC:A_1wnw_1_14_99_3
PDB:1wnw
EC:1.14.99.3
RESI:asn,gly
LOCI:a-136,140;
'''
import motifFunctions as cmd
ASN_GLY = { 
	'distances':
		[[9.01, 8.3, 7.03, 7.16], [8.16, 7.61, 6.58, 7.08], [7.0, 6.44, 5.54, 6.19], [8.98, 8.6, 7.7, 8.34], [7.48, 6.39, 5.42, 5.01], [8.43, 7.39, 6.21, 5.75], [8.47, 7.59, 6.21, 5.98], [9.58, 8.69, 7.23, 6.77]],
	'comparisons':
		[[('CB', 'ASN', 'O', 'GLY', 9.01), ('CB', 'ASN', 'C', 'GLY', 8.3), ('CB', 'ASN', 'CA', 'GLY', 7.03), ('CB', 'ASN', 'N', 'GLY', 7.16)], [('CG', 'ASN', 'O', 'GLY', 8.16), ('CG', 'ASN', 'C', 'GLY', 7.61), ('CG', 'ASN', 'CA', 'GLY', 6.58), ('CG', 'ASN', 'N', 'GLY', 7.08)], [('OD1', 'ASN', 'O', 'GLY', 7.0), ('OD1', 'ASN', 'C', 'GLY', 6.44), ('OD1', 'ASN', 'CA', 'GLY', 5.54), ('OD1', 'ASN', 'N', 'GLY', 6.19)], [('ND2', 'ASN', 'O', 'GLY', 8.98), ('ND2', 'ASN', 'C', 'GLY', 8.6), ('ND2', 'ASN', 'CA', 'GLY', 7.7), ('ND2', 'ASN', 'N', 'GLY', 8.34)], [('O', 'ASN', 'O', 'GLY', 7.48), ('O', 'ASN', 'C', 'GLY', 6.39), ('O', 'ASN', 'CA', 'GLY', 5.42), ('O', 'ASN', 'N', 'GLY', 5.01)], [('C', 'ASN', 'O', 'GLY', 8.43), ('C', 'ASN', 'C', 'GLY', 7.39), ('C', 'ASN', 'CA', 'GLY', 6.21), ('C', 'ASN', 'N', 'GLY', 5.75)], [('CA', 'ASN', 'O', 'GLY', 8.47), ('CA', 'ASN', 'C', 'GLY', 7.59), ('CA', 'ASN', 'CA', 'GLY', 6.21), ('CA', 'ASN', 'N', 'GLY', 5.98)], [('N', 'ASN', 'O', 'GLY', 9.58), ('N', 'ASN', 'C', 'GLY', 8.69), ('N', 'ASN', 'CA', 'GLY', 7.23), ('N', 'ASN', 'N', 'GLY', 6.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLY, d, 'A_1wnw_1_14_99_3')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLY' :  match1}