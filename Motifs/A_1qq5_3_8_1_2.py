'''
FUNC:A_1qq5_3_8_1_2
PDB:1qq5
EC:3.8.1.2
RESI:asp,thr,arg,asn,lys,ser,asn,phe,asp
LOCI:a-8,12,39,115,147,171,173,175,176;
'''
import motifFunctions as cmd
THR_ARG = { 
	'distances':
		[[15.02, 13.71, 12.86, 11.63, 10.89, 11.36, 9.87], [14.5, 13.11, 12.3, 10.97, 10.23, 10.81, 9.09], [16.48, 15.17, 14.35, 13.1, 12.37, 12.86, 11.32]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ARG', 15.02), ('CB', 'THR', 'CG', 'ARG', 13.71), ('CB', 'THR', 'CD', 'ARG', 12.86), ('CB', 'THR', 'NE', 'ARG', 11.63), ('CB', 'THR', 'CZ', 'ARG', 10.89), ('CB', 'THR', 'NH1', 'ARG', 11.36), ('CB', 'THR', 'NH2', 'ARG', 9.87)], [('OG1', 'THR', 'CB', 'ARG', 14.5), ('OG1', 'THR', 'CG', 'ARG', 13.11), ('OG1', 'THR', 'CD', 'ARG', 12.3), ('OG1', 'THR', 'NE', 'ARG', 10.97), ('OG1', 'THR', 'CZ', 'ARG', 10.23), ('OG1', 'THR', 'NH1', 'ARG', 10.81), ('OG1', 'THR', 'NH2', 'ARG', 9.09)], [('CG2', 'THR', 'CB', 'ARG', 16.48), ('CG2', 'THR', 'CG', 'ARG', 15.17), ('CG2', 'THR', 'CD', 'ARG', 14.35), ('CG2', 'THR', 'NE', 'ARG', 13.1), ('CG2', 'THR', 'CZ', 'ARG', 12.37), ('CG2', 'THR', 'NH1', 'ARG', 12.86), ('CG2', 'THR', 'NH2', 'ARG', 11.32)]]}
THR_PHE = { 
	'distances':
		[[14.19, 13.19, 12.4, 13.22, 11.6, 12.48, 11.64], [12.79, 11.84, 11.06, 11.93, 10.32, 11.27, 10.44], [14.93, 14.04, 13.34, 14.07, 12.65, 13.42, 12.69]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'PHE', 14.19), ('CB', 'THR', 'CG', 'PHE', 13.19), ('CB', 'THR', 'CD1', 'PHE', 12.4), ('CB', 'THR', 'CD2', 'PHE', 13.22), ('CB', 'THR', 'CE1', 'PHE', 11.6), ('CB', 'THR', 'CE2', 'PHE', 12.48), ('CB', 'THR', 'CZ', 'PHE', 11.64)], [('OG1', 'THR', 'CB', 'PHE', 12.79), ('OG1', 'THR', 'CG', 'PHE', 11.84), ('OG1', 'THR', 'CD1', 'PHE', 11.06), ('OG1', 'THR', 'CD2', 'PHE', 11.93), ('OG1', 'THR', 'CE1', 'PHE', 10.32), ('OG1', 'THR', 'CE2', 'PHE', 11.27), ('OG1', 'THR', 'CZ', 'PHE', 10.44)], [('CG2', 'THR', 'CB', 'PHE', 14.93), ('CG2', 'THR', 'CG', 'PHE', 14.04), ('CG2', 'THR', 'CD1', 'PHE', 13.34), ('CG2', 'THR', 'CD2', 'PHE', 14.07), ('CG2', 'THR', 'CE1', 'PHE', 12.65), ('CG2', 'THR', 'CE2', 'PHE', 13.42), ('CG2', 'THR', 'CZ', 'PHE', 12.69)]]}
