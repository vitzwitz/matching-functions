'''
FUNC:A_1ybv_1_1_1_252
PDB:1ybv
EC:1.1.1.252
RESI:asn,ser,tyr,lys
LOCI:a-138,164,178,182;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[9.69, 8.43, 8.49, 7.47, 7.66, 6.44, 6.56, 6.02], [9.53, 8.29, 8.55, 7.12, 7.78, 6.08, 6.5, 6.02]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 9.69), ('CB', 'SER', 'CG', 'TYR', 8.43), ('CB', 'SER', 'CD1', 'TYR', 8.49), ('CB', 'SER', 'CD2', 'TYR', 7.47), ('CB', 'SER', 'CE1', 'TYR', 7.66), ('CB', 'SER', 'CE2', 'TYR', 6.44), ('CB', 'SER', 'CZ', 'TYR', 6.56), ('CB', 'SER', 'OH', 'TYR', 6.02)], [('OG', 'SER', 'CB', 'TYR', 9.53), ('OG', 'SER', 'CG', 'TYR', 8.29), ('OG', 'SER', 'CD1', 'TYR', 8.55), ('OG', 'SER', 'CD2', 'TYR', 7.12), ('OG', 'SER', 'CE1', 'TYR', 7.78), ('OG', 'SER', 'CE2', 'TYR', 6.08), ('OG', 'SER', 'CZ', 'TYR', 6.5), ('OG', 'SER', 'OH', 'TYR', 6.02)]]}
SER_LYS = { 
	'distances':
		[[6.04, 5.74, 6.33, 6.42, 7.46], [7.05, 6.69, 7.47, 7.41, 8.52]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 6.04), ('CB', 'SER', 'CG', 'LYS', 5.74), ('CB', 'SER', 'CD', 'LYS', 6.33), ('CB', 'SER', 'CE', 'LYS', 6.42), ('CB', 'SER', 'NZ', 'LYS', 7.46)], [('OG', 'SER', 'CB', 'LYS', 7.05), ('OG', 'SER', 'CG', 'LYS', 6.69), ('OG', 'SER', 'CD', 'LYS', 7.47), ('OG', 'SER', 'CE', 'LYS', 7.41), ('OG', 'SER', 'NZ', 'LYS', 8.52)]]}
TYR_ASN = { 
	'distances':
		[[9.23, 8.52, 9.26, 7.26], [8.8, 7.94, 8.63, 6.62], [7.75, 6.73, 7.32, 5.44], [9.72, 8.89, 9.57, 7.57], [7.79, 6.67, 7.13, 5.48], [9.76, 8.85, 9.45, 7.6], [8.86, 7.84, 8.31, 6.67], [9.31, 8.28, 8.61, 7.28]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASN', 9.23), ('CB', 'TYR', 'CG', 'ASN', 8.52), ('CB', 'TYR', 'OD1', 'ASN', 9.26), ('CB', 'TYR', 'ND2', 'ASN', 7.26)], [('CG', 'TYR', 'CB', 'ASN', 8.8), ('CG', 'TYR', 'CG', 'ASN', 7.94), ('CG', 'TYR', 'OD1', 'ASN', 8.63), ('CG', 'TYR', 'ND2', 'ASN', 6.62)], [('CD1', 'TYR', 'CB', 'ASN', 7.75), ('CD1', 'TYR', 'CG', 'ASN', 6.73), ('CD1', 'TYR', 'OD1', 'ASN', 7.32), ('CD1', 'TYR', 'ND2', 'ASN', 5.44)], [('CD2', 'TYR', 'CB', 'ASN', 9.72), ('CD2', 'TYR', 'CG', 'ASN', 8.89), ('CD2', 'TYR', 'OD1', 'ASN', 9.57), ('CD2', 'TYR', 'ND2', 'ASN', 7.57)], [('CE1', 'TYR', 'CB', 'ASN', 7.79), ('CE1', 'TYR', 'CG', 'ASN', 6.67), ('CE1', 'TYR', 'OD1', 'ASN', 7.13), ('CE1', 'TYR', 'ND2', 'ASN', 5.48)], [('CE2', 'TYR', 'CB', 'ASN', 9.76), ('CE2', 'TYR', 'CG', 'ASN', 8.85), ('CE2', 'TYR', 'OD1', 'ASN', 9.45), ('CE2', 'TYR', 'ND2', 'ASN', 7.6)], [('CZ', 'TYR', 'CB', 'ASN', 8.86), ('CZ', 'TYR', 'CG', 'ASN', 7.84), ('CZ', 'TYR', 'OD1', 'ASN', 8.31), ('CZ', 'TYR', 'ND2', 'ASN', 6.67)], [('OH', 'TYR', 'CB', 'ASN', 9.31), ('OH', 'TYR', 'CG', 'ASN', 8.28), ('OH', 'TYR', 'OD1', 'ASN', 8.61), ('OH', 'TYR', 'ND2', 'ASN', 7.28)]]}
LYS_TYR = { 
	'distances':
		[[8.63, 7.85, 7.86, 7.58, 7.62, 7.33, 7.35, 7.6], [7.81, 6.83, 6.61, 6.65, 6.21, 6.25, 6.02, 6.27], [8.79, 7.73, 7.17, 7.72, 6.54, 7.17, 6.55, 6.51], [8.76, 7.52, 6.7, 7.53, 5.77, 6.76, 5.81, 5.52], [10.05, 8.83, 7.85, 8.92, 6.87, 8.12, 7.03, 6.54]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 8.63), ('CB', 'LYS', 'CG', 'TYR', 7.85), ('CB', 'LYS', 'CD1', 'TYR', 7.86), ('CB', 'LYS', 'CD2', 'TYR', 7.58), ('CB', 'LYS', 'CE1', 'TYR', 7.62), ('CB', 'LYS', 'CE2', 'TYR', 7.33), ('CB', 'LYS', 'CZ', 'TYR', 7.35), ('CB', 'LYS', 'OH', 'TYR', 7.6)], [('CG', 'LYS', 'CB', 'TYR', 7.81), ('CG', 'LYS', 'CG', 'TYR', 6.83), ('CG', 'LYS', 'CD1', 'TYR', 6.61), ('CG', 'LYS', 'CD2', 'TYR', 6.65), ('CG', 'LYS', 'CE1', 'TYR', 6.21), ('CG', 'LYS', 'CE2', 'TYR', 6.25), ('CG', 'LYS', 'CZ', 'TYR', 6.02), ('CG', 'LYS', 'OH', 'TYR', 6.27)], [('CD', 'LYS', 'CB', 'TYR', 8.79), ('CD', 'LYS', 'CG', 'TYR', 7.73), ('CD', 'LYS', 'CD1', 'TYR', 7.17), ('CD', 'LYS', 'CD2', 'TYR', 7.72), ('CD', 'LYS', 'CE1', 'TYR', 6.54), ('CD', 'LYS', 'CE2', 'TYR', 7.17), ('CD', 'LYS', 'CZ', 'TYR', 6.55), ('CD', 'LYS', 'OH', 'TYR', 6.51)], [('CE', 'LYS', 'CB', 'TYR', 8.76), ('CE', 'LYS', 'CG', 'TYR', 7.52), ('CE', 'LYS', 'CD1', 'TYR', 6.7), ('CE', 'LYS', 'CD2', 'TYR', 7.53), ('CE', 'LYS', 'CE1', 'TYR', 5.77), ('CE', 'LYS', 'CE2', 'TYR', 6.76), ('CE', 'LYS', 'CZ', 'TYR', 5.81), ('CE', 'LYS', 'OH', 'TYR', 5.52)], [('NZ', 'LYS', 'CB', 'TYR', 10.05), ('NZ', 'LYS', 'CG', 'TYR', 8.83), ('NZ', 'LYS', 'CD1', 'TYR', 7.85), ('NZ', 'LYS', 'CD2', 'TYR', 8.92), ('NZ', 'LYS', 'CE1', 'TYR', 6.87), ('NZ', 'LYS', 'CE2', 'TYR', 8.12), ('NZ', 'LYS', 'CZ', 'TYR', 7.03), ('NZ', 'LYS', 'OH', 'TYR', 6.54)]]}
LYS_ASN = { 
	'distances':
		[[8.54, 8.69, 9.72, 7.92], [7.68, 7.56, 8.51, 6.7], [6.94, 6.88, 7.73, 6.33], [6.91, 6.45, 7.03, 5.9], [6.84, 6.46, 6.8, 6.34]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 8.54), ('CB', 'LYS', 'CG', 'ASN', 8.69), ('CB', 'LYS', 'OD1', 'ASN', 9.72), ('CB', 'LYS', 'ND2', 'ASN', 7.92)], [('CG', 'LYS', 'CB', 'ASN', 7.68), ('CG', 'LYS', 'CG', 'ASN', 7.56), ('CG', 'LYS', 'OD1', 'ASN', 8.51), ('CG', 'LYS', 'ND2', 'ASN', 6.7)], [('CD', 'LYS', 'CB', 'ASN', 6.94), ('CD', 'LYS', 'CG', 'ASN', 6.88), ('CD', 'LYS', 'OD1', 'ASN', 7.73), ('CD', 'LYS', 'ND2', 'ASN', 6.33)], [('CE', 'LYS', 'CB', 'ASN', 6.91), ('CE', 'LYS', 'CG', 'ASN', 6.45), ('CE', 'LYS', 'OD1', 'ASN', 7.03), ('CE', 'LYS', 'ND2', 'ASN', 5.9)], [('NZ', 'LYS', 'CB', 'ASN', 6.84), ('NZ', 'LYS', 'CG', 'ASN', 6.46), ('NZ', 'LYS', 'OD1', 'ASN', 6.8), ('NZ', 'LYS', 'ND2', 'ASN', 6.34)]]}
SER_ASN = { 
	'distances':
		[[11.04, 10.59, 11.26, 9.69], [11.93, 11.34, 11.97, 10.32]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 11.04), ('CB', 'SER', 'CG', 'ASN', 10.59), ('CB', 'SER', 'OD1', 'ASN', 11.26), ('CB', 'SER', 'ND2', 'ASN', 9.69)], [('OG', 'SER', 'CB', 'ASN', 11.93), ('OG', 'SER', 'CG', 'ASN', 11.34), ('OG', 'SER', 'OD1', 'ASN', 11.97), ('OG', 'SER', 'ND2', 'ASN', 10.32)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_1ybv_1_1_1_252')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_LYS, d, 'A_1ybv_1_1_1_252')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ASN, d, 'A_1ybv_1_1_1_252')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_TYR, d, 'A_1ybv_1_1_1_252')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LYS_ASN, d, 'A_1ybv_1_1_1_252')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_ASN, d, 'A_1ybv_1_1_1_252')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'SER_LYS' :  match2,
		'TYR_ASN' :  match3,
		'LYS_TYR' :  match4,
		'LYS_ASN' :  match5,
		'SER_ASN' :  match6}