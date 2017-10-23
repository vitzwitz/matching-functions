'''
FUNC:A_2acy_3_6_1_7
PDB:2acy
EC:3.6.1.7
RESI:arg,asn
LOCI:a-23,41;
'''
import motifFunctions as cmd
ARG_ASN = { 
	'distances':
		[[8.84, 7.85, 8.05, 7.15], [7.42, 6.49, 6.88, 5.72], [6.55, 5.78, 6.1, 5.44], [6.83, 5.84, 5.69, 5.79], [6.73, 5.93, 5.53, 6.3], [6.27, 5.9, 5.7, 6.48], [7.54, 6.63, 5.9, 7.11]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASN', 8.84), ('CB', 'ARG', 'CG', 'ASN', 7.85), ('CB', 'ARG', 'OD1', 'ASN', 8.05), ('CB', 'ARG', 'ND2', 'ASN', 7.15)], [('CG', 'ARG', 'CB', 'ASN', 7.42), ('CG', 'ARG', 'CG', 'ASN', 6.49), ('CG', 'ARG', 'OD1', 'ASN', 6.88), ('CG', 'ARG', 'ND2', 'ASN', 5.72)], [('CD', 'ARG', 'CB', 'ASN', 6.55), ('CD', 'ARG', 'CG', 'ASN', 5.78), ('CD', 'ARG', 'OD1', 'ASN', 6.1), ('CD', 'ARG', 'ND2', 'ASN', 5.44)], [('NE', 'ARG', 'CB', 'ASN', 6.83), ('NE', 'ARG', 'CG', 'ASN', 5.84), ('NE', 'ARG', 'OD1', 'ASN', 5.69), ('NE', 'ARG', 'ND2', 'ASN', 5.79)], [('CZ', 'ARG', 'CB', 'ASN', 6.73), ('CZ', 'ARG', 'CG', 'ASN', 5.93), ('CZ', 'ARG', 'OD1', 'ASN', 5.53), ('CZ', 'ARG', 'ND2', 'ASN', 6.3)], [('NH1', 'ARG', 'CB', 'ASN', 6.27), ('NH1', 'ARG', 'CG', 'ASN', 5.9), ('NH1', 'ARG', 'OD1', 'ASN', 5.7), ('NH1', 'ARG', 'ND2', 'ASN', 6.48)], [('NH2', 'ARG', 'CB', 'ASN', 7.54), ('NH2', 'ARG', 'CG', 'ASN', 6.63), ('NH2', 'ARG', 'OD1', 'ASN', 5.9), ('NH2', 'ARG', 'ND2', 'ASN', 7.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_ASN, d, 'A_2acy_3_6_1_7')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ASN' :  match1}