PHE_ASPI = { 
	'distances':
		[[7.31, 8.61, 8.83, 9.61], [6.55, 7.77, 8.06, 8.68], [6.69, 7.97, 8.5, 8.68], [6.24, 7.18, 7.25, 8.16], [6.57, 7.64, 8.24, 8.17], [6.09, 6.79, 6.91, 7.61], [6.27, 7.04, 7.46, 7.62]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ASPI', 7.31), ('CB', 'PHE', 'CG', 'ASPI', 8.61), ('CB', 'PHE', 'OD1', 'ASPI', 8.83), ('CB', 'PHE', 'OD2', 'ASPI', 9.61)], [('CG', 'PHE', 'CB', 'ASPI', 6.55), ('CG', 'PHE', 'CG', 'ASPI', 7.77), ('CG', 'PHE', 'OD1', 'ASPI', 8.06), ('CG', 'PHE', 'OD2', 'ASPI', 8.68)], [('CD1', 'PHE', 'CB', 'ASPI', 6.69), ('CD1', 'PHE', 'CG', 'ASPI', 7.97), ('CD1', 'PHE', 'OD1', 'ASPI', 8.5), ('CD1', 'PHE', 'OD2', 'ASPI', 8.68)], [('CD2', 'PHE', 'CB', 'ASPI', 6.24), ('CD2', 'PHE', 'CG', 'ASPI', 7.18), ('CD2', 'PHE', 'OD1', 'ASPI', 7.25), ('CD2', 'PHE', 'OD2', 'ASPI', 8.16)], [('CE1', 'PHE', 'CB', 'ASPI', 6.57), ('CE1', 'PHE', 'CG', 'ASPI', 7.64), ('CE1', 'PHE', 'OD1', 'ASPI', 8.24), ('CE1', 'PHE', 'OD2', 'ASPI', 8.17)], [('CE2', 'PHE', 'CB', 'ASPI', 6.09), ('CE2', 'PHE', 'CG', 'ASPI', 6.79), ('CE2', 'PHE', 'OD1', 'ASPI', 6.91), ('CE2', 'PHE', 'OD2', 'ASPI', 7.61)], [('CZ', 'PHE', 'CB', 'ASPI', 6.27), ('CZ', 'PHE', 'CG', 'ASPI', 7.04), ('CZ', 'PHE', 'OD1', 'ASPI', 7.46), ('CZ', 'PHE', 'OD2', 'ASPI', 7.62)]]}
ARG_ASNI = { 
	'distances':
		[[13.96, 14.08, 15.22, 13.03], [13.19, 13.2, 14.31, 12.08], [11.76, 11.84, 12.98, 10.76], [11.27, 11.21, 12.31, 10.07], [10.06, 10.0, 11.1, 8.89], [9.11, 9.23, 10.39, 8.22], [9.98, 9.75, 10.77, 8.61]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASNI', 13.96), ('CB', 'ARG', 'CG', 'ASNI', 14.08), ('CB', 'ARG', 'OD1', 'ASNI', 15.22), ('CB', 'ARG', 'ND2', 'ASNI', 13.03)], [('CG', 'ARG', 'CB', 'ASNI', 13.19), ('CG', 'ARG', 'CG', 'ASNI', 13.2), ('CG', 'ARG', 'OD1', 'ASNI', 14.31), ('CG', 'ARG', 'ND2', 'ASNI', 12.08)], [('CD', 'ARG', 'CB', 'ASNI', 11.76), ('CD', 'ARG', 'CG', 'ASNI', 11.84), ('CD', 'ARG', 'OD1', 'ASNI', 12.98), ('CD', 'ARG', 'ND2', 'ASNI', 10.76)], [('NE', 'ARG', 'CB', 'ASNI', 11.27), ('NE', 'ARG', 'CG', 'ASNI', 11.21), ('NE', 'ARG', 'OD1', 'ASNI', 12.31), ('NE', 'ARG', 'ND2', 'ASNI', 10.07)], [('CZ', 'ARG', 'CB', 'ASNI', 10.06), ('CZ', 'ARG', 'CG', 'ASNI', 10.0), ('CZ', 'ARG', 'OD1', 'ASNI', 11.1), ('CZ', 'ARG', 'ND2', 'ASNI', 8.89)], [('NH1', 'ARG', 'CB', 'ASNI', 9.11), ('NH1', 'ARG', 'CG', 'ASNI', 9.23), ('NH1', 'ARG', 'OD1', 'ASNI', 10.39), ('NH1', 'ARG', 'ND2', 'ASNI', 8.22)], [('NH2', 'ARG', 'CB', 'ASNI', 9.98), ('NH2', 'ARG', 'CG', 'ASNI', 9.75), ('NH2', 'ARG', 'OD1', 'ASNI', 10.77), ('NH2', 'ARG', 'ND2', 'ASNI', 8.61)]]}
ASN_ARG = { 
	'distances':
		[[12.56, 11.03, 10.47, 9.04, 8.45, 9.34, 7.17], [11.23, 9.71, 9.12, 7.67, 7.13, 8.1, 5.85], [10.29, 8.76, 8.36, 6.94, 6.66, 7.79, 5.52], [11.31, 9.82, 9.05, 7.61, 6.88, 7.7, 5.57], [13.96, 13.19, 11.76, 11.27, 10.06, 9.11, 9.98], [14.08, 13.2, 11.84, 11.21, 10.0, 9.23, 9.75], [15.22, 14.31, 12.98, 12.31, 11.1, 10.39, 10.77], [13.03, 12.08, 10.76, 10.07, 8.89, 8.22, 8.61]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ARG', 12.56), ('CB', 'ASN', 'CG', 'ARG', 11.03), ('CB', 'ASN', 'CD', 'ARG', 10.47), ('CB', 'ASN', 'NE', 'ARG', 9.04), ('CB', 'ASN', 'CZ', 'ARG', 8.45), ('CB', 'ASN', 'NH1', 'ARG', 9.34), ('CB', 'ASN', 'NH2', 'ARG', 7.17)], [('CG', 'ASN', 'CB', 'ARG', 11.23), ('CG', 'ASN', 'CG', 'ARG', 9.71), ('CG', 'ASN', 'CD', 'ARG', 9.12), ('CG', 'ASN', 'NE', 'ARG', 7.67), ('CG', 'ASN', 'CZ', 'ARG', 7.13), ('CG', 'ASN', 'NH1', 'ARG', 8.1), ('CG', 'ASN', 'NH2', 'ARG', 5.85)], [('OD1', 'ASN', 'CB', 'ARG', 10.29), ('OD1', 'ASN', 'CG', 'ARG', 8.76), ('OD1', 'ASN', 'CD', 'ARG', 8.36), ('OD1', 'ASN', 'NE', 'ARG', 6.94), ('OD1', 'ASN', 'CZ', 'ARG', 6.66), ('OD1', 'ASN', 'NH1', 'ARG', 7.79), ('OD1', 'ASN', 'NH2', 'ARG', 5.52)], [('ND2', 'ASN', 'CB', 'ARG', 11.31), ('ND2', 'ASN', 'CG', 'ARG', 9.82), ('ND2', 'ASN', 'CD', 'ARG', 9.05), ('ND2', 'ASN', 'NE', 'ARG', 7.61), ('ND2', 'ASN', 'CZ', 'ARG', 6.88), ('ND2', 'ASN', 'NH1', 'ARG', 7.7), ('ND2', 'ASN', 'NH2', 'ARG', 5.57)], [('CB', 'ASN', 'CB', 'ARG', 13.96), ('CB', 'ASN', 'CG', 'ARG', 13.19), ('CB', 'ASN', 'CD', 'ARG', 11.76), ('CB', 'ASN', 'NE', 'ARG', 11.27), ('CB', 'ASN', 'CZ', 'ARG', 10.06), ('CB', 'ASN', 'NH1', 'ARG', 9.11), ('CB', 'ASN', 'NH2', 'ARG', 9.98)], [('CG', 'ASN', 'CB', 'ARG', 14.08), ('CG', 'ASN', 'CG', 'ARG', 13.2), ('CG', 'ASN', 'CD', 'ARG', 11.84), ('CG', 'ASN', 'NE', 'ARG', 11.21), ('CG', 'ASN', 'CZ', 'ARG', 10.0), ('CG', 'ASN', 'NH1', 'ARG', 9.23), ('CG', 'ASN', 'NH2', 'ARG', 9.75)], [('OD1', 'ASN', 'CB', 'ARG', 15.22), ('OD1', 'ASN', 'CG', 'ARG', 14.31), ('OD1', 'ASN', 'CD', 'ARG', 12.98), ('OD1', 'ASN', 'NE', 'ARG', 12.31), ('OD1', 'ASN', 'CZ', 'ARG', 11.1), ('OD1', 'ASN', 'NH1', 'ARG', 10.39), ('OD1', 'ASN', 'NH2', 'ARG', 10.77)], [('ND2', 'ASN', 'CB', 'ARG', 13.03), ('ND2', 'ASN', 'CG', 'ARG', 12.08), ('ND2', 'ASN', 'CD', 'ARG', 10.76), ('ND2', 'ASN', 'NE', 'ARG', 10.07), ('ND2', 'ASN', 'CZ', 'ARG', 8.89), ('ND2', 'ASN', 'NH1', 'ARG', 8.22), ('ND2', 'ASN', 'NH2', 'ARG', 8.61)]]}
THR_ASN = { 
	'distances':
		[[8.8, 8.38, 9.24, 7.31], [7.4, 7.11, 8.05, 6.13], [9.68, 9.49, 10.4, 8.53], [13.54, 13.4, 14.0, 12.85], [13.07, 12.77, 13.34, 12.12], [14.66, 14.48, 14.98, 13.99]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASN', 8.8), ('CB', 'THR', 'CG', 'ASN', 8.38), ('CB', 'THR', 'OD1', 'ASN', 9.24), ('CB', 'THR', 'ND2', 'ASN', 7.31)], [('OG1', 'THR', 'CB', 'ASN', 7.4), ('OG1', 'THR', 'CG', 'ASN', 7.11), ('OG1', 'THR', 'OD1', 'ASN', 8.05), ('OG1', 'THR', 'ND2', 'ASN', 6.13)], [('CG2', 'THR', 'CB', 'ASN', 9.68), ('CG2', 'THR', 'CG', 'ASN', 9.49), ('CG2', 'THR', 'OD1', 'ASN', 10.4), ('CG2', 'THR', 'ND2', 'ASN', 8.53)], [('CB', 'THR', 'CB', 'ASN', 13.54), ('CB', 'THR', 'CG', 'ASN', 13.4), ('CB', 'THR', 'OD1', 'ASN', 14.0), ('CB', 'THR', 'ND2', 'ASN', 12.85)], [('OG1', 'THR', 'CB', 'ASN', 13.07), ('OG1', 'THR', 'CG', 'ASN', 12.77), ('OG1', 'THR', 'OD1', 'ASN', 13.34), ('OG1', 'THR', 'ND2', 'ASN', 12.12)], [('CG2', 'THR', 'CB', 'ASN', 14.66), ('CG2', 'THR', 'CG', 'ASN', 14.48), ('CG2', 'THR', 'OD1', 'ASN', 14.98), ('CG2', 'THR', 'ND2', 'ASN', 13.99)]]}
SER_ARG = { 
	'distances':
		[[16.85, 15.35, 14.57, 13.13, 12.29, 12.88, 10.98], [15.49, 13.99, 13.21, 11.76, 10.92, 11.54, 9.61]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 16.85), ('CB', 'SER', 'CG', 'ARG', 15.35), ('CB', 'SER', 'CD', 'ARG', 14.57), ('CB', 'SER', 'NE', 'ARG', 13.13), ('CB', 'SER', 'CZ', 'ARG', 12.29), ('CB', 'SER', 'NH1', 'ARG', 12.88), ('CB', 'SER', 'NH2', 'ARG', 10.98)], [('OG', 'SER', 'CB', 'ARG', 15.49), ('OG', 'SER', 'CG', 'ARG', 13.99), ('OG', 'SER', 'CD', 'ARG', 13.21), ('OG', 'SER', 'NE', 'ARG', 11.76), ('OG', 'SER', 'CZ', 'ARG', 10.92), ('OG', 'SER', 'NH1', 'ARG', 11.54), ('OG', 'SER', 'NH2', 'ARG', 9.61)]]}
ASP_PHE = { 
	'distances':
		[[12.18, 11.12, 10.72, 10.75, 9.92, 9.96, 9.51], [11.42, 10.23, 9.71, 9.89, 8.77, 8.97, 8.35], [11.16, 9.89, 9.45, 9.37, 8.41, 8.32, 7.77], [11.3, 10.13, 9.42, 9.98, 8.47, 9.11, 8.3], [7.31, 6.55, 6.69, 6.24, 6.57, 6.09, 6.27], [8.61, 7.77, 7.97, 7.18, 7.64, 6.79, 7.04], [8.83, 8.06, 8.5, 7.25, 8.24, 6.91, 7.46], [9.61, 8.68, 8.68, 8.16, 8.17, 7.61, 7.62]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'PHE', 12.18), ('CB', 'ASP', 'CG', 'PHE', 11.12), ('CB', 'ASP', 'CD1', 'PHE', 10.72), ('CB', 'ASP', 'CD2', 'PHE', 10.75), ('CB', 'ASP', 'CE1', 'PHE', 9.92), ('CB', 'ASP', 'CE2', 'PHE', 9.96), ('CB', 'ASP', 'CZ', 'PHE', 9.51)], [('CG', 'ASP', 'CB', 'PHE', 11.42), ('CG', 'ASP', 'CG', 'PHE', 10.23), ('CG', 'ASP', 'CD1', 'PHE', 9.71), ('CG', 'ASP', 'CD2', 'PHE', 9.89), ('CG', 'ASP', 'CE1', 'PHE', 8.77), ('CG', 'ASP', 'CE2', 'PHE', 8.97), ('CG', 'ASP', 'CZ', 'PHE', 8.35)], [('OD1', 'ASP', 'CB', 'PHE', 11.16), ('OD1', 'ASP', 'CG', 'PHE', 9.89), ('OD1', 'ASP', 'CD1', 'PHE', 9.45), ('OD1', 'ASP', 'CD2', 'PHE', 9.37), ('OD1', 'ASP', 'CE1', 'PHE', 8.41), ('OD1', 'ASP', 'CE2', 'PHE', 8.32), ('OD1', 'ASP', 'CZ', 'PHE', 7.77)], [('OD2', 'ASP', 'CB', 'PHE', 11.3), ('OD2', 'ASP', 'CG', 'PHE', 10.13), ('OD2', 'ASP', 'CD1', 'PHE', 9.42), ('OD2', 'ASP', 'CD2', 'PHE', 9.98), ('OD2', 'ASP', 'CE1', 'PHE', 8.47), ('OD2', 'ASP', 'CE2', 'PHE', 9.11), ('OD2', 'ASP', 'CZ', 'PHE', 8.3)], [('CB', 'ASP', 'CB', 'PHE', 7.31), ('CB', 'ASP', 'CG', 'PHE', 6.55), ('CB', 'ASP', 'CD1', 'PHE', 6.69), ('CB', 'ASP', 'CD2', 'PHE', 6.24), ('CB', 'ASP', 'CE1', 'PHE', 6.57), ('CB', 'ASP', 'CE2', 'PHE', 6.09), ('CB', 'ASP', 'CZ', 'PHE', 6.27)], [('CG', 'ASP', 'CB', 'PHE', 8.61), ('CG', 'ASP', 'CG', 'PHE', 7.77), ('CG', 'ASP', 'CD1', 'PHE', 7.97), ('CG', 'ASP', 'CD2', 'PHE', 7.18), ('CG', 'ASP', 'CE1', 'PHE', 7.64), ('CG', 'ASP', 'CE2', 'PHE', 6.79), ('CG', 'ASP', 'CZ', 'PHE', 7.04)], [('OD1', 'ASP', 'CB', 'PHE', 8.83), ('OD1', 'ASP', 'CG', 'PHE', 8.06), ('OD1', 'ASP', 'CD1', 'PHE', 8.5), ('OD1', 'ASP', 'CD2', 'PHE', 7.25), ('OD1', 'ASP', 'CE1', 'PHE', 8.24), ('OD1', 'ASP', 'CE2', 'PHE', 6.91), ('OD1', 'ASP', 'CZ', 'PHE', 7.46)], [('OD2', 'ASP', 'CB', 'PHE', 9.61), ('OD2', 'ASP', 'CG', 'PHE', 8.68), ('OD2', 'ASP', 'CD1', 'PHE', 8.68), ('OD2', 'ASP', 'CD2', 'PHE', 8.16), ('OD2', 'ASP', 'CE1', 'PHE', 8.17), ('OD2', 'ASP', 'CE2', 'PHE', 7.61), ('OD2', 'ASP', 'CZ', 'PHE', 7.62)]]}
SER_ASP = { 
	'distances':
		[[5.68, 6.31, 7.19, 6.35], [5.44, 5.54, 6.36, 5.39], [6.15, 6.12, 7.16, 5.46], [5.37, 5.59, 6.8, 4.98]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 5.68), ('CB', 'SER', 'CG', 'ASP', 6.31), ('CB', 'SER', 'OD1', 'ASP', 7.19), ('CB', 'SER', 'OD2', 'ASP', 6.35)], [('OG', 'SER', 'CB', 'ASP', 5.44), ('OG', 'SER', 'CG', 'ASP', 5.54), ('OG', 'SER', 'OD1', 'ASP', 6.36), ('OG', 'SER', 'OD2', 'ASP', 5.39)], [('CB', 'SER', 'CB', 'ASP', 6.15), ('CB', 'SER', 'CG', 'ASP', 6.12), ('CB', 'SER', 'OD1', 'ASP', 7.16), ('CB', 'SER', 'OD2', 'ASP', 5.46)], [('OG', 'SER', 'CB', 'ASP', 5.37), ('OG', 'SER', 'CG', 'ASP', 5.59), ('OG', 'SER', 'OD1', 'ASP', 6.8), ('OG', 'SER', 'OD2', 'ASP', 4.98)]]}
ASN_ASN = { 
	'distances':
		[[12.11, 11.25, 11.73, 10.16], [11.76, 11.09, 11.75, 9.96], [12.25, 11.61, 12.34, 10.4], [11.18, 10.65, 11.36, 9.61], [12.11, 11.76, 12.25, 11.18], [11.25, 11.09, 11.61, 10.65], [11.73, 11.75, 12.34, 11.36], [10.16, 9.96, 10.4, 9.61]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASN', 12.11), ('CB', 'ASN', 'CG', 'ASN', 11.25), ('CB', 'ASN', 'OD1', 'ASN', 11.73), ('CB', 'ASN', 'ND2', 'ASN', 10.16)], [('CG', 'ASN', 'CB', 'ASN', 11.76), ('CG', 'ASN', 'CG', 'ASN', 11.09), ('CG', 'ASN', 'OD1', 'ASN', 11.75), ('CG', 'ASN', 'ND2', 'ASN', 9.96)], [('OD1', 'ASN', 'CB', 'ASN', 12.25), ('OD1', 'ASN', 'CG', 'ASN', 11.61), ('OD1', 'ASN', 'OD1', 'ASN', 12.34), ('OD1', 'ASN', 'ND2', 'ASN', 10.4)], [('ND2', 'ASN', 'CB', 'ASN', 11.18), ('ND2', 'ASN', 'CG', 'ASN', 10.65), ('ND2', 'ASN', 'OD1', 'ASN', 11.36), ('ND2', 'ASN', 'ND2', 'ASN', 9.61)], [('CB', 'ASN', 'CB', 'ASN', 12.11), ('CB', 'ASN', 'CG', 'ASN', 11.76), ('CB', 'ASN', 'OD1', 'ASN', 12.25), ('CB', 'ASN', 'ND2', 'ASN', 11.18)], [('CG', 'ASN', 'CB', 'ASN', 11.25), ('CG', 'ASN', 'CG', 'ASN', 11.09), ('CG', 'ASN', 'OD1', 'ASN', 11.61), ('CG', 'ASN', 'ND2', 'ASN', 10.65)], [('OD1', 'ASN', 'CB', 'ASN', 11.73), ('OD1', 'ASN', 'CG', 'ASN', 11.75), ('OD1', 'ASN', 'OD1', 'ASN', 12.34), ('OD1', 'ASN', 'ND2', 'ASN', 11.36)], [('ND2', 'ASN', 'CB', 'ASN', 10.16), ('ND2', 'ASN', 'CG', 'ASN', 9.96), ('ND2', 'ASN', 'OD1', 'ASN', 10.4), ('ND2', 'ASN', 'ND2', 'ASN', 9.61)]]}
ASP_THR = { 
	'distances':
		[[5.86, 5.37, 6.32], [6.07, 5.37, 6.98], [7.23, 6.58, 8.17], [5.47, 4.58, 6.6], [9.92, 8.66, 10.44], [9.69, 8.59, 10.13], [10.77, 9.75, 11.16], [8.57, 7.57, 8.99]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 5.86), ('CB', 'ASP', 'OG1', 'THR', 5.37), ('CB', 'ASP', 'CG2', 'THR', 6.32)], [('CG', 'ASP', 'CB', 'THR', 6.07), ('CG', 'ASP', 'OG1', 'THR', 5.37), ('CG', 'ASP', 'CG2', 'THR', 6.98)], [('OD1', 'ASP', 'CB', 'THR', 7.23), ('OD1', 'ASP', 'OG1', 'THR', 6.58), ('OD1', 'ASP', 'CG2', 'THR', 8.17)], [('OD2', 'ASP', 'CB', 'THR', 5.47), ('OD2', 'ASP', 'OG1', 'THR', 4.58), ('OD2', 'ASP', 'CG2', 'THR', 6.6)], [('CB', 'ASP', 'CB', 'THR', 9.92), ('CB', 'ASP', 'OG1', 'THR', 8.66), ('CB', 'ASP', 'CG2', 'THR', 10.44)], [('CG', 'ASP', 'CB', 'THR', 9.69), ('CG', 'ASP', 'OG1', 'THR', 8.59), ('CG', 'ASP', 'CG2', 'THR', 10.13)], [('OD1', 'ASP', 'CB', 'THR', 10.77), ('OD1', 'ASP', 'OG1', 'THR', 9.75), ('OD1', 'ASP', 'CG2', 'THR', 11.16)], [('OD2', 'ASP', 'CB', 'THR', 8.57), ('OD2', 'ASP', 'OG1', 'THR', 7.57), ('OD2', 'ASP', 'CG2', 'THR', 8.99)]]}
SER_LYS = { 
	'distances':
		[[11.0, 10.94, 9.62, 9.22, 8.18], [10.31, 10.4, 9.16, 8.57, 7.66]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 11.0), ('CB', 'SER', 'CG', 'LYS', 10.94), ('CB', 'SER', 'CD', 'LYS', 9.62), ('CB', 'SER', 'CE', 'LYS', 9.22), ('CB', 'SER', 'NZ', 'LYS', 8.18)], [('OG', 'SER', 'CB', 'LYS', 10.31), ('OG', 'SER', 'CG', 'LYS', 10.4), ('OG', 'SER', 'CD', 'LYS', 9.16), ('OG', 'SER', 'CE', 'LYS', 8.57), ('OG', 'SER', 'NZ', 'LYS', 7.66)]]}
