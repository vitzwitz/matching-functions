'''
FUNC:A_1c2t_2_1_2_2
PDB:1c2t
EC:2.1.2.2
RESI:asn,his,ser,asp
LOCI:a-106,108,135,144;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[6.64, 6.21, 6.18, 6.47, 6.43, 6.6], [6.05, 5.52, 5.1, 6.07, 5.48, 6.04], [5.58, 5.46, 5.1, 6.37, 5.9, 6.58], [6.57, 5.66, 4.87, 6.01, 4.83, 5.56]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.64), ('CB', 'ASP', 'CG', 'HIS', 6.21), ('CB', 'ASP', 'ND1', 'HIS', 6.18), ('CB', 'ASP', 'CD2', 'HIS', 6.47), ('CB', 'ASP', 'CE1', 'HIS', 6.43), ('CB', 'ASP', 'NE2', 'HIS', 6.6)], [('CG', 'ASP', 'CB', 'HIS', 6.05), ('CG', 'ASP', 'CG', 'HIS', 5.52), ('CG', 'ASP', 'ND1', 'HIS', 5.1), ('CG', 'ASP', 'CD2', 'HIS', 6.07), ('CG', 'ASP', 'CE1', 'HIS', 5.48), ('CG', 'ASP', 'NE2', 'HIS', 6.04)], [('OD1', 'ASP', 'CB', 'HIS', 5.58), ('OD1', 'ASP', 'CG', 'HIS', 5.46), ('OD1', 'ASP', 'ND1', 'HIS', 5.1), ('OD1', 'ASP', 'CD2', 'HIS', 6.37), ('OD1', 'ASP', 'CE1', 'HIS', 5.9), ('OD1', 'ASP', 'NE2', 'HIS', 6.58)], [('OD2', 'ASP', 'CB', 'HIS', 6.57), ('OD2', 'ASP', 'CG', 'HIS', 5.66), ('OD2', 'ASP', 'ND1', 'HIS', 4.87), ('OD2', 'ASP', 'CD2', 'HIS', 6.01), ('OD2', 'ASP', 'CE1', 'HIS', 4.83), ('OD2', 'ASP', 'NE2', 'HIS', 5.56)]]}
ASP_ASN = { 
	'distances':
		[[9.36, 8.78, 9.65, 7.51], [8.75, 7.92, 8.62, 6.63], [7.53, 6.67, 7.41, 5.39], [9.69, 8.69, 9.23, 7.44]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 9.36), ('CB', 'ASP', 'CG', 'ASN', 8.78), ('CB', 'ASP', 'OD1', 'ASN', 9.65), ('CB', 'ASP', 'ND2', 'ASN', 7.51)], [('CG', 'ASP', 'CB', 'ASN', 8.75), ('CG', 'ASP', 'CG', 'ASN', 7.92), ('CG', 'ASP', 'OD1', 'ASN', 8.62), ('CG', 'ASP', 'ND2', 'ASN', 6.63)], [('OD1', 'ASP', 'CB', 'ASN', 7.53), ('OD1', 'ASP', 'CG', 'ASN', 6.67), ('OD1', 'ASP', 'OD1', 'ASN', 7.41), ('OD1', 'ASP', 'ND2', 'ASN', 5.39)], [('OD2', 'ASP', 'CB', 'ASN', 9.69), ('OD2', 'ASP', 'CG', 'ASN', 8.69), ('OD2', 'ASP', 'OD1', 'ASN', 9.23), ('OD2', 'ASP', 'ND2', 'ASN', 7.44)]]}
HIS_ASN = { 
	'distances':
		[[8.25, 7.37, 7.97, 6.24], [9.32, 8.3, 8.8, 7.08], [9.35, 8.16, 8.51, 6.95], [10.6, 9.63, 10.16, 8.38], [10.6, 9.4, 9.72, 8.19], [11.3, 10.2, 10.63, 8.95]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 8.25), ('CB', 'HIS', 'CG', 'ASN', 7.37), ('CB', 'HIS', 'OD1', 'ASN', 7.97), ('CB', 'HIS', 'ND2', 'ASN', 6.24)], [('CG', 'HIS', 'CB', 'ASN', 9.32), ('CG', 'HIS', 'CG', 'ASN', 8.3), ('CG', 'HIS', 'OD1', 'ASN', 8.8), ('CG', 'HIS', 'ND2', 'ASN', 7.08)], [('ND1', 'HIS', 'CB', 'ASN', 9.35), ('ND1', 'HIS', 'CG', 'ASN', 8.16), ('ND1', 'HIS', 'OD1', 'ASN', 8.51), ('ND1', 'HIS', 'ND2', 'ASN', 6.95)], [('CD2', 'HIS', 'CB', 'ASN', 10.6), ('CD2', 'HIS', 'CG', 'ASN', 9.63), ('CD2', 'HIS', 'OD1', 'ASN', 10.16), ('CD2', 'HIS', 'ND2', 'ASN', 8.38)], [('CE1', 'HIS', 'CB', 'ASN', 10.6), ('CE1', 'HIS', 'CG', 'ASN', 9.4), ('CE1', 'HIS', 'OD1', 'ASN', 9.72), ('CE1', 'HIS', 'ND2', 'ASN', 8.19)], [('NE2', 'HIS', 'CB', 'ASN', 11.3), ('NE2', 'HIS', 'CG', 'ASN', 10.2), ('NE2', 'HIS', 'OD1', 'ASN', 10.63), ('NE2', 'HIS', 'ND2', 'ASN', 8.95)]]}
ASP_SER = { 
	'distances':
		[[9.63, 10.25], [9.9, 10.59], [9.62, 10.47], [10.64, 11.21]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 9.63), ('CB', 'ASP', 'OG', 'SER', 10.25)], [('CG', 'ASP', 'CB', 'SER', 9.9), ('CG', 'ASP', 'OG', 'SER', 10.59)], [('OD1', 'ASP', 'CB', 'SER', 9.62), ('OD1', 'ASP', 'OG', 'SER', 10.47)], [('OD2', 'ASP', 'CB', 'SER', 10.64), ('OD2', 'ASP', 'OG', 'SER', 11.21)]]}
ASN_SER = { 
	'distances':
		[[10.79, 12.13], [10.64, 11.9], [11.45, 12.68], [9.83, 11.02]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'SER', 10.79), ('CB', 'ASN', 'OG', 'SER', 12.13)], [('CG', 'ASN', 'CB', 'SER', 10.64), ('CG', 'ASN', 'OG', 'SER', 11.9)], [('OD1', 'ASN', 'CB', 'SER', 11.45), ('OD1', 'ASN', 'OG', 'SER', 12.68)], [('ND2', 'ASN', 'CB', 'SER', 9.83), ('ND2', 'ASN', 'OG', 'SER', 11.02)]]}
HIS_SER = { 
	'distances':
		[[6.82, 7.62], [7.71, 8.23], [9.07, 9.61], [7.74, 7.95], [9.78, 10.11], [9.1, 9.24]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 6.82), ('CB', 'HIS', 'OG', 'SER', 7.62)], [('CG', 'HIS', 'CB', 'SER', 7.71), ('CG', 'HIS', 'OG', 'SER', 8.23)], [('ND1', 'HIS', 'CB', 'SER', 9.07), ('ND1', 'HIS', 'OG', 'SER', 9.61)], [('CD2', 'HIS', 'CB', 'SER', 7.74), ('CD2', 'HIS', 'OG', 'SER', 7.95)], [('CE1', 'HIS', 'CB', 'SER', 9.78), ('CE1', 'HIS', 'OG', 'SER', 10.11)], [('NE2', 'HIS', 'CB', 'SER', 9.1), ('NE2', 'HIS', 'OG', 'SER', 9.24)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1c2t_2_1_2_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASN, d, 'A_1c2t_2_1_2_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_1c2t_2_1_2_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_SER, d, 'A_1c2t_2_1_2_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_SER, d, 'A_1c2t_2_1_2_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_SER, d, 'A_1c2t_2_1_2_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'ASP_ASN' :  match2,
		'HIS_ASN' :  match3,
		'ASP_SER' :  match4,
		'ASN_SER' :  match5,
		'HIS_SER' :  match6}