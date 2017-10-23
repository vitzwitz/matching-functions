'''
FUNC:M_1gt7_4_1_2_19
PDB:1gt7
EC:4.1.2.19
RESI:glu,glu,zn
LOCI:a-117,171,275;
'''
import motifFunctions as cmd
ZN_GLUI = { 
	'distances':
		[27.81, 26.49, 26.19, 26.84, 25.36],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'GLUI', 27.81), ('ZN', 'ZN', 'CG', 'GLUI', 26.49), ('ZN', 'ZN', 'CD', 'GLUI', 26.19), ('ZN', 'ZN', 'OE1', 'GLUI', 26.84), ('ZN', 'ZN', 'OE2', 'GLUI', 25.36)]}
GLU_ZN = { 
	'distances':
		[[8.76], [7.46], [7.51], [6.64], [8.62], [27.81], [26.49], [26.19], [26.84], [25.36]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.76)], [('CG', 'GLU', 'ZN', 'ZN', 7.46)], [('CD', 'GLU', 'ZN', 'ZN', 7.51)], [('OE1', 'GLU', 'ZN', 'ZN', 6.64)], [('OE2', 'GLU', 'ZN', 'ZN', 8.62)], [('CB', 'GLU', 'ZN', 'ZN', 27.81)], [('CG', 'GLU', 'ZN', 'ZN', 26.49)], [('CD', 'GLU', 'ZN', 'ZN', 26.19)], [('OE1', 'GLU', 'ZN', 'ZN', 26.84)], [('OE2', 'GLU', 'ZN', 'ZN', 25.36)]]}
GLU_GLU = { 
	'distances':
		[[30.04, 28.93, 28.82, 29.38, 28.24], [30.08, 28.92, 28.77, 29.37, 28.13], [30.46, 29.29, 29.2, 29.85, 28.54], [30.44, 29.24, 29.12, 29.79, 28.42], [30.85, 29.72, 29.68, 30.35, 29.06], [30.04, 30.08, 30.46, 30.44, 30.85], [28.93, 28.92, 29.29, 29.24, 29.72], [28.82, 28.77, 29.2, 29.12, 29.68], [29.38, 29.37, 29.85, 29.79, 30.35], [28.24, 28.13, 28.54, 28.42, 29.06]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 30.04), ('CB', 'GLU', 'CG', 'GLU', 28.93), ('CB', 'GLU', 'CD', 'GLU', 28.82), ('CB', 'GLU', 'OE1', 'GLU', 29.38), ('CB', 'GLU', 'OE2', 'GLU', 28.24)], [('CG', 'GLU', 'CB', 'GLU', 30.08), ('CG', 'GLU', 'CG', 'GLU', 28.92), ('CG', 'GLU', 'CD', 'GLU', 28.77), ('CG', 'GLU', 'OE1', 'GLU', 29.37), ('CG', 'GLU', 'OE2', 'GLU', 28.13)], [('CD', 'GLU', 'CB', 'GLU', 30.46), ('CD', 'GLU', 'CG', 'GLU', 29.29), ('CD', 'GLU', 'CD', 'GLU', 29.2), ('CD', 'GLU', 'OE1', 'GLU', 29.85), ('CD', 'GLU', 'OE2', 'GLU', 28.54)], [('OE1', 'GLU', 'CB', 'GLU', 30.44), ('OE1', 'GLU', 'CG', 'GLU', 29.24), ('OE1', 'GLU', 'CD', 'GLU', 29.12), ('OE1', 'GLU', 'OE1', 'GLU', 29.79), ('OE1', 'GLU', 'OE2', 'GLU', 28.42)], [('OE2', 'GLU', 'CB', 'GLU', 30.85), ('OE2', 'GLU', 'CG', 'GLU', 29.72), ('OE2', 'GLU', 'CD', 'GLU', 29.68), ('OE2', 'GLU', 'OE1', 'GLU', 30.35), ('OE2', 'GLU', 'OE2', 'GLU', 29.06)], [('CB', 'GLU', 'CB', 'GLU', 30.04), ('CB', 'GLU', 'CG', 'GLU', 30.08), ('CB', 'GLU', 'CD', 'GLU', 30.46), ('CB', 'GLU', 'OE1', 'GLU', 30.44), ('CB', 'GLU', 'OE2', 'GLU', 30.85)], [('CG', 'GLU', 'CB', 'GLU', 28.93), ('CG', 'GLU', 'CG', 'GLU', 28.92), ('CG', 'GLU', 'CD', 'GLU', 29.29), ('CG', 'GLU', 'OE1', 'GLU', 29.24), ('CG', 'GLU', 'OE2', 'GLU', 29.72)], [('CD', 'GLU', 'CB', 'GLU', 28.82), ('CD', 'GLU', 'CG', 'GLU', 28.77), ('CD', 'GLU', 'CD', 'GLU', 29.2), ('CD', 'GLU', 'OE1', 'GLU', 29.12), ('CD', 'GLU', 'OE2', 'GLU', 29.68)], [('OE1', 'GLU', 'CB', 'GLU', 29.38), ('OE1', 'GLU', 'CG', 'GLU', 29.37), ('OE1', 'GLU', 'CD', 'GLU', 29.85), ('OE1', 'GLU', 'OE1', 'GLU', 29.79), ('OE1', 'GLU', 'OE2', 'GLU', 30.35)], [('OE2', 'GLU', 'CB', 'GLU', 28.24), ('OE2', 'GLU', 'CG', 'GLU', 28.13), ('OE2', 'GLU', 'CD', 'GLU', 28.54), ('OE2', 'GLU', 'OE1', 'GLU', 28.42), ('OE2', 'GLU', 'OE2', 'GLU', 29.06)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ZN_GLUI, d, 'M_1gt7_4_1_2_19')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ZN, d, 'M_1gt7_4_1_2_19')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_GLU, d, 'M_1gt7_4_1_2_19')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ZN_GLUI' :  match1,
		'GLU_ZN' :  match2,
		'GLU_GLU' :  match3}