ASP_ASN = { 
	'distances':
		[[8.01, 8.14, 9.31, 7.16], [7.13, 7.02, 8.15, 5.96], [7.47, 7.36, 8.42, 6.36], [6.44, 6.11, 7.18, 4.94], [10.98, 10.59, 10.9, 10.23], [9.98, 9.6, 10.06, 9.09], [8.76, 8.37, 8.83, 7.92], [10.57, 10.21, 10.79, 9.54], [5.94, 7.1, 8.13, 7.25], [7.06, 8.01, 9.13, 7.85], [8.18, 9.14, 10.21, 8.99], [7.08, 7.83, 9.03, 7.42], [11.08, 9.94, 9.94, 9.22], [10.51, 9.45, 9.35, 8.95], [10.35, 9.21, 8.91, 8.87], [10.48, 9.6, 9.61, 9.14]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 8.01), ('CB', 'ASP', 'CG', 'ASN', 8.14), ('CB', 'ASP', 'OD1', 'ASN', 9.31), ('CB', 'ASP', 'ND2', 'ASN', 7.16)], [('CG', 'ASP', 'CB', 'ASN', 7.13), ('CG', 'ASP', 'CG', 'ASN', 7.02), ('CG', 'ASP', 'OD1', 'ASN', 8.15), ('CG', 'ASP', 'ND2', 'ASN', 5.96)], [('OD1', 'ASP', 'CB', 'ASN', 7.47), ('OD1', 'ASP', 'CG', 'ASN', 7.36), ('OD1', 'ASP', 'OD1', 'ASN', 8.42), ('OD1', 'ASP', 'ND2', 'ASN', 6.36)], [('OD2', 'ASP', 'CB', 'ASN', 6.44), ('OD2', 'ASP', 'CG', 'ASN', 6.11), ('OD2', 'ASP', 'OD1', 'ASN', 7.18), ('OD2', 'ASP', 'ND2', 'ASN', 4.94)], [('CB', 'ASP', 'CB', 'ASN', 10.98), ('CB', 'ASP', 'CG', 'ASN', 10.59), ('CB', 'ASP', 'OD1', 'ASN', 10.9), ('CB', 'ASP', 'ND2', 'ASN', 10.23)], [('CG', 'ASP', 'CB', 'ASN', 9.98), ('CG', 'ASP', 'CG', 'ASN', 9.6), ('CG', 'ASP', 'OD1', 'ASN', 10.06), ('CG', 'ASP', 'ND2', 'ASN', 9.09)], [('OD1', 'ASP', 'CB', 'ASN', 8.76), ('OD1', 'ASP', 'CG', 'ASN', 8.37), ('OD1', 'ASP', 'OD1', 'ASN', 8.83), ('OD1', 'ASP', 'ND2', 'ASN', 7.92)], [('OD2', 'ASP', 'CB', 'ASN', 10.57), ('OD2', 'ASP', 'CG', 'ASN', 10.21), ('OD2', 'ASP', 'OD1', 'ASN', 10.79), ('OD2', 'ASP', 'ND2', 'ASN', 9.54)], [('CB', 'ASP', 'CB', 'ASN', 5.94), ('CB', 'ASP', 'CG', 'ASN', 7.1), ('CB', 'ASP', 'OD1', 'ASN', 8.13), ('CB', 'ASP', 'ND2', 'ASN', 7.25)], [('CG', 'ASP', 'CB', 'ASN', 7.06), ('CG', 'ASP', 'CG', 'ASN', 8.01), ('CG', 'ASP', 'OD1', 'ASN', 9.13), ('CG', 'ASP', 'ND2', 'ASN', 7.85)], [('OD1', 'ASP', 'CB', 'ASN', 8.18), ('OD1', 'ASP', 'CG', 'ASN', 9.14), ('OD1', 'ASP', 'OD1', 'ASN', 10.21), ('OD1', 'ASP', 'ND2', 'ASN', 8.99)], [('OD2', 'ASP', 'CB', 'ASN', 7.08), ('OD2', 'ASP', 'CG', 'ASN', 7.83), ('OD2', 'ASP', 'OD1', 'ASN', 9.03), ('OD2', 'ASP', 'ND2', 'ASN', 7.42)], [('CB', 'ASP', 'CB', 'ASN', 11.08), ('CB', 'ASP', 'CG', 'ASN', 9.94), ('CB', 'ASP', 'OD1', 'ASN', 9.94), ('CB', 'ASP', 'ND2', 'ASN', 9.22)], [('CG', 'ASP', 'CB', 'ASN', 10.51), ('CG', 'ASP', 'CG', 'ASN', 9.45), ('CG', 'ASP', 'OD1', 'ASN', 9.35), ('CG', 'ASP', 'ND2', 'ASN', 8.95)], [('OD1', 'ASP', 'CB', 'ASN', 10.35), ('OD1', 'ASP', 'CG', 'ASN', 9.21), ('OD1', 'ASP', 'OD1', 'ASN', 8.91), ('OD1', 'ASP', 'ND2', 'ASN', 8.87)], [('OD2', 'ASP', 'CB', 'ASN', 10.48), ('OD2', 'ASP', 'CG', 'ASN', 9.6), ('OD2', 'ASP', 'OD1', 'ASN', 9.61), ('OD2', 'ASP', 'ND2', 'ASN', 9.14)]]}
