'''
FUNC:M_1mqw_3_6_1_13
PDB:1mqw
EC:3.6.1.13
RESI:arg,glu,mn,mn,mn
LOCI:a-64,142,401,402,403;
'''
import motifFunctions as cmd
ARG_MN = { 
	'distances':
		[[12.76], [11.54], [10.39], [9.26], [8.11], [8.11], [7.24], [15.53], [14.44], [13.25], [12.27], [11.12], [10.86], [10.41], [17.15], [16.19], [14.8], [13.94], [12.64], [12.06], [12.06]],
	'comparisons':
		[[('CB', 'ARG', 'MN', 'MN', 12.76)], [('CG', 'ARG', 'MN', 'MN', 11.54)], [('CD', 'ARG', 'MN', 'MN', 10.39)], [('NE', 'ARG', 'MN', 'MN', 9.26)], [('CZ', 'ARG', 'MN', 'MN', 8.11)], [('NH1', 'ARG', 'MN', 'MN', 8.11)], [('NH2', 'ARG', 'MN', 'MN', 7.24)], [('CB', 'ARG', 'MN', 'MN', 15.53)], [('CG', 'ARG', 'MN', 'MN', 14.44)], [('CD', 'ARG', 'MN', 'MN', 13.25)], [('NE', 'ARG', 'MN', 'MN', 12.27)], [('CZ', 'ARG', 'MN', 'MN', 11.12)], [('NH1', 'ARG', 'MN', 'MN', 10.86)], [('NH2', 'ARG', 'MN', 'MN', 10.41)], [('CB', 'ARG', 'MN', 'MN', 17.15)], [('CG', 'ARG', 'MN', 'MN', 16.19)], [('CD', 'ARG', 'MN', 'MN', 14.8)], [('NE', 'ARG', 'MN', 'MN', 13.94)], [('CZ', 'ARG', 'MN', 'MN', 12.64)], [('NH1', 'ARG', 'MN', 'MN', 12.06)], [('NH2', 'ARG', 'MN', 'MN', 12.06)]]}
GLU_ARG = { 
	'distances':
		[[14.36, 13.64, 12.77, 12.3, 11.59, 11.26, 11.46], [13.73, 12.92, 11.92, 11.35, 10.51, 10.15, 10.3], [14.85, 13.96, 12.89, 12.19, 11.24, 10.87, 10.87], [15.97, 15.08, 14.05, 13.34, 12.41, 12.09, 12.0], [14.72, 13.79, 12.62, 11.85, 10.79, 10.38, 10.35]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 14.36), ('CB', 'GLU', 'CG', 'ARG', 13.64), ('CB', 'GLU', 'CD', 'ARG', 12.77), ('CB', 'GLU', 'NE', 'ARG', 12.3), ('CB', 'GLU', 'CZ', 'ARG', 11.59), ('CB', 'GLU', 'NH1', 'ARG', 11.26), ('CB', 'GLU', 'NH2', 'ARG', 11.46)], [('CG', 'GLU', 'CB', 'ARG', 13.73), ('CG', 'GLU', 'CG', 'ARG', 12.92), ('CG', 'GLU', 'CD', 'ARG', 11.92), ('CG', 'GLU', 'NE', 'ARG', 11.35), ('CG', 'GLU', 'CZ', 'ARG', 10.51), ('CG', 'GLU', 'NH1', 'ARG', 10.15), ('CG', 'GLU', 'NH2', 'ARG', 10.3)], [('CD', 'GLU', 'CB', 'ARG', 14.85), ('CD', 'GLU', 'CG', 'ARG', 13.96), ('CD', 'GLU', 'CD', 'ARG', 12.89), ('CD', 'GLU', 'NE', 'ARG', 12.19), ('CD', 'GLU', 'CZ', 'ARG', 11.24), ('CD', 'GLU', 'NH1', 'ARG', 10.87), ('CD', 'GLU', 'NH2', 'ARG', 10.87)], [('OE1', 'GLU', 'CB', 'ARG', 15.97), ('OE1', 'GLU', 'CG', 'ARG', 15.08), ('OE1', 'GLU', 'CD', 'ARG', 14.05), ('OE1', 'GLU', 'NE', 'ARG', 13.34), ('OE1', 'GLU', 'CZ', 'ARG', 12.41), ('OE1', 'GLU', 'NH1', 'ARG', 12.09), ('OE1', 'GLU', 'NH2', 'ARG', 12.0)], [('OE2', 'GLU', 'CB', 'ARG', 14.72), ('OE2', 'GLU', 'CG', 'ARG', 13.79), ('OE2', 'GLU', 'CD', 'ARG', 12.62), ('OE2', 'GLU', 'NE', 'ARG', 11.85), ('OE2', 'GLU', 'CZ', 'ARG', 10.79), ('OE2', 'GLU', 'NH1', 'ARG', 10.38), ('OE2', 'GLU', 'NH2', 'ARG', 10.35)]]}
MN_MN = { 
	'distances':
		[5.29, 7.71, 5.29, 5.77, 7.71],
	'comparisons':
		[('MN', 'MN', 'MN', 'MN', 5.29), ('MN', 'MN', 'MN', 'MN', 7.71), ('MN', 'MN', 'MN', 'MN', 5.29), ('MN', 'MN', 'MN', 'MN', 5.77), ('MN', 'MN', 'MN', 'MN', 7.71)]}
MN_MNI = { 
	'distances':
		[5.77],
	'comparisons':
		[('MN', 'MN', 'MN', 'MNI', 5.77)]}
GLU_MN = { 
	'distances':
		[[8.49], [7.08], [6.79], [7.72], [5.97], [7.6], [6.35], [5.14], [5.6], [4.13], [10.41], [9.14], [8.0], [8.45], [6.85]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 8.49)], [('CG', 'GLU', 'MN', 'MN', 7.08)], [('CD', 'GLU', 'MN', 'MN', 6.79)], [('OE1', 'GLU', 'MN', 'MN', 7.72)], [('OE2', 'GLU', 'MN', 'MN', 5.97)], [('CB', 'GLU', 'MN', 'MN', 7.6)], [('CG', 'GLU', 'MN', 'MN', 6.35)], [('CD', 'GLU', 'MN', 'MN', 5.14)], [('OE1', 'GLU', 'MN', 'MN', 5.6)], [('OE2', 'GLU', 'MN', 'MN', 4.13)], [('CB', 'GLU', 'MN', 'MN', 10.41)], [('CG', 'GLU', 'MN', 'MN', 9.14)], [('CD', 'GLU', 'MN', 'MN', 8.0)], [('OE1', 'GLU', 'MN', 'MN', 8.45)], [('OE2', 'GLU', 'MN', 'MN', 6.85)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_MN, d, 'M_1mqw_3_6_1_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ARG, d, 'M_1mqw_3_6_1_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(MN_MN, d, 'M_1mqw_3_6_1_13')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(MN_MNI, d, 'M_1mqw_3_6_1_13')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_MN, d, 'M_1mqw_3_6_1_13')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_MN' :  match1,
		'GLU_ARG' :  match2,
		'MN_MN' :  match3,
		'MN_MNI' :  match4,
		'GLU_MN' :  match5}