'''
FUNC:A_1pii_4_1_1_48
PDB:1pii
EC:4.1.1.48
RESI:glu,lys,lys,glu,asn,ser
LOCI:a-53,55,114,163,184,215;
'''
import motifFunctions as cmd
LYS_GLU = { 
	'distances':
		[[7.02, 6.26, 6.66, 6.38, 7.8], [8.0, 7.05, 7.03, 6.52, 8.06], [8.18, 7.43, 7.12, 6.29, 8.19], [7.18, 6.54, 6.0, 5.0, 7.08], [8.13, 7.62, 6.79, 5.62, 7.72], [17.27, 16.71, 15.5, 14.36, 15.68], [16.81, 16.19, 14.9, 13.84, 14.95], [16.47, 15.71, 14.4, 13.39, 14.42], [15.37, 14.58, 13.34, 12.29, 13.45], [14.95, 14.03, 12.77, 11.81, 12.8], [8.68, 7.43, 7.01, 7.78, 6.07], [8.53, 7.28, 6.45, 6.97, 5.48], [8.49, 7.5, 6.48, 6.97, 5.3], [8.32, 7.47, 6.16, 6.33, 5.14], [7.79, 6.84, 5.4, 5.25, 4.77], [11.69, 11.88, 11.0, 9.86, 11.48], [10.76, 10.76, 9.76, 8.61, 10.19], [9.6, 9.57, 8.69, 7.47, 9.28], [9.24, 8.91, 7.93, 6.67, 8.49], [10.35, 9.84, 8.7, 7.5, 9.07]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 7.02), ('CB', 'LYS', 'CG', 'GLU', 6.26), ('CB', 'LYS', 'CD', 'GLU', 6.66), ('CB', 'LYS', 'OE1', 'GLU', 6.38), ('CB', 'LYS', 'OE2', 'GLU', 7.8)], [('CG', 'LYS', 'CB', 'GLU', 8.0), ('CG', 'LYS', 'CG', 'GLU', 7.05), ('CG', 'LYS', 'CD', 'GLU', 7.03), ('CG', 'LYS', 'OE1', 'GLU', 6.52), ('CG', 'LYS', 'OE2', 'GLU', 8.06)], [('CD', 'LYS', 'CB', 'GLU', 8.18), ('CD', 'LYS', 'CG', 'GLU', 7.43), ('CD', 'LYS', 'CD', 'GLU', 7.12), ('CD', 'LYS', 'OE1', 'GLU', 6.29), ('CD', 'LYS', 'OE2', 'GLU', 8.19)], [('CE', 'LYS', 'CB', 'GLU', 7.18), ('CE', 'LYS', 'CG', 'GLU', 6.54), ('CE', 'LYS', 'CD', 'GLU', 6.0), ('CE', 'LYS', 'OE1', 'GLU', 5.0), ('CE', 'LYS', 'OE2', 'GLU', 7.08)], [('NZ', 'LYS', 'CB', 'GLU', 8.13), ('NZ', 'LYS', 'CG', 'GLU', 7.62), ('NZ', 'LYS', 'CD', 'GLU', 6.79), ('NZ', 'LYS', 'OE1', 'GLU', 5.62), ('NZ', 'LYS', 'OE2', 'GLU', 7.72)], [('CB', 'LYS', 'CB', 'GLU', 17.27), ('CB', 'LYS', 'CG', 'GLU', 16.71), ('CB', 'LYS', 'CD', 'GLU', 15.5), ('CB', 'LYS', 'OE1', 'GLU', 14.36), ('CB', 'LYS', 'OE2', 'GLU', 15.68)], [('CG', 'LYS', 'CB', 'GLU', 16.81), ('CG', 'LYS', 'CG', 'GLU', 16.19), ('CG', 'LYS', 'CD', 'GLU', 14.9), ('CG', 'LYS', 'OE1', 'GLU', 13.84), ('CG', 'LYS', 'OE2', 'GLU', 14.95)], [('CD', 'LYS', 'CB', 'GLU', 16.47), ('CD', 'LYS', 'CG', 'GLU', 15.71), ('CD', 'LYS', 'CD', 'GLU', 14.4), ('CD', 'LYS', 'OE1', 'GLU', 13.39), ('CD', 'LYS', 'OE2', 'GLU', 14.42)], [('CE', 'LYS', 'CB', 'GLU', 15.37), ('CE', 'LYS', 'CG', 'GLU', 14.58), ('CE', 'LYS', 'CD', 'GLU', 13.34), ('CE', 'LYS', 'OE1', 'GLU', 12.29), ('CE', 'LYS', 'OE2', 'GLU', 13.45)], [('NZ', 'LYS', 'CB', 'GLU', 14.95), ('NZ', 'LYS', 'CG', 'GLU', 14.03), ('NZ', 'LYS', 'CD', 'GLU', 12.77), ('NZ', 'LYS', 'OE1', 'GLU', 11.81), ('NZ', 'LYS', 'OE2', 'GLU', 12.8)], [('CB', 'LYS', 'CB', 'GLU', 8.68), ('CB', 'LYS', 'CG', 'GLU', 7.43), ('CB', 'LYS', 'CD', 'GLU', 7.01), ('CB', 'LYS', 'OE1', 'GLU', 7.78), ('CB', 'LYS', 'OE2', 'GLU', 6.07)], [('CG', 'LYS', 'CB', 'GLU', 8.53), ('CG', 'LYS', 'CG', 'GLU', 7.28), ('CG', 'LYS', 'CD', 'GLU', 6.45), ('CG', 'LYS', 'OE1', 'GLU', 6.97), ('CG', 'LYS', 'OE2', 'GLU', 5.48)], [('CD', 'LYS', 'CB', 'GLU', 8.49), ('CD', 'LYS', 'CG', 'GLU', 7.5), ('CD', 'LYS', 'CD', 'GLU', 6.48), ('CD', 'LYS', 'OE1', 'GLU', 6.97), ('CD', 'LYS', 'OE2', 'GLU', 5.3)], [('CE', 'LYS', 'CB', 'GLU', 8.32), ('CE', 'LYS', 'CG', 'GLU', 7.47), ('CE', 'LYS', 'CD', 'GLU', 6.16), ('CE', 'LYS', 'OE1', 'GLU', 6.33), ('CE', 'LYS', 'OE2', 'GLU', 5.14)], [('NZ', 'LYS', 'CB', 'GLU', 7.79), ('NZ', 'LYS', 'CG', 'GLU', 6.84), ('NZ', 'LYS', 'CD', 'GLU', 5.4), ('NZ', 'LYS', 'OE1', 'GLU', 5.25), ('NZ', 'LYS', 'OE2', 'GLU', 4.77)], [('CB', 'LYS', 'CB', 'GLU', 11.69), ('CB', 'LYS', 'CG', 'GLU', 11.88), ('CB', 'LYS', 'CD', 'GLU', 11.0), ('CB', 'LYS', 'OE1', 'GLU', 9.86), ('CB', 'LYS', 'OE2', 'GLU', 11.48)], [('CG', 'LYS', 'CB', 'GLU', 10.76), ('CG', 'LYS', 'CG', 'GLU', 10.76), ('CG', 'LYS', 'CD', 'GLU', 9.76), ('CG', 'LYS', 'OE1', 'GLU', 8.61), ('CG', 'LYS', 'OE2', 'GLU', 10.19)], [('CD', 'LYS', 'CB', 'GLU', 9.6), ('CD', 'LYS', 'CG', 'GLU', 9.57), ('CD', 'LYS', 'CD', 'GLU', 8.69), ('CD', 'LYS', 'OE1', 'GLU', 7.47), ('CD', 'LYS', 'OE2', 'GLU', 9.28)], [('CE', 'LYS', 'CB', 'GLU', 9.24), ('CE', 'LYS', 'CG', 'GLU', 8.91), ('CE', 'LYS', 'CD', 'GLU', 7.93), ('CE', 'LYS', 'OE1', 'GLU', 6.67), ('CE', 'LYS', 'OE2', 'GLU', 8.49)], [('NZ', 'LYS', 'CB', 'GLU', 10.35), ('NZ', 'LYS', 'CG', 'GLU', 9.84), ('NZ', 'LYS', 'CD', 'GLU', 8.7), ('NZ', 'LYS', 'OE1', 'GLU', 7.5), ('NZ', 'LYS', 'OE2', 'GLU', 9.07)]]}