ARG_ASPI = { 
	'distances':
		[[15.55, 16.24, 17.04, 16.08], [14.09, 14.81, 15.65, 14.66], [13.24, 13.83, 14.63, 13.63], [11.87, 12.48, 13.33, 12.28], [10.93, 11.42, 12.24, 11.19], [11.36, 11.68, 12.39, 11.43], [9.71, 10.24, 11.12, 9.99]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASPI', 15.55), ('CB', 'ARG', 'CG', 'ASPI', 16.24), ('CB', 'ARG', 'OD1', 'ASPI', 17.04), ('CB', 'ARG', 'OD2', 'ASPI', 16.08)], [('CG', 'ARG', 'CB', 'ASPI', 14.09), ('CG', 'ARG', 'CG', 'ASPI', 14.81), ('CG', 'ARG', 'OD1', 'ASPI', 15.65), ('CG', 'ARG', 'OD2', 'ASPI', 14.66)], [('CD', 'ARG', 'CB', 'ASPI', 13.24), ('CD', 'ARG', 'CG', 'ASPI', 13.83), ('CD', 'ARG', 'OD1', 'ASPI', 14.63), ('CD', 'ARG', 'OD2', 'ASPI', 13.63)], [('NE', 'ARG', 'CB', 'ASPI', 11.87), ('NE', 'ARG', 'CG', 'ASPI', 12.48), ('NE', 'ARG', 'OD1', 'ASPI', 13.33), ('NE', 'ARG', 'OD2', 'ASPI', 12.28)], [('CZ', 'ARG', 'CB', 'ASPI', 10.93), ('CZ', 'ARG', 'CG', 'ASPI', 11.42), ('CZ', 'ARG', 'OD1', 'ASPI', 12.24), ('CZ', 'ARG', 'OD2', 'ASPI', 11.19)], [('NH1', 'ARG', 'CB', 'ASPI', 11.36), ('NH1', 'ARG', 'CG', 'ASPI', 11.68), ('NH1', 'ARG', 'OD1', 'ASPI', 12.39), ('NH1', 'ARG', 'OD2', 'ASPI', 11.43)], [('NH2', 'ARG', 'CB', 'ASPI', 9.71), ('NH2', 'ARG', 'CG', 'ASPI', 10.24), ('NH2', 'ARG', 'OD1', 'ASPI', 11.12), ('NH2', 'ARG', 'OD2', 'ASPI', 9.99)]]}
LYS_ARG = { 
	'distances':
		[[16.64, 15.48, 14.33, 13.34, 12.19, 11.93, 11.45], [17.34, 16.18, 14.95, 13.95, 12.73, 12.39, 11.98], [17.15, 15.92, 14.68, 13.59, 12.34, 12.09, 11.48], [15.82, 14.61, 13.33, 12.25, 10.97, 10.7, 10.14], [15.97, 14.71, 13.44, 12.28, 11.01, 10.83, 10.08]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 16.64), ('CB', 'LYS', 'CG', 'ARG', 15.48), ('CB', 'LYS', 'CD', 'ARG', 14.33), ('CB', 'LYS', 'NE', 'ARG', 13.34), ('CB', 'LYS', 'CZ', 'ARG', 12.19), ('CB', 'LYS', 'NH1', 'ARG', 11.93), ('CB', 'LYS', 'NH2', 'ARG', 11.45)], [('CG', 'LYS', 'CB', 'ARG', 17.34), ('CG', 'LYS', 'CG', 'ARG', 16.18), ('CG', 'LYS', 'CD', 'ARG', 14.95), ('CG', 'LYS', 'NE', 'ARG', 13.95), ('CG', 'LYS', 'CZ', 'ARG', 12.73), ('CG', 'LYS', 'NH1', 'ARG', 12.39), ('CG', 'LYS', 'NH2', 'ARG', 11.98)], [('CD', 'LYS', 'CB', 'ARG', 17.15), ('CD', 'LYS', 'CG', 'ARG', 15.92), ('CD', 'LYS', 'CD', 'ARG', 14.68), ('CD', 'LYS', 'NE', 'ARG', 13.59), ('CD', 'LYS', 'CZ', 'ARG', 12.34), ('CD', 'LYS', 'NH1', 'ARG', 12.09), ('CD', 'LYS', 'NH2', 'ARG', 11.48)], [('CE', 'LYS', 'CB', 'ARG', 15.82), ('CE', 'LYS', 'CG', 'ARG', 14.61), ('CE', 'LYS', 'CD', 'ARG', 13.33), ('CE', 'LYS', 'NE', 'ARG', 12.25), ('CE', 'LYS', 'CZ', 'ARG', 10.97), ('CE', 'LYS', 'NH1', 'ARG', 10.7), ('CE', 'LYS', 'NH2', 'ARG', 10.14)], [('NZ', 'LYS', 'CB', 'ARG', 15.97), ('NZ', 'LYS', 'CG', 'ARG', 14.71), ('NZ', 'LYS', 'CD', 'ARG', 13.44), ('NZ', 'LYS', 'NE', 'ARG', 12.28), ('NZ', 'LYS', 'CZ', 'ARG', 11.01), ('NZ', 'LYS', 'NH1', 'ARG', 10.83), ('NZ', 'LYS', 'NH2', 'ARG', 10.08)]]}
