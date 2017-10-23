'''
FUNC:P_1b0p_1_2_7_1
PDB:1b0p
EC:1.2.7.1
RESI:thr,glu,arg,asn
LOCI:a-31,64,114,996;
'''
import motifFunctions as cmd
THR_ARG = { 
	'distances':
		[[7.88, 7.24, 6.11, 6.38, 5.77, 4.63, 6.62], [9.24, 8.56, 7.35, 7.45, 6.66, 5.46, 7.31], [8.06, 7.47, 6.6, 7.02, 6.62, 5.67, 7.51]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ARG', 7.88), ('CB', 'THR', 'CG', 'ARG', 7.24), ('CB', 'THR', 'CD', 'ARG', 6.11), ('CB', 'THR', 'NE', 'ARG', 6.38), ('CB', 'THR', 'CZ', 'ARG', 5.77), ('CB', 'THR', 'NH1', 'ARG', 4.63), ('CB', 'THR', 'NH2', 'ARG', 6.62)], [('OG1', 'THR', 'CB', 'ARG', 9.24), ('OG1', 'THR', 'CG', 'ARG', 8.56), ('OG1', 'THR', 'CD', 'ARG', 7.35), ('OG1', 'THR', 'NE', 'ARG', 7.45), ('OG1', 'THR', 'CZ', 'ARG', 6.66), ('OG1', 'THR', 'NH1', 'ARG', 5.46), ('OG1', 'THR', 'NH2', 'ARG', 7.31)], [('CG2', 'THR', 'CB', 'ARG', 8.06), ('CG2', 'THR', 'CG', 'ARG', 7.47), ('CG2', 'THR', 'CD', 'ARG', 6.6), ('CG2', 'THR', 'NE', 'ARG', 7.02), ('CG2', 'THR', 'CZ', 'ARG', 6.62), ('CG2', 'THR', 'NH1', 'ARG', 5.67), ('CG2', 'THR', 'NH2', 'ARG', 7.51)]]}
GLU_ASN = { 
	'distances':
		[[16.94, 15.51, 14.64, 15.35], [15.98, 14.52, 13.68, 14.31], [14.53, 13.08, 12.22, 12.92], [13.97, 12.54, 11.73, 12.34], [14.01, 12.57, 11.65, 12.48]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASN', 16.94), ('CB', 'GLU', 'CG', 'ASN', 15.51), ('CB', 'GLU', 'OD1', 'ASN', 14.64), ('CB', 'GLU', 'ND2', 'ASN', 15.35)], [('CG', 'GLU', 'CB', 'ASN', 15.98), ('CG', 'GLU', 'CG', 'ASN', 14.52), ('CG', 'GLU', 'OD1', 'ASN', 13.68), ('CG', 'GLU', 'ND2', 'ASN', 14.31)], [('CD', 'GLU', 'CB', 'ASN', 14.53), ('CD', 'GLU', 'CG', 'ASN', 13.08), ('CD', 'GLU', 'OD1', 'ASN', 12.22), ('CD', 'GLU', 'ND2', 'ASN', 12.92)], [('OE1', 'GLU', 'CB', 'ASN', 13.97), ('OE1', 'GLU', 'CG', 'ASN', 12.54), ('OE1', 'GLU', 'OD1', 'ASN', 11.73), ('OE1', 'GLU', 'ND2', 'ASN', 12.34)], [('OE2', 'GLU', 'CB', 'ASN', 14.01), ('OE2', 'GLU', 'CG', 'ASN', 12.57), ('OE2', 'GLU', 'OD1', 'ASN', 11.65), ('OE2', 'GLU', 'ND2', 'ASN', 12.48)]]}
ARG_ASN = { 
	'distances':
		[[15.58, 14.38, 14.52, 13.3], [14.5, 13.31, 13.52, 12.18], [13.23, 12.0, 12.13, 10.9], [12.6, 11.34, 11.49, 10.21], [11.38, 10.09, 10.21, 8.98], [10.59, 9.29, 9.36, 8.25], [11.1, 9.8, 9.93, 8.68]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASN', 15.58), ('CB', 'ARG', 'CG', 'ASN', 14.38), ('CB', 'ARG', 'OD1', 'ASN', 14.52), ('CB', 'ARG', 'ND2', 'ASN', 13.3)], [('CG', 'ARG', 'CB', 'ASN', 14.5), ('CG', 'ARG', 'CG', 'ASN', 13.31), ('CG', 'ARG', 'OD1', 'ASN', 13.52), ('CG', 'ARG', 'ND2', 'ASN', 12.18)], [('CD', 'ARG', 'CB', 'ASN', 13.23), ('CD', 'ARG', 'CG', 'ASN', 12.0), ('CD', 'ARG', 'OD1', 'ASN', 12.13), ('CD', 'ARG', 'ND2', 'ASN', 10.9)], [('NE', 'ARG', 'CB', 'ASN', 12.6), ('NE', 'ARG', 'CG', 'ASN', 11.34), ('NE', 'ARG', 'OD1', 'ASN', 11.49), ('NE', 'ARG', 'ND2', 'ASN', 10.21)], [('CZ', 'ARG', 'CB', 'ASN', 11.38), ('CZ', 'ARG', 'CG', 'ASN', 10.09), ('CZ', 'ARG', 'OD1', 'ASN', 10.21), ('CZ', 'ARG', 'ND2', 'ASN', 8.98)], [('NH1', 'ARG', 'CB', 'ASN', 10.59), ('NH1', 'ARG', 'CG', 'ASN', 9.29), ('NH1', 'ARG', 'OD1', 'ASN', 9.36), ('NH1', 'ARG', 'ND2', 'ASN', 8.25)], [('NH2', 'ARG', 'CB', 'ASN', 11.1), ('NH2', 'ARG', 'CG', 'ASN', 9.8), ('NH2', 'ARG', 'OD1', 'ASN', 9.93), ('NH2', 'ARG', 'ND2', 'ASN', 8.68)]]}
GLU_ARG = { 
	'distances':
		[[12.88, 13.15, 12.14, 12.25, 11.92, 11.43, 12.26], [12.15, 12.28, 11.22, 11.18, 10.79, 10.37, 11.03], [11.87, 11.87, 10.68, 10.59, 10.06, 9.51, 10.28], [11.08, 11.12, 9.91, 9.94, 9.41, 8.75, 9.77], [12.57, 12.43, 11.19, 10.95, 10.29, 9.75, 10.37]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 12.88), ('CB', 'GLU', 'CG', 'ARG', 13.15), ('CB', 'GLU', 'CD', 'ARG', 12.14), ('CB', 'GLU', 'NE', 'ARG', 12.25), ('CB', 'GLU', 'CZ', 'ARG', 11.92), ('CB', 'GLU', 'NH1', 'ARG', 11.43), ('CB', 'GLU', 'NH2', 'ARG', 12.26)], [('CG', 'GLU', 'CB', 'ARG', 12.15), ('CG', 'GLU', 'CG', 'ARG', 12.28), ('CG', 'GLU', 'CD', 'ARG', 11.22), ('CG', 'GLU', 'NE', 'ARG', 11.18), ('CG', 'GLU', 'CZ', 'ARG', 10.79), ('CG', 'GLU', 'NH1', 'ARG', 10.37), ('CG', 'GLU', 'NH2', 'ARG', 11.03)], [('CD', 'GLU', 'CB', 'ARG', 11.87), ('CD', 'GLU', 'CG', 'ARG', 11.87), ('CD', 'GLU', 'CD', 'ARG', 10.68), ('CD', 'GLU', 'NE', 'ARG', 10.59), ('CD', 'GLU', 'CZ', 'ARG', 10.06), ('CD', 'GLU', 'NH1', 'ARG', 9.51), ('CD', 'GLU', 'NH2', 'ARG', 10.28)], [('OE1', 'GLU', 'CB', 'ARG', 11.08), ('OE1', 'GLU', 'CG', 'ARG', 11.12), ('OE1', 'GLU', 'CD', 'ARG', 9.91), ('OE1', 'GLU', 'NE', 'ARG', 9.94), ('OE1', 'GLU', 'CZ', 'ARG', 9.41), ('OE1', 'GLU', 'NH1', 'ARG', 8.75), ('OE1', 'GLU', 'NH2', 'ARG', 9.77)], [('OE2', 'GLU', 'CB', 'ARG', 12.57), ('OE2', 'GLU', 'CG', 'ARG', 12.43), ('OE2', 'GLU', 'CD', 'ARG', 11.19), ('OE2', 'GLU', 'NE', 'ARG', 10.95), ('OE2', 'GLU', 'CZ', 'ARG', 10.29), ('OE2', 'GLU', 'NH1', 'ARG', 9.75), ('OE2', 'GLU', 'NH2', 'ARG', 10.37)]]}
THR_GLU = { 
	'distances':
		[[13.13, 12.37, 11.26, 10.22, 11.52], [13.27, 12.51, 11.28, 10.27, 11.42], [14.52, 13.8, 12.73, 11.66, 13.04]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'GLU', 13.13), ('CB', 'THR', 'CG', 'GLU', 12.37), ('CB', 'THR', 'CD', 'GLU', 11.26), ('CB', 'THR', 'OE1', 'GLU', 10.22), ('CB', 'THR', 'OE2', 'GLU', 11.52)], [('OG1', 'THR', 'CB', 'GLU', 13.27), ('OG1', 'THR', 'CG', 'GLU', 12.51), ('OG1', 'THR', 'CD', 'GLU', 11.28), ('OG1', 'THR', 'OE1', 'GLU', 10.27), ('OG1', 'THR', 'OE2', 'GLU', 11.42)], [('CG2', 'THR', 'CB', 'GLU', 14.52), ('CG2', 'THR', 'CG', 'GLU', 13.8), ('CG2', 'THR', 'CD', 'GLU', 12.73), ('CG2', 'THR', 'OE1', 'GLU', 11.66), ('CG2', 'THR', 'OE2', 'GLU', 13.04)]]}
THR_ASN = { 
	'distances':
		[[9.03, 8.06, 8.31, 7.19], [7.79, 6.87, 7.09, 6.13], [9.63, 8.86, 9.27, 7.95]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASN', 9.03), ('CB', 'THR', 'CG', 'ASN', 8.06), ('CB', 'THR', 'OD1', 'ASN', 8.31), ('CB', 'THR', 'ND2', 'ASN', 7.19)], [('OG1', 'THR', 'CB', 'ASN', 7.79), ('OG1', 'THR', 'CG', 'ASN', 6.87), ('OG1', 'THR', 'OD1', 'ASN', 7.09), ('OG1', 'THR', 'ND2', 'ASN', 6.13)], [('CG2', 'THR', 'CB', 'ASN', 9.63), ('CG2', 'THR', 'CG', 'ASN', 8.86), ('CG2', 'THR', 'OD1', 'ASN', 9.27), ('CG2', 'THR', 'ND2', 'ASN', 7.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_ARG, d, 'P_1b0p_1_2_7_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ASN, d, 'P_1b0p_1_2_7_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ASN, d, 'P_1b0p_1_2_7_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_ARG, d, 'P_1b0p_1_2_7_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(THR_GLU, d, 'P_1b0p_1_2_7_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_ASN, d, 'P_1b0p_1_2_7_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_ARG' :  match1,
		'GLU_ASN' :  match2,
		'ARG_ASN' :  match3,
		'GLU_ARG' :  match4,
		'THR_GLU' :  match5,
		'THR_ASN' :  match6}