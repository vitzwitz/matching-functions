'''
FUNC:P_1njs_2_1_2_2
PDB:1njs
EC:2.1.2.2
RESI:asn,his,thr,asp
LOCI:a-106,108,135,144;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[7.48, 6.72, 6.13, 7.08], [6.89, 6.12, 5.91, 6.21], [6.58, 5.51, 5.43, 5.25], [7.2, 6.7, 6.8, 6.68], [6.68, 5.79, 6.12, 5.22], [7.05, 6.49, 6.88, 6.14]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.48), ('CB', 'HIS', 'CG', 'ASP', 6.72), ('CB', 'HIS', 'OD1', 'ASP', 6.13), ('CB', 'HIS', 'OD2', 'ASP', 7.08)], [('CG', 'HIS', 'CB', 'ASP', 6.89), ('CG', 'HIS', 'CG', 'ASP', 6.12), ('CG', 'HIS', 'OD1', 'ASP', 5.91), ('CG', 'HIS', 'OD2', 'ASP', 6.21)], [('ND1', 'HIS', 'CB', 'ASP', 6.58), ('ND1', 'HIS', 'CG', 'ASP', 5.51), ('ND1', 'HIS', 'OD1', 'ASP', 5.43), ('ND1', 'HIS', 'OD2', 'ASP', 5.25)], [('CD2', 'HIS', 'CB', 'ASP', 7.2), ('CD2', 'HIS', 'CG', 'ASP', 6.7), ('CD2', 'HIS', 'OD1', 'ASP', 6.8), ('CD2', 'HIS', 'OD2', 'ASP', 6.68)], [('CE1', 'HIS', 'CB', 'ASP', 6.68), ('CE1', 'HIS', 'CG', 'ASP', 5.79), ('CE1', 'HIS', 'OD1', 'ASP', 6.12), ('CE1', 'HIS', 'OD2', 'ASP', 5.22)], [('NE2', 'HIS', 'CB', 'ASP', 7.05), ('NE2', 'HIS', 'CG', 'ASP', 6.49), ('NE2', 'HIS', 'OD1', 'ASP', 6.88), ('NE2', 'HIS', 'OD2', 'ASP', 6.14)]]}
HIS_THR = { 
	'distances':
		[[6.65, 7.43, 7.53], [7.33, 7.77, 8.25], [8.7, 9.13, 9.56], [7.18, 7.28, 8.18], [9.28, 9.47, 10.17], [8.5, 8.49, 9.45]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'THR', 6.65), ('CB', 'HIS', 'OG1', 'THR', 7.43), ('CB', 'HIS', 'CG2', 'THR', 7.53)], [('CG', 'HIS', 'CB', 'THR', 7.33), ('CG', 'HIS', 'OG1', 'THR', 7.77), ('CG', 'HIS', 'CG2', 'THR', 8.25)], [('ND1', 'HIS', 'CB', 'THR', 8.7), ('ND1', 'HIS', 'OG1', 'THR', 9.13), ('ND1', 'HIS', 'CG2', 'THR', 9.56)], [('CD2', 'HIS', 'CB', 'THR', 7.18), ('CD2', 'HIS', 'OG1', 'THR', 7.28), ('CD2', 'HIS', 'CG2', 'THR', 8.18)], [('CE1', 'HIS', 'CB', 'THR', 9.28), ('CE1', 'HIS', 'OG1', 'THR', 9.47), ('CE1', 'HIS', 'CG2', 'THR', 10.17)], [('NE2', 'HIS', 'CB', 'THR', 8.5), ('NE2', 'HIS', 'OG1', 'THR', 8.49), ('NE2', 'HIS', 'CG2', 'THR', 9.45)]]}
THR_ASP = { 
	'distances':
		[[10.1, 10.14, 9.76, 10.8], [10.53, 10.68, 10.48, 11.23], [10.1, 10.36, 9.97, 11.19]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 10.1), ('CB', 'THR', 'CG', 'ASP', 10.14), ('CB', 'THR', 'OD1', 'ASP', 9.76), ('CB', 'THR', 'OD2', 'ASP', 10.8)], [('OG1', 'THR', 'CB', 'ASP', 10.53), ('OG1', 'THR', 'CG', 'ASP', 10.68), ('OG1', 'THR', 'OD1', 'ASP', 10.48), ('OG1', 'THR', 'OD2', 'ASP', 11.23)], [('CG2', 'THR', 'CB', 'ASP', 10.1), ('CG2', 'THR', 'CG', 'ASP', 10.36), ('CG2', 'THR', 'OD1', 'ASP', 9.97), ('CG2', 'THR', 'OD2', 'ASP', 11.19)]]}
ASN_THR = { 
	'distances':
		[[10.25, 11.58, 10.16], [10.23, 11.48, 10.4], [11.17, 12.4, 11.45], [9.39, 10.56, 9.63]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'THR', 10.25), ('CB', 'ASN', 'OG1', 'THR', 11.58), ('CB', 'ASN', 'CG2', 'THR', 10.16)], [('CG', 'ASN', 'CB', 'THR', 10.23), ('CG', 'ASN', 'OG1', 'THR', 11.48), ('CG', 'ASN', 'CG2', 'THR', 10.4)], [('OD1', 'ASN', 'CB', 'THR', 11.17), ('OD1', 'ASN', 'OG1', 'THR', 12.4), ('OD1', 'ASN', 'CG2', 'THR', 11.45)], [('ND2', 'ASN', 'CB', 'THR', 9.39), ('ND2', 'ASN', 'OG1', 'THR', 10.56), ('ND2', 'ASN', 'CG2', 'THR', 9.63)]]}
ASN_ASP = { 
	'distances':
		[[9.61, 8.95, 7.71, 9.78], [9.06, 8.14, 6.89, 8.79], [9.87, 8.81, 7.58, 9.29], [7.89, 6.96, 5.71, 7.62]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 9.61), ('CB', 'ASN', 'CG', 'ASP', 8.95), ('CB', 'ASN', 'OD1', 'ASP', 7.71), ('CB', 'ASN', 'OD2', 'ASP', 9.78)], [('CG', 'ASN', 'CB', 'ASP', 9.06), ('CG', 'ASN', 'CG', 'ASP', 8.14), ('CG', 'ASN', 'OD1', 'ASP', 6.89), ('CG', 'ASN', 'OD2', 'ASP', 8.79)], [('OD1', 'ASN', 'CB', 'ASP', 9.87), ('OD1', 'ASN', 'CG', 'ASP', 8.81), ('OD1', 'ASN', 'OD1', 'ASP', 7.58), ('OD1', 'ASN', 'OD2', 'ASP', 9.29)], [('ND2', 'ASN', 'CB', 'ASP', 7.89), ('ND2', 'ASN', 'CG', 'ASP', 6.96), ('ND2', 'ASN', 'OD1', 'ASP', 5.71), ('ND2', 'ASN', 'OD2', 'ASP', 7.62)]]}
ASN_HIS = { 
	'distances':
		[[7.92, 9.09, 9.31, 10.33, 10.58, 11.14], [7.1, 8.15, 8.18, 9.47, 9.46, 10.16], [7.76, 8.75, 8.63, 10.1, 9.89, 10.7], [5.95, 6.91, 6.95, 8.21, 8.21, 8.88]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 7.92), ('CB', 'ASN', 'CG', 'HIS', 9.09), ('CB', 'ASN', 'ND1', 'HIS', 9.31), ('CB', 'ASN', 'CD2', 'HIS', 10.33), ('CB', 'ASN', 'CE1', 'HIS', 10.58), ('CB', 'ASN', 'NE2', 'HIS', 11.14)], [('CG', 'ASN', 'CB', 'HIS', 7.1), ('CG', 'ASN', 'CG', 'HIS', 8.15), ('CG', 'ASN', 'ND1', 'HIS', 8.18), ('CG', 'ASN', 'CD2', 'HIS', 9.47), ('CG', 'ASN', 'CE1', 'HIS', 9.46), ('CG', 'ASN', 'NE2', 'HIS', 10.16)], [('OD1', 'ASN', 'CB', 'HIS', 7.76), ('OD1', 'ASN', 'CG', 'HIS', 8.75), ('OD1', 'ASN', 'ND1', 'HIS', 8.63), ('OD1', 'ASN', 'CD2', 'HIS', 10.1), ('OD1', 'ASN', 'CE1', 'HIS', 9.89), ('OD1', 'ASN', 'NE2', 'HIS', 10.7)], [('ND2', 'ASN', 'CB', 'HIS', 5.95), ('ND2', 'ASN', 'CG', 'HIS', 6.91), ('ND2', 'ASN', 'ND1', 'HIS', 6.95), ('ND2', 'ASN', 'CD2', 'HIS', 8.21), ('ND2', 'ASN', 'CE1', 'HIS', 8.21), ('ND2', 'ASN', 'NE2', 'HIS', 8.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'P_1njs_2_1_2_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_THR, d, 'P_1njs_2_1_2_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_ASP, d, 'P_1njs_2_1_2_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_THR, d, 'P_1njs_2_1_2_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_ASP, d, 'P_1njs_2_1_2_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASN_HIS, d, 'P_1njs_2_1_2_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'HIS_THR' :  match2,
		'THR_ASP' :  match3,
		'ASN_THR' :  match4,
		'ASN_ASP' :  match5,
		'ASN_HIS' :  match6}