ASP_ARG = { 
	'distances':
		[[15.73, 14.36, 13.27, 11.96, 10.88, 11.09, 9.75], [14.28, 12.92, 11.8, 10.5, 9.39, 9.59, 8.28], [14.08, 12.77, 11.56, 10.32, 9.12, 9.13, 8.08], [13.44, 12.05, 11.02, 9.68, 8.68, 9.05, 7.52], [15.55, 14.09, 13.24, 11.87, 10.93, 11.36, 9.71], [16.24, 14.81, 13.83, 12.48, 11.42, 11.68, 10.24], [17.04, 15.65, 14.63, 13.33, 12.24, 12.39, 11.12], [16.08, 14.66, 13.63, 12.28, 11.19, 11.43, 9.99]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 15.73), ('CB', 'ASP', 'CG', 'ARG', 14.36), ('CB', 'ASP', 'CD', 'ARG', 13.27), ('CB', 'ASP', 'NE', 'ARG', 11.96), ('CB', 'ASP', 'CZ', 'ARG', 10.88), ('CB', 'ASP', 'NH1', 'ARG', 11.09), ('CB', 'ASP', 'NH2', 'ARG', 9.75)], [('CG', 'ASP', 'CB', 'ARG', 14.28), ('CG', 'ASP', 'CG', 'ARG', 12.92), ('CG', 'ASP', 'CD', 'ARG', 11.8), ('CG', 'ASP', 'NE', 'ARG', 10.5), ('CG', 'ASP', 'CZ', 'ARG', 9.39), ('CG', 'ASP', 'NH1', 'ARG', 9.59), ('CG', 'ASP', 'NH2', 'ARG', 8.28)], [('OD1', 'ASP', 'CB', 'ARG', 14.08), ('OD1', 'ASP', 'CG', 'ARG', 12.77), ('OD1', 'ASP', 'CD', 'ARG', 11.56), ('OD1', 'ASP', 'NE', 'ARG', 10.32), ('OD1', 'ASP', 'CZ', 'ARG', 9.12), ('OD1', 'ASP', 'NH1', 'ARG', 9.13), ('OD1', 'ASP', 'NH2', 'ARG', 8.08)], [('OD2', 'ASP', 'CB', 'ARG', 13.44), ('OD2', 'ASP', 'CG', 'ARG', 12.05), ('OD2', 'ASP', 'CD', 'ARG', 11.02), ('OD2', 'ASP', 'NE', 'ARG', 9.68), ('OD2', 'ASP', 'CZ', 'ARG', 8.68), ('OD2', 'ASP', 'NH1', 'ARG', 9.05), ('OD2', 'ASP', 'NH2', 'ARG', 7.52)], [('CB', 'ASP', 'CB', 'ARG', 15.55), ('CB', 'ASP', 'CG', 'ARG', 14.09), ('CB', 'ASP', 'CD', 'ARG', 13.24), ('CB', 'ASP', 'NE', 'ARG', 11.87), ('CB', 'ASP', 'CZ', 'ARG', 10.93), ('CB', 'ASP', 'NH1', 'ARG', 11.36), ('CB', 'ASP', 'NH2', 'ARG', 9.71)], [('CG', 'ASP', 'CB', 'ARG', 16.24), ('CG', 'ASP', 'CG', 'ARG', 14.81), ('CG', 'ASP', 'CD', 'ARG', 13.83), ('CG', 'ASP', 'NE', 'ARG', 12.48), ('CG', 'ASP', 'CZ', 'ARG', 11.42), ('CG', 'ASP', 'NH1', 'ARG', 11.68), ('CG', 'ASP', 'NH2', 'ARG', 10.24)], [('OD1', 'ASP', 'CB', 'ARG', 17.04), ('OD1', 'ASP', 'CG', 'ARG', 15.65), ('OD1', 'ASP', 'CD', 'ARG', 14.63), ('OD1', 'ASP', 'NE', 'ARG', 13.33), ('OD1', 'ASP', 'CZ', 'ARG', 12.24), ('OD1', 'ASP', 'NH1', 'ARG', 12.39), ('OD1', 'ASP', 'NH2', 'ARG', 11.12)], [('OD2', 'ASP', 'CB', 'ARG', 16.08), ('OD2', 'ASP', 'CG', 'ARG', 14.66), ('OD2', 'ASP', 'CD', 'ARG', 13.63), ('OD2', 'ASP', 'NE', 'ARG', 12.28), ('OD2', 'ASP', 'CZ', 'ARG', 11.19), ('OD2', 'ASP', 'NH1', 'ARG', 11.43), ('OD2', 'ASP', 'NH2', 'ARG', 9.99)]]}
ASN_LYS = { 
	'distances':
		[[10.36, 11.0, 10.21, 9.38, 9.06], [10.94, 11.52, 10.74, 9.69, 9.34], [11.71, 12.4, 11.72, 10.66, 10.41], [10.83, 11.22, 10.32, 9.16, 8.64], [7.82, 7.64, 8.0, 7.1, 8.0], [6.43, 6.47, 6.99, 6.22, 7.36], [5.66, 5.62, 6.42, 6.02, 7.34], [6.44, 6.82, 7.19, 6.26, 7.34]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'LYS', 10.36), ('CB', 'ASN', 'CG', 'LYS', 11.0), ('CB', 'ASN', 'CD', 'LYS', 10.21), ('CB', 'ASN', 'CE', 'LYS', 9.38), ('CB', 'ASN', 'NZ', 'LYS', 9.06)], [('CG', 'ASN', 'CB', 'LYS', 10.94), ('CG', 'ASN', 'CG', 'LYS', 11.52), ('CG', 'ASN', 'CD', 'LYS', 10.74), ('CG', 'ASN', 'CE', 'LYS', 9.69), ('CG', 'ASN', 'NZ', 'LYS', 9.34)], [('OD1', 'ASN', 'CB', 'LYS', 11.71), ('OD1', 'ASN', 'CG', 'LYS', 12.4), ('OD1', 'ASN', 'CD', 'LYS', 11.72), ('OD1', 'ASN', 'CE', 'LYS', 10.66), ('OD1', 'ASN', 'NZ', 'LYS', 10.41)], [('ND2', 'ASN', 'CB', 'LYS', 10.83), ('ND2', 'ASN', 'CG', 'LYS', 11.22), ('ND2', 'ASN', 'CD', 'LYS', 10.32), ('ND2', 'ASN', 'CE', 'LYS', 9.16), ('ND2', 'ASN', 'NZ', 'LYS', 8.64)], [('CB', 'ASN', 'CB', 'LYS', 7.82), ('CB', 'ASN', 'CG', 'LYS', 7.64), ('CB', 'ASN', 'CD', 'LYS', 8.0), ('CB', 'ASN', 'CE', 'LYS', 7.1), ('CB', 'ASN', 'NZ', 'LYS', 8.0)], [('CG', 'ASN', 'CB', 'LYS', 6.43), ('CG', 'ASN', 'CG', 'LYS', 6.47), ('CG', 'ASN', 'CD', 'LYS', 6.99), ('CG', 'ASN', 'CE', 'LYS', 6.22), ('CG', 'ASN', 'NZ', 'LYS', 7.36)], [('OD1', 'ASN', 'CB', 'LYS', 5.66), ('OD1', 'ASN', 'CG', 'LYS', 5.62), ('OD1', 'ASN', 'CD', 'LYS', 6.42), ('OD1', 'ASN', 'CE', 'LYS', 6.02), ('OD1', 'ASN', 'NZ', 'LYS', 7.34)], [('ND2', 'ASN', 'CB', 'LYS', 6.44), ('ND2', 'ASN', 'CG', 'LYS', 6.82), ('ND2', 'ASN', 'CD', 'LYS', 7.19), ('ND2', 'ASN', 'CE', 'LYS', 6.26), ('ND2', 'ASN', 'NZ', 'LYS', 7.34)]]}
