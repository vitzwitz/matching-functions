'''
FUNC:P_1ezr_3_2_2_1
PDB:1ezr
EC:3.2.2.1
RESI:asp,asn,his
LOCI:a-10,168,240;
'''
import motifFunctions as cmd
HIS_ASN = { 
	'distances':
		[[9.45, 8.42, 8.66, 7.49, 12.66, 11.75, 10.5, 10.08], [9.93, 8.95, 9.08, 8.2, 13.08, 12.08, 10.81, 10.2], [10.33, 9.25, 9.18, 8.62, 13.41, 12.43, 11.07, 10.37], [10.36, 9.54, 9.73, 8.86, 13.42, 12.36, 11.18, 10.45], [10.94, 9.95, 9.85, 9.45, 13.92, 12.88, 11.56, 10.71], [10.97, 10.13, 10.17, 9.6, 13.94, 12.85, 11.63, 10.76], [11.16, 10.17, 10.64, 8.95, 14.32, 13.59, 12.48, 12.42], [10.46, 9.39, 9.75, 8.24, 13.67, 12.91, 11.71, 11.58], [10.69, 9.64, 9.92, 8.61, 13.92, 13.06, 11.82, 11.5], [11.64, 10.49, 10.61, 9.53, 14.86, 14.0, 12.69, 12.3]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 9.45), ('CB', 'HIS', 'CG', 'ASN', 8.42), ('CB', 'HIS', 'OD1', 'ASN', 8.66), ('CB', 'HIS', 'ND2', 'ASN', 7.49), ('CB', 'HIS', 'O', 'ASN', 12.66), ('CB', 'HIS', 'C', 'ASN', 11.75), ('CB', 'HIS', 'CA', 'ASN', 10.5), ('CB', 'HIS', 'N', 'ASN', 10.08)], [('CG', 'HIS', 'CB', 'ASN', 9.93), ('CG', 'HIS', 'CG', 'ASN', 8.95), ('CG', 'HIS', 'OD1', 'ASN', 9.08), ('CG', 'HIS', 'ND2', 'ASN', 8.2), ('CG', 'HIS', 'O', 'ASN', 13.08), ('CG', 'HIS', 'C', 'ASN', 12.08), ('CG', 'HIS', 'CA', 'ASN', 10.81), ('CG', 'HIS', 'N', 'ASN', 10.2)], [('ND1', 'HIS', 'CB', 'ASN', 10.33), ('ND1', 'HIS', 'CG', 'ASN', 9.25), ('ND1', 'HIS', 'OD1', 'ASN', 9.18), ('ND1', 'HIS', 'ND2', 'ASN', 8.62), ('ND1', 'HIS', 'O', 'ASN', 13.41), ('ND1', 'HIS', 'C', 'ASN', 12.43), ('ND1', 'HIS', 'CA', 'ASN', 11.07), ('ND1', 'HIS', 'N', 'ASN', 10.37)], [('CD2', 'HIS', 'CB', 'ASN', 10.36), ('CD2', 'HIS', 'CG', 'ASN', 9.54), ('CD2', 'HIS', 'OD1', 'ASN', 9.73), ('CD2', 'HIS', 'ND2', 'ASN', 8.86), ('CD2', 'HIS', 'O', 'ASN', 13.42), ('CD2', 'HIS', 'C', 'ASN', 12.36), ('CD2', 'HIS', 'CA', 'ASN', 11.18), ('CD2', 'HIS', 'N', 'ASN', 10.45)], [('CE1', 'HIS', 'CB', 'ASN', 10.94), ('CE1', 'HIS', 'CG', 'ASN', 9.95), ('CE1', 'HIS', 'OD1', 'ASN', 9.85), ('CE1', 'HIS', 'ND2', 'ASN', 9.45), ('CE1', 'HIS', 'O', 'ASN', 13.92), ('CE1', 'HIS', 'C', 'ASN', 12.88), ('CE1', 'HIS', 'CA', 'ASN', 11.56), ('CE1', 'HIS', 'N', 'ASN', 10.71)], [('NE2', 'HIS', 'CB', 'ASN', 10.97), ('NE2', 'HIS', 'CG', 'ASN', 10.13), ('NE2', 'HIS', 'OD1', 'ASN', 10.17), ('NE2', 'HIS', 'ND2', 'ASN', 9.6), ('NE2', 'HIS', 'O', 'ASN', 13.94), ('NE2', 'HIS', 'C', 'ASN', 12.85), ('NE2', 'HIS', 'CA', 'ASN', 11.63), ('NE2', 'HIS', 'N', 'ASN', 10.76)], [('O', 'HIS', 'CB', 'ASN', 11.16), ('O', 'HIS', 'CG', 'ASN', 10.17), ('O', 'HIS', 'OD1', 'ASN', 10.64), ('O', 'HIS', 'ND2', 'ASN', 8.95), ('O', 'HIS', 'O', 'ASN', 14.32), ('O', 'HIS', 'C', 'ASN', 13.59), ('O', 'HIS', 'CA', 'ASN', 12.48), ('O', 'HIS', 'N', 'ASN', 12.42)], [('C', 'HIS', 'CB', 'ASN', 10.46), ('C', 'HIS', 'CG', 'ASN', 9.39), ('C', 'HIS', 'OD1', 'ASN', 9.75), ('C', 'HIS', 'ND2', 'ASN', 8.24), ('C', 'HIS', 'O', 'ASN', 13.67), ('C', 'HIS', 'C', 'ASN', 12.91), ('C', 'HIS', 'CA', 'ASN', 11.71), ('C', 'HIS', 'N', 'ASN', 11.58)], [('CA', 'HIS', 'CB', 'ASN', 10.69), ('CA', 'HIS', 'CG', 'ASN', 9.64), ('CA', 'HIS', 'OD1', 'ASN', 9.92), ('CA', 'HIS', 'ND2', 'ASN', 8.61), ('CA', 'HIS', 'O', 'ASN', 13.92), ('CA', 'HIS', 'C', 'ASN', 13.06), ('CA', 'HIS', 'CA', 'ASN', 11.82), ('CA', 'HIS', 'N', 'ASN', 11.5)], [('N', 'HIS', 'CB', 'ASN', 11.64), ('N', 'HIS', 'CG', 'ASN', 10.49), ('N', 'HIS', 'OD1', 'ASN', 10.61), ('N', 'HIS', 'ND2', 'ASN', 9.53), ('N', 'HIS', 'O', 'ASN', 14.86), ('N', 'HIS', 'C', 'ASN', 14.0), ('N', 'HIS', 'CA', 'ASN', 12.69), ('N', 'HIS', 'N', 'ASN', 12.3)]]}
