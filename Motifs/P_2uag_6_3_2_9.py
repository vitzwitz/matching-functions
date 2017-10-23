'''
FUNC:P_2uag_6_3_2_9
PDB:2uag
EC:6.3.2.9
RESI:lys,asn,his
LOCI:a-115,138,183;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[14.95, 13.75, 13.96, 12.44, 12.85, 11.81], [13.87, 12.76, 13.12, 11.44, 12.1, 10.97], [12.79, 11.67, 12.01, 10.39, 11.02, 9.92], [11.94, 10.71, 10.89, 9.44, 9.81, 8.79], [11.23, 10.02, 10.27, 8.7, 9.2, 8.09]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 14.95), ('CB', 'LYS', 'CG', 'HIS', 13.75), ('CB', 'LYS', 'ND1', 'HIS', 13.96), ('CB', 'LYS', 'CD2', 'HIS', 12.44), ('CB', 'LYS', 'CE1', 'HIS', 12.85), ('CB', 'LYS', 'NE2', 'HIS', 11.81)], [('CG', 'LYS', 'CB', 'HIS', 13.87), ('CG', 'LYS', 'CG', 'HIS', 12.76), ('CG', 'LYS', 'ND1', 'HIS', 13.12), ('CG', 'LYS', 'CD2', 'HIS', 11.44), ('CG', 'LYS', 'CE1', 'HIS', 12.1), ('CG', 'LYS', 'NE2', 'HIS', 10.97)], [('CD', 'LYS', 'CB', 'HIS', 12.79), ('CD', 'LYS', 'CG', 'HIS', 11.67), ('CD', 'LYS', 'ND1', 'HIS', 12.01), ('CD', 'LYS', 'CD2', 'HIS', 10.39), ('CD', 'LYS', 'CE1', 'HIS', 11.02), ('CD', 'LYS', 'NE2', 'HIS', 9.92)], [('CE', 'LYS', 'CB', 'HIS', 11.94), ('CE', 'LYS', 'CG', 'HIS', 10.71), ('CE', 'LYS', 'ND1', 'HIS', 10.89), ('CE', 'LYS', 'CD2', 'HIS', 9.44), ('CE', 'LYS', 'CE1', 'HIS', 9.81), ('CE', 'LYS', 'NE2', 'HIS', 8.79)], [('NZ', 'LYS', 'CB', 'HIS', 11.23), ('NZ', 'LYS', 'CG', 'HIS', 10.02), ('NZ', 'LYS', 'ND1', 'HIS', 10.27), ('NZ', 'LYS', 'CD2', 'HIS', 8.7), ('NZ', 'LYS', 'CE1', 'HIS', 9.2), ('NZ', 'LYS', 'NE2', 'HIS', 8.09)]]}
LYS_ASN = { 
	'distances':
		[[8.56, 8.81, 9.96, 7.91], [8.94, 9.05, 10.09, 8.16], [7.87, 7.9, 8.85, 7.11], [7.31, 7.0, 7.88, 6.01], [8.58, 8.03, 8.79, 6.91]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 8.56), ('CB', 'LYS', 'CG', 'ASN', 8.81), ('CB', 'LYS', 'OD1', 'ASN', 9.96), ('CB', 'LYS', 'ND2', 'ASN', 7.91)], [('CG', 'LYS', 'CB', 'ASN', 8.94), ('CG', 'LYS', 'CG', 'ASN', 9.05), ('CG', 'LYS', 'OD1', 'ASN', 10.09), ('CG', 'LYS', 'ND2', 'ASN', 8.16)], [('CD', 'LYS', 'CB', 'ASN', 7.87), ('CD', 'LYS', 'CG', 'ASN', 7.9), ('CD', 'LYS', 'OD1', 'ASN', 8.85), ('CD', 'LYS', 'ND2', 'ASN', 7.11)], [('CE', 'LYS', 'CB', 'ASN', 7.31), ('CE', 'LYS', 'CG', 'ASN', 7.0), ('CE', 'LYS', 'OD1', 'ASN', 7.88), ('CE', 'LYS', 'ND2', 'ASN', 6.01)], [('NZ', 'LYS', 'CB', 'ASN', 8.58), ('NZ', 'LYS', 'CG', 'ASN', 8.03), ('NZ', 'LYS', 'OD1', 'ASN', 8.79), ('NZ', 'LYS', 'ND2', 'ASN', 6.91)]]}
ASN_HIS = { 
	'distances':
		[[14.14, 12.84, 12.53, 11.98, 11.48, 11.07], [12.97, 11.62, 11.21, 10.8, 10.12, 9.8], [12.53, 11.21, 10.7, 10.54, 9.68, 9.53], [12.54, 11.14, 10.77, 10.21, 9.59, 9.15]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 14.14), ('CB', 'ASN', 'CG', 'HIS', 12.84), ('CB', 'ASN', 'ND1', 'HIS', 12.53), ('CB', 'ASN', 'CD2', 'HIS', 11.98), ('CB', 'ASN', 'CE1', 'HIS', 11.48), ('CB', 'ASN', 'NE2', 'HIS', 11.07)], [('CG', 'ASN', 'CB', 'HIS', 12.97), ('CG', 'ASN', 'CG', 'HIS', 11.62), ('CG', 'ASN', 'ND1', 'HIS', 11.21), ('CG', 'ASN', 'CD2', 'HIS', 10.8), ('CG', 'ASN', 'CE1', 'HIS', 10.12), ('CG', 'ASN', 'NE2', 'HIS', 9.8)], [('OD1', 'ASN', 'CB', 'HIS', 12.53), ('OD1', 'ASN', 'CG', 'HIS', 11.21), ('OD1', 'ASN', 'ND1', 'HIS', 10.7), ('OD1', 'ASN', 'CD2', 'HIS', 10.54), ('OD1', 'ASN', 'CE1', 'HIS', 9.68), ('OD1', 'ASN', 'NE2', 'HIS', 9.53)], [('ND2', 'ASN', 'CB', 'HIS', 12.54), ('ND2', 'ASN', 'CG', 'HIS', 11.14), ('ND2', 'ASN', 'ND1', 'HIS', 10.77), ('ND2', 'ASN', 'CD2', 'HIS', 10.21), ('ND2', 'ASN', 'CE1', 'HIS', 9.59), ('ND2', 'ASN', 'NE2', 'HIS', 9.15)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'P_2uag_6_3_2_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ASN, d, 'P_2uag_6_3_2_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_HIS, d, 'P_2uag_6_3_2_9')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'LYS_ASN' :  match2,
		'ASN_HIS' :  match3}