GLU_GLU = { 
	'distances':
		[[15.14, 14.73, 13.91, 12.64, 14.51], [14.57, 14.21, 13.28, 12.01, 13.8], [13.29, 12.84, 11.87, 10.61, 12.35], [13.33, 12.73, 11.67, 10.47, 12.05], [12.22, 11.88, 10.97, 9.69, 11.54], [15.14, 14.57, 13.29, 13.33, 12.22], [14.73, 14.21, 12.84, 12.73, 11.88], [13.91, 13.28, 11.87, 11.67, 10.97], [12.64, 12.01, 10.61, 10.47, 9.69], [14.51, 13.8, 12.35, 12.05, 11.54]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 15.14), ('CB', 'GLU', 'CG', 'GLU', 14.73), ('CB', 'GLU', 'CD', 'GLU', 13.91), ('CB', 'GLU', 'OE1', 'GLU', 12.64), ('CB', 'GLU', 'OE2', 'GLU', 14.51)], [('CG', 'GLU', 'CB', 'GLU', 14.57), ('CG', 'GLU', 'CG', 'GLU', 14.21), ('CG', 'GLU', 'CD', 'GLU', 13.28), ('CG', 'GLU', 'OE1', 'GLU', 12.01), ('CG', 'GLU', 'OE2', 'GLU', 13.8)], [('CD', 'GLU', 'CB', 'GLU', 13.29), ('CD', 'GLU', 'CG', 'GLU', 12.84), ('CD', 'GLU', 'CD', 'GLU', 11.87), ('CD', 'GLU', 'OE1', 'GLU', 10.61), ('CD', 'GLU', 'OE2', 'GLU', 12.35)], [('OE1', 'GLU', 'CB', 'GLU', 13.33), ('OE1', 'GLU', 'CG', 'GLU', 12.73), ('OE1', 'GLU', 'CD', 'GLU', 11.67), ('OE1', 'GLU', 'OE1', 'GLU', 10.47), ('OE1', 'GLU', 'OE2', 'GLU', 12.05)], [('OE2', 'GLU', 'CB', 'GLU', 12.22), ('OE2', 'GLU', 'CG', 'GLU', 11.88), ('OE2', 'GLU', 'CD', 'GLU', 10.97), ('OE2', 'GLU', 'OE1', 'GLU', 9.69), ('OE2', 'GLU', 'OE2', 'GLU', 11.54)], [('CB', 'GLU', 'CB', 'GLU', 15.14), ('CB', 'GLU', 'CG', 'GLU', 14.57), ('CB', 'GLU', 'CD', 'GLU', 13.29), ('CB', 'GLU', 'OE1', 'GLU', 13.33), ('CB', 'GLU', 'OE2', 'GLU', 12.22)], [('CG', 'GLU', 'CB', 'GLU', 14.73), ('CG', 'GLU', 'CG', 'GLU', 14.21), ('CG', 'GLU', 'CD', 'GLU', 12.84), ('CG', 'GLU', 'OE1', 'GLU', 12.73), ('CG', 'GLU', 'OE2', 'GLU', 11.88)], [('CD', 'GLU', 'CB', 'GLU', 13.91), ('CD', 'GLU', 'CG', 'GLU', 13.28), ('CD', 'GLU', 'CD', 'GLU', 11.87), ('CD', 'GLU', 'OE1', 'GLU', 11.67), ('CD', 'GLU', 'OE2', 'GLU', 10.97)], [('OE1', 'GLU', 'CB', 'GLU', 12.64), ('OE1', 'GLU', 'CG', 'GLU', 12.01), ('OE1', 'GLU', 'CD', 'GLU', 10.61), ('OE1', 'GLU', 'OE1', 'GLU', 10.47), ('OE1', 'GLU', 'OE2', 'GLU', 9.69)], [('OE2', 'GLU', 'CB', 'GLU', 14.51), ('OE2', 'GLU', 'CG', 'GLU', 13.8), ('OE2', 'GLU', 'CD', 'GLU', 12.35), ('OE2', 'GLU', 'OE1', 'GLU', 12.05), ('OE2', 'GLU', 'OE2', 'GLU', 11.54)]]}
