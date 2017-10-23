'''
FUNC:P_2nac_1_2_1_2
PDB:2nac
EC:1.2.1.2
RESI:asn,arg,gln,his
LOCI:a-146,284,313,332;
'''
import motifFunctions as cmd
ASN_GLN = { 
	'distances':
		[[18.63, 17.35, 16.21, 16.26, 15.29], [17.61, 16.37, 15.23, 15.32, 14.24], [17.67, 16.49, 15.29, 15.35, 14.28], [16.77, 15.51, 14.45, 14.64, 13.43]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLN', 18.63), ('CB', 'ASN', 'CG', 'GLN', 17.35), ('CB', 'ASN', 'CD', 'GLN', 16.21), ('CB', 'ASN', 'OE1', 'GLN', 16.26), ('CB', 'ASN', 'NE2', 'GLN', 15.29)], [('CG', 'ASN', 'CB', 'GLN', 17.61), ('CG', 'ASN', 'CG', 'GLN', 16.37), ('CG', 'ASN', 'CD', 'GLN', 15.23), ('CG', 'ASN', 'OE1', 'GLN', 15.32), ('CG', 'ASN', 'NE2', 'GLN', 14.24)], [('OD1', 'ASN', 'CB', 'GLN', 17.67), ('OD1', 'ASN', 'CG', 'GLN', 16.49), ('OD1', 'ASN', 'CD', 'GLN', 15.29), ('OD1', 'ASN', 'OE1', 'GLN', 15.35), ('OD1', 'ASN', 'NE2', 'GLN', 14.28)], [('ND2', 'ASN', 'CB', 'GLN', 16.77), ('ND2', 'ASN', 'CG', 'GLN', 15.51), ('ND2', 'ASN', 'CD', 'GLN', 14.45), ('ND2', 'ASN', 'OE1', 'GLN', 14.64), ('ND2', 'ASN', 'NE2', 'GLN', 13.43)]]}
GLN_HIS = { 
	'distances':
		[[7.61, 7.98, 7.58, 9.03, 8.43, 9.28], [6.2, 6.6, 6.24, 7.72, 7.2, 8.04], [5.51, 5.61, 5.28, 6.55, 6.08, 6.81], [5.51, 5.66, 5.68, 6.43, 6.4, 6.84], [5.5, 5.18, 4.46, 6.03, 5.09, 6.0]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 7.61), ('CB', 'GLN', 'CG', 'HIS', 7.98), ('CB', 'GLN', 'ND1', 'HIS', 7.58), ('CB', 'GLN', 'CD2', 'HIS', 9.03), ('CB', 'GLN', 'CE1', 'HIS', 8.43), ('CB', 'GLN', 'NE2', 'HIS', 9.28)], [('CG', 'GLN', 'CB', 'HIS', 6.2), ('CG', 'GLN', 'CG', 'HIS', 6.6), ('CG', 'GLN', 'ND1', 'HIS', 6.24), ('CG', 'GLN', 'CD2', 'HIS', 7.72), ('CG', 'GLN', 'CE1', 'HIS', 7.2), ('CG', 'GLN', 'NE2', 'HIS', 8.04)], [('CD', 'GLN', 'CB', 'HIS', 5.51), ('CD', 'GLN', 'CG', 'HIS', 5.61), ('CD', 'GLN', 'ND1', 'HIS', 5.28), ('CD', 'GLN', 'CD2', 'HIS', 6.55), ('CD', 'GLN', 'CE1', 'HIS', 6.08), ('CD', 'GLN', 'NE2', 'HIS', 6.81)], [('OE1', 'GLN', 'CB', 'HIS', 5.51), ('OE1', 'GLN', 'CG', 'HIS', 5.66), ('OE1', 'GLN', 'ND1', 'HIS', 5.68), ('OE1', 'GLN', 'CD2', 'HIS', 6.43), ('OE1', 'GLN', 'CE1', 'HIS', 6.4), ('OE1', 'GLN', 'NE2', 'HIS', 6.84)], [('NE2', 'GLN', 'CB', 'HIS', 5.5), ('NE2', 'GLN', 'CG', 'HIS', 5.18), ('NE2', 'GLN', 'ND1', 'HIS', 4.46), ('NE2', 'GLN', 'CD2', 'HIS', 6.03), ('NE2', 'GLN', 'CE1', 'HIS', 5.09), ('NE2', 'GLN', 'NE2', 'HIS', 6.0)]]}
