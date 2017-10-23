'''
FUNC:P_1fm7_5_5_1_6
PDB:1fm7
EC:5.5.1.6
RESI:thr,tyr,asn,thr
LOCI:a-48,106,113,190;
'''
import motifFunctions as cmd
THR_TYR = { 
	'distances':
		[[9.53, 8.74, 7.44, 9.56, 7.07, 9.31, 8.14, 8.32], [9.81, 8.92, 7.53, 9.68, 6.98, 9.3, 8.03, 8.06], [8.14, 7.51, 6.27, 8.48, 6.23, 8.46, 7.45, 7.96], [15.44, 14.32, 13.78, 13.94, 12.82, 12.99, 12.4, 11.6], [14.35, 13.16, 12.63, 12.72, 11.6, 11.71, 11.11, 10.25], [15.88, 14.83, 14.44, 14.34, 13.54, 13.44, 13.02, 12.28]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'TYR', 9.53), ('CB', 'THR', 'CG', 'TYR', 8.74), ('CB', 'THR', 'CD1', 'TYR', 7.44), ('CB', 'THR', 'CD2', 'TYR', 9.56), ('CB', 'THR', 'CE1', 'TYR', 7.07), ('CB', 'THR', 'CE2', 'TYR', 9.31), ('CB', 'THR', 'CZ', 'TYR', 8.14), ('CB', 'THR', 'OH', 'TYR', 8.32)], [('OG1', 'THR', 'CB', 'TYR', 9.81), ('OG1', 'THR', 'CG', 'TYR', 8.92), ('OG1', 'THR', 'CD1', 'TYR', 7.53), ('OG1', 'THR', 'CD2', 'TYR', 9.68), ('OG1', 'THR', 'CE1', 'TYR', 6.98), ('OG1', 'THR', 'CE2', 'TYR', 9.3), ('OG1', 'THR', 'CZ', 'TYR', 8.03), ('OG1', 'THR', 'OH', 'TYR', 8.06)], [('CG2', 'THR', 'CB', 'TYR', 8.14), ('CG2', 'THR', 'CG', 'TYR', 7.51), ('CG2', 'THR', 'CD1', 'TYR', 6.27), ('CG2', 'THR', 'CD2', 'TYR', 8.48), ('CG2', 'THR', 'CE1', 'TYR', 6.23), ('CG2', 'THR', 'CE2', 'TYR', 8.46), ('CG2', 'THR', 'CZ', 'TYR', 7.45), ('CG2', 'THR', 'OH', 'TYR', 7.96)], [('CB', 'THR', 'CB', 'TYR', 15.44), ('CB', 'THR', 'CG', 'TYR', 14.32), ('CB', 'THR', 'CD1', 'TYR', 13.78), ('CB', 'THR', 'CD2', 'TYR', 13.94), ('CB', 'THR', 'CE1', 'TYR', 12.82), ('CB', 'THR', 'CE2', 'TYR', 12.99), ('CB', 'THR', 'CZ', 'TYR', 12.4), ('CB', 'THR', 'OH', 'TYR', 11.6)], [('OG1', 'THR', 'CB', 'TYR', 14.35), ('OG1', 'THR', 'CG', 'TYR', 13.16), ('OG1', 'THR', 'CD1', 'TYR', 12.63), ('OG1', 'THR', 'CD2', 'TYR', 12.72), ('OG1', 'THR', 'CE1', 'TYR', 11.6), ('OG1', 'THR', 'CE2', 'TYR', 11.71), ('OG1', 'THR', 'CZ', 'TYR', 11.11), ('OG1', 'THR', 'OH', 'TYR', 10.25)], [('CG2', 'THR', 'CB', 'TYR', 15.88), ('CG2', 'THR', 'CG', 'TYR', 14.83), ('CG2', 'THR', 'CD1', 'TYR', 14.44), ('CG2', 'THR', 'CD2', 'TYR', 14.34), ('CG2', 'THR', 'CE1', 'TYR', 13.54), ('CG2', 'THR', 'CE2', 'TYR', 13.44), ('CG2', 'THR', 'CZ', 'TYR', 13.02), ('CG2', 'THR', 'OH', 'TYR', 12.28)]]}
