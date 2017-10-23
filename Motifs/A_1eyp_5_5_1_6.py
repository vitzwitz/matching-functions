'''
FUNC:A_1eyp_5_5_1_6
PDB:1eyp
EC:5.5.1.6
RESI:thr,tyr,asn,thr
LOCI:a-48,106,113,190;
'''
import motifFunctions as cmd
THR_TYR = { 
	'distances':
		[[15.62, 14.47, 13.92, 14.07, 12.93, 13.1, 12.5, 11.7], [14.56, 13.34, 12.79, 12.89, 11.74, 11.86, 11.24, 10.37], [16.03, 14.93, 14.53, 14.43, 13.61, 13.5, 13.07, 12.33], [9.5, 8.75, 7.5, 9.57, 7.16, 9.34, 8.21, 8.37], [9.63, 8.75, 7.39, 9.52, 6.86, 9.15, 7.89, 7.9], [8.23, 7.69, 6.52, 8.67, 6.54, 8.69, 7.73, 8.21]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'TYR', 15.62), ('CB', 'THR', 'CG', 'TYR', 14.47), ('CB', 'THR', 'CD1', 'TYR', 13.92), ('CB', 'THR', 'CD2', 'TYR', 14.07), ('CB', 'THR', 'CE1', 'TYR', 12.93), ('CB', 'THR', 'CE2', 'TYR', 13.1), ('CB', 'THR', 'CZ', 'TYR', 12.5), ('CB', 'THR', 'OH', 'TYR', 11.7)], [('OG1', 'THR', 'CB', 'TYR', 14.56), ('OG1', 'THR', 'CG', 'TYR', 13.34), ('OG1', 'THR', 'CD1', 'TYR', 12.79), ('OG1', 'THR', 'CD2', 'TYR', 12.89), ('OG1', 'THR', 'CE1', 'TYR', 11.74), ('OG1', 'THR', 'CE2', 'TYR', 11.86), ('OG1', 'THR', 'CZ', 'TYR', 11.24), ('OG1', 'THR', 'OH', 'TYR', 10.37)], [('CG2', 'THR', 'CB', 'TYR', 16.03), ('CG2', 'THR', 'CG', 'TYR', 14.93), ('CG2', 'THR', 'CD1', 'TYR', 14.53), ('CG2', 'THR', 'CD2', 'TYR', 14.43), ('CG2', 'THR', 'CE1', 'TYR', 13.61), ('CG2', 'THR', 'CE2', 'TYR', 13.5), ('CG2', 'THR', 'CZ', 'TYR', 13.07), ('CG2', 'THR', 'OH', 'TYR', 12.33)], [('CB', 'THR', 'CB', 'TYR', 9.5), ('CB', 'THR', 'CG', 'TYR', 8.75), ('CB', 'THR', 'CD1', 'TYR', 7.5), ('CB', 'THR', 'CD2', 'TYR', 9.57), ('CB', 'THR', 'CE1', 'TYR', 7.16), ('CB', 'THR', 'CE2', 'TYR', 9.34), ('CB', 'THR', 'CZ', 'TYR', 8.21), ('CB', 'THR', 'OH', 'TYR', 8.37)], [('OG1', 'THR', 'CB', 'TYR', 9.63), ('OG1', 'THR', 'CG', 'TYR', 8.75), ('OG1', 'THR', 'CD1', 'TYR', 7.39), ('OG1', 'THR', 'CD2', 'TYR', 9.52), ('OG1', 'THR', 'CE1', 'TYR', 6.86), ('OG1', 'THR', 'CE2', 'TYR', 9.15), ('OG1', 'THR', 'CZ', 'TYR', 7.89), ('OG1', 'THR', 'OH', 'TYR', 7.9)], [('CG2', 'THR', 'CB', 'TYR', 8.23), ('CG2', 'THR', 'CG', 'TYR', 7.69), ('CG2', 'THR', 'CD1', 'TYR', 6.52), ('CG2', 'THR', 'CD2', 'TYR', 8.67), ('CG2', 'THR', 'CE1', 'TYR', 6.54), ('CG2', 'THR', 'CE2', 'TYR', 8.69), ('CG2', 'THR', 'CZ', 'TYR', 7.73), ('CG2', 'THR', 'OH', 'TYR', 8.21)]]}