ASP_HIS = { 
	'distances':
		[[12.31, 12.91, 12.57, 13.99, 13.46, 14.29, 13.46, 12.59, 13.08, 13.24], [10.86, 11.45, 11.14, 12.5, 12.02, 12.82, 12.19, 11.27, 11.7, 11.92], [9.98, 10.68, 10.46, 11.8, 11.43, 12.21, 11.07, 10.2, 10.73, 10.97], [10.74, 11.18, 10.84, 12.15, 11.61, 12.38, 12.4, 11.43, 11.71, 11.94], [11.63, 12.13, 11.57, 13.3, 12.44, 13.46, 12.81, 11.86, 12.24, 12.1], [12.08, 12.71, 12.25, 13.92, 13.21, 14.18, 12.95, 12.08, 12.61, 12.53], [12.53, 13.23, 12.9, 14.4, 13.87, 14.75, 13.33, 12.52, 13.13, 13.22], [11.94, 12.79, 12.59, 13.98, 13.65, 14.46, 12.43, 11.71, 12.46, 12.65]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 12.31), ('CB', 'ASP', 'CG', 'HIS', 12.91), ('CB', 'ASP', 'ND1', 'HIS', 12.57), ('CB', 'ASP', 'CD2', 'HIS', 13.99), ('CB', 'ASP', 'CE1', 'HIS', 13.46), ('CB', 'ASP', 'NE2', 'HIS', 14.29), ('CB', 'ASP', 'O', 'HIS', 13.46), ('CB', 'ASP', 'C', 'HIS', 12.59), ('CB', 'ASP', 'CA', 'HIS', 13.08), ('CB', 'ASP', 'N', 'HIS', 13.24)], [('CG', 'ASP', 'CB', 'HIS', 10.86), ('CG', 'ASP', 'CG', 'HIS', 11.45), ('CG', 'ASP', 'ND1', 'HIS', 11.14), ('CG', 'ASP', 'CD2', 'HIS', 12.5), ('CG', 'ASP', 'CE1', 'HIS', 12.02), ('CG', 'ASP', 'NE2', 'HIS', 12.82), ('CG', 'ASP', 'O', 'HIS', 12.19), ('CG', 'ASP', 'C', 'HIS', 11.27), ('CG', 'ASP', 'CA', 'HIS', 11.7), ('CG', 'ASP', 'N', 'HIS', 11.92)], [('OD1', 'ASP', 'CB', 'HIS', 9.98), ('OD1', 'ASP', 'CG', 'HIS', 10.68), ('OD1', 'ASP', 'ND1', 'HIS', 10.46), ('OD1', 'ASP', 'CD2', 'HIS', 11.8), ('OD1', 'ASP', 'CE1', 'HIS', 11.43), ('OD1', 'ASP', 'NE2', 'HIS', 12.21), ('OD1', 'ASP', 'O', 'HIS', 11.07), ('OD1', 'ASP', 'C', 'HIS', 10.2), ('OD1', 'ASP', 'CA', 'HIS', 10.73), ('OD1', 'ASP', 'N', 'HIS', 10.97)], [('OD2', 'ASP', 'CB', 'HIS', 10.74), ('OD2', 'ASP', 'CG', 'HIS', 11.18), ('OD2', 'ASP', 'ND1', 'HIS', 10.84), ('OD2', 'ASP', 'CD2', 'HIS', 12.15), ('OD2', 'ASP', 'CE1', 'HIS', 11.61), ('OD2', 'ASP', 'NE2', 'HIS', 12.38), ('OD2', 'ASP', 'O', 'HIS', 12.4), ('OD2', 'ASP', 'C', 'HIS', 11.43), ('OD2', 'ASP', 'CA', 'HIS', 11.71), ('OD2', 'ASP', 'N', 'HIS', 11.94)], [('O', 'ASP', 'CB', 'HIS', 11.63), ('O', 'ASP', 'CG', 'HIS', 12.13), ('O', 'ASP', 'ND1', 'HIS', 11.57), ('O', 'ASP', 'CD2', 'HIS', 13.3), ('O', 'ASP', 'CE1', 'HIS', 12.44), ('O', 'ASP', 'NE2', 'HIS', 13.46), ('O', 'ASP', 'O', 'HIS', 12.81), ('O', 'ASP', 'C', 'HIS', 11.86), ('O', 'ASP', 'CA', 'HIS', 12.24), ('O', 'ASP', 'N', 'HIS', 12.1)], [('C', 'ASP', 'CB', 'HIS', 12.08), ('C', 'ASP', 'CG', 'HIS', 12.71), ('C', 'ASP', 'ND1', 'HIS', 12.25), ('C', 'ASP', 'CD2', 'HIS', 13.92), ('C', 'ASP', 'CE1', 'HIS', 13.21), ('C', 'ASP', 'NE2', 'HIS', 14.18), ('C', 'ASP', 'O', 'HIS', 12.95), ('C', 'ASP', 'C', 'HIS', 12.08), ('C', 'ASP', 'CA', 'HIS', 12.61), ('C', 'ASP', 'N', 'HIS', 12.53)], [('CA', 'ASP', 'CB', 'HIS', 12.53), ('CA', 'ASP', 'CG', 'HIS', 13.23), ('CA', 'ASP', 'ND1', 'HIS', 12.9), ('CA', 'ASP', 'CD2', 'HIS', 14.4), ('CA', 'ASP', 'CE1', 'HIS', 13.87), ('CA', 'ASP', 'NE2', 'HIS', 14.75), ('CA', 'ASP', 'O', 'HIS', 13.33), ('CA', 'ASP', 'C', 'HIS', 12.52), ('CA', 'ASP', 'CA', 'HIS', 13.13), ('CA', 'ASP', 'N', 'HIS', 13.22)], [('N', 'ASP', 'CB', 'HIS', 11.94), ('N', 'ASP', 'CG', 'HIS', 12.79), ('N', 'ASP', 'ND1', 'HIS', 12.59), ('N', 'ASP', 'CD2', 'HIS', 13.98), ('N', 'ASP', 'CE1', 'HIS', 13.65), ('N', 'ASP', 'NE2', 'HIS', 14.46), ('N', 'ASP', 'O', 'HIS', 12.43), ('N', 'ASP', 'C', 'HIS', 11.71), ('N', 'ASP', 'CA', 'HIS', 12.46), ('N', 'ASP', 'N', 'HIS', 12.65)]]}