GLU_LYSI = { 
	'distances':
		[[11.69, 10.76, 9.6, 9.24, 10.35], [11.88, 10.76, 9.57, 8.91, 9.84], [11.0, 9.76, 8.69, 7.93, 8.7], [9.86, 8.61, 7.47, 6.67, 7.5], [11.48, 10.19, 9.28, 8.49, 9.07]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYSI', 11.69), ('CB', 'GLU', 'CG', 'LYSI', 10.76), ('CB', 'GLU', 'CD', 'LYSI', 9.6), ('CB', 'GLU', 'CE', 'LYSI', 9.24), ('CB', 'GLU', 'NZ', 'LYSI', 10.35)], [('CG', 'GLU', 'CB', 'LYSI', 11.88), ('CG', 'GLU', 'CG', 'LYSI', 10.76), ('CG', 'GLU', 'CD', 'LYSI', 9.57), ('CG', 'GLU', 'CE', 'LYSI', 8.91), ('CG', 'GLU', 'NZ', 'LYSI', 9.84)], [('CD', 'GLU', 'CB', 'LYSI', 11.0), ('CD', 'GLU', 'CG', 'LYSI', 9.76), ('CD', 'GLU', 'CD', 'LYSI', 8.69), ('CD', 'GLU', 'CE', 'LYSI', 7.93), ('CD', 'GLU', 'NZ', 'LYSI', 8.7)], [('OE1', 'GLU', 'CB', 'LYSI', 9.86), ('OE1', 'GLU', 'CG', 'LYSI', 8.61), ('OE1', 'GLU', 'CD', 'LYSI', 7.47), ('OE1', 'GLU', 'CE', 'LYSI', 6.67), ('OE1', 'GLU', 'NZ', 'LYSI', 7.5)], [('OE2', 'GLU', 'CB', 'LYSI', 11.48), ('OE2', 'GLU', 'CG', 'LYSI', 10.19), ('OE2', 'GLU', 'CD', 'LYSI', 9.28), ('OE2', 'GLU', 'CE', 'LYSI', 8.49), ('OE2', 'GLU', 'NZ', 'LYSI', 9.07)]]}
LYS_LYS = { 
	'distances':
		[[9.87, 9.58, 10.34, 10.14, 8.93], [9.85, 9.37, 10.19, 9.9, 8.56], [10.48, 9.75, 10.35, 9.79, 8.36], [9.89, 9.04, 9.41, 8.69, 7.29], [10.62, 9.58, 9.75, 8.78, 7.36], [9.87, 9.85, 10.48, 9.89, 10.62], [9.58, 9.37, 9.75, 9.04, 9.58], [10.34, 10.19, 10.35, 9.41, 9.75], [10.14, 9.9, 9.79, 8.69, 8.78], [8.93, 8.56, 8.36, 7.29, 7.36]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 9.87), ('CB', 'LYS', 'CG', 'LYS', 9.58), ('CB', 'LYS', 'CD', 'LYS', 10.34), ('CB', 'LYS', 'CE', 'LYS', 10.14), ('CB', 'LYS', 'NZ', 'LYS', 8.93)], [('CG', 'LYS', 'CB', 'LYS', 9.85), ('CG', 'LYS', 'CG', 'LYS', 9.37), ('CG', 'LYS', 'CD', 'LYS', 10.19), ('CG', 'LYS', 'CE', 'LYS', 9.9), ('CG', 'LYS', 'NZ', 'LYS', 8.56)], [('CD', 'LYS', 'CB', 'LYS', 10.48), ('CD', 'LYS', 'CG', 'LYS', 9.75), ('CD', 'LYS', 'CD', 'LYS', 10.35), ('CD', 'LYS', 'CE', 'LYS', 9.79), ('CD', 'LYS', 'NZ', 'LYS', 8.36)], [('CE', 'LYS', 'CB', 'LYS', 9.89), ('CE', 'LYS', 'CG', 'LYS', 9.04), ('CE', 'LYS', 'CD', 'LYS', 9.41), ('CE', 'LYS', 'CE', 'LYS', 8.69), ('CE', 'LYS', 'NZ', 'LYS', 7.29)], [('NZ', 'LYS', 'CB', 'LYS', 10.62), ('NZ', 'LYS', 'CG', 'LYS', 9.58), ('NZ', 'LYS', 'CD', 'LYS', 9.75), ('NZ', 'LYS', 'CE', 'LYS', 8.78), ('NZ', 'LYS', 'NZ', 'LYS', 7.36)], [('CB', 'LYS', 'CB', 'LYS', 9.87), ('CB', 'LYS', 'CG', 'LYS', 9.85), ('CB', 'LYS', 'CD', 'LYS', 10.48), ('CB', 'LYS', 'CE', 'LYS', 9.89), ('CB', 'LYS', 'NZ', 'LYS', 10.62)], [('CG', 'LYS', 'CB', 'LYS', 9.58), ('CG', 'LYS', 'CG', 'LYS', 9.37), ('CG', 'LYS', 'CD', 'LYS', 9.75), ('CG', 'LYS', 'CE', 'LYS', 9.04), ('CG', 'LYS', 'NZ', 'LYS', 9.58)], [('CD', 'LYS', 'CB', 'LYS', 10.34), ('CD', 'LYS', 'CG', 'LYS', 10.19), ('CD', 'LYS', 'CD', 'LYS', 10.35), ('CD', 'LYS', 'CE', 'LYS', 9.41), ('CD', 'LYS', 'NZ', 'LYS', 9.75)], [('CE', 'LYS', 'CB', 'LYS', 10.14), ('CE', 'LYS', 'CG', 'LYS', 9.9), ('CE', 'LYS', 'CD', 'LYS', 9.79), ('CE', 'LYS', 'CE', 'LYS', 8.69), ('CE', 'LYS', 'NZ', 'LYS', 8.78)], [('NZ', 'LYS', 'CB', 'LYS', 8.93), ('NZ', 'LYS', 'CG', 'LYS', 8.56), ('NZ', 'LYS', 'CD', 'LYS', 8.36), ('NZ', 'LYS', 'CE', 'LYS', 7.29), ('NZ', 'LYS', 'NZ', 'LYS', 7.36)]]}