ARG_HIS = { 
	'distances':
		[[11.82, 10.93, 10.58, 10.57, 10.0, 9.98], [11.87, 10.82, 10.31, 10.41, 9.57, 9.61], [10.89, 9.82, 9.15, 9.54, 8.44, 8.67], [11.28, 10.07, 9.3, 9.71, 8.41, 8.66], [11.25, 9.93, 9.22, 9.38, 8.18, 8.25], [10.8, 9.47, 8.96, 8.76, 7.88, 7.7], [11.95, 10.57, 9.78, 9.99, 8.65, 8.75]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 11.82), ('CB', 'ARG', 'CG', 'HIS', 10.93), ('CB', 'ARG', 'ND1', 'HIS', 10.58), ('CB', 'ARG', 'CD2', 'HIS', 10.57), ('CB', 'ARG', 'CE1', 'HIS', 10.0), ('CB', 'ARG', 'NE2', 'HIS', 9.98)], [('CG', 'ARG', 'CB', 'HIS', 11.87), ('CG', 'ARG', 'CG', 'HIS', 10.82), ('CG', 'ARG', 'ND1', 'HIS', 10.31), ('CG', 'ARG', 'CD2', 'HIS', 10.41), ('CG', 'ARG', 'CE1', 'HIS', 9.57), ('CG', 'ARG', 'NE2', 'HIS', 9.61)], [('CD', 'ARG', 'CB', 'HIS', 10.89), ('CD', 'ARG', 'CG', 'HIS', 9.82), ('CD', 'ARG', 'ND1', 'HIS', 9.15), ('CD', 'ARG', 'CD2', 'HIS', 9.54), ('CD', 'ARG', 'CE1', 'HIS', 8.44), ('CD', 'ARG', 'NE2', 'HIS', 8.67)], [('NE', 'ARG', 'CB', 'HIS', 11.28), ('NE', 'ARG', 'CG', 'HIS', 10.07), ('NE', 'ARG', 'ND1', 'HIS', 9.3), ('NE', 'ARG', 'CD2', 'HIS', 9.71), ('NE', 'ARG', 'CE1', 'HIS', 8.41), ('NE', 'ARG', 'NE2', 'HIS', 8.66)], [('CZ', 'ARG', 'CB', 'HIS', 11.25), ('CZ', 'ARG', 'CG', 'HIS', 9.93), ('CZ', 'ARG', 'ND1', 'HIS', 9.22), ('CZ', 'ARG', 'CD2', 'HIS', 9.38), ('CZ', 'ARG', 'CE1', 'HIS', 8.18), ('CZ', 'ARG', 'NE2', 'HIS', 8.25)], [('NH1', 'ARG', 'CB', 'HIS', 10.8), ('NH1', 'ARG', 'CG', 'HIS', 9.47), ('NH1', 'ARG', 'ND1', 'HIS', 8.96), ('NH1', 'ARG', 'CD2', 'HIS', 8.76), ('NH1', 'ARG', 'CE1', 'HIS', 7.88), ('NH1', 'ARG', 'NE2', 'HIS', 7.7)], [('NH2', 'ARG', 'CB', 'HIS', 11.95), ('NH2', 'ARG', 'CG', 'HIS', 10.57), ('NH2', 'ARG', 'ND1', 'HIS', 9.78), ('NH2', 'ARG', 'CD2', 'HIS', 9.99), ('NH2', 'ARG', 'CE1', 'HIS', 8.65), ('NH2', 'ARG', 'NE2', 'HIS', 8.75)]]}
