'''
FUNC:A_1aq0_3_2_1_73
PDB:1aq0
EC:3.2.1.73
RESI:glu,glu,lys,glu
LOCI:a-232,280,283,288;
'''
import motifFunctions as cmd
GLU_GLUI = { 
	'distances':
		[[15.2, 14.52, 13.29, 13.5, 12.22], [14.37, 13.63, 12.33, 12.44, 11.3], [13.73, 13.12, 11.77, 11.76, 10.85], [13.78, 13.31, 12.01, 12.01, 11.13], [13.39, 12.75, 11.34, 11.19, 10.5]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLUI', 15.2), ('CB', 'GLU', 'CG', 'GLUI', 14.52), ('CB', 'GLU', 'CD', 'GLUI', 13.29), ('CB', 'GLU', 'OE1', 'GLUI', 13.5), ('CB', 'GLU', 'OE2', 'GLUI', 12.22)], [('CG', 'GLU', 'CB', 'GLUI', 14.37), ('CG', 'GLU', 'CG', 'GLUI', 13.63), ('CG', 'GLU', 'CD', 'GLUI', 12.33), ('CG', 'GLU', 'OE1', 'GLUI', 12.44), ('CG', 'GLU', 'OE2', 'GLUI', 11.3)], [('CD', 'GLU', 'CB', 'GLUI', 13.73), ('CD', 'GLU', 'CG', 'GLUI', 13.12), ('CD', 'GLU', 'CD', 'GLUI', 11.77), ('CD', 'GLU', 'OE1', 'GLUI', 11.76), ('CD', 'GLU', 'OE2', 'GLUI', 10.85)], [('OE1', 'GLU', 'CB', 'GLUI', 13.78), ('OE1', 'GLU', 'CG', 'GLUI', 13.31), ('OE1', 'GLU', 'CD', 'GLUI', 12.01), ('OE1', 'GLU', 'OE1', 'GLUI', 12.01), ('OE1', 'GLU', 'OE2', 'GLUI', 11.13)], [('OE2', 'GLU', 'CB', 'GLUI', 13.39), ('OE2', 'GLU', 'CG', 'GLUI', 12.75), ('OE2', 'GLU', 'CD', 'GLUI', 11.34), ('OE2', 'GLU', 'OE1', 'GLUI', 11.19), ('OE2', 'GLU', 'OE2', 'GLUI', 10.5)]]}
LYS_GLU = { 
	'distances':
		[[5.98, 7.05, 7.38, 6.87, 8.47], [6.74, 7.6, 7.52, 6.73, 8.53], [6.46, 7.28, 6.93, 6.21, 7.74], [7.54, 8.06, 7.35, 6.43, 8.03], [7.49, 7.65, 6.77, 5.65, 7.48], [6.72, 7.98, 8.01, 7.76, 8.65], [6.2, 7.2, 6.92, 6.51, 7.54], [5.97, 6.72, 6.28, 6.16, 6.61], [6.49, 6.8, 5.9, 5.61, 6.03], [7.93, 8.26, 7.27, 6.81, 7.33], [15.58, 14.92, 13.85, 13.48, 13.56], [14.53, 13.76, 12.69, 12.42, 12.31], [13.25, 12.54, 11.56, 11.28, 11.28], [12.11, 11.29, 10.28, 10.1, 9.91], [11.77, 10.96, 9.77, 9.49, 9.36]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 5.98), ('CB', 'LYS', 'CG', 'GLU', 7.05), ('CB', 'LYS', 'CD', 'GLU', 7.38), ('CB', 'LYS', 'OE1', 'GLU', 6.87), ('CB', 'LYS', 'OE2', 'GLU', 8.47)], [('CG', 'LYS', 'CB', 'GLU', 6.74), ('CG', 'LYS', 'CG', 'GLU', 7.6), ('CG', 'LYS', 'CD', 'GLU', 7.52), ('CG', 'LYS', 'OE1', 'GLU', 6.73), ('CG', 'LYS', 'OE2', 'GLU', 8.53)], [('CD', 'LYS', 'CB', 'GLU', 6.46), ('CD', 'LYS', 'CG', 'GLU', 7.28), ('CD', 'LYS', 'CD', 'GLU', 6.93), ('CD', 'LYS', 'OE1', 'GLU', 6.21), ('CD', 'LYS', 'OE2', 'GLU', 7.74)], [('CE', 'LYS', 'CB', 'GLU', 7.54), ('CE', 'LYS', 'CG', 'GLU', 8.06), ('CE', 'LYS', 'CD', 'GLU', 7.35), ('CE', 'LYS', 'OE1', 'GLU', 6.43), ('CE', 'LYS', 'OE2', 'GLU', 8.03)], [('NZ', 'LYS', 'CB', 'GLU', 7.49), ('NZ', 'LYS', 'CG', 'GLU', 7.65), ('NZ', 'LYS', 'CD', 'GLU', 6.77), ('NZ', 'LYS', 'OE1', 'GLU', 5.65), ('NZ', 'LYS', 'OE2', 'GLU', 7.48)], [('CB', 'LYS', 'CB', 'GLU', 6.72), ('CB', 'LYS', 'CG', 'GLU', 7.98), ('CB', 'LYS', 'CD', 'GLU', 8.01), ('CB', 'LYS', 'OE1', 'GLU', 7.76), ('CB', 'LYS', 'OE2', 'GLU', 8.65)], [('CG', 'LYS', 'CB', 'GLU', 6.2), ('CG', 'LYS', 'CG', 'GLU', 7.2), ('CG', 'LYS', 'CD', 'GLU', 6.92), ('CG', 'LYS', 'OE1', 'GLU', 6.51), ('CG', 'LYS', 'OE2', 'GLU', 7.54)], [('CD', 'LYS', 'CB', 'GLU', 5.97), ('CD', 'LYS', 'CG', 'GLU', 6.72), ('CD', 'LYS', 'CD', 'GLU', 6.28), ('CD', 'LYS', 'OE1', 'GLU', 6.16), ('CD', 'LYS', 'OE2', 'GLU', 6.61)], [('CE', 'LYS', 'CB', 'GLU', 6.49), ('CE', 'LYS', 'CG', 'GLU', 6.8), ('CE', 'LYS', 'CD', 'GLU', 5.9), ('CE', 'LYS', 'OE1', 'GLU', 5.61), ('CE', 'LYS', 'OE2', 'GLU', 6.03)], [('NZ', 'LYS', 'CB', 'GLU', 7.93), ('NZ', 'LYS', 'CG', 'GLU', 8.26), ('NZ', 'LYS', 'CD', 'GLU', 7.27), ('NZ', 'LYS', 'OE1', 'GLU', 6.81), ('NZ', 'LYS', 'OE2', 'GLU', 7.33)], [('CB', 'LYS', 'CB', 'GLU', 15.58), ('CB', 'LYS', 'CG', 'GLU', 14.92), ('CB', 'LYS', 'CD', 'GLU', 13.85), ('CB', 'LYS', 'OE1', 'GLU', 13.48), ('CB', 'LYS', 'OE2', 'GLU', 13.56)], [('CG', 'LYS', 'CB', 'GLU', 14.53), ('CG', 'LYS', 'CG', 'GLU', 13.76), ('CG', 'LYS', 'CD', 'GLU', 12.69), ('CG', 'LYS', 'OE1', 'GLU', 12.42), ('CG', 'LYS', 'OE2', 'GLU', 12.31)], [('CD', 'LYS', 'CB', 'GLU', 13.25), ('CD', 'LYS', 'CG', 'GLU', 12.54), ('CD', 'LYS', 'CD', 'GLU', 11.56), ('CD', 'LYS', 'OE1', 'GLU', 11.28), ('CD', 'LYS', 'OE2', 'GLU', 11.28)], [('CE', 'LYS', 'CB', 'GLU', 12.11), ('CE', 'LYS', 'CG', 'GLU', 11.29), ('CE', 'LYS', 'CD', 'GLU', 10.28), ('CE', 'LYS', 'OE1', 'GLU', 10.1), ('CE', 'LYS', 'OE2', 'GLU', 9.91)], [('NZ', 'LYS', 'CB', 'GLU', 11.77), ('NZ', 'LYS', 'CG', 'GLU', 10.96), ('NZ', 'LYS', 'CD', 'GLU', 9.77), ('NZ', 'LYS', 'OE1', 'GLU', 9.49), ('NZ', 'LYS', 'OE2', 'GLU', 9.36)]]}
