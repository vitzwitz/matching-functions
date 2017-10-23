'''
FUNC:A_1qaz_3_5_1_45
PDB:1qaz
EC:3.5.1.45
RESI:asn,arg,tyr
LOCI:a-191,239,246;
'''
import motifFunctions as cmd
ARG_ASN = { 
	'distances':
		[[11.73, 10.95, 11.64, 9.69], [10.46, 9.7, 10.45, 8.41], [10.66, 9.78, 10.44, 8.46], [10.8, 9.72, 10.18, 8.43], [9.95, 8.75, 9.09, 7.52], [8.75, 7.58, 7.99, 6.33], [10.5, 9.17, 9.29, 8.05]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASN', 11.73), ('CB', 'ARG', 'CG', 'ASN', 10.95), ('CB', 'ARG', 'OD1', 'ASN', 11.64), ('CB', 'ARG', 'ND2', 'ASN', 9.69)], [('CG', 'ARG', 'CB', 'ASN', 10.46), ('CG', 'ARG', 'CG', 'ASN', 9.7), ('CG', 'ARG', 'OD1', 'ASN', 10.45), ('CG', 'ARG', 'ND2', 'ASN', 8.41)], [('CD', 'ARG', 'CB', 'ASN', 10.66), ('CD', 'ARG', 'CG', 'ASN', 9.78), ('CD', 'ARG', 'OD1', 'ASN', 10.44), ('CD', 'ARG', 'ND2', 'ASN', 8.46)], [('NE', 'ARG', 'CB', 'ASN', 10.8), ('NE', 'ARG', 'CG', 'ASN', 9.72), ('NE', 'ARG', 'OD1', 'ASN', 10.18), ('NE', 'ARG', 'ND2', 'ASN', 8.43)], [('CZ', 'ARG', 'CB', 'ASN', 9.95), ('CZ', 'ARG', 'CG', 'ASN', 8.75), ('CZ', 'ARG', 'OD1', 'ASN', 9.09), ('CZ', 'ARG', 'ND2', 'ASN', 7.52)], [('NH1', 'ARG', 'CB', 'ASN', 8.75), ('NH1', 'ARG', 'CG', 'ASN', 7.58), ('NH1', 'ARG', 'OD1', 'ASN', 7.99), ('NH1', 'ARG', 'ND2', 'ASN', 6.33)], [('NH2', 'ARG', 'CB', 'ASN', 10.5), ('NH2', 'ARG', 'CG', 'ASN', 9.17), ('NH2', 'ARG', 'OD1', 'ASN', 9.29), ('NH2', 'ARG', 'ND2', 'ASN', 8.05)]]}
TYR_ARG = { 
	'distances':
		[[6.88, 6.39, 7.49, 7.67, 7.53, 7.21, 8.14], [6.84, 6.36, 7.17, 6.96, 6.6, 6.39, 6.95], [6.15, 6.01, 6.79, 6.36, 6.17, 6.37, 6.34], [8.01, 7.33, 7.86, 7.49, 6.8, 6.35, 6.99], [6.86, 6.76, 7.18, 6.36, 5.94, 6.33, 5.68], [8.53, 7.92, 8.19, 7.51, 6.62, 6.32, 6.44], [8.02, 7.66, 7.87, 6.97, 6.18, 6.3, 5.74], [8.95, 8.65, 8.63, 7.51, 6.62, 6.88, 5.81]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 6.88), ('CB', 'TYR', 'CG', 'ARG', 6.39), ('CB', 'TYR', 'CD', 'ARG', 7.49), ('CB', 'TYR', 'NE', 'ARG', 7.67), ('CB', 'TYR', 'CZ', 'ARG', 7.53), ('CB', 'TYR', 'NH1', 'ARG', 7.21), ('CB', 'TYR', 'NH2', 'ARG', 8.14)], [('CG', 'TYR', 'CB', 'ARG', 6.84), ('CG', 'TYR', 'CG', 'ARG', 6.36), ('CG', 'TYR', 'CD', 'ARG', 7.17), ('CG', 'TYR', 'NE', 'ARG', 6.96), ('CG', 'TYR', 'CZ', 'ARG', 6.6), ('CG', 'TYR', 'NH1', 'ARG', 6.39), ('CG', 'TYR', 'NH2', 'ARG', 6.95)], [('CD1', 'TYR', 'CB', 'ARG', 6.15), ('CD1', 'TYR', 'CG', 'ARG', 6.01), ('CD1', 'TYR', 'CD', 'ARG', 6.79), ('CD1', 'TYR', 'NE', 'ARG', 6.36), ('CD1', 'TYR', 'CZ', 'ARG', 6.17), ('CD1', 'TYR', 'NH1', 'ARG', 6.37), ('CD1', 'TYR', 'NH2', 'ARG', 6.34)], [('CD2', 'TYR', 'CB', 'ARG', 8.01), ('CD2', 'TYR', 'CG', 'ARG', 7.33), ('CD2', 'TYR', 'CD', 'ARG', 7.86), ('CD2', 'TYR', 'NE', 'ARG', 7.49), ('CD2', 'TYR', 'CZ', 'ARG', 6.8), ('CD2', 'TYR', 'NH1', 'ARG', 6.35), ('CD2', 'TYR', 'NH2', 'ARG', 6.99)], [('CE1', 'TYR', 'CB', 'ARG', 6.86), ('CE1', 'TYR', 'CG', 'ARG', 6.76), ('CE1', 'TYR', 'CD', 'ARG', 7.18), ('CE1', 'TYR', 'NE', 'ARG', 6.36), ('CE1', 'TYR', 'CZ', 'ARG', 5.94), ('CE1', 'TYR', 'NH1', 'ARG', 6.33), ('CE1', 'TYR', 'NH2', 'ARG', 5.68)], [('CE2', 'TYR', 'CB', 'ARG', 8.53), ('CE2', 'TYR', 'CG', 'ARG', 7.92), ('CE2', 'TYR', 'CD', 'ARG', 8.19), ('CE2', 'TYR', 'NE', 'ARG', 7.51), ('CE2', 'TYR', 'CZ', 'ARG', 6.62), ('CE2', 'TYR', 'NH1', 'ARG', 6.32), ('CE2', 'TYR', 'NH2', 'ARG', 6.44)], [('CZ', 'TYR', 'CB', 'ARG', 8.02), ('CZ', 'TYR', 'CG', 'ARG', 7.66), ('CZ', 'TYR', 'CD', 'ARG', 7.87), ('CZ', 'TYR', 'NE', 'ARG', 6.97), ('CZ', 'TYR', 'CZ', 'ARG', 6.18), ('CZ', 'TYR', 'NH1', 'ARG', 6.3), ('CZ', 'TYR', 'NH2', 'ARG', 5.74)], [('OH', 'TYR', 'CB', 'ARG', 8.95), ('OH', 'TYR', 'CG', 'ARG', 8.65), ('OH', 'TYR', 'CD', 'ARG', 8.63), ('OH', 'TYR', 'NE', 'ARG', 7.51), ('OH', 'TYR', 'CZ', 'ARG', 6.62), ('OH', 'TYR', 'NH1', 'ARG', 6.88), ('OH', 'TYR', 'NH2', 'ARG', 5.81)]]}