ASN_ASPI = { 
	'distances':
		[[11.08, 10.51, 10.35, 10.48], [9.94, 9.45, 9.21, 9.6], [9.94, 9.35, 8.91, 9.61], [9.22, 8.95, 8.87, 9.14]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASPI', 11.08), ('CB', 'ASN', 'CG', 'ASPI', 10.51), ('CB', 'ASN', 'OD1', 'ASPI', 10.35), ('CB', 'ASN', 'OD2', 'ASPI', 10.48)], [('CG', 'ASN', 'CB', 'ASPI', 9.94), ('CG', 'ASN', 'CG', 'ASPI', 9.45), ('CG', 'ASN', 'OD1', 'ASPI', 9.21), ('CG', 'ASN', 'OD2', 'ASPI', 9.6)], [('OD1', 'ASN', 'CB', 'ASPI', 9.94), ('OD1', 'ASN', 'CG', 'ASPI', 9.35), ('OD1', 'ASN', 'OD1', 'ASPI', 8.91), ('OD1', 'ASN', 'OD2', 'ASPI', 9.61)], [('ND2', 'ASN', 'CB', 'ASPI', 9.22), ('ND2', 'ASN', 'CG', 'ASPI', 8.95), ('ND2', 'ASN', 'OD1', 'ASPI', 8.87), ('ND2', 'ASN', 'OD2', 'ASPI', 9.14)]]}
ASP_LYS = { 
	'distances':
		[[10.05, 9.59, 8.15, 7.28, 5.9], [9.52, 9.25, 7.95, 6.82, 5.66], [8.53, 8.23, 7.01, 5.74, 4.72], [10.31, 10.21, 8.99, 7.81, 6.79], [7.46, 7.94, 7.09, 6.87, 6.71], [6.91, 7.02, 5.92, 5.81, 5.47], [6.08, 6.12, 5.13, 5.48, 5.46], [7.65, 7.51, 6.2, 5.81, 5.01]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 10.05), ('CB', 'ASP', 'CG', 'LYS', 9.59), ('CB', 'ASP', 'CD', 'LYS', 8.15), ('CB', 'ASP', 'CE', 'LYS', 7.28), ('CB', 'ASP', 'NZ', 'LYS', 5.9)], [('CG', 'ASP', 'CB', 'LYS', 9.52), ('CG', 'ASP', 'CG', 'LYS', 9.25), ('CG', 'ASP', 'CD', 'LYS', 7.95), ('CG', 'ASP', 'CE', 'LYS', 6.82), ('CG', 'ASP', 'NZ', 'LYS', 5.66)], [('OD1', 'ASP', 'CB', 'LYS', 8.53), ('OD1', 'ASP', 'CG', 'LYS', 8.23), ('OD1', 'ASP', 'CD', 'LYS', 7.01), ('OD1', 'ASP', 'CE', 'LYS', 5.74), ('OD1', 'ASP', 'NZ', 'LYS', 4.72)], [('OD2', 'ASP', 'CB', 'LYS', 10.31), ('OD2', 'ASP', 'CG', 'LYS', 10.21), ('OD2', 'ASP', 'CD', 'LYS', 8.99), ('OD2', 'ASP', 'CE', 'LYS', 7.81), ('OD2', 'ASP', 'NZ', 'LYS', 6.79)], [('CB', 'ASP', 'CB', 'LYS', 7.46), ('CB', 'ASP', 'CG', 'LYS', 7.94), ('CB', 'ASP', 'CD', 'LYS', 7.09), ('CB', 'ASP', 'CE', 'LYS', 6.87), ('CB', 'ASP', 'NZ', 'LYS', 6.71)], [('CG', 'ASP', 'CB', 'LYS', 6.91), ('CG', 'ASP', 'CG', 'LYS', 7.02), ('CG', 'ASP', 'CD', 'LYS', 5.92), ('CG', 'ASP', 'CE', 'LYS', 5.81), ('CG', 'ASP', 'NZ', 'LYS', 5.47)], [('OD1', 'ASP', 'CB', 'LYS', 6.08), ('OD1', 'ASP', 'CG', 'LYS', 6.12), ('OD1', 'ASP', 'CD', 'LYS', 5.13), ('OD1', 'ASP', 'CE', 'LYS', 5.48), ('OD1', 'ASP', 'NZ', 'LYS', 5.46)], [('OD2', 'ASP', 'CB', 'LYS', 7.65), ('OD2', 'ASP', 'CG', 'LYS', 7.51), ('OD2', 'ASP', 'CD', 'LYS', 6.2), ('OD2', 'ASP', 'CE', 'LYS', 5.81), ('OD2', 'ASP', 'NZ', 'LYS', 5.01)]]}
ASP_ASP = { 
	'distances':
		[[7.17, 6.39, 7.25, 5.16], [6.84, 6.3, 7.24, 5.22], [6.77, 6.1, 6.85, 5.19], [7.13, 6.94, 8.02, 5.98], [7.17, 6.84, 6.77, 7.13], [6.39, 6.3, 6.1, 6.94], [7.25, 7.24, 6.85, 8.02], [5.16, 5.22, 5.19, 5.98]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 7.17), ('CB', 'ASP', 'CG', 'ASP', 6.39), ('CB', 'ASP', 'OD1', 'ASP', 7.25), ('CB', 'ASP', 'OD2', 'ASP', 5.16)], [('CG', 'ASP', 'CB', 'ASP', 6.84), ('CG', 'ASP', 'CG', 'ASP', 6.3), ('CG', 'ASP', 'OD1', 'ASP', 7.24), ('CG', 'ASP', 'OD2', 'ASP', 5.22)], [('OD1', 'ASP', 'CB', 'ASP', 6.77), ('OD1', 'ASP', 'CG', 'ASP', 6.1), ('OD1', 'ASP', 'OD1', 'ASP', 6.85), ('OD1', 'ASP', 'OD2', 'ASP', 5.19)], [('OD2', 'ASP', 'CB', 'ASP', 7.13), ('OD2', 'ASP', 'CG', 'ASP', 6.94), ('OD2', 'ASP', 'OD1', 'ASP', 8.02), ('OD2', 'ASP', 'OD2', 'ASP', 5.98)], [('CB', 'ASP', 'CB', 'ASP', 7.17), ('CB', 'ASP', 'CG', 'ASP', 6.84), ('CB', 'ASP', 'OD1', 'ASP', 6.77), ('CB', 'ASP', 'OD2', 'ASP', 7.13)], [('CG', 'ASP', 'CB', 'ASP', 6.39), ('CG', 'ASP', 'CG', 'ASP', 6.3), ('CG', 'ASP', 'OD1', 'ASP', 6.1), ('CG', 'ASP', 'OD2', 'ASP', 6.94)], [('OD1', 'ASP', 'CB', 'ASP', 7.25), ('OD1', 'ASP', 'CG', 'ASP', 7.24), ('OD1', 'ASP', 'OD1', 'ASP', 6.85), ('OD1', 'ASP', 'OD2', 'ASP', 8.02)], [('OD2', 'ASP', 'CB', 'ASP', 5.16), ('OD2', 'ASP', 'CG', 'ASP', 5.22), ('OD2', 'ASP', 'OD1', 'ASP', 5.19), ('OD2', 'ASP', 'OD2', 'ASP', 5.98)]]}
LYS_ASPI = { 
	'distances':
		[[7.46, 6.91, 6.08, 7.65], [7.94, 7.02, 6.12, 7.51], [7.09, 5.92, 5.13, 6.2], [6.87, 5.81, 5.48, 5.81], [6.71, 5.47, 5.46, 5.01]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASPI', 7.46), ('CB', 'LYS', 'CG', 'ASPI', 6.91), ('CB', 'LYS', 'OD1', 'ASPI', 6.08), ('CB', 'LYS', 'OD2', 'ASPI', 7.65)], [('CG', 'LYS', 'CB', 'ASPI', 7.94), ('CG', 'LYS', 'CG', 'ASPI', 7.02), ('CG', 'LYS', 'OD1', 'ASPI', 6.12), ('CG', 'LYS', 'OD2', 'ASPI', 7.51)], [('CD', 'LYS', 'CB', 'ASPI', 7.09), ('CD', 'LYS', 'CG', 'ASPI', 5.92), ('CD', 'LYS', 'OD1', 'ASPI', 5.13), ('CD', 'LYS', 'OD2', 'ASPI', 6.2)], [('CE', 'LYS', 'CB', 'ASPI', 6.87), ('CE', 'LYS', 'CG', 'ASPI', 5.81), ('CE', 'LYS', 'OD1', 'ASPI', 5.48), ('CE', 'LYS', 'OD2', 'ASPI', 5.81)], [('NZ', 'LYS', 'CB', 'ASPI', 6.71), ('NZ', 'LYS', 'CG', 'ASPI', 5.47), ('NZ', 'LYS', 'OD1', 'ASPI', 5.46), ('NZ', 'LYS', 'OD2', 'ASPI', 5.01)]]}
PHE_LYS = { 
	'distances':
		[[9.31, 10.63, 10.67, 10.59, 11.15], [8.35, 9.64, 9.64, 9.38, 9.97], [9.02, 10.2, 10.06, 9.55, 9.99], [6.99, 8.32, 8.46, 8.3, 9.06], [8.56, 9.64, 9.44, 8.71, 9.13], [6.3, 7.55, 7.65, 7.25, 8.06], [7.26, 8.33, 8.22, 7.51, 8.1]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'LYS', 9.31), ('CB', 'PHE', 'CG', 'LYS', 10.63), ('CB', 'PHE', 'CD', 'LYS', 10.67), ('CB', 'PHE', 'CE', 'LYS', 10.59), ('CB', 'PHE', 'NZ', 'LYS', 11.15)], [('CG', 'PHE', 'CB', 'LYS', 8.35), ('CG', 'PHE', 'CG', 'LYS', 9.64), ('CG', 'PHE', 'CD', 'LYS', 9.64), ('CG', 'PHE', 'CE', 'LYS', 9.38), ('CG', 'PHE', 'NZ', 'LYS', 9.97)], [('CD1', 'PHE', 'CB', 'LYS', 9.02), ('CD1', 'PHE', 'CG', 'LYS', 10.2), ('CD1', 'PHE', 'CD', 'LYS', 10.06), ('CD1', 'PHE', 'CE', 'LYS', 9.55), ('CD1', 'PHE', 'NZ', 'LYS', 9.99)], [('CD2', 'PHE', 'CB', 'LYS', 6.99), ('CD2', 'PHE', 'CG', 'LYS', 8.32), ('CD2', 'PHE', 'CD', 'LYS', 8.46), ('CD2', 'PHE', 'CE', 'LYS', 8.3), ('CD2', 'PHE', 'NZ', 'LYS', 9.06)], [('CE1', 'PHE', 'CB', 'LYS', 8.56), ('CE1', 'PHE', 'CG', 'LYS', 9.64), ('CE1', 'PHE', 'CD', 'LYS', 9.44), ('CE1', 'PHE', 'CE', 'LYS', 8.71), ('CE1', 'PHE', 'NZ', 'LYS', 9.13)], [('CE2', 'PHE', 'CB', 'LYS', 6.3), ('CE2', 'PHE', 'CG', 'LYS', 7.55), ('CE2', 'PHE', 'CD', 'LYS', 7.65), ('CE2', 'PHE', 'CE', 'LYS', 7.25), ('CE2', 'PHE', 'NZ', 'LYS', 8.06)], [('CZ', 'PHE', 'CB', 'LYS', 7.26), ('CZ', 'PHE', 'CG', 'LYS', 8.33), ('CZ', 'PHE', 'CD', 'LYS', 8.22), ('CZ', 'PHE', 'CE', 'LYS', 7.51), ('CZ', 'PHE', 'NZ', 'LYS', 8.1)]]}