THR_ASN = { 
	'distances':
		[[15.31, 14.7, 15.46, 13.46], [14.14, 13.51, 14.27, 12.24], [15.12, 14.49, 15.19, 13.31], [6.0, 6.92, 7.99, 6.84], [6.44, 7.29, 8.48, 6.99], [5.77, 7.03, 7.99, 7.33]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASN', 15.31), ('CB', 'THR', 'CG', 'ASN', 14.7), ('CB', 'THR', 'OD1', 'ASN', 15.46), ('CB', 'THR', 'ND2', 'ASN', 13.46)], [('OG1', 'THR', 'CB', 'ASN', 14.14), ('OG1', 'THR', 'CG', 'ASN', 13.51), ('OG1', 'THR', 'OD1', 'ASN', 14.27), ('OG1', 'THR', 'ND2', 'ASN', 12.24)], [('CG2', 'THR', 'CB', 'ASN', 15.12), ('CG2', 'THR', 'CG', 'ASN', 14.49), ('CG2', 'THR', 'OD1', 'ASN', 15.19), ('CG2', 'THR', 'ND2', 'ASN', 13.31)], [('CB', 'THR', 'CB', 'ASN', 6.0), ('CB', 'THR', 'CG', 'ASN', 6.92), ('CB', 'THR', 'OD1', 'ASN', 7.99), ('CB', 'THR', 'ND2', 'ASN', 6.84)], [('OG1', 'THR', 'CB', 'ASN', 6.44), ('OG1', 'THR', 'CG', 'ASN', 7.29), ('OG1', 'THR', 'OD1', 'ASN', 8.48), ('OG1', 'THR', 'ND2', 'ASN', 6.99)], [('CG2', 'THR', 'CB', 'ASN', 5.77), ('CG2', 'THR', 'CG', 'ASN', 7.03), ('CG2', 'THR', 'OD1', 'ASN', 7.99), ('CG2', 'THR', 'ND2', 'ASN', 7.33)]]}
TYR_ASN = { 
	'distances':
		[[14.07, 13.69, 14.22, 12.99], [13.32, 13.04, 13.69, 12.27], [12.99, 12.62, 13.31, 11.72], [13.12, 13.03, 13.75, 12.34], [12.45, 12.18, 12.99, 11.23], [12.58, 12.6, 13.44, 11.88], [12.24, 12.17, 13.06, 11.31], [11.93, 11.98, 12.97, 11.11]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASN', 14.07), ('CB', 'TYR', 'CG', 'ASN', 13.69), ('CB', 'TYR', 'OD1', 'ASN', 14.22), ('CB', 'TYR', 'ND2', 'ASN', 12.99)], [('CG', 'TYR', 'CB', 'ASN', 13.32), ('CG', 'TYR', 'CG', 'ASN', 13.04), ('CG', 'TYR', 'OD1', 'ASN', 13.69), ('CG', 'TYR', 'ND2', 'ASN', 12.27)], [('CD1', 'TYR', 'CB', 'ASN', 12.99), ('CD1', 'TYR', 'CG', 'ASN', 12.62), ('CD1', 'TYR', 'OD1', 'ASN', 13.31), ('CD1', 'TYR', 'ND2', 'ASN', 11.72)], [('CD2', 'TYR', 'CB', 'ASN', 13.12), ('CD2', 'TYR', 'CG', 'ASN', 13.03), ('CD2', 'TYR', 'OD1', 'ASN', 13.75), ('CD2', 'TYR', 'ND2', 'ASN', 12.34)], [('CE1', 'TYR', 'CB', 'ASN', 12.45), ('CE1', 'TYR', 'CG', 'ASN', 12.18), ('CE1', 'TYR', 'OD1', 'ASN', 12.99), ('CE1', 'TYR', 'ND2', 'ASN', 11.23)], [('CE2', 'TYR', 'CB', 'ASN', 12.58), ('CE2', 'TYR', 'CG', 'ASN', 12.6), ('CE2', 'TYR', 'OD1', 'ASN', 13.44), ('CE2', 'TYR', 'ND2', 'ASN', 11.88)], [('CZ', 'TYR', 'CB', 'ASN', 12.24), ('CZ', 'TYR', 'CG', 'ASN', 12.17), ('CZ', 'TYR', 'OD1', 'ASN', 13.06), ('CZ', 'TYR', 'ND2', 'ASN', 11.31)], [('OH', 'TYR', 'CB', 'ASN', 11.93), ('OH', 'TYR', 'CG', 'ASN', 11.98), ('OH', 'TYR', 'OD1', 'ASN', 12.97), ('OH', 'TYR', 'ND2', 'ASN', 11.11)]]}
THR_THR = { 
	'distances':
		[[15.1, 14.03, 16.25], [13.88, 12.87, 15.07], [15.3, 14.21, 16.34], [15.1, 13.88, 15.3], [14.03, 12.87, 14.21], [16.25, 15.07, 16.34]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'THR', 15.1), ('CB', 'THR', 'OG1', 'THR', 14.03), ('CB', 'THR', 'CG2', 'THR', 16.25)], [('OG1', 'THR', 'CB', 'THR', 13.88), ('OG1', 'THR', 'OG1', 'THR', 12.87), ('OG1', 'THR', 'CG2', 'THR', 15.07)], [('CG2', 'THR', 'CB', 'THR', 15.3), ('CG2', 'THR', 'OG1', 'THR', 14.21), ('CG2', 'THR', 'CG2', 'THR', 16.34)], [('CB', 'THR', 'CB', 'THR', 15.1), ('CB', 'THR', 'OG1', 'THR', 13.88), ('CB', 'THR', 'CG2', 'THR', 15.3)], [('OG1', 'THR', 'CB', 'THR', 14.03), ('OG1', 'THR', 'OG1', 'THR', 12.87), ('OG1', 'THR', 'CG2', 'THR', 14.21)], [('CG2', 'THR', 'CB', 'THR', 16.25), ('CG2', 'THR', 'OG1', 'THR', 15.07), ('CG2', 'THR', 'CG2', 'THR', 16.34)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_TYR, d, 'P_1fm7_5_5_1_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(THR_ASN, d, 'P_1fm7_5_5_1_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ASN, d, 'P_1fm7_5_5_1_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_THR, d, 'P_1fm7_5_5_1_6')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_TYR' :  match1,
		'THR_ASN' :  match2,
		'TYR_ASN' :  match3,
		'THR_THR' :  match4}