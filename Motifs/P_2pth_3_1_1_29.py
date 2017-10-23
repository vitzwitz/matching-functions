'''
FUNC:P_2pth_3_1_1_29
PDB:2pth
EC:3.1.1.29
RESI:asn,his,asp
LOCI:a-10,20,93;
'''
import motifFunctions as cmd
ASN_ASP = { 
	'distances':
		[[13.23, 12.23, 11.61, 12.22], [12.86, 11.71, 11.07, 11.6], [13.57, 12.35, 11.63, 12.25], [11.9, 10.72, 10.18, 10.51]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 13.23), ('CB', 'ASN', 'CG', 'ASP', 12.23), ('CB', 'ASN', 'OD1', 'ASP', 11.61), ('CB', 'ASN', 'OD2', 'ASP', 12.22)], [('CG', 'ASN', 'CB', 'ASP', 12.86), ('CG', 'ASN', 'CG', 'ASP', 11.71), ('CG', 'ASN', 'OD1', 'ASP', 11.07), ('CG', 'ASN', 'OD2', 'ASP', 11.6)], [('OD1', 'ASN', 'CB', 'ASP', 13.57), ('OD1', 'ASN', 'CG', 'ASP', 12.35), ('OD1', 'ASN', 'OD1', 'ASP', 11.63), ('OD1', 'ASN', 'OD2', 'ASP', 12.25)], [('ND2', 'ASN', 'CB', 'ASP', 11.9), ('ND2', 'ASN', 'CG', 'ASP', 10.72), ('ND2', 'ASN', 'OD1', 'ASP', 10.18), ('ND2', 'ASN', 'OD2', 'ASP', 10.51)]]}
HIS_ASP = { 
	'distances':
		[[7.73, 6.7, 6.63, 6.33], [7.71, 6.4, 6.23, 5.9], [6.79, 5.37, 5.31, 4.74], [8.86, 7.45, 7.13, 6.92], [7.58, 6.09, 5.89, 5.43], [8.76, 7.27, 6.94, 6.67]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.73), ('CB', 'HIS', 'CG', 'ASP', 6.7), ('CB', 'HIS', 'OD1', 'ASP', 6.63), ('CB', 'HIS', 'OD2', 'ASP', 6.33)], [('CG', 'HIS', 'CB', 'ASP', 7.71), ('CG', 'HIS', 'CG', 'ASP', 6.4), ('CG', 'HIS', 'OD1', 'ASP', 6.23), ('CG', 'HIS', 'OD2', 'ASP', 5.9)], [('ND1', 'HIS', 'CB', 'ASP', 6.79), ('ND1', 'HIS', 'CG', 'ASP', 5.37), ('ND1', 'HIS', 'OD1', 'ASP', 5.31), ('ND1', 'HIS', 'OD2', 'ASP', 4.74)], [('CD2', 'HIS', 'CB', 'ASP', 8.86), ('CD2', 'HIS', 'CG', 'ASP', 7.45), ('CD2', 'HIS', 'OD1', 'ASP', 7.13), ('CD2', 'HIS', 'OD2', 'ASP', 6.92)], [('CE1', 'HIS', 'CB', 'ASP', 7.58), ('CE1', 'HIS', 'CG', 'ASP', 6.09), ('CE1', 'HIS', 'OD1', 'ASP', 5.89), ('CE1', 'HIS', 'OD2', 'ASP', 5.43)], [('NE2', 'HIS', 'CB', 'ASP', 8.76), ('NE2', 'HIS', 'CG', 'ASP', 7.27), ('NE2', 'HIS', 'OD1', 'ASP', 6.94), ('NE2', 'HIS', 'OD2', 'ASP', 6.67)]]}
ASN_HIS = { 
	'distances':
		[[8.2, 8.73, 10.01, 8.43, 10.46, 9.61], [7.71, 7.92, 9.18, 7.38, 9.44, 8.46], [8.6, 8.58, 9.75, 7.84, 9.82, 8.74], [6.54, 6.73, 8.03, 6.21, 8.33, 7.37]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 8.2), ('CB', 'ASN', 'CG', 'HIS', 8.73), ('CB', 'ASN', 'ND1', 'HIS', 10.01), ('CB', 'ASN', 'CD2', 'HIS', 8.43), ('CB', 'ASN', 'CE1', 'HIS', 10.46), ('CB', 'ASN', 'NE2', 'HIS', 9.61)], [('CG', 'ASN', 'CB', 'HIS', 7.71), ('CG', 'ASN', 'CG', 'HIS', 7.92), ('CG', 'ASN', 'ND1', 'HIS', 9.18), ('CG', 'ASN', 'CD2', 'HIS', 7.38), ('CG', 'ASN', 'CE1', 'HIS', 9.44), ('CG', 'ASN', 'NE2', 'HIS', 8.46)], [('OD1', 'ASN', 'CB', 'HIS', 8.6), ('OD1', 'ASN', 'CG', 'HIS', 8.58), ('OD1', 'ASN', 'ND1', 'HIS', 9.75), ('OD1', 'ASN', 'CD2', 'HIS', 7.84), ('OD1', 'ASN', 'CE1', 'HIS', 9.82), ('OD1', 'ASN', 'NE2', 'HIS', 8.74)], [('ND2', 'ASN', 'CB', 'HIS', 6.54), ('ND2', 'ASN', 'CG', 'HIS', 6.73), ('ND2', 'ASN', 'ND1', 'HIS', 8.03), ('ND2', 'ASN', 'CD2', 'HIS', 6.21), ('ND2', 'ASN', 'CE1', 'HIS', 8.33), ('ND2', 'ASN', 'NE2', 'HIS', 7.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_ASP, d, 'P_2pth_3_1_1_29')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_2pth_3_1_1_29')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_HIS, d, 'P_2pth_3_1_1_29')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_ASP' :  match1,
		'HIS_ASP' :  match2,
		'ASN_HIS' :  match3}