ASN_SER = { 
	'distances':
		[[7.89, 7.2], [6.86, 5.99], [5.66, 4.92], [7.58, 6.48]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'SER', 7.89), ('CB', 'ASN', 'OG', 'SER', 7.2)], [('CG', 'ASN', 'CB', 'SER', 6.86), ('CG', 'ASN', 'OG', 'SER', 5.99)], [('OD1', 'ASN', 'CB', 'SER', 5.66), ('OD1', 'ASN', 'OG', 'SER', 4.92)], [('ND2', 'ASN', 'CB', 'SER', 7.58), ('ND2', 'ASN', 'OG', 'SER', 6.48)]]}
ASN_LYSI = { 
	'distances':
		[[13.5, 12.11, 10.96, 9.72, 10.04], [12.74, 11.28, 10.25, 8.9, 8.99], [13.11, 11.63, 10.64, 9.18, 9.09], [11.84, 10.36, 9.44, 8.16, 8.23]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'LYSI', 13.5), ('CB', 'ASN', 'CG', 'LYSI', 12.11), ('CB', 'ASN', 'CD', 'LYSI', 10.96), ('CB', 'ASN', 'CE', 'LYSI', 9.72), ('CB', 'ASN', 'NZ', 'LYSI', 10.04)], [('CG', 'ASN', 'CB', 'LYSI', 12.74), ('CG', 'ASN', 'CG', 'LYSI', 11.28), ('CG', 'ASN', 'CD', 'LYSI', 10.25), ('CG', 'ASN', 'CE', 'LYSI', 8.9), ('CG', 'ASN', 'NZ', 'LYSI', 8.99)], [('OD1', 'ASN', 'CB', 'LYSI', 13.11), ('OD1', 'ASN', 'CG', 'LYSI', 11.63), ('OD1', 'ASN', 'CD', 'LYSI', 10.64), ('OD1', 'ASN', 'CE', 'LYSI', 9.18), ('OD1', 'ASN', 'NZ', 'LYSI', 9.09)], [('ND2', 'ASN', 'CB', 'LYSI', 11.84), ('ND2', 'ASN', 'CG', 'LYSI', 10.36), ('ND2', 'ASN', 'CD', 'LYSI', 9.44), ('ND2', 'ASN', 'CE', 'LYSI', 8.16), ('ND2', 'ASN', 'NZ', 'LYSI', 8.23)]]}