GLU_GLU = { 
	'distances':
		[[9.56, 10.6, 10.49, 10.58, 10.62], [10.76, 11.7, 11.4, 11.41, 11.43], [10.64, 11.38, 10.88, 10.87, 10.76], [10.1, 10.79, 10.16, 10.01, 10.09], [11.32, 11.94, 11.4, 11.49, 11.12], [14.71, 14.48, 13.44, 12.71, 13.53], [14.26, 14.1, 13.0, 12.15, 13.13], [12.79, 12.63, 11.51, 10.64, 11.66], [12.44, 12.11, 10.91, 10.13, 10.92], [12.11, 12.11, 11.07, 10.12, 11.37], [9.56, 10.76, 10.64, 10.1, 11.32], [10.6, 11.7, 11.38, 10.79, 11.94], [10.49, 11.4, 10.88, 10.16, 11.4], [10.58, 11.41, 10.87, 10.01, 11.49], [10.62, 11.43, 10.76, 10.09, 11.12], [15.2, 14.37, 13.73, 13.78, 13.39], [14.52, 13.63, 13.12, 13.31, 12.75], [13.29, 12.33, 11.77, 12.01, 11.34], [13.5, 12.44, 11.76, 12.01, 11.19], [12.22, 11.3, 10.85, 11.13, 10.5], [14.71, 14.26, 12.79, 12.44, 12.11], [14.48, 14.1, 12.63, 12.11, 12.11], [13.44, 13.0, 11.51, 10.91, 11.07], [12.71, 12.15, 10.64, 10.13, 10.12], [13.53, 13.13, 11.66, 10.92, 11.37]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 9.56), ('CB', 'GLU', 'CG', 'GLU', 10.6), ('CB', 'GLU', 'CD', 'GLU', 10.49), ('CB', 'GLU', 'OE1', 'GLU', 10.58), ('CB', 'GLU', 'OE2', 'GLU', 10.62)], [('CG', 'GLU', 'CB', 'GLU', 10.76), ('CG', 'GLU', 'CG', 'GLU', 11.7), ('CG', 'GLU', 'CD', 'GLU', 11.4), ('CG', 'GLU', 'OE1', 'GLU', 11.41), ('CG', 'GLU', 'OE2', 'GLU', 11.43)], [('CD', 'GLU', 'CB', 'GLU', 10.64), ('CD', 'GLU', 'CG', 'GLU', 11.38), ('CD', 'GLU', 'CD', 'GLU', 10.88), ('CD', 'GLU', 'OE1', 'GLU', 10.87), ('CD', 'GLU', 'OE2', 'GLU', 10.76)], [('OE1', 'GLU', 'CB', 'GLU', 10.1), ('OE1', 'GLU', 'CG', 'GLU', 10.79), ('OE1', 'GLU', 'CD', 'GLU', 10.16), ('OE1', 'GLU', 'OE1', 'GLU', 10.01), ('OE1', 'GLU', 'OE2', 'GLU', 10.09)], [('OE2', 'GLU', 'CB', 'GLU', 11.32), ('OE2', 'GLU', 'CG', 'GLU', 11.94), ('OE2', 'GLU', 'CD', 'GLU', 11.4), ('OE2', 'GLU', 'OE1', 'GLU', 11.49), ('OE2', 'GLU', 'OE2', 'GLU', 11.12)], [('CB', 'GLU', 'CB', 'GLU', 14.71), ('CB', 'GLU', 'CG', 'GLU', 14.48), ('CB', 'GLU', 'CD', 'GLU', 13.44), ('CB', 'GLU', 'OE1', 'GLU', 12.71), ('CB', 'GLU', 'OE2', 'GLU', 13.53)], [('CG', 'GLU', 'CB', 'GLU', 14.26), ('CG', 'GLU', 'CG', 'GLU', 14.1), ('CG', 'GLU', 'CD', 'GLU', 13.0), ('CG', 'GLU', 'OE1', 'GLU', 12.15), ('CG', 'GLU', 'OE2', 'GLU', 13.13)], [('CD', 'GLU', 'CB', 'GLU', 12.79), ('CD', 'GLU', 'CG', 'GLU', 12.63), ('CD', 'GLU', 'CD', 'GLU', 11.51), ('CD', 'GLU', 'OE1', 'GLU', 10.64), ('CD', 'GLU', 'OE2', 'GLU', 11.66)], [('OE1', 'GLU', 'CB', 'GLU', 12.44), ('OE1', 'GLU', 'CG', 'GLU', 12.11), ('OE1', 'GLU', 'CD', 'GLU', 10.91), ('OE1', 'GLU', 'OE1', 'GLU', 10.13), ('OE1', 'GLU', 'OE2', 'GLU', 10.92)], [('OE2', 'GLU', 'CB', 'GLU', 12.11), ('OE2', 'GLU', 'CG', 'GLU', 12.11), ('OE2', 'GLU', 'CD', 'GLU', 11.07), ('OE2', 'GLU', 'OE1', 'GLU', 10.12), ('OE2', 'GLU', 'OE2', 'GLU', 11.37)], [('CB', 'GLU', 'CB', 'GLU', 9.56), ('CB', 'GLU', 'CG', 'GLU', 10.76), ('CB', 'GLU', 'CD', 'GLU', 10.64), ('CB', 'GLU', 'OE1', 'GLU', 10.1), ('CB', 'GLU', 'OE2', 'GLU', 11.32)], [('CG', 'GLU', 'CB', 'GLU', 10.6), ('CG', 'GLU', 'CG', 'GLU', 11.7), ('CG', 'GLU', 'CD', 'GLU', 11.38), ('CG', 'GLU', 'OE1', 'GLU', 10.79), ('CG', 'GLU', 'OE2', 'GLU', 11.94)], [('CD', 'GLU', 'CB', 'GLU', 10.49), ('CD', 'GLU', 'CG', 'GLU', 11.4), ('CD', 'GLU', 'CD', 'GLU', 10.88), ('CD', 'GLU', 'OE1', 'GLU', 10.16), ('CD', 'GLU', 'OE2', 'GLU', 11.4)], [('OE1', 'GLU', 'CB', 'GLU', 10.58), ('OE1', 'GLU', 'CG', 'GLU', 11.41), ('OE1', 'GLU', 'CD', 'GLU', 10.87), ('OE1', 'GLU', 'OE1', 'GLU', 10.01), ('OE1', 'GLU', 'OE2', 'GLU', 11.49)], [('OE2', 'GLU', 'CB', 'GLU', 10.62), ('OE2', 'GLU', 'CG', 'GLU', 11.43), ('OE2', 'GLU', 'CD', 'GLU', 10.76), ('OE2', 'GLU', 'OE1', 'GLU', 10.09), ('OE2', 'GLU', 'OE2', 'GLU', 11.12)], [('CB', 'GLU', 'CB', 'GLU', 15.2), ('CB', 'GLU', 'CG', 'GLU', 14.37), ('CB', 'GLU', 'CD', 'GLU', 13.73), ('CB', 'GLU', 'OE1', 'GLU', 13.78), ('CB', 'GLU', 'OE2', 'GLU', 13.39)], [('CG', 'GLU', 'CB', 'GLU', 14.52), ('CG', 'GLU', 'CG', 'GLU', 13.63), ('CG', 'GLU', 'CD', 'GLU', 13.12), ('CG', 'GLU', 'OE1', 'GLU', 13.31), ('CG', 'GLU', 'OE2', 'GLU', 12.75)], [('CD', 'GLU', 'CB', 'GLU', 13.29), ('CD', 'GLU', 'CG', 'GLU', 12.33), ('CD', 'GLU', 'CD', 'GLU', 11.77), ('CD', 'GLU', 'OE1', 'GLU', 12.01), ('CD', 'GLU', 'OE2', 'GLU', 11.34)], [('OE1', 'GLU', 'CB', 'GLU', 13.5), ('OE1', 'GLU', 'CG', 'GLU', 12.44), ('OE1', 'GLU', 'CD', 'GLU', 11.76), ('OE1', 'GLU', 'OE1', 'GLU', 12.01), ('OE1', 'GLU', 'OE2', 'GLU', 11.19)], [('OE2', 'GLU', 'CB', 'GLU', 12.22), ('OE2', 'GLU', 'CG', 'GLU', 11.3), ('OE2', 'GLU', 'CD', 'GLU', 10.85), ('OE2', 'GLU', 'OE1', 'GLU', 11.13), ('OE2', 'GLU', 'OE2', 'GLU', 10.5)], [('CB', 'GLU', 'CB', 'GLU', 14.71), ('CB', 'GLU', 'CG', 'GLU', 14.26), ('CB', 'GLU', 'CD', 'GLU', 12.79), ('CB', 'GLU', 'OE1', 'GLU', 12.44), ('CB', 'GLU', 'OE2', 'GLU', 12.11)], [('CG', 'GLU', 'CB', 'GLU', 14.48), ('CG', 'GLU', 'CG', 'GLU', 14.1), ('CG', 'GLU', 'CD', 'GLU', 12.63), ('CG', 'GLU', 'OE1', 'GLU', 12.11), ('CG', 'GLU', 'OE2', 'GLU', 12.11)], [('CD', 'GLU', 'CB', 'GLU', 13.44), ('CD', 'GLU', 'CG', 'GLU', 13.0), ('CD', 'GLU', 'CD', 'GLU', 11.51), ('CD', 'GLU', 'OE1', 'GLU', 10.91), ('CD', 'GLU', 'OE2', 'GLU', 11.07)], [('OE1', 'GLU', 'CB', 'GLU', 12.71), ('OE1', 'GLU', 'CG', 'GLU', 12.15), ('OE1', 'GLU', 'CD', 'GLU', 10.64), ('OE1', 'GLU', 'OE1', 'GLU', 10.13), ('OE1', 'GLU', 'OE2', 'GLU', 10.12)], [('OE2', 'GLU', 'CB', 'GLU', 13.53), ('OE2', 'GLU', 'CG', 'GLU', 13.13), ('OE2', 'GLU', 'CD', 'GLU', 11.66), ('OE2', 'GLU', 'OE1', 'GLU', 10.92), ('OE2', 'GLU', 'OE2', 'GLU', 11.37)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLUI, d, 'A_1aq0_3_2_1_73')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_GLU, d, 'A_1aq0_3_2_1_73')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_GLU, d, 'A_1aq0_3_2_1_73')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLUI' :  match1,
		'LYS_GLU' :  match2,
		'GLU_GLU' :  match3}