'''
FUNC:A_1eh6_2_1_1_63
PDB:1eh6
EC:2.1.1.63
RESI:asn,cys,his,glu
LOCI:a-137,145,146,172;
'''
import motifFunctions as cmd
ASN_GLU = { 
	'distances':
		[[19.19, 18.11, 16.85, 16.92, 15.87], [18.34, 17.2, 15.92, 16.04, 14.9], [18.93, 17.75, 16.47, 16.59, 15.41], [17.03, 15.89, 14.63, 14.75, 13.6]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLU', 19.19), ('CB', 'ASN', 'CG', 'GLU', 18.11), ('CB', 'ASN', 'CD', 'GLU', 16.85), ('CB', 'ASN', 'OE1', 'GLU', 16.92), ('CB', 'ASN', 'OE2', 'GLU', 15.87)], [('CG', 'ASN', 'CB', 'GLU', 18.34), ('CG', 'ASN', 'CG', 'GLU', 17.2), ('CG', 'ASN', 'CD', 'GLU', 15.92), ('CG', 'ASN', 'OE1', 'GLU', 16.04), ('CG', 'ASN', 'OE2', 'GLU', 14.9)], [('OD1', 'ASN', 'CB', 'GLU', 18.93), ('OD1', 'ASN', 'CG', 'GLU', 17.75), ('OD1', 'ASN', 'CD', 'GLU', 16.47), ('OD1', 'ASN', 'OE1', 'GLU', 16.59), ('OD1', 'ASN', 'OE2', 'GLU', 15.41)], [('ND2', 'ASN', 'CB', 'GLU', 17.03), ('ND2', 'ASN', 'CG', 'GLU', 15.89), ('ND2', 'ASN', 'CD', 'GLU', 14.63), ('ND2', 'ASN', 'OE1', 'GLU', 14.75), ('ND2', 'ASN', 'OE2', 'GLU', 13.6)]]}
CYS_ASN = { 
	'distances':
		[[6.83, 6.78, 7.89, 5.82], [6.7, 6.53, 7.65, 5.45]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASN', 6.83), ('CB', 'CYS', 'CG', 'ASN', 6.78), ('CB', 'CYS', 'OD1', 'ASN', 7.89), ('CB', 'CYS', 'ND2', 'ASN', 5.82)], [('SG', 'CYS', 'CB', 'ASN', 6.7), ('SG', 'CYS', 'CG', 'ASN', 6.53), ('SG', 'CYS', 'OD1', 'ASN', 7.65), ('SG', 'CYS', 'ND2', 'ASN', 5.45)]]}
ASN_HIS = { 
	'distances':
		[[11.89, 12.19, 11.35, 13.41, 12.18, 13.4], [11.49, 11.57, 10.59, 12.73, 11.28, 12.55], [12.44, 12.4, 11.32, 13.49, 11.9, 13.19], [10.22, 10.26, 9.26, 11.4, 9.97, 11.23]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 11.89), ('CB', 'ASN', 'CG', 'HIS', 12.19), ('CB', 'ASN', 'ND1', 'HIS', 11.35), ('CB', 'ASN', 'CD2', 'HIS', 13.41), ('CB', 'ASN', 'CE1', 'HIS', 12.18), ('CB', 'ASN', 'NE2', 'HIS', 13.4)], [('CG', 'ASN', 'CB', 'HIS', 11.49), ('CG', 'ASN', 'CG', 'HIS', 11.57), ('CG', 'ASN', 'ND1', 'HIS', 10.59), ('CG', 'ASN', 'CD2', 'HIS', 12.73), ('CG', 'ASN', 'CE1', 'HIS', 11.28), ('CG', 'ASN', 'NE2', 'HIS', 12.55)], [('OD1', 'ASN', 'CB', 'HIS', 12.44), ('OD1', 'ASN', 'CG', 'HIS', 12.4), ('OD1', 'ASN', 'ND1', 'HIS', 11.32), ('OD1', 'ASN', 'CD2', 'HIS', 13.49), ('OD1', 'ASN', 'CE1', 'HIS', 11.9), ('OD1', 'ASN', 'NE2', 'HIS', 13.19)], [('ND2', 'ASN', 'CB', 'HIS', 10.22), ('ND2', 'ASN', 'CG', 'HIS', 10.26), ('ND2', 'ASN', 'ND1', 'HIS', 9.26), ('ND2', 'ASN', 'CD2', 'HIS', 11.4), ('ND2', 'ASN', 'CE1', 'HIS', 9.97), ('ND2', 'ASN', 'NE2', 'HIS', 11.23)]]}
HIS_GLU = { 
	'distances':
		[[10.38, 9.63, 8.76, 8.97, 8.15], [9.38, 8.48, 7.51, 7.79, 6.78], [9.98, 8.9, 7.81, 8.14, 6.87], [8.03, 7.15, 6.2, 6.51, 5.59], [9.13, 7.94, 6.79, 7.18, 5.75], [7.84, 6.74, 5.61, 6.02, 4.71]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 10.38), ('CB', 'HIS', 'CG', 'GLU', 9.63), ('CB', 'HIS', 'CD', 'GLU', 8.76), ('CB', 'HIS', 'OE1', 'GLU', 8.97), ('CB', 'HIS', 'OE2', 'GLU', 8.15)], [('CG', 'HIS', 'CB', 'GLU', 9.38), ('CG', 'HIS', 'CG', 'GLU', 8.48), ('CG', 'HIS', 'CD', 'GLU', 7.51), ('CG', 'HIS', 'OE1', 'GLU', 7.79), ('CG', 'HIS', 'OE2', 'GLU', 6.78)], [('ND1', 'HIS', 'CB', 'GLU', 9.98), ('ND1', 'HIS', 'CG', 'GLU', 8.9), ('ND1', 'HIS', 'CD', 'GLU', 7.81), ('ND1', 'HIS', 'OE1', 'GLU', 8.14), ('ND1', 'HIS', 'OE2', 'GLU', 6.87)], [('CD2', 'HIS', 'CB', 'GLU', 8.03), ('CD2', 'HIS', 'CG', 'GLU', 7.15), ('CD2', 'HIS', 'CD', 'GLU', 6.2), ('CD2', 'HIS', 'OE1', 'GLU', 6.51), ('CD2', 'HIS', 'OE2', 'GLU', 5.59)], [('CE1', 'HIS', 'CB', 'GLU', 9.13), ('CE1', 'HIS', 'CG', 'GLU', 7.94), ('CE1', 'HIS', 'CD', 'GLU', 6.79), ('CE1', 'HIS', 'OE1', 'GLU', 7.18), ('CE1', 'HIS', 'OE2', 'GLU', 5.75)], [('NE2', 'HIS', 'CB', 'GLU', 7.84), ('NE2', 'HIS', 'CG', 'GLU', 6.74), ('NE2', 'HIS', 'CD', 'GLU', 5.61), ('NE2', 'HIS', 'OE1', 'GLU', 6.02), ('NE2', 'HIS', 'OE2', 'GLU', 4.71)]]}