ASP_ASN = { 
	'distances':
		[[8.83, 7.78, 6.95, 8.06, 9.77, 9.96, 8.91, 9.45], [7.61, 6.45, 5.6, 6.69, 8.95, 8.98, 7.8, 8.24], [7.48, 6.2, 5.52, 6.17, 9.19, 9.15, 7.92, 8.4], [7.04, 5.93, 4.92, 6.39, 8.3, 8.25, 7.03, 7.33], [10.32, 9.03, 8.14, 9.09, 11.83, 11.79, 10.53, 10.78], [10.55, 9.29, 8.51, 9.28, 11.97, 12.03, 10.84, 11.25], [9.87, 8.75, 8.04, 8.82, 11.0, 11.2, 10.14, 10.72], [9.45, 8.33, 7.8, 8.21, 10.76, 10.96, 9.92, 10.62]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 8.83), ('CB', 'ASP', 'CG', 'ASN', 7.78), ('CB', 'ASP', 'OD1', 'ASN', 6.95), ('CB', 'ASP', 'ND2', 'ASN', 8.06), ('CB', 'ASP', 'O', 'ASN', 9.77), ('CB', 'ASP', 'C', 'ASN', 9.96), ('CB', 'ASP', 'CA', 'ASN', 8.91), ('CB', 'ASP', 'N', 'ASN', 9.45)], [('CG', 'ASP', 'CB', 'ASN', 7.61), ('CG', 'ASP', 'CG', 'ASN', 6.45), ('CG', 'ASP', 'OD1', 'ASN', 5.6), ('CG', 'ASP', 'ND2', 'ASN', 6.69), ('CG', 'ASP', 'O', 'ASN', 8.95), ('CG', 'ASP', 'C', 'ASN', 8.98), ('CG', 'ASP', 'CA', 'ASN', 7.8), ('CG', 'ASP', 'N', 'ASN', 8.24)], [('OD1', 'ASP', 'CB', 'ASN', 7.48), ('OD1', 'ASP', 'CG', 'ASN', 6.2), ('OD1', 'ASP', 'OD1', 'ASN', 5.52), ('OD1', 'ASP', 'ND2', 'ASN', 6.17), ('OD1', 'ASP', 'O', 'ASN', 9.19), ('OD1', 'ASP', 'C', 'ASN', 9.15), ('OD1', 'ASP', 'CA', 'ASN', 7.92), ('OD1', 'ASP', 'N', 'ASN', 8.4)], [('OD2', 'ASP', 'CB', 'ASN', 7.04), ('OD2', 'ASP', 'CG', 'ASN', 5.93), ('OD2', 'ASP', 'OD1', 'ASN', 4.92), ('OD2', 'ASP', 'ND2', 'ASN', 6.39), ('OD2', 'ASP', 'O', 'ASN', 8.3), ('OD2', 'ASP', 'C', 'ASN', 8.25), ('OD2', 'ASP', 'CA', 'ASN', 7.03), ('OD2', 'ASP', 'N', 'ASN', 7.33)], [('O', 'ASP', 'CB', 'ASN', 10.32), ('O', 'ASP', 'CG', 'ASN', 9.03), ('O', 'ASP', 'OD1', 'ASN', 8.14), ('O', 'ASP', 'ND2', 'ASN', 9.09), ('O', 'ASP', 'O', 'ASN', 11.83), ('O', 'ASP', 'C', 'ASN', 11.79), ('O', 'ASP', 'CA', 'ASN', 10.53), ('O', 'ASP', 'N', 'ASN', 10.78)], [('C', 'ASP', 'CB', 'ASN', 10.55), ('C', 'ASP', 'CG', 'ASN', 9.29), ('C', 'ASP', 'OD1', 'ASN', 8.51), ('C', 'ASP', 'ND2', 'ASN', 9.28), ('C', 'ASP', 'O', 'ASN', 11.97), ('C', 'ASP', 'C', 'ASN', 12.03), ('C', 'ASP', 'CA', 'ASN', 10.84), ('C', 'ASP', 'N', 'ASN', 11.25)], [('CA', 'ASP', 'CB', 'ASN', 9.87), ('CA', 'ASP', 'CG', 'ASN', 8.75), ('CA', 'ASP', 'OD1', 'ASN', 8.04), ('CA', 'ASP', 'ND2', 'ASN', 8.82), ('CA', 'ASP', 'O', 'ASN', 11.0), ('CA', 'ASP', 'C', 'ASN', 11.2), ('CA', 'ASP', 'CA', 'ASN', 10.14), ('CA', 'ASP', 'N', 'ASN', 10.72)], [('N', 'ASP', 'CB', 'ASN', 9.45), ('N', 'ASP', 'CG', 'ASN', 8.33), ('N', 'ASP', 'OD1', 'ASN', 7.8), ('N', 'ASP', 'ND2', 'ASN', 8.21), ('N', 'ASP', 'O', 'ASN', 10.76), ('N', 'ASP', 'C', 'ASN', 10.96), ('N', 'ASP', 'CA', 'ASN', 9.92), ('N', 'ASP', 'N', 'ASN', 10.62)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASN, d, 'P_1ezr_3_2_2_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'P_1ezr_3_2_2_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASN, d, 'P_1ezr_3_2_2_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASN' :  match1,
		'ASP_HIS' :  match2,
		'ASP_ASN' :  match3}