LYS_SER = { 
	'distances':
		[[13.13, 12.35], [12.71, 11.88], [11.46, 10.71], [10.23, 9.46], [9.01, 8.31], [14.01, 12.71], [12.63, 11.29], [11.75, 10.43], [10.22, 8.89], [9.7, 8.39]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'SER', 13.13), ('CB', 'LYS', 'OG', 'SER', 12.35)], [('CG', 'LYS', 'CB', 'SER', 12.71), ('CG', 'LYS', 'OG', 'SER', 11.88)], [('CD', 'LYS', 'CB', 'SER', 11.46), ('CD', 'LYS', 'OG', 'SER', 10.71)], [('CE', 'LYS', 'CB', 'SER', 10.23), ('CE', 'LYS', 'OG', 'SER', 9.46)], [('NZ', 'LYS', 'CB', 'SER', 9.01), ('NZ', 'LYS', 'OG', 'SER', 8.31)], [('CB', 'LYS', 'CB', 'SER', 14.01), ('CB', 'LYS', 'OG', 'SER', 12.71)], [('CG', 'LYS', 'CB', 'SER', 12.63), ('CG', 'LYS', 'OG', 'SER', 11.29)], [('CD', 'LYS', 'CB', 'SER', 11.75), ('CD', 'LYS', 'OG', 'SER', 10.43)], [('CE', 'LYS', 'CB', 'SER', 10.22), ('CE', 'LYS', 'OG', 'SER', 8.89)], [('NZ', 'LYS', 'CB', 'SER', 9.7), ('NZ', 'LYS', 'OG', 'SER', 8.39)]]}