CYS_HIS = { 
	'distances':
		[[7.59, 8.06, 7.59, 9.26, 8.61, 9.55], [7.22, 7.71, 7.13, 9.01, 8.24, 9.29]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 7.59), ('CB', 'CYS', 'CG', 'HIS', 8.06), ('CB', 'CYS', 'ND1', 'HIS', 7.59), ('CB', 'CYS', 'CD2', 'HIS', 9.26), ('CB', 'CYS', 'CE1', 'HIS', 8.61), ('CB', 'CYS', 'NE2', 'HIS', 9.55)], [('SG', 'CYS', 'CB', 'HIS', 7.22), ('SG', 'CYS', 'CG', 'HIS', 7.71), ('SG', 'CYS', 'ND1', 'HIS', 7.13), ('SG', 'CYS', 'CD2', 'HIS', 9.01), ('SG', 'CYS', 'CE1', 'HIS', 8.24), ('SG', 'CYS', 'NE2', 'HIS', 9.29)]]}
CYS_GLU = { 
	'distances':
		[[15.06, 14.2, 12.94, 12.87, 12.15], [14.99, 14.0, 12.85, 12.99, 11.95]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 15.06), ('CB', 'CYS', 'CG', 'GLU', 14.2), ('CB', 'CYS', 'CD', 'GLU', 12.94), ('CB', 'CYS', 'OE1', 'GLU', 12.87), ('CB', 'CYS', 'OE2', 'GLU', 12.15)], [('SG', 'CYS', 'CB', 'GLU', 14.99), ('SG', 'CYS', 'CG', 'GLU', 14.0), ('SG', 'CYS', 'CD', 'GLU', 12.85), ('SG', 'CYS', 'OE1', 'GLU', 12.99), ('SG', 'CYS', 'OE2', 'GLU', 11.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLU, d, 'A_1eh6_2_1_1_63')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_ASN, d, 'A_1eh6_2_1_1_63')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_HIS, d, 'A_1eh6_2_1_1_63')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'A_1eh6_2_1_1_63')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_HIS, d, 'A_1eh6_2_1_1_63')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_GLU, d, 'A_1eh6_2_1_1_63')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLU' :  match1,
		'CYS_ASN' :  match2,
		'ASN_HIS' :  match3,
		'HIS_GLU' :  match4,
		'CYS_HIS' :  match5,
		'CYS_GLU' :  match6}