'''
FUNC:A_1glo_3_4_22_27
PDB:1glo
EC:3.4.22.27
RESI:gln,ser,his,asn
LOCI:a-19,25,164,184;
'''
import motifFunctions as cmd
ASN_GLN = { 
	'distances':
		[[10.93, 10.27, 9.83, 8.73, 10.87], [10.21, 9.35, 8.78, 7.71, 9.71], [10.57, 9.55, 9.03, 8.09, 9.91], [9.49, 8.68, 7.91, 6.77, 8.78]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLN', 10.93), ('CB', 'ASN', 'CG', 'GLN', 10.27), ('CB', 'ASN', 'CD', 'GLN', 9.83), ('CB', 'ASN', 'OE1', 'GLN', 8.73), ('CB', 'ASN', 'NE2', 'GLN', 10.87)], [('CG', 'ASN', 'CB', 'GLN', 10.21), ('CG', 'ASN', 'CG', 'GLN', 9.35), ('CG', 'ASN', 'CD', 'GLN', 8.78), ('CG', 'ASN', 'OE1', 'GLN', 7.71), ('CG', 'ASN', 'NE2', 'GLN', 9.71)], [('OD1', 'ASN', 'CB', 'GLN', 10.57), ('OD1', 'ASN', 'CG', 'GLN', 9.55), ('OD1', 'ASN', 'CD', 'GLN', 9.03), ('OD1', 'ASN', 'OE1', 'GLN', 8.09), ('OD1', 'ASN', 'NE2', 'GLN', 9.91)], [('ND2', 'ASN', 'CB', 'GLN', 9.49), ('ND2', 'ASN', 'CG', 'GLN', 8.68), ('ND2', 'ASN', 'CD', 'GLN', 7.91), ('ND2', 'ASN', 'OE1', 'GLN', 6.77), ('ND2', 'ASN', 'NE2', 'GLN', 8.78)]]}
SER_GLN = { 
	'distances':
		[[7.74, 7.43, 5.99, 5.42, 5.85], [8.91, 8.5, 7.01, 6.57, 6.56], [9.24, 9.54, 8.46, 7.83, 8.55], [8.77, 9.0, 7.83, 7.37, 7.71], [7.4, 7.5, 6.3, 5.91, 6.19], [7.05, 7.25, 6.16, 6.2, 5.71]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLN', 7.74), ('CB', 'SER', 'CG', 'GLN', 7.43), ('CB', 'SER', 'CD', 'GLN', 5.99), ('CB', 'SER', 'OE1', 'GLN', 5.42), ('CB', 'SER', 'NE2', 'GLN', 5.85)], [('OG', 'SER', 'CB', 'GLN', 8.91), ('OG', 'SER', 'CG', 'GLN', 8.5), ('OG', 'SER', 'CD', 'GLN', 7.01), ('OG', 'SER', 'OE1', 'GLN', 6.57), ('OG', 'SER', 'NE2', 'GLN', 6.56)], [('O', 'SER', 'CB', 'GLN', 9.24), ('O', 'SER', 'CG', 'GLN', 9.54), ('O', 'SER', 'CD', 'GLN', 8.46), ('O', 'SER', 'OE1', 'GLN', 7.83), ('O', 'SER', 'NE2', 'GLN', 8.55)], [('C', 'SER', 'CB', 'GLN', 8.77), ('C', 'SER', 'CG', 'GLN', 9.0), ('C', 'SER', 'CD', 'GLN', 7.83), ('C', 'SER', 'OE1', 'GLN', 7.37), ('C', 'SER', 'NE2', 'GLN', 7.71)], [('CA', 'SER', 'CB', 'GLN', 7.4), ('CA', 'SER', 'CG', 'GLN', 7.5), ('CA', 'SER', 'CD', 'GLN', 6.3), ('CA', 'SER', 'OE1', 'GLN', 5.91), ('CA', 'SER', 'NE2', 'GLN', 6.19)], [('N', 'SER', 'CB', 'GLN', 7.05), ('N', 'SER', 'CG', 'GLN', 7.25), ('N', 'SER', 'CD', 'GLN', 6.16), ('N', 'SER', 'OE1', 'GLN', 6.2), ('N', 'SER', 'NE2', 'GLN', 5.71)]]}
HIS_GLN = { 
	'distances':
		[[11.87, 10.88, 9.42, 8.79, 9.11], [10.62, 9.62, 8.2, 7.46, 8.09], [9.37, 8.35, 6.91, 6.28, 6.72], [10.62, 9.63, 8.32, 7.4, 8.5], [8.52, 7.5, 6.15, 5.33, 6.32], [9.37, 8.38, 7.15, 6.16, 7.52]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 11.87), ('CB', 'HIS', 'CG', 'GLN', 10.88), ('CB', 'HIS', 'CD', 'GLN', 9.42), ('CB', 'HIS', 'OE1', 'GLN', 8.79), ('CB', 'HIS', 'NE2', 'GLN', 9.11)], [('CG', 'HIS', 'CB', 'GLN', 10.62), ('CG', 'HIS', 'CG', 'GLN', 9.62), ('CG', 'HIS', 'CD', 'GLN', 8.2), ('CG', 'HIS', 'OE1', 'GLN', 7.46), ('CG', 'HIS', 'NE2', 'GLN', 8.09)], [('ND1', 'HIS', 'CB', 'GLN', 9.37), ('ND1', 'HIS', 'CG', 'GLN', 8.35), ('ND1', 'HIS', 'CD', 'GLN', 6.91), ('ND1', 'HIS', 'OE1', 'GLN', 6.28), ('ND1', 'HIS', 'NE2', 'GLN', 6.72)], [('CD2', 'HIS', 'CB', 'GLN', 10.62), ('CD2', 'HIS', 'CG', 'GLN', 9.63), ('CD2', 'HIS', 'CD', 'GLN', 8.32), ('CD2', 'HIS', 'OE1', 'GLN', 7.4), ('CD2', 'HIS', 'NE2', 'GLN', 8.5)], [('CE1', 'HIS', 'CB', 'GLN', 8.52), ('CE1', 'HIS', 'CG', 'GLN', 7.5), ('CE1', 'HIS', 'CD', 'GLN', 6.15), ('CE1', 'HIS', 'OE1', 'GLN', 5.33), ('CE1', 'HIS', 'NE2', 'GLN', 6.32)], [('NE2', 'HIS', 'CB', 'GLN', 9.37), ('NE2', 'HIS', 'CG', 'GLN', 8.38), ('NE2', 'HIS', 'CD', 'GLN', 7.15), ('NE2', 'HIS', 'OE1', 'GLN', 6.16), ('NE2', 'HIS', 'NE2', 'GLN', 7.52)]]}
HIS_ASN = { 
	'distances':
		[[10.37, 9.09, 9.17, 8.18], [9.06, 7.75, 7.88, 6.77], [9.17, 7.8, 7.94, 6.75], [7.77, 6.51, 6.71, 5.59], [8.06, 6.7, 6.92, 5.62], [7.05, 5.71, 5.99, 4.66]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 10.37), ('CB', 'HIS', 'CG', 'ASN', 9.09), ('CB', 'HIS', 'OD1', 'ASN', 9.17), ('CB', 'HIS', 'ND2', 'ASN', 8.18)], [('CG', 'HIS', 'CB', 'ASN', 9.06), ('CG', 'HIS', 'CG', 'ASN', 7.75), ('CG', 'HIS', 'OD1', 'ASN', 7.88), ('CG', 'HIS', 'ND2', 'ASN', 6.77)], [('ND1', 'HIS', 'CB', 'ASN', 9.17), ('ND1', 'HIS', 'CG', 'ASN', 7.8), ('ND1', 'HIS', 'OD1', 'ASN', 7.94), ('ND1', 'HIS', 'ND2', 'ASN', 6.75)], [('CD2', 'HIS', 'CB', 'ASN', 7.77), ('CD2', 'HIS', 'CG', 'ASN', 6.51), ('CD2', 'HIS', 'OD1', 'ASN', 6.71), ('CD2', 'HIS', 'ND2', 'ASN', 5.59)], [('CE1', 'HIS', 'CB', 'ASN', 8.06), ('CE1', 'HIS', 'CG', 'ASN', 6.7), ('CE1', 'HIS', 'OD1', 'ASN', 6.92), ('CE1', 'HIS', 'ND2', 'ASN', 5.62)], [('NE2', 'HIS', 'CB', 'ASN', 7.05), ('NE2', 'HIS', 'CG', 'ASN', 5.71), ('NE2', 'HIS', 'OD1', 'ASN', 5.99), ('NE2', 'HIS', 'ND2', 'ASN', 4.66)]]}