SER_THR = { 
	'distances':
		[[7.17, 6.1, 7.08], [6.98, 5.69, 7.3]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'THR', 7.17), ('CB', 'SER', 'OG1', 'THR', 6.1), ('CB', 'SER', 'CG2', 'THR', 7.08)], [('OG', 'SER', 'CB', 'THR', 6.98), ('OG', 'SER', 'OG1', 'THR', 5.69), ('OG', 'SER', 'CG2', 'THR', 7.3)]]}
SER_PHE = { 
	'distances':
		[[10.8, 10.21, 9.94, 10.24, 9.7, 10.01, 9.74], [9.86, 9.13, 8.73, 9.19, 8.39, 8.88, 8.47]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'PHE', 10.8), ('CB', 'SER', 'CG', 'PHE', 10.21), ('CB', 'SER', 'CD1', 'PHE', 9.94), ('CB', 'SER', 'CD2', 'PHE', 10.24), ('CB', 'SER', 'CE1', 'PHE', 9.7), ('CB', 'SER', 'CE2', 'PHE', 10.01), ('CB', 'SER', 'CZ', 'PHE', 9.74)], [('OG', 'SER', 'CB', 'PHE', 9.86), ('OG', 'SER', 'CG', 'PHE', 9.13), ('OG', 'SER', 'CD1', 'PHE', 8.73), ('OG', 'SER', 'CD2', 'PHE', 9.19), ('OG', 'SER', 'CE1', 'PHE', 8.39), ('OG', 'SER', 'CE2', 'PHE', 8.88), ('OG', 'SER', 'CZ', 'PHE', 8.47)]]}
THR_LYS = { 
	'distances':
		[[13.56, 13.27, 11.9, 10.85, 9.57], [12.64, 12.49, 11.16, 10.14, 8.95], [14.28, 13.91, 12.46, 11.57, 10.2]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'LYS', 13.56), ('CB', 'THR', 'CG', 'LYS', 13.27), ('CB', 'THR', 'CD', 'LYS', 11.9), ('CB', 'THR', 'CE', 'LYS', 10.85), ('CB', 'THR', 'NZ', 'LYS', 9.57)], [('OG1', 'THR', 'CB', 'LYS', 12.64), ('OG1', 'THR', 'CG', 'LYS', 12.49), ('OG1', 'THR', 'CD', 'LYS', 11.16), ('OG1', 'THR', 'CE', 'LYS', 10.14), ('OG1', 'THR', 'NZ', 'LYS', 8.95)], [('CG2', 'THR', 'CB', 'LYS', 14.28), ('CG2', 'THR', 'CG', 'LYS', 13.91), ('CG2', 'THR', 'CD', 'LYS', 12.46), ('CG2', 'THR', 'CE', 'LYS', 11.57), ('CG2', 'THR', 'NZ', 'LYS', 10.2)]]}
ASN_PHE = { 
	'distances':
		[[7.69, 6.83, 5.88, 7.4, 5.54, 7.17, 6.29], [8.72, 7.71, 6.55, 8.21, 5.86, 7.74, 6.59], [8.87, 7.92, 6.62, 8.59, 5.99, 8.18, 6.94], [9.71, 8.58, 7.51, 8.86, 6.61, 8.16, 7.01], [13.0, 11.6, 11.49, 10.54, 10.33, 9.21, 9.09], [11.64, 10.28, 10.3, 9.15, 9.24, 7.87, 7.93], [11.65, 10.38, 10.61, 9.14, 9.68, 7.97, 8.31], [10.61, 9.2, 9.11, 8.17, 8.01, 6.84, 6.74]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'PHE', 7.69), ('CB', 'ASN', 'CG', 'PHE', 6.83), ('CB', 'ASN', 'CD1', 'PHE', 5.88), ('CB', 'ASN', 'CD2', 'PHE', 7.4), ('CB', 'ASN', 'CE1', 'PHE', 5.54), ('CB', 'ASN', 'CE2', 'PHE', 7.17), ('CB', 'ASN', 'CZ', 'PHE', 6.29)], [('CG', 'ASN', 'CB', 'PHE', 8.72), ('CG', 'ASN', 'CG', 'PHE', 7.71), ('CG', 'ASN', 'CD1', 'PHE', 6.55), ('CG', 'ASN', 'CD2', 'PHE', 8.21), ('CG', 'ASN', 'CE1', 'PHE', 5.86), ('CG', 'ASN', 'CE2', 'PHE', 7.74), ('CG', 'ASN', 'CZ', 'PHE', 6.59)], [('OD1', 'ASN', 'CB', 'PHE', 8.87), ('OD1', 'ASN', 'CG', 'PHE', 7.92), ('OD1', 'ASN', 'CD1', 'PHE', 6.62), ('OD1', 'ASN', 'CD2', 'PHE', 8.59), ('OD1', 'ASN', 'CE1', 'PHE', 5.99), ('OD1', 'ASN', 'CE2', 'PHE', 8.18), ('OD1', 'ASN', 'CZ', 'PHE', 6.94)], [('ND2', 'ASN', 'CB', 'PHE', 9.71), ('ND2', 'ASN', 'CG', 'PHE', 8.58), ('ND2', 'ASN', 'CD1', 'PHE', 7.51), ('ND2', 'ASN', 'CD2', 'PHE', 8.86), ('ND2', 'ASN', 'CE1', 'PHE', 6.61), ('ND2', 'ASN', 'CE2', 'PHE', 8.16), ('ND2', 'ASN', 'CZ', 'PHE', 7.01)], [('CB', 'ASN', 'CB', 'PHE', 13.0), ('CB', 'ASN', 'CG', 'PHE', 11.6), ('CB', 'ASN', 'CD1', 'PHE', 11.49), ('CB', 'ASN', 'CD2', 'PHE', 10.54), ('CB', 'ASN', 'CE1', 'PHE', 10.33), ('CB', 'ASN', 'CE2', 'PHE', 9.21), ('CB', 'ASN', 'CZ', 'PHE', 9.09)], [('CG', 'ASN', 'CB', 'PHE', 11.64), ('CG', 'ASN', 'CG', 'PHE', 10.28), ('CG', 'ASN', 'CD1', 'PHE', 10.3), ('CG', 'ASN', 'CD2', 'PHE', 9.15), ('CG', 'ASN', 'CE1', 'PHE', 9.24), ('CG', 'ASN', 'CE2', 'PHE', 7.87), ('CG', 'ASN', 'CZ', 'PHE', 7.93)], [('OD1', 'ASN', 'CB', 'PHE', 11.65), ('OD1', 'ASN', 'CG', 'PHE', 10.38), ('OD1', 'ASN', 'CD1', 'PHE', 10.61), ('OD1', 'ASN', 'CD2', 'PHE', 9.14), ('OD1', 'ASN', 'CE1', 'PHE', 9.68), ('OD1', 'ASN', 'CE2', 'PHE', 7.97), ('OD1', 'ASN', 'CZ', 'PHE', 8.31)], [('ND2', 'ASN', 'CB', 'PHE', 10.61), ('ND2', 'ASN', 'CG', 'PHE', 9.2), ('ND2', 'ASN', 'CD1', 'PHE', 9.11), ('ND2', 'ASN', 'CD2', 'PHE', 8.17), ('ND2', 'ASN', 'CE1', 'PHE', 8.01), ('ND2', 'ASN', 'CE2', 'PHE', 6.84), ('ND2', 'ASN', 'CZ', 'PHE', 6.74)]]}