TYR_ASN = { 
	'distances':
		[[8.11, 7.59, 8.28, 6.74], [8.2, 7.34, 7.79, 6.44], [9.48, 8.51, 8.86, 7.53], [7.29, 6.28, 6.55, 5.54], [9.95, 8.79, 8.92, 7.87], [7.93, 6.68, 6.62, 6.04], [9.26, 7.98, 7.91, 7.22], [10.1, 8.71, 8.42, 8.06]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASN', 8.11), ('CB', 'TYR', 'CG', 'ASN', 7.59), ('CB', 'TYR', 'OD1', 'ASN', 8.28), ('CB', 'TYR', 'ND2', 'ASN', 6.74)], [('CG', 'TYR', 'CB', 'ASN', 8.2), ('CG', 'TYR', 'CG', 'ASN', 7.34), ('CG', 'TYR', 'OD1', 'ASN', 7.79), ('CG', 'TYR', 'ND2', 'ASN', 6.44)], [('CD1', 'TYR', 'CB', 'ASN', 9.48), ('CD1', 'TYR', 'CG', 'ASN', 8.51), ('CD1', 'TYR', 'OD1', 'ASN', 8.86), ('CD1', 'TYR', 'ND2', 'ASN', 7.53)], [('CD2', 'TYR', 'CB', 'ASN', 7.29), ('CD2', 'TYR', 'CG', 'ASN', 6.28), ('CD2', 'TYR', 'OD1', 'ASN', 6.55), ('CD2', 'TYR', 'ND2', 'ASN', 5.54)], [('CE1', 'TYR', 'CB', 'ASN', 9.95), ('CE1', 'TYR', 'CG', 'ASN', 8.79), ('CE1', 'TYR', 'OD1', 'ASN', 8.92), ('CE1', 'TYR', 'ND2', 'ASN', 7.87)], [('CE2', 'TYR', 'CB', 'ASN', 7.93), ('CE2', 'TYR', 'CG', 'ASN', 6.68), ('CE2', 'TYR', 'OD1', 'ASN', 6.62), ('CE2', 'TYR', 'ND2', 'ASN', 6.04)], [('CZ', 'TYR', 'CB', 'ASN', 9.26), ('CZ', 'TYR', 'CG', 'ASN', 7.98), ('CZ', 'TYR', 'OD1', 'ASN', 7.91), ('CZ', 'TYR', 'ND2', 'ASN', 7.22)], [('OH', 'TYR', 'CB', 'ASN', 10.1), ('OH', 'TYR', 'CG', 'ASN', 8.71), ('OH', 'TYR', 'OD1', 'ASN', 8.42), ('OH', 'TYR', 'ND2', 'ASN', 8.06)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_ASN, d, 'A_1qaz_3_5_1_45')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ARG, d, 'A_1qaz_3_5_1_45')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ASN, d, 'A_1qaz_3_5_1_45')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ASN' :  match1,
		'TYR_ARG' :  match2,
		'TYR_ASN' :  match3}