SER_ASN = { 
	'distances':
		[[10.02, 9.07, 9.68, 7.79], [10.91, 9.87, 10.4, 8.6], [11.16, 10.69, 11.62, 9.45], [11.54, 10.89, 11.7, 9.61], [10.84, 10.05, 10.76, 8.8], [11.95, 11.07, 11.68, 9.86]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 10.02), ('CB', 'SER', 'CG', 'ASN', 9.07), ('CB', 'SER', 'OD1', 'ASN', 9.68), ('CB', 'SER', 'ND2', 'ASN', 7.79)], [('OG', 'SER', 'CB', 'ASN', 10.91), ('OG', 'SER', 'CG', 'ASN', 9.87), ('OG', 'SER', 'OD1', 'ASN', 10.4), ('OG', 'SER', 'ND2', 'ASN', 8.6)], [('O', 'SER', 'CB', 'ASN', 11.16), ('O', 'SER', 'CG', 'ASN', 10.69), ('O', 'SER', 'OD1', 'ASN', 11.62), ('O', 'SER', 'ND2', 'ASN', 9.45)], [('C', 'SER', 'CB', 'ASN', 11.54), ('C', 'SER', 'CG', 'ASN', 10.89), ('C', 'SER', 'OD1', 'ASN', 11.7), ('C', 'SER', 'ND2', 'ASN', 9.61)], [('CA', 'SER', 'CB', 'ASN', 10.84), ('CA', 'SER', 'CG', 'ASN', 10.05), ('CA', 'SER', 'OD1', 'ASN', 10.76), ('CA', 'SER', 'ND2', 'ASN', 8.8)], [('N', 'SER', 'CB', 'ASN', 11.95), ('N', 'SER', 'CG', 'ASN', 11.07), ('N', 'SER', 'OD1', 'ASN', 11.68), ('N', 'SER', 'ND2', 'ASN', 9.86)]]}