PHE_ARG = { 
	'distances':
		[[14.9, 13.59, 13.19, 12.08, 11.6, 12.19, 10.72], [13.87, 12.54, 12.01, 10.88, 10.29, 10.81, 9.41], [12.64, 11.28, 10.79, 9.62, 9.11, 9.75, 8.21], [14.27, 12.98, 12.28, 11.18, 10.43, 10.75, 9.57], [11.77, 10.4, 9.75, 8.55, 7.9, 8.46, 6.99], [13.54, 12.26, 11.41, 10.32, 9.44, 9.64, 8.61], [12.27, 10.95, 10.11, 8.96, 8.1, 8.39, 7.24]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ARG', 14.9), ('CB', 'PHE', 'CG', 'ARG', 13.59), ('CB', 'PHE', 'CD', 'ARG', 13.19), ('CB', 'PHE', 'NE', 'ARG', 12.08), ('CB', 'PHE', 'CZ', 'ARG', 11.6), ('CB', 'PHE', 'NH1', 'ARG', 12.19), ('CB', 'PHE', 'NH2', 'ARG', 10.72)], [('CG', 'PHE', 'CB', 'ARG', 13.87), ('CG', 'PHE', 'CG', 'ARG', 12.54), ('CG', 'PHE', 'CD', 'ARG', 12.01), ('CG', 'PHE', 'NE', 'ARG', 10.88), ('CG', 'PHE', 'CZ', 'ARG', 10.29), ('CG', 'PHE', 'NH1', 'ARG', 10.81), ('CG', 'PHE', 'NH2', 'ARG', 9.41)], [('CD1', 'PHE', 'CB', 'ARG', 12.64), ('CD1', 'PHE', 'CG', 'ARG', 11.28), ('CD1', 'PHE', 'CD', 'ARG', 10.79), ('CD1', 'PHE', 'NE', 'ARG', 9.62), ('CD1', 'PHE', 'CZ', 'ARG', 9.11), ('CD1', 'PHE', 'NH1', 'ARG', 9.75), ('CD1', 'PHE', 'NH2', 'ARG', 8.21)], [('CD2', 'PHE', 'CB', 'ARG', 14.27), ('CD2', 'PHE', 'CG', 'ARG', 12.98), ('CD2', 'PHE', 'CD', 'ARG', 12.28), ('CD2', 'PHE', 'NE', 'ARG', 11.18), ('CD2', 'PHE', 'CZ', 'ARG', 10.43), ('CD2', 'PHE', 'NH1', 'ARG', 10.75), ('CD2', 'PHE', 'NH2', 'ARG', 9.57)], [('CE1', 'PHE', 'CB', 'ARG', 11.77), ('CE1', 'PHE', 'CG', 'ARG', 10.4), ('CE1', 'PHE', 'CD', 'ARG', 9.75), ('CE1', 'PHE', 'NE', 'ARG', 8.55), ('CE1', 'PHE', 'CZ', 'ARG', 7.9), ('CE1', 'PHE', 'NH1', 'ARG', 8.46), ('CE1', 'PHE', 'NH2', 'ARG', 6.99)], [('CE2', 'PHE', 'CB', 'ARG', 13.54), ('CE2', 'PHE', 'CG', 'ARG', 12.26), ('CE2', 'PHE', 'CD', 'ARG', 11.41), ('CE2', 'PHE', 'NE', 'ARG', 10.32), ('CE2', 'PHE', 'CZ', 'ARG', 9.44), ('CE2', 'PHE', 'NH1', 'ARG', 9.64), ('CE2', 'PHE', 'NH2', 'ARG', 8.61)], [('CZ', 'PHE', 'CB', 'ARG', 12.27), ('CZ', 'PHE', 'CG', 'ARG', 10.95), ('CZ', 'PHE', 'CD', 'ARG', 10.11), ('CZ', 'PHE', 'NE', 'ARG', 8.96), ('CZ', 'PHE', 'CZ', 'ARG', 8.1), ('CZ', 'PHE', 'NH1', 'ARG', 8.39), ('CZ', 'PHE', 'NH2', 'ARG', 7.24)]]}
SER_ASN = { 
	'distances':
		[[6.99, 7.84, 8.99, 7.54], [5.67, 6.47, 7.66, 6.19], [13.58, 12.81, 12.97, 12.21], [12.61, 11.83, 12.09, 11.12]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 6.99), ('CB', 'SER', 'CG', 'ASN', 7.84), ('CB', 'SER', 'OD1', 'ASN', 8.99), ('CB', 'SER', 'ND2', 'ASN', 7.54)], [('OG', 'SER', 'CB', 'ASN', 5.67), ('OG', 'SER', 'CG', 'ASN', 6.47), ('OG', 'SER', 'OD1', 'ASN', 7.66), ('OG', 'SER', 'ND2', 'ASN', 6.19)], [('CB', 'SER', 'CB', 'ASN', 13.58), ('CB', 'SER', 'CG', 'ASN', 12.81), ('CB', 'SER', 'OD1', 'ASN', 12.97), ('CB', 'SER', 'ND2', 'ASN', 12.21)], [('OG', 'SER', 'CB', 'ASN', 12.61), ('OG', 'SER', 'CG', 'ASN', 11.83), ('OG', 'SER', 'OD1', 'ASN', 12.09), ('OG', 'SER', 'ND2', 'ASN', 11.12)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_ARG, d, 'A_1qq5_3_8_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(THR_PHE, d, 'A_1qq5_3_8_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_ASPI, d, 'A_1qq5_3_8_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_ASNI, d, 'A_1qq5_3_8_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_ARG, d, 'A_1qq5_3_8_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_ASN, d, 'A_1qq5_3_8_1_2')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(SER_ARG, d, 'A_1qq5_3_8_1_2')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_PHE, d, 'A_1qq5_3_8_1_2')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_ASP, d, 'A_1qq5_3_8_1_2')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASN_ASN, d, 'A_1qq5_3_8_1_2')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ASP_THR, d, 'A_1qq5_3_8_1_2')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(SER_LYS, d, 'A_1qq5_3_8_1_2')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(ASP_ASN, d, 'A_1qq5_3_8_1_2')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(ARG_ASPI, d, 'A_1qq5_3_8_1_2')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(LYS_ARG, d, 'A_1qq5_3_8_1_2')
	if match15 == []:
		 flag = True
		 break
	match16 , totTime16 = cmd.detect(ASP_ARG, d, 'A_1qq5_3_8_1_2')
	if match16 == []:
		 flag = True
		 break
	match17 , totTime17 = cmd.detect(ASN_LYS, d, 'A_1qq5_3_8_1_2')
	if match17 == []:
		 flag = True
		 break
	match18 , totTime18 = cmd.detect(ASN_ASPI, d, 'A_1qq5_3_8_1_2')
	if match18 == []:
		 flag = True
		 break
	match19 , totTime19 = cmd.detect(ASP_LYS, d, 'A_1qq5_3_8_1_2')
	if match19 == []:
		 flag = True
		 break
	match20 , totTime20 = cmd.detect(ASP_ASP, d, 'A_1qq5_3_8_1_2')
	if match20 == []:
		 flag = True
		 break
	match21 , totTime21 = cmd.detect(LYS_ASPI, d, 'A_1qq5_3_8_1_2')
	if match21 == []:
		 flag = True
		 break
	match22 , totTime22 = cmd.detect(PHE_LYS, d, 'A_1qq5_3_8_1_2')
	if match22 == []:
		 flag = True
		 break
	match23 , totTime23 = cmd.detect(SER_THR, d, 'A_1qq5_3_8_1_2')
	if match23 == []:
		 flag = True
		 break
	match24 , totTime24 = cmd.detect(SER_PHE, d, 'A_1qq5_3_8_1_2')
	if match24 == []:
		 flag = True
		 break
	match25 , totTime25 = cmd.detect(THR_LYS, d, 'A_1qq5_3_8_1_2')
	if match25 == []:
		 flag = True
		 break
	match26 , totTime26 = cmd.detect(ASN_PHE, d, 'A_1qq5_3_8_1_2')
	if match26 == []:
		 flag = True
		 break
	match27 , totTime27 = cmd.detect(PHE_ARG, d, 'A_1qq5_3_8_1_2')
	if match27 == []:
		 flag = True
		 break
	match28 , totTime28 = cmd.detect(SER_ASN, d, 'A_1qq5_3_8_1_2')
	if match28 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_ARG' :  match1,
		'THR_PHE' :  match2,
		'PHE_ASPI' :  match3,
		'ARG_ASNI' :  match4,
		'ASN_ARG' :  match5,
		'THR_ASN' :  match6,
		'SER_ARG' :  match7,
		'ASP_PHE' :  match8,
		'SER_ASP' :  match9,
		'ASN_ASN' :  match10,
		'ASP_THR' :  match11,
		'SER_LYS' :  match12,
		'ASP_ASN' :  match13,
		'ARG_ASPI' :  match14,
		'LYS_ARG' :  match15,
		'ASP_ARG' :  match16,
		'ASN_LYS' :  match17,
		'ASN_ASPI' :  match18,
		'ASP_LYS' :  match19,
		'ASP_ASP' :  match20,
		'LYS_ASPI' :  match21,
		'PHE_LYS' :  match22,
		'SER_THR' :  match23,
		'SER_PHE' :  match24,
		'THR_LYS' :  match25,
		'ASN_PHE' :  match26,
		'PHE_ARG' :  match27,
		'SER_ASN' :  match28}