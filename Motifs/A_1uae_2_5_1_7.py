'''
FUNC:A_1uae_2_5_1_7
PDB:1uae
EC:2.5.1.7
RESI:asn,cys,asp,arg
LOCI:a-23,115,305,397;
'''
import motifFunctions as cmd
ASP_CYS = { 
	'distances':
		[[11.07, 10.25], [10.0, 9.25], [9.05, 8.49], [10.28, 9.43]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYS', 11.07), ('CB', 'ASP', 'SG', 'CYS', 10.25)], [('CG', 'ASP', 'CB', 'CYS', 10.0), ('CG', 'ASP', 'SG', 'CYS', 9.25)], [('OD1', 'ASP', 'CB', 'CYS', 9.05), ('OD1', 'ASP', 'SG', 'CYS', 8.49)], [('OD2', 'ASP', 'CB', 'CYS', 10.28), ('OD2', 'ASP', 'SG', 'CYS', 9.43)]]}
ASP_ARG = { 
	'distances':
		[[13.79, 14.84, 14.43, 14.21, 13.41, 12.8, 13.43], [13.1, 14.1, 13.57, 13.23, 12.33, 11.74, 12.25], [13.03, 13.89, 13.24, 12.92, 11.95, 11.24, 11.91], [12.81, 13.87, 13.4, 12.93, 12.04, 11.59, 11.83]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 13.79), ('CB', 'ASP', 'CG', 'ARG', 14.84), ('CB', 'ASP', 'CD', 'ARG', 14.43), ('CB', 'ASP', 'NE', 'ARG', 14.21), ('CB', 'ASP', 'CZ', 'ARG', 13.41), ('CB', 'ASP', 'NH1', 'ARG', 12.8), ('CB', 'ASP', 'NH2', 'ARG', 13.43)], [('CG', 'ASP', 'CB', 'ARG', 13.1), ('CG', 'ASP', 'CG', 'ARG', 14.1), ('CG', 'ASP', 'CD', 'ARG', 13.57), ('CG', 'ASP', 'NE', 'ARG', 13.23), ('CG', 'ASP', 'CZ', 'ARG', 12.33), ('CG', 'ASP', 'NH1', 'ARG', 11.74), ('CG', 'ASP', 'NH2', 'ARG', 12.25)], [('OD1', 'ASP', 'CB', 'ARG', 13.03), ('OD1', 'ASP', 'CG', 'ARG', 13.89), ('OD1', 'ASP', 'CD', 'ARG', 13.24), ('OD1', 'ASP', 'NE', 'ARG', 12.92), ('OD1', 'ASP', 'CZ', 'ARG', 11.95), ('OD1', 'ASP', 'NH1', 'ARG', 11.24), ('OD1', 'ASP', 'NH2', 'ARG', 11.91)], [('OD2', 'ASP', 'CB', 'ARG', 12.81), ('OD2', 'ASP', 'CG', 'ARG', 13.87), ('OD2', 'ASP', 'CD', 'ARG', 13.4), ('OD2', 'ASP', 'NE', 'ARG', 12.93), ('OD2', 'ASP', 'CZ', 'ARG', 12.04), ('OD2', 'ASP', 'NH1', 'ARG', 11.59), ('OD2', 'ASP', 'NH2', 'ARG', 11.83)]]}
ASN_CYS = { 
	'distances':
		[[13.2, 12.1], [11.71, 10.58], [11.27, 10.1], [11.06, 9.98]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 13.2), ('CB', 'ASN', 'SG', 'CYS', 12.1)], [('CG', 'ASN', 'CB', 'CYS', 11.71), ('CG', 'ASN', 'SG', 'CYS', 10.58)], [('OD1', 'ASN', 'CB', 'CYS', 11.27), ('OD1', 'ASN', 'SG', 'CYS', 10.1)], [('ND2', 'ASN', 'CB', 'CYS', 11.06), ('ND2', 'ASN', 'SG', 'CYS', 9.98)]]}