HIS_SER = { 
	'distances':
		[[7.25, 6.52, 9.61, 9.16, 8.72, 9.38], [6.38, 6.03, 8.93, 8.54, 7.9, 8.65], [5.49, 5.31, 8.44, 7.9, 7.01, 7.59], [6.77, 6.76, 9.06, 8.87, 8.23, 9.16], [5.38, 5.74, 8.25, 7.85, 6.81, 7.51], [6.21, 6.58, 8.63, 8.45, 7.59, 8.5]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 7.25), ('CB', 'HIS', 'OG', 'SER', 6.52), ('CB', 'HIS', 'O', 'SER', 9.61), ('CB', 'HIS', 'C', 'SER', 9.16), ('CB', 'HIS', 'CA', 'SER', 8.72), ('CB', 'HIS', 'N', 'SER', 9.38)], [('CG', 'HIS', 'CB', 'SER', 6.38), ('CG', 'HIS', 'OG', 'SER', 6.03), ('CG', 'HIS', 'O', 'SER', 8.93), ('CG', 'HIS', 'C', 'SER', 8.54), ('CG', 'HIS', 'CA', 'SER', 7.9), ('CG', 'HIS', 'N', 'SER', 8.65)], [('ND1', 'HIS', 'CB', 'SER', 5.49), ('ND1', 'HIS', 'OG', 'SER', 5.31), ('ND1', 'HIS', 'O', 'SER', 8.44), ('ND1', 'HIS', 'C', 'SER', 7.9), ('ND1', 'HIS', 'CA', 'SER', 7.01), ('ND1', 'HIS', 'N', 'SER', 7.59)], [('CD2', 'HIS', 'CB', 'SER', 6.77), ('CD2', 'HIS', 'OG', 'SER', 6.76), ('CD2', 'HIS', 'O', 'SER', 9.06), ('CD2', 'HIS', 'C', 'SER', 8.87), ('CD2', 'HIS', 'CA', 'SER', 8.23), ('CD2', 'HIS', 'N', 'SER', 9.16)], [('CE1', 'HIS', 'CB', 'SER', 5.38), ('CE1', 'HIS', 'OG', 'SER', 5.74), ('CE1', 'HIS', 'O', 'SER', 8.25), ('CE1', 'HIS', 'C', 'SER', 7.85), ('CE1', 'HIS', 'CA', 'SER', 6.81), ('CE1', 'HIS', 'N', 'SER', 7.51)], [('NE2', 'HIS', 'CB', 'SER', 6.21), ('NE2', 'HIS', 'OG', 'SER', 6.58), ('NE2', 'HIS', 'O', 'SER', 8.63), ('NE2', 'HIS', 'C', 'SER', 8.45), ('NE2', 'HIS', 'CA', 'SER', 7.59), ('NE2', 'HIS', 'N', 'SER', 8.5)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLN, d, 'A_1glo_3_4_22_27')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLN, d, 'A_1glo_3_4_22_27')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_GLN, d, 'A_1glo_3_4_22_27')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ASN, d, 'A_1glo_3_4_22_27')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_ASN, d, 'A_1glo_3_4_22_27')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_SER, d, 'A_1glo_3_4_22_27')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLN' :  match1,
		'SER_GLN' :  match2,
		'HIS_GLN' :  match3,
		'HIS_ASN' :  match4,
		'SER_ASN' :  match5,
		'HIS_SER' :  match6}