ASN_TYR = { 
	'distances':
		[[14.35, 13.54, 13.18, 13.31, 12.6, 12.74, 12.37, 12.05], [13.88, 13.16, 12.71, 13.12, 12.22, 12.64, 12.19, 11.98], [14.57, 13.95, 13.51, 13.99, 13.12, 13.61, 13.17, 13.04], [12.88, 12.11, 11.57, 12.14, 11.05, 11.65, 11.09, 10.88]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 14.35), ('CB', 'ASN', 'CG', 'TYR', 13.54), ('CB', 'ASN', 'CD1', 'TYR', 13.18), ('CB', 'ASN', 'CD2', 'TYR', 13.31), ('CB', 'ASN', 'CE1', 'TYR', 12.6), ('CB', 'ASN', 'CE2', 'TYR', 12.74), ('CB', 'ASN', 'CZ', 'TYR', 12.37), ('CB', 'ASN', 'OH', 'TYR', 12.05)], [('CG', 'ASN', 'CB', 'TYR', 13.88), ('CG', 'ASN', 'CG', 'TYR', 13.16), ('CG', 'ASN', 'CD1', 'TYR', 12.71), ('CG', 'ASN', 'CD2', 'TYR', 13.12), ('CG', 'ASN', 'CE1', 'TYR', 12.22), ('CG', 'ASN', 'CE2', 'TYR', 12.64), ('CG', 'ASN', 'CZ', 'TYR', 12.19), ('CG', 'ASN', 'OH', 'TYR', 11.98)], [('OD1', 'ASN', 'CB', 'TYR', 14.57), ('OD1', 'ASN', 'CG', 'TYR', 13.95), ('OD1', 'ASN', 'CD1', 'TYR', 13.51), ('OD1', 'ASN', 'CD2', 'TYR', 13.99), ('OD1', 'ASN', 'CE1', 'TYR', 13.12), ('OD1', 'ASN', 'CE2', 'TYR', 13.61), ('OD1', 'ASN', 'CZ', 'TYR', 13.17), ('OD1', 'ASN', 'OH', 'TYR', 13.04)], [('ND2', 'ASN', 'CB', 'TYR', 12.88), ('ND2', 'ASN', 'CG', 'TYR', 12.11), ('ND2', 'ASN', 'CD1', 'TYR', 11.57), ('ND2', 'ASN', 'CD2', 'TYR', 12.14), ('ND2', 'ASN', 'CE1', 'TYR', 11.05), ('ND2', 'ASN', 'CE2', 'TYR', 11.65), ('ND2', 'ASN', 'CZ', 'TYR', 11.09), ('ND2', 'ASN', 'OH', 'TYR', 10.88)]]}
THR_ASN = { 
	'distances':
		[[5.93, 6.81, 7.77, 6.86], [6.46, 7.23, 8.35, 6.97], [5.7, 6.95, 7.86, 7.32], [15.8, 15.12, 15.87, 13.79], [14.55, 13.85, 14.6, 12.51], [15.78, 15.07, 15.78, 13.76]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASN', 5.93), ('CB', 'THR', 'CG', 'ASN', 6.81), ('CB', 'THR', 'OD1', 'ASN', 7.77), ('CB', 'THR', 'ND2', 'ASN', 6.86)], [('OG1', 'THR', 'CB', 'ASN', 6.46), ('OG1', 'THR', 'CG', 'ASN', 7.23), ('OG1', 'THR', 'OD1', 'ASN', 8.35), ('OG1', 'THR', 'ND2', 'ASN', 6.97)], [('CG2', 'THR', 'CB', 'ASN', 5.7), ('CG2', 'THR', 'CG', 'ASN', 6.95), ('CG2', 'THR', 'OD1', 'ASN', 7.86), ('CG2', 'THR', 'ND2', 'ASN', 7.32)], [('CB', 'THR', 'CB', 'ASN', 15.8), ('CB', 'THR', 'CG', 'ASN', 15.12), ('CB', 'THR', 'OD1', 'ASN', 15.87), ('CB', 'THR', 'ND2', 'ASN', 13.79)], [('OG1', 'THR', 'CB', 'ASN', 14.55), ('OG1', 'THR', 'CG', 'ASN', 13.85), ('OG1', 'THR', 'OD1', 'ASN', 14.6), ('OG1', 'THR', 'ND2', 'ASN', 12.51)], [('CG2', 'THR', 'CB', 'ASN', 15.78), ('CG2', 'THR', 'CG', 'ASN', 15.07), ('CG2', 'THR', 'OD1', 'ASN', 15.78), ('CG2', 'THR', 'ND2', 'ASN', 13.76)]]}
THR_THR = { 
	'distances':
		[[15.53, 14.24, 15.89], [14.43, 13.18, 14.79], [16.64, 15.38, 16.89], [15.53, 14.43, 16.64], [14.24, 13.18, 15.38], [15.89, 14.79, 16.89]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'THR', 15.53), ('CB', 'THR', 'OG1', 'THR', 14.24), ('CB', 'THR', 'CG2', 'THR', 15.89)], [('OG1', 'THR', 'CB', 'THR', 14.43), ('OG1', 'THR', 'OG1', 'THR', 13.18), ('OG1', 'THR', 'CG2', 'THR', 14.79)], [('CG2', 'THR', 'CB', 'THR', 16.64), ('CG2', 'THR', 'OG1', 'THR', 15.38), ('CG2', 'THR', 'CG2', 'THR', 16.89)], [('CB', 'THR', 'CB', 'THR', 15.53), ('CB', 'THR', 'OG1', 'THR', 14.43), ('CB', 'THR', 'CG2', 'THR', 16.64)], [('OG1', 'THR', 'CB', 'THR', 14.24), ('OG1', 'THR', 'OG1', 'THR', 13.18), ('OG1', 'THR', 'CG2', 'THR', 15.38)], [('CG2', 'THR', 'CB', 'THR', 15.89), ('CG2', 'THR', 'OG1', 'THR', 14.79), ('CG2', 'THR', 'CG2', 'THR', 16.89)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_TYR, d, 'A_1eyp_5_5_1_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_TYR, d, 'A_1eyp_5_5_1_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_ASN, d, 'A_1eyp_5_5_1_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_THR, d, 'A_1eyp_5_5_1_6')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_TYR' :  match1,
		'ASN_TYR' :  match2,
		'THR_ASN' :  match3,
		'THR_THR' :  match4}