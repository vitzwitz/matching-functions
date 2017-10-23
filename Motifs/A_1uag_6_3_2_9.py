'''
FUNC:A_1uag_6_3_2_9
PDB:1uag
EC:6.3.2.9
RESI:lys,asn,his
LOCI:a-115,138,183;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[15.07, 13.84, 14.02, 12.54, 12.87, 11.86], [14.14, 12.99, 13.33, 11.66, 12.25, 11.13], [13.13, 11.97, 12.29, 10.63, 11.21, 10.09], [12.3, 11.02, 11.19, 9.74, 10.04, 9.01], [11.59, 10.32, 10.48, 9.05, 9.35, 8.33]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 15.07), ('CB', 'LYS', 'CG', 'HIS', 13.84), ('CB', 'LYS', 'ND1', 'HIS', 14.02), ('CB', 'LYS', 'CD2', 'HIS', 12.54), ('CB', 'LYS', 'CE1', 'HIS', 12.87), ('CB', 'LYS', 'NE2', 'HIS', 11.86)], [('CG', 'LYS', 'CB', 'HIS', 14.14), ('CG', 'LYS', 'CG', 'HIS', 12.99), ('CG', 'LYS', 'ND1', 'HIS', 13.33), ('CG', 'LYS', 'CD2', 'HIS', 11.66), ('CG', 'LYS', 'CE1', 'HIS', 12.25), ('CG', 'LYS', 'NE2', 'HIS', 11.13)], [('CD', 'LYS', 'CB', 'HIS', 13.13), ('CD', 'LYS', 'CG', 'HIS', 11.97), ('CD', 'LYS', 'ND1', 'HIS', 12.29), ('CD', 'LYS', 'CD2', 'HIS', 10.63), ('CD', 'LYS', 'CE1', 'HIS', 11.21), ('CD', 'LYS', 'NE2', 'HIS', 10.09)], [('CE', 'LYS', 'CB', 'HIS', 12.3), ('CE', 'LYS', 'CG', 'HIS', 11.02), ('CE', 'LYS', 'ND1', 'HIS', 11.19), ('CE', 'LYS', 'CD2', 'HIS', 9.74), ('CE', 'LYS', 'CE1', 'HIS', 10.04), ('CE', 'LYS', 'NE2', 'HIS', 9.01)], [('NZ', 'LYS', 'CB', 'HIS', 11.59), ('NZ', 'LYS', 'CG', 'HIS', 10.32), ('NZ', 'LYS', 'ND1', 'HIS', 10.48), ('NZ', 'LYS', 'CD2', 'HIS', 9.05), ('NZ', 'LYS', 'CE1', 'HIS', 9.35), ('NZ', 'LYS', 'NE2', 'HIS', 8.33)]]}
LYS_ASN = { 
	'distances':
		[[8.9, 9.01, 10.15, 8.02], [9.02, 9.08, 10.14, 8.13], [7.77, 7.79, 8.79, 6.94], [7.13, 6.81, 7.75, 5.76], [8.32, 7.72, 8.52, 6.54]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 8.9), ('CB', 'LYS', 'CG', 'ASN', 9.01), ('CB', 'LYS', 'OD1', 'ASN', 10.15), ('CB', 'LYS', 'ND2', 'ASN', 8.02)], [('CG', 'LYS', 'CB', 'ASN', 9.02), ('CG', 'LYS', 'CG', 'ASN', 9.08), ('CG', 'LYS', 'OD1', 'ASN', 10.14), ('CG', 'LYS', 'ND2', 'ASN', 8.13)], [('CD', 'LYS', 'CB', 'ASN', 7.77), ('CD', 'LYS', 'CG', 'ASN', 7.79), ('CD', 'LYS', 'OD1', 'ASN', 8.79), ('CD', 'LYS', 'ND2', 'ASN', 6.94)], [('CE', 'LYS', 'CB', 'ASN', 7.13), ('CE', 'LYS', 'CG', 'ASN', 6.81), ('CE', 'LYS', 'OD1', 'ASN', 7.75), ('CE', 'LYS', 'ND2', 'ASN', 5.76)], [('NZ', 'LYS', 'CB', 'ASN', 8.32), ('NZ', 'LYS', 'CG', 'ASN', 7.72), ('NZ', 'LYS', 'OD1', 'ASN', 8.52), ('NZ', 'LYS', 'ND2', 'ASN', 6.54)]]}
ASN_HIS = { 
	'distances':
		[[14.0, 12.69, 12.5, 11.7, 11.36, 10.78], [12.81, 11.45, 11.15, 10.52, 9.98, 9.5], [12.35, 11.02, 10.62, 10.22, 9.52, 9.19], [12.43, 11.02, 10.74, 10.02, 9.5, 8.95]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 14.0), ('CB', 'ASN', 'CG', 'HIS', 12.69), ('CB', 'ASN', 'ND1', 'HIS', 12.5), ('CB', 'ASN', 'CD2', 'HIS', 11.7), ('CB', 'ASN', 'CE1', 'HIS', 11.36), ('CB', 'ASN', 'NE2', 'HIS', 10.78)], [('CG', 'ASN', 'CB', 'HIS', 12.81), ('CG', 'ASN', 'CG', 'HIS', 11.45), ('CG', 'ASN', 'ND1', 'HIS', 11.15), ('CG', 'ASN', 'CD2', 'HIS', 10.52), ('CG', 'ASN', 'CE1', 'HIS', 9.98), ('CG', 'ASN', 'NE2', 'HIS', 9.5)], [('OD1', 'ASN', 'CB', 'HIS', 12.35), ('OD1', 'ASN', 'CG', 'HIS', 11.02), ('OD1', 'ASN', 'ND1', 'HIS', 10.62), ('OD1', 'ASN', 'CD2', 'HIS', 10.22), ('OD1', 'ASN', 'CE1', 'HIS', 9.52), ('OD1', 'ASN', 'NE2', 'HIS', 9.19)], [('ND2', 'ASN', 'CB', 'HIS', 12.43), ('ND2', 'ASN', 'CG', 'HIS', 11.02), ('ND2', 'ASN', 'ND1', 'HIS', 10.74), ('ND2', 'ASN', 'CD2', 'HIS', 10.02), ('ND2', 'ASN', 'CE1', 'HIS', 9.5), ('ND2', 'ASN', 'NE2', 'HIS', 8.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'A_1uag_6_3_2_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ASN, d, 'A_1uag_6_3_2_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_HIS, d, 'A_1uag_6_3_2_9')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'LYS_ASN' :  match2,
		'ASN_HIS' :  match3}