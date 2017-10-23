'''
FUNC:A_2pth_3_1_1_29
PDB:2pth
EC:3.1.1.29
RESI:asn,his,asp
LOCI:a-10,20,93;
'''
import motifFunctions as cmd
ASP_ASN = { 
	'distances':
		[[13.23, 12.86, 13.57, 11.9], [12.23, 11.71, 12.35, 10.72], [11.61, 11.07, 11.63, 10.18], [12.22, 11.6, 12.25, 10.51]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 13.23), ('CB', 'ASP', 'CG', 'ASN', 12.86), ('CB', 'ASP', 'OD1', 'ASN', 13.57), ('CB', 'ASP', 'ND2', 'ASN', 11.9)], [('CG', 'ASP', 'CB', 'ASN', 12.23), ('CG', 'ASP', 'CG', 'ASN', 11.71), ('CG', 'ASP', 'OD1', 'ASN', 12.35), ('CG', 'ASP', 'ND2', 'ASN', 10.72)], [('OD1', 'ASP', 'CB', 'ASN', 11.61), ('OD1', 'ASP', 'CG', 'ASN', 11.07), ('OD1', 'ASP', 'OD1', 'ASN', 11.63), ('OD1', 'ASP', 'ND2', 'ASN', 10.18)], [('OD2', 'ASP', 'CB', 'ASN', 12.22), ('OD2', 'ASP', 'CG', 'ASN', 11.6), ('OD2', 'ASP', 'OD1', 'ASN', 12.25), ('OD2', 'ASP', 'ND2', 'ASN', 10.51)]]}
HIS_ASP = { 
	'distances':
		[[7.73, 6.7, 6.63, 6.33], [7.71, 6.4, 6.23, 5.9], [6.79, 5.37, 5.31, 4.74], [8.86, 7.45, 7.13, 6.92], [7.58, 6.09, 5.89, 5.43], [8.76, 7.27, 6.94, 6.67]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.73), ('CB', 'HIS', 'CG', 'ASP', 6.7), ('CB', 'HIS', 'OD1', 'ASP', 6.63), ('CB', 'HIS', 'OD2', 'ASP', 6.33)], [('CG', 'HIS', 'CB', 'ASP', 7.71), ('CG', 'HIS', 'CG', 'ASP', 6.4), ('CG', 'HIS', 'OD1', 'ASP', 6.23), ('CG', 'HIS', 'OD2', 'ASP', 5.9)], [('ND1', 'HIS', 'CB', 'ASP', 6.79), ('ND1', 'HIS', 'CG', 'ASP', 5.37), ('ND1', 'HIS', 'OD1', 'ASP', 5.31), ('ND1', 'HIS', 'OD2', 'ASP', 4.74)], [('CD2', 'HIS', 'CB', 'ASP', 8.86), ('CD2', 'HIS', 'CG', 'ASP', 7.45), ('CD2', 'HIS', 'OD1', 'ASP', 7.13), ('CD2', 'HIS', 'OD2', 'ASP', 6.92)], [('CE1', 'HIS', 'CB', 'ASP', 7.58), ('CE1', 'HIS', 'CG', 'ASP', 6.09), ('CE1', 'HIS', 'OD1', 'ASP', 5.89), ('CE1', 'HIS', 'OD2', 'ASP', 5.43)], [('NE2', 'HIS', 'CB', 'ASP', 8.76), ('NE2', 'HIS', 'CG', 'ASP', 7.27), ('NE2', 'HIS', 'OD1', 'ASP', 6.94), ('NE2', 'HIS', 'OD2', 'ASP', 6.67)]]}
HIS_ASN = { 
	'distances':
		[[8.2, 7.71, 8.6, 6.54], [8.73, 7.92, 8.58, 6.73], [10.01, 9.18, 9.75, 8.03], [8.43, 7.38, 7.84, 6.21], [10.46, 9.44, 9.82, 8.33], [9.61, 8.46, 8.74, 7.37]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 8.2), ('CB', 'HIS', 'CG', 'ASN', 7.71), ('CB', 'HIS', 'OD1', 'ASN', 8.6), ('CB', 'HIS', 'ND2', 'ASN', 6.54)], [('CG', 'HIS', 'CB', 'ASN', 8.73), ('CG', 'HIS', 'CG', 'ASN', 7.92), ('CG', 'HIS', 'OD1', 'ASN', 8.58), ('CG', 'HIS', 'ND2', 'ASN', 6.73)], [('ND1', 'HIS', 'CB', 'ASN', 10.01), ('ND1', 'HIS', 'CG', 'ASN', 9.18), ('ND1', 'HIS', 'OD1', 'ASN', 9.75), ('ND1', 'HIS', 'ND2', 'ASN', 8.03)], [('CD2', 'HIS', 'CB', 'ASN', 8.43), ('CD2', 'HIS', 'CG', 'ASN', 7.38), ('CD2', 'HIS', 'OD1', 'ASN', 7.84), ('CD2', 'HIS', 'ND2', 'ASN', 6.21)], [('CE1', 'HIS', 'CB', 'ASN', 10.46), ('CE1', 'HIS', 'CG', 'ASN', 9.44), ('CE1', 'HIS', 'OD1', 'ASN', 9.82), ('CE1', 'HIS', 'ND2', 'ASN', 8.33)], [('NE2', 'HIS', 'CB', 'ASN', 9.61), ('NE2', 'HIS', 'CG', 'ASN', 8.46), ('NE2', 'HIS', 'OD1', 'ASN', 8.74), ('NE2', 'HIS', 'ND2', 'ASN', 7.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASN, d, 'A_2pth_3_1_1_29')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_2pth_3_1_1_29')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_2pth_3_1_1_29')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASN' :  match1,
		'HIS_ASP' :  match2,
		'HIS_ASN' :  match3}