ASN_ARG = { 
	'distances':
		[[16.82, 15.98, 15.5, 14.7, 13.51, 12.83, 13.04], [15.65, 14.73, 14.2, 13.33, 12.15, 11.54, 11.62], [15.02, 14.07, 13.63, 12.71, 11.48, 10.87, 10.9], [15.47, 14.54, 13.87, 13.0, 11.9, 11.39, 11.37]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ARG', 16.82), ('CB', 'ASN', 'CG', 'ARG', 15.98), ('CB', 'ASN', 'CD', 'ARG', 15.5), ('CB', 'ASN', 'NE', 'ARG', 14.7), ('CB', 'ASN', 'CZ', 'ARG', 13.51), ('CB', 'ASN', 'NH1', 'ARG', 12.83), ('CB', 'ASN', 'NH2', 'ARG', 13.04)], [('CG', 'ASN', 'CB', 'ARG', 15.65), ('CG', 'ASN', 'CG', 'ARG', 14.73), ('CG', 'ASN', 'CD', 'ARG', 14.2), ('CG', 'ASN', 'NE', 'ARG', 13.33), ('CG', 'ASN', 'CZ', 'ARG', 12.15), ('CG', 'ASN', 'NH1', 'ARG', 11.54), ('CG', 'ASN', 'NH2', 'ARG', 11.62)], [('OD1', 'ASN', 'CB', 'ARG', 15.02), ('OD1', 'ASN', 'CG', 'ARG', 14.07), ('OD1', 'ASN', 'CD', 'ARG', 13.63), ('OD1', 'ASN', 'NE', 'ARG', 12.71), ('OD1', 'ASN', 'CZ', 'ARG', 11.48), ('OD1', 'ASN', 'NH1', 'ARG', 10.87), ('OD1', 'ASN', 'NH2', 'ARG', 10.9)], [('ND2', 'ASN', 'CB', 'ARG', 15.47), ('ND2', 'ASN', 'CG', 'ARG', 14.54), ('ND2', 'ASN', 'CD', 'ARG', 13.87), ('ND2', 'ASN', 'NE', 'ARG', 13.0), ('ND2', 'ASN', 'CZ', 'ARG', 11.9), ('ND2', 'ASN', 'NH1', 'ARG', 11.39), ('ND2', 'ASN', 'NH2', 'ARG', 11.37)]]}
ASN_HIS = { 
	'distances':
		[[13.61, 12.52, 12.62, 11.49, 11.71, 10.93], [12.93, 11.73, 11.68, 10.71, 10.68, 9.99], [13.26, 11.98, 11.89, 10.9, 10.79, 10.09], [12.13, 10.95, 10.82, 10.04, 9.87, 9.31]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 13.61), ('CB', 'ASN', 'CG', 'HIS', 12.52), ('CB', 'ASN', 'ND1', 'HIS', 12.62), ('CB', 'ASN', 'CD2', 'HIS', 11.49), ('CB', 'ASN', 'CE1', 'HIS', 11.71), ('CB', 'ASN', 'NE2', 'HIS', 10.93)], [('CG', 'ASN', 'CB', 'HIS', 12.93), ('CG', 'ASN', 'CG', 'HIS', 11.73), ('CG', 'ASN', 'ND1', 'HIS', 11.68), ('CG', 'ASN', 'CD2', 'HIS', 10.71), ('CG', 'ASN', 'CE1', 'HIS', 10.68), ('CG', 'ASN', 'NE2', 'HIS', 9.99)], [('OD1', 'ASN', 'CB', 'HIS', 13.26), ('OD1', 'ASN', 'CG', 'HIS', 11.98), ('OD1', 'ASN', 'ND1', 'HIS', 11.89), ('OD1', 'ASN', 'CD2', 'HIS', 10.9), ('OD1', 'ASN', 'CE1', 'HIS', 10.79), ('OD1', 'ASN', 'NE2', 'HIS', 10.09)], [('ND2', 'ASN', 'CB', 'HIS', 12.13), ('ND2', 'ASN', 'CG', 'HIS', 10.95), ('ND2', 'ASN', 'ND1', 'HIS', 10.82), ('ND2', 'ASN', 'CD2', 'HIS', 10.04), ('ND2', 'ASN', 'CE1', 'HIS', 9.87), ('ND2', 'ASN', 'NE2', 'HIS', 9.31)]]}
ARG_GLN = { 
	'distances':
		[[10.64, 10.72, 9.55, 9.14, 9.25], [10.98, 10.95, 9.75, 9.52, 9.22], [9.91, 9.82, 8.67, 8.62, 8.0], [10.77, 10.56, 9.4, 9.49, 8.55], [11.53, 11.15, 9.91, 9.95, 8.98], [11.69, 11.2, 9.85, 9.73, 8.99], [12.46, 12.03, 10.83, 10.97, 9.8]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLN', 10.64), ('CB', 'ARG', 'CG', 'GLN', 10.72), ('CB', 'ARG', 'CD', 'GLN', 9.55), ('CB', 'ARG', 'OE1', 'GLN', 9.14), ('CB', 'ARG', 'NE2', 'GLN', 9.25)], [('CG', 'ARG', 'CB', 'GLN', 10.98), ('CG', 'ARG', 'CG', 'GLN', 10.95), ('CG', 'ARG', 'CD', 'GLN', 9.75), ('CG', 'ARG', 'OE1', 'GLN', 9.52), ('CG', 'ARG', 'NE2', 'GLN', 9.22)], [('CD', 'ARG', 'CB', 'GLN', 9.91), ('CD', 'ARG', 'CG', 'GLN', 9.82), ('CD', 'ARG', 'CD', 'GLN', 8.67), ('CD', 'ARG', 'OE1', 'GLN', 8.62), ('CD', 'ARG', 'NE2', 'GLN', 8.0)], [('NE', 'ARG', 'CB', 'GLN', 10.77), ('NE', 'ARG', 'CG', 'GLN', 10.56), ('NE', 'ARG', 'CD', 'GLN', 9.4), ('NE', 'ARG', 'OE1', 'GLN', 9.49), ('NE', 'ARG', 'NE2', 'GLN', 8.55)], [('CZ', 'ARG', 'CB', 'GLN', 11.53), ('CZ', 'ARG', 'CG', 'GLN', 11.15), ('CZ', 'ARG', 'CD', 'GLN', 9.91), ('CZ', 'ARG', 'OE1', 'GLN', 9.95), ('CZ', 'ARG', 'NE2', 'GLN', 8.98)], [('NH1', 'ARG', 'CB', 'GLN', 11.69), ('NH1', 'ARG', 'CG', 'GLN', 11.2), ('NH1', 'ARG', 'CD', 'GLN', 9.85), ('NH1', 'ARG', 'OE1', 'GLN', 9.73), ('NH1', 'ARG', 'NE2', 'GLN', 8.99)], [('NH2', 'ARG', 'CB', 'GLN', 12.46), ('NH2', 'ARG', 'CG', 'GLN', 12.03), ('NH2', 'ARG', 'CD', 'GLN', 10.83), ('NH2', 'ARG', 'OE1', 'GLN', 10.97), ('NH2', 'ARG', 'NE2', 'GLN', 9.8)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_GLN, d, 'P_2nac_1_2_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_HIS, d, 'P_2nac_1_2_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_HIS, d, 'P_2nac_1_2_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_ARG, d, 'P_2nac_1_2_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_HIS, d, 'P_2nac_1_2_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_GLN, d, 'P_2nac_1_2_1_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_GLN' :  match1,
		'GLN_HIS' :  match2,
		'ARG_HIS' :  match3,
		'ASN_ARG' :  match4,
		'ASN_HIS' :  match5,
		'ARG_GLN' :  match6}