SER_LYSI = { 
	'distances':
		[[14.01, 12.63, 11.75, 10.22, 9.7], [12.71, 11.29, 10.43, 8.89, 8.39]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYSI', 14.01), ('CB', 'SER', 'CG', 'LYSI', 12.63), ('CB', 'SER', 'CD', 'LYSI', 11.75), ('CB', 'SER', 'CE', 'LYSI', 10.22), ('CB', 'SER', 'NZ', 'LYSI', 9.7)], [('OG', 'SER', 'CB', 'LYSI', 12.71), ('OG', 'SER', 'CG', 'LYSI', 11.29), ('OG', 'SER', 'CD', 'LYSI', 10.43), ('OG', 'SER', 'CE', 'LYSI', 8.89), ('OG', 'SER', 'NZ', 'LYSI', 8.39)]]}
SER_GLUI = { 
	'distances':
		[[12.57, 11.17, 10.46, 10.0, 10.57], [11.5, 10.15, 9.31, 8.77, 9.43]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLUI', 12.57), ('CB', 'SER', 'CG', 'GLUI', 11.17), ('CB', 'SER', 'CD', 'GLUI', 10.46), ('CB', 'SER', 'OE1', 'GLUI', 10.0), ('CB', 'SER', 'OE2', 'GLUI', 10.57)], [('OG', 'SER', 'CB', 'GLUI', 11.5), ('OG', 'SER', 'CG', 'GLUI', 10.15), ('OG', 'SER', 'CD', 'GLUI', 9.31), ('OG', 'SER', 'OE1', 'GLUI', 8.77), ('OG', 'SER', 'OE2', 'GLUI', 9.43)]]}
LYS_ASN = { 
	'distances':
		[[16.13, 14.79, 14.39, 14.18], [15.52, 14.13, 13.77, 13.45], [14.65, 13.21, 12.74, 12.62], [13.47, 12.07, 11.57, 11.56], [12.52, 11.07, 10.48, 10.64], [13.5, 12.74, 13.11, 11.84], [12.11, 11.28, 11.63, 10.36], [10.96, 10.25, 10.64, 9.44], [9.72, 8.9, 9.18, 8.16], [10.04, 8.99, 9.09, 8.23]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 16.13), ('CB', 'LYS', 'CG', 'ASN', 14.79), ('CB', 'LYS', 'OD1', 'ASN', 14.39), ('CB', 'LYS', 'ND2', 'ASN', 14.18)], [('CG', 'LYS', 'CB', 'ASN', 15.52), ('CG', 'LYS', 'CG', 'ASN', 14.13), ('CG', 'LYS', 'OD1', 'ASN', 13.77), ('CG', 'LYS', 'ND2', 'ASN', 13.45)], [('CD', 'LYS', 'CB', 'ASN', 14.65), ('CD', 'LYS', 'CG', 'ASN', 13.21), ('CD', 'LYS', 'OD1', 'ASN', 12.74), ('CD', 'LYS', 'ND2', 'ASN', 12.62)], [('CE', 'LYS', 'CB', 'ASN', 13.47), ('CE', 'LYS', 'CG', 'ASN', 12.07), ('CE', 'LYS', 'OD1', 'ASN', 11.57), ('CE', 'LYS', 'ND2', 'ASN', 11.56)], [('NZ', 'LYS', 'CB', 'ASN', 12.52), ('NZ', 'LYS', 'CG', 'ASN', 11.07), ('NZ', 'LYS', 'OD1', 'ASN', 10.48), ('NZ', 'LYS', 'ND2', 'ASN', 10.64)], [('CB', 'LYS', 'CB', 'ASN', 13.5), ('CB', 'LYS', 'CG', 'ASN', 12.74), ('CB', 'LYS', 'OD1', 'ASN', 13.11), ('CB', 'LYS', 'ND2', 'ASN', 11.84)], [('CG', 'LYS', 'CB', 'ASN', 12.11), ('CG', 'LYS', 'CG', 'ASN', 11.28), ('CG', 'LYS', 'OD1', 'ASN', 11.63), ('CG', 'LYS', 'ND2', 'ASN', 10.36)], [('CD', 'LYS', 'CB', 'ASN', 10.96), ('CD', 'LYS', 'CG', 'ASN', 10.25), ('CD', 'LYS', 'OD1', 'ASN', 10.64), ('CD', 'LYS', 'ND2', 'ASN', 9.44)], [('CE', 'LYS', 'CB', 'ASN', 9.72), ('CE', 'LYS', 'CG', 'ASN', 8.9), ('CE', 'LYS', 'OD1', 'ASN', 9.18), ('CE', 'LYS', 'ND2', 'ASN', 8.16)], [('NZ', 'LYS', 'CB', 'ASN', 10.04), ('NZ', 'LYS', 'CG', 'ASN', 8.99), ('NZ', 'LYS', 'OD1', 'ASN', 9.09), ('NZ', 'LYS', 'ND2', 'ASN', 8.23)]]}
GLU_SER = { 
	'distances':
		[[11.93, 11.19], [12.05, 11.14], [10.8, 9.81], [9.9, 8.92], [10.95, 9.85], [12.57, 11.5], [11.17, 10.15], [10.46, 9.31], [10.0, 8.77], [10.57, 9.43]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 11.93), ('CB', 'GLU', 'OG', 'SER', 11.19)], [('CG', 'GLU', 'CB', 'SER', 12.05), ('CG', 'GLU', 'OG', 'SER', 11.14)], [('CD', 'GLU', 'CB', 'SER', 10.8), ('CD', 'GLU', 'OG', 'SER', 9.81)], [('OE1', 'GLU', 'CB', 'SER', 9.9), ('OE1', 'GLU', 'OG', 'SER', 8.92)], [('OE2', 'GLU', 'CB', 'SER', 10.95), ('OE2', 'GLU', 'OG', 'SER', 9.85)], [('CB', 'GLU', 'CB', 'SER', 12.57), ('CB', 'GLU', 'OG', 'SER', 11.5)], [('CG', 'GLU', 'CB', 'SER', 11.17), ('CG', 'GLU', 'OG', 'SER', 10.15)], [('CD', 'GLU', 'CB', 'SER', 10.46), ('CD', 'GLU', 'OG', 'SER', 9.31)], [('OE1', 'GLU', 'CB', 'SER', 10.0), ('OE1', 'GLU', 'OG', 'SER', 8.77)], [('OE2', 'GLU', 'CB', 'SER', 10.57), ('OE2', 'GLU', 'OG', 'SER', 9.43)]]}