ASN_ARG = { 
	'distances':
		[[12.59, 13.85, 13.69, 12.74, 12.11, 12.41, 11.39], [11.36, 12.57, 12.33, 11.41, 10.72, 10.95, 10.05], [10.44, 11.61, 11.37, 10.37, 9.72, 10.08, 9.0], [11.55, 12.74, 12.41, 11.59, 10.82, 10.85, 10.26]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ARG', 12.59), ('CB', 'ASN', 'CG', 'ARG', 13.85), ('CB', 'ASN', 'CD', 'ARG', 13.69), ('CB', 'ASN', 'NE', 'ARG', 12.74), ('CB', 'ASN', 'CZ', 'ARG', 12.11), ('CB', 'ASN', 'NH1', 'ARG', 12.41), ('CB', 'ASN', 'NH2', 'ARG', 11.39)], [('CG', 'ASN', 'CB', 'ARG', 11.36), ('CG', 'ASN', 'CG', 'ARG', 12.57), ('CG', 'ASN', 'CD', 'ARG', 12.33), ('CG', 'ASN', 'NE', 'ARG', 11.41), ('CG', 'ASN', 'CZ', 'ARG', 10.72), ('CG', 'ASN', 'NH1', 'ARG', 10.95), ('CG', 'ASN', 'NH2', 'ARG', 10.05)], [('OD1', 'ASN', 'CB', 'ARG', 10.44), ('OD1', 'ASN', 'CG', 'ARG', 11.61), ('OD1', 'ASN', 'CD', 'ARG', 11.37), ('OD1', 'ASN', 'NE', 'ARG', 10.37), ('OD1', 'ASN', 'CZ', 'ARG', 9.72), ('OD1', 'ASN', 'NH1', 'ARG', 10.08), ('OD1', 'ASN', 'NH2', 'ARG', 9.0)], [('ND2', 'ASN', 'CB', 'ARG', 11.55), ('ND2', 'ASN', 'CG', 'ARG', 12.74), ('ND2', 'ASN', 'CD', 'ARG', 12.41), ('ND2', 'ASN', 'NE', 'ARG', 11.59), ('ND2', 'ASN', 'CZ', 'ARG', 10.82), ('ND2', 'ASN', 'NH1', 'ARG', 10.85), ('ND2', 'ASN', 'NH2', 'ARG', 10.26)]]}
ARG_CYS = { 
	'distances':
		[[10.22, 8.66], [10.15, 8.81], [8.83, 7.66], [8.68, 7.57], [7.58, 6.57], [6.35, 5.39], [7.93, 7.06]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYS', 10.22), ('CB', 'ARG', 'SG', 'CYS', 8.66)], [('CG', 'ARG', 'CB', 'CYS', 10.15), ('CG', 'ARG', 'SG', 'CYS', 8.81)], [('CD', 'ARG', 'CB', 'CYS', 8.83), ('CD', 'ARG', 'SG', 'CYS', 7.66)], [('NE', 'ARG', 'CB', 'CYS', 8.68), ('NE', 'ARG', 'SG', 'CYS', 7.57)], [('CZ', 'ARG', 'CB', 'CYS', 7.58), ('CZ', 'ARG', 'SG', 'CYS', 6.57)], [('NH1', 'ARG', 'CB', 'CYS', 6.35), ('NH1', 'ARG', 'SG', 'CYS', 5.39)], [('NH2', 'ARG', 'CB', 'CYS', 7.93), ('NH2', 'ARG', 'SG', 'CYS', 7.06)]]}
ASP_ASN = { 
	'distances':
		[[9.86, 9.12, 9.88, 7.84], [9.05, 8.16, 8.84, 6.84], [9.79, 8.77, 9.31, 7.47], [7.83, 6.99, 7.75, 5.67]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 9.86), ('CB', 'ASP', 'CG', 'ASN', 9.12), ('CB', 'ASP', 'OD1', 'ASN', 9.88), ('CB', 'ASP', 'ND2', 'ASN', 7.84)], [('CG', 'ASP', 'CB', 'ASN', 9.05), ('CG', 'ASP', 'CG', 'ASN', 8.16), ('CG', 'ASP', 'OD1', 'ASN', 8.84), ('CG', 'ASP', 'ND2', 'ASN', 6.84)], [('OD1', 'ASP', 'CB', 'ASN', 9.79), ('OD1', 'ASP', 'CG', 'ASN', 8.77), ('OD1', 'ASP', 'OD1', 'ASN', 9.31), ('OD1', 'ASP', 'ND2', 'ASN', 7.47)], [('OD2', 'ASP', 'CB', 'ASN', 7.83), ('OD2', 'ASP', 'CG', 'ASN', 6.99), ('OD2', 'ASP', 'OD1', 'ASN', 7.75), ('OD2', 'ASP', 'ND2', 'ASN', 5.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_CYS, d, 'A_1uae_2_5_1_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ARG, d, 'A_1uae_2_5_1_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_CYS, d, 'A_1uae_2_5_1_7')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_ARG, d, 'A_1uae_2_5_1_7')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_CYS, d, 'A_1uae_2_5_1_7')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_ASN, d, 'A_1uae_2_5_1_7')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_CYS' :  match1,
		'ASP_ARG' :  match2,
		'ASN_CYS' :  match3,
		'ASN_ARG' :  match4,
		'ARG_CYS' :  match5,
		'ASP_ASN' :  match6}