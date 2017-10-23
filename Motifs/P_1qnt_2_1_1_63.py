'''
FUNC:P_1qnt_2_1_1_63
PDB:1qnt
EC:2.1.1.63
RESI:asn,cys,his,glu
LOCI:a-137,145,146,172;
'''
import motifFunctions as cmd
ASN_GLU = { 
	'distances':
		[[19.1, 18.09, 16.77, 16.8, 15.78], [18.25, 17.17, 15.84, 15.91, 14.82], [18.83, 17.69, 16.37, 16.46, 15.33], [16.94, 15.87, 14.55, 14.64, 13.52]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLU', 19.1), ('CB', 'ASN', 'CG', 'GLU', 18.09), ('CB', 'ASN', 'CD', 'GLU', 16.77), ('CB', 'ASN', 'OE1', 'GLU', 16.8), ('CB', 'ASN', 'OE2', 'GLU', 15.78)], [('CG', 'ASN', 'CB', 'GLU', 18.25), ('CG', 'ASN', 'CG', 'GLU', 17.17), ('CG', 'ASN', 'CD', 'GLU', 15.84), ('CG', 'ASN', 'OE1', 'GLU', 15.91), ('CG', 'ASN', 'OE2', 'GLU', 14.82)], [('OD1', 'ASN', 'CB', 'GLU', 18.83), ('OD1', 'ASN', 'CG', 'GLU', 17.69), ('OD1', 'ASN', 'CD', 'GLU', 16.37), ('OD1', 'ASN', 'OE1', 'GLU', 16.46), ('OD1', 'ASN', 'OE2', 'GLU', 15.33)], [('ND2', 'ASN', 'CB', 'GLU', 16.94), ('ND2', 'ASN', 'CG', 'GLU', 15.87), ('ND2', 'ASN', 'CD', 'GLU', 14.55), ('ND2', 'ASN', 'OE1', 'GLU', 14.64), ('ND2', 'ASN', 'OE2', 'GLU', 13.52)]]}
ASN_HIS = { 
	'distances':
		[[11.74, 12.02, 11.17, 13.24, 11.98, 13.2], [11.37, 11.43, 10.43, 12.57, 11.09, 12.36], [12.33, 12.26, 11.17, 13.34, 11.7, 13.0], [10.11, 10.12, 9.11, 11.25, 9.78, 11.04]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 11.74), ('CB', 'ASN', 'CG', 'HIS', 12.02), ('CB', 'ASN', 'ND1', 'HIS', 11.17), ('CB', 'ASN', 'CD2', 'HIS', 13.24), ('CB', 'ASN', 'CE1', 'HIS', 11.98), ('CB', 'ASN', 'NE2', 'HIS', 13.2)], [('CG', 'ASN', 'CB', 'HIS', 11.37), ('CG', 'ASN', 'CG', 'HIS', 11.43), ('CG', 'ASN', 'ND1', 'HIS', 10.43), ('CG', 'ASN', 'CD2', 'HIS', 12.57), ('CG', 'ASN', 'CE1', 'HIS', 11.09), ('CG', 'ASN', 'NE2', 'HIS', 12.36)], [('OD1', 'ASN', 'CB', 'HIS', 12.33), ('OD1', 'ASN', 'CG', 'HIS', 12.26), ('OD1', 'ASN', 'ND1', 'HIS', 11.17), ('OD1', 'ASN', 'CD2', 'HIS', 13.34), ('OD1', 'ASN', 'CE1', 'HIS', 11.7), ('OD1', 'ASN', 'NE2', 'HIS', 13.0)], [('ND2', 'ASN', 'CB', 'HIS', 10.11), ('ND2', 'ASN', 'CG', 'HIS', 10.12), ('ND2', 'ASN', 'ND1', 'HIS', 9.11), ('ND2', 'ASN', 'CD2', 'HIS', 11.25), ('ND2', 'ASN', 'CE1', 'HIS', 9.78), ('ND2', 'ASN', 'NE2', 'HIS', 11.04)]]}
ASN_CYS = { 
	'distances':
		[[6.76, 6.43], [6.81, 6.35], [7.92, 7.49], [5.93, 5.32]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 6.76), ('CB', 'ASN', 'SG', 'CYS', 6.43)], [('CG', 'ASN', 'CB', 'CYS', 6.81), ('CG', 'ASN', 'SG', 'CYS', 6.35)], [('OD1', 'ASN', 'CB', 'CYS', 7.92), ('OD1', 'ASN', 'SG', 'CYS', 7.49)], [('ND2', 'ASN', 'CB', 'CYS', 5.93), ('ND2', 'ASN', 'SG', 'CYS', 5.32)]]}
HIS_GLU = { 
	'distances':
		[[10.48, 9.89, 8.87, 9.0, 8.21], [9.47, 8.71, 7.61, 7.81, 6.85], [10.03, 9.07, 7.86, 8.1, 6.92], [8.12, 7.38, 6.3, 6.54, 5.62], [9.2, 8.12, 6.87, 7.18, 5.83], [7.95, 6.94, 5.73, 6.07, 4.79]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 10.48), ('CB', 'HIS', 'CG', 'GLU', 9.89), ('CB', 'HIS', 'CD', 'GLU', 8.87), ('CB', 'HIS', 'OE1', 'GLU', 9.0), ('CB', 'HIS', 'OE2', 'GLU', 8.21)], [('CG', 'HIS', 'CB', 'GLU', 9.47), ('CG', 'HIS', 'CG', 'GLU', 8.71), ('CG', 'HIS', 'CD', 'GLU', 7.61), ('CG', 'HIS', 'OE1', 'GLU', 7.81), ('CG', 'HIS', 'OE2', 'GLU', 6.85)], [('ND1', 'HIS', 'CB', 'GLU', 10.03), ('ND1', 'HIS', 'CG', 'GLU', 9.07), ('ND1', 'HIS', 'CD', 'GLU', 7.86), ('ND1', 'HIS', 'OE1', 'GLU', 8.1), ('ND1', 'HIS', 'OE2', 'GLU', 6.92)], [('CD2', 'HIS', 'CB', 'GLU', 8.12), ('CD2', 'HIS', 'CG', 'GLU', 7.38), ('CD2', 'HIS', 'CD', 'GLU', 6.3), ('CD2', 'HIS', 'OE1', 'GLU', 6.54), ('CD2', 'HIS', 'OE2', 'GLU', 5.62)], [('CE1', 'HIS', 'CB', 'GLU', 9.2), ('CE1', 'HIS', 'CG', 'GLU', 8.12), ('CE1', 'HIS', 'CD', 'GLU', 6.87), ('CE1', 'HIS', 'OE1', 'GLU', 7.18), ('CE1', 'HIS', 'OE2', 'GLU', 5.83)], [('NE2', 'HIS', 'CB', 'GLU', 7.95), ('NE2', 'HIS', 'CG', 'GLU', 6.94), ('NE2', 'HIS', 'CD', 'GLU', 5.73), ('NE2', 'HIS', 'OE1', 'GLU', 6.07), ('NE2', 'HIS', 'OE2', 'GLU', 4.79)]]}
CYS_HIS = { 
	'distances':
		[[7.63, 8.12, 7.65, 9.35, 8.69, 9.63], [7.35, 7.84, 7.26, 9.14, 8.36, 9.39]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 7.63), ('CB', 'CYS', 'CG', 'HIS', 8.12), ('CB', 'CYS', 'ND1', 'HIS', 7.65), ('CB', 'CYS', 'CD2', 'HIS', 9.35), ('CB', 'CYS', 'CE1', 'HIS', 8.69), ('CB', 'CYS', 'NE2', 'HIS', 9.63)], [('SG', 'CYS', 'CB', 'HIS', 7.35), ('SG', 'CYS', 'CG', 'HIS', 7.84), ('SG', 'CYS', 'ND1', 'HIS', 7.26), ('SG', 'CYS', 'CD2', 'HIS', 9.14), ('SG', 'CYS', 'CE1', 'HIS', 8.36), ('SG', 'CYS', 'NE2', 'HIS', 9.39)]]}
CYS_GLU = { 
	'distances':
		[[15.23, 14.48, 13.13, 12.99, 12.34], [15.21, 14.33, 13.07, 13.14, 12.15]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 15.23), ('CB', 'CYS', 'CG', 'GLU', 14.48), ('CB', 'CYS', 'CD', 'GLU', 13.13), ('CB', 'CYS', 'OE1', 'GLU', 12.99), ('CB', 'CYS', 'OE2', 'GLU', 12.34)], [('SG', 'CYS', 'CB', 'GLU', 15.21), ('SG', 'CYS', 'CG', 'GLU', 14.33), ('SG', 'CYS', 'CD', 'GLU', 13.07), ('SG', 'CYS', 'OE1', 'GLU', 13.14), ('SG', 'CYS', 'OE2', 'GLU', 12.15)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLU, d, 'P_1qnt_2_1_1_63')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_HIS, d, 'P_1qnt_2_1_1_63')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_CYS, d, 'P_1qnt_2_1_1_63')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'P_1qnt_2_1_1_63')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_HIS, d, 'P_1qnt_2_1_1_63')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_GLU, d, 'P_1qnt_2_1_1_63')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLU' :  match1,
		'ASN_HIS' :  match2,
		'ASN_CYS' :  match3,
		'HIS_GLU' :  match4,
		'CYS_HIS' :  match5,
		'CYS_GLU' :  match6}