GLU_ASN = { 
	'distances':
		[[14.52, 13.51, 13.17, 13.2], [14.21, 13.15, 12.91, 12.67], [12.75, 11.66, 11.45, 11.16], [12.24, 11.05, 10.74, 10.57], [12.18, 11.21, 11.14, 10.66], [7.56, 8.27, 9.4, 7.88], [6.02, 6.75, 7.9, 6.46], [5.76, 6.02, 7.18, 5.37], [6.18, 6.11, 7.1, 5.4], [5.79, 5.93, 7.13, 5.09]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 14.52), ('CB', 'GLU', 'CG', 'ASN', 13.51), ('CB', 'GLU', 'OD1', 'ASN', 13.17), ('CB', 'GLU', 'ND2', 'ASN', 13.2)], [('CG', 'GLU', 'CB', 'ASN', 14.21), ('CG', 'GLU', 'CG', 'ASN', 13.15), ('CG', 'GLU', 'OD1', 'ASN', 12.91), ('CG', 'GLU', 'ND2', 'ASN', 12.67)], [('CD', 'GLU', 'CB', 'ASN', 12.75), ('CD', 'GLU', 'CG', 'ASN', 11.66), ('CD', 'GLU', 'OD1', 'ASN', 11.45), ('CD', 'GLU', 'ND2', 'ASN', 11.16)], [('OE1', 'GLU', 'CB', 'ASN', 12.24), ('OE1', 'GLU', 'CG', 'ASN', 11.05), ('OE1', 'GLU', 'OD1', 'ASN', 10.74), ('OE1', 'GLU', 'ND2', 'ASN', 10.57)], [('OE2', 'GLU', 'CB', 'ASN', 12.18), ('OE2', 'GLU', 'CG', 'ASN', 11.21), ('OE2', 'GLU', 'OD1', 'ASN', 11.14), ('OE2', 'GLU', 'ND2', 'ASN', 10.66)], [('CB', 'GLU', 'CB', 'ASN', 7.56), ('CB', 'GLU', 'CG', 'ASN', 8.27), ('CB', 'GLU', 'OD1', 'ASN', 9.4), ('CB', 'GLU', 'ND2', 'ASN', 7.88)], [('CG', 'GLU', 'CB', 'ASN', 6.02), ('CG', 'GLU', 'CG', 'ASN', 6.75), ('CG', 'GLU', 'OD1', 'ASN', 7.9), ('CG', 'GLU', 'ND2', 'ASN', 6.46)], [('CD', 'GLU', 'CB', 'ASN', 5.76), ('CD', 'GLU', 'CG', 'ASN', 6.02), ('CD', 'GLU', 'OD1', 'ASN', 7.18), ('CD', 'GLU', 'ND2', 'ASN', 5.37)], [('OE1', 'GLU', 'CB', 'ASN', 6.18), ('OE1', 'GLU', 'CG', 'ASN', 6.11), ('OE1', 'GLU', 'OD1', 'ASN', 7.1), ('OE1', 'GLU', 'ND2', 'ASN', 5.4)], [('OE2', 'GLU', 'CB', 'ASN', 5.79), ('OE2', 'GLU', 'CG', 'ASN', 5.93), ('OE2', 'GLU', 'OD1', 'ASN', 7.13), ('OE2', 'GLU', 'ND2', 'ASN', 5.09)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_GLU, d, 'A_1pii_4_1_1_48')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_GLU, d, 'A_1pii_4_1_1_48')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_LYSI, d, 'A_1pii_4_1_1_48')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_LYS, d, 'A_1pii_4_1_1_48')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_SER, d, 'A_1pii_4_1_1_48')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASN_LYSI, d, 'A_1pii_4_1_1_48')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(LYS_SER, d, 'A_1pii_4_1_1_48')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_LYSI, d, 'A_1pii_4_1_1_48')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_GLUI, d, 'A_1pii_4_1_1_48')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(LYS_ASN, d, 'A_1pii_4_1_1_48')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(GLU_SER, d, 'A_1pii_4_1_1_48')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(GLU_ASN, d, 'A_1pii_4_1_1_48')
	if match12 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_GLU' :  match1,
		'GLU_GLU' :  match2,
		'GLU_LYSI' :  match3,
		'LYS_LYS' :  match4,
		'ASN_SER' :  match5,
		'ASN_LYSI' :  match6,
		'LYS_SER' :  match7,
		'SER_LYSI' :  match8,
		'SER_GLUI' :  match9,
		'LYS_ASN' :  match10,
		'GLU_SER' :  match11,
		'GLU_ASN' :  match12}