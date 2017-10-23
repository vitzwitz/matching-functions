'''
FUNC:A_1d6m_5_99_1_2
PDB:1d6m
EC:5.99.1.2
RESI:glu,lys,tyr,arg
LOCI:a-7,8,328,330;
'''
import motifFunctions as cmd
ARG_TYR = { 
	'distances':
		[[9.03, 7.92, 7.9, 7.18, 7.23, 6.39, 6.44, 6.2], [8.44, 7.19, 6.87, 6.68, 6.03, 5.78, 5.4, 5.08], [9.66, 8.32, 7.76, 7.88, 6.68, 6.82, 6.12, 5.34], [10.17, 8.95, 8.23, 8.76, 7.24, 7.85, 7.03, 6.4], [11.46, 10.27, 9.54, 10.05, 8.56, 9.13, 8.34, 7.62], [12.33, 11.08, 10.45, 10.69, 9.4, 9.66, 8.96, 8.1], [11.99, 10.91, 10.09, 10.87, 9.21, 10.06, 9.21, 8.61]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TYR', 9.03), ('CB', 'ARG', 'CG', 'TYR', 7.92), ('CB', 'ARG', 'CD1', 'TYR', 7.9), ('CB', 'ARG', 'CD2', 'TYR', 7.18), ('CB', 'ARG', 'CE1', 'TYR', 7.23), ('CB', 'ARG', 'CE2', 'TYR', 6.39), ('CB', 'ARG', 'CZ', 'TYR', 6.44), ('CB', 'ARG', 'OH', 'TYR', 6.2)], [('CG', 'ARG', 'CB', 'TYR', 8.44), ('CG', 'ARG', 'CG', 'TYR', 7.19), ('CG', 'ARG', 'CD1', 'TYR', 6.87), ('CG', 'ARG', 'CD2', 'TYR', 6.68), ('CG', 'ARG', 'CE1', 'TYR', 6.03), ('CG', 'ARG', 'CE2', 'TYR', 5.78), ('CG', 'ARG', 'CZ', 'TYR', 5.4), ('CG', 'ARG', 'OH', 'TYR', 5.08)], [('CD', 'ARG', 'CB', 'TYR', 9.66), ('CD', 'ARG', 'CG', 'TYR', 8.32), ('CD', 'ARG', 'CD1', 'TYR', 7.76), ('CD', 'ARG', 'CD2', 'TYR', 7.88), ('CD', 'ARG', 'CE1', 'TYR', 6.68), ('CD', 'ARG', 'CE2', 'TYR', 6.82), ('CD', 'ARG', 'CZ', 'TYR', 6.12), ('CD', 'ARG', 'OH', 'TYR', 5.34)], [('NE', 'ARG', 'CB', 'TYR', 10.17), ('NE', 'ARG', 'CG', 'TYR', 8.95), ('NE', 'ARG', 'CD1', 'TYR', 8.23), ('NE', 'ARG', 'CD2', 'TYR', 8.76), ('NE', 'ARG', 'CE1', 'TYR', 7.24), ('NE', 'ARG', 'CE2', 'TYR', 7.85), ('NE', 'ARG', 'CZ', 'TYR', 7.03), ('NE', 'ARG', 'OH', 'TYR', 6.4)], [('CZ', 'ARG', 'CB', 'TYR', 11.46), ('CZ', 'ARG', 'CG', 'TYR', 10.27), ('CZ', 'ARG', 'CD1', 'TYR', 9.54), ('CZ', 'ARG', 'CD2', 'TYR', 10.05), ('CZ', 'ARG', 'CE1', 'TYR', 8.56), ('CZ', 'ARG', 'CE2', 'TYR', 9.13), ('CZ', 'ARG', 'CZ', 'TYR', 8.34), ('CZ', 'ARG', 'OH', 'TYR', 7.62)], [('NH1', 'ARG', 'CB', 'TYR', 12.33), ('NH1', 'ARG', 'CG', 'TYR', 11.08), ('NH1', 'ARG', 'CD1', 'TYR', 10.45), ('NH1', 'ARG', 'CD2', 'TYR', 10.69), ('NH1', 'ARG', 'CE1', 'TYR', 9.4), ('NH1', 'ARG', 'CE2', 'TYR', 9.66), ('NH1', 'ARG', 'CZ', 'TYR', 8.96), ('NH1', 'ARG', 'OH', 'TYR', 8.1)], [('NH2', 'ARG', 'CB', 'TYR', 11.99), ('NH2', 'ARG', 'CG', 'TYR', 10.91), ('NH2', 'ARG', 'CD1', 'TYR', 10.09), ('NH2', 'ARG', 'CD2', 'TYR', 10.87), ('NH2', 'ARG', 'CE1', 'TYR', 9.21), ('NH2', 'ARG', 'CE2', 'TYR', 10.06), ('NH2', 'ARG', 'CZ', 'TYR', 9.21), ('NH2', 'ARG', 'OH', 'TYR', 8.61)]]}
GLU_TYR = { 
	'distances':
		[[12.61, 11.59, 10.36, 12.03, 9.54, 11.35, 10.1, 9.64], [12.49, 11.34, 10.09, 11.68, 9.1, 10.87, 9.55, 8.91], [12.52, 11.25, 10.11, 11.37, 8.97, 10.41, 9.15, 8.31], [12.35, 11.09, 10.05, 11.15, 8.96, 10.2, 9.04, 8.25], [12.94, 11.6, 10.48, 11.61, 9.24, 10.53, 9.28, 8.27]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 12.61), ('CB', 'GLU', 'CG', 'TYR', 11.59), ('CB', 'GLU', 'CD1', 'TYR', 10.36), ('CB', 'GLU', 'CD2', 'TYR', 12.03), ('CB', 'GLU', 'CE1', 'TYR', 9.54), ('CB', 'GLU', 'CE2', 'TYR', 11.35), ('CB', 'GLU', 'CZ', 'TYR', 10.1), ('CB', 'GLU', 'OH', 'TYR', 9.64)], [('CG', 'GLU', 'CB', 'TYR', 12.49), ('CG', 'GLU', 'CG', 'TYR', 11.34), ('CG', 'GLU', 'CD1', 'TYR', 10.09), ('CG', 'GLU', 'CD2', 'TYR', 11.68), ('CG', 'GLU', 'CE1', 'TYR', 9.1), ('CG', 'GLU', 'CE2', 'TYR', 10.87), ('CG', 'GLU', 'CZ', 'TYR', 9.55), ('CG', 'GLU', 'OH', 'TYR', 8.91)], [('CD', 'GLU', 'CB', 'TYR', 12.52), ('CD', 'GLU', 'CG', 'TYR', 11.25), ('CD', 'GLU', 'CD1', 'TYR', 10.11), ('CD', 'GLU', 'CD2', 'TYR', 11.37), ('CD', 'GLU', 'CE1', 'TYR', 8.97), ('CD', 'GLU', 'CE2', 'TYR', 10.41), ('CD', 'GLU', 'CZ', 'TYR', 9.15), ('CD', 'GLU', 'OH', 'TYR', 8.31)], [('OE1', 'GLU', 'CB', 'TYR', 12.35), ('OE1', 'GLU', 'CG', 'TYR', 11.09), ('OE1', 'GLU', 'CD1', 'TYR', 10.05), ('OE1', 'GLU', 'CD2', 'TYR', 11.15), ('OE1', 'GLU', 'CE1', 'TYR', 8.96), ('OE1', 'GLU', 'CE2', 'TYR', 10.2), ('OE1', 'GLU', 'CZ', 'TYR', 9.04), ('OE1', 'GLU', 'OH', 'TYR', 8.25)], [('OE2', 'GLU', 'CB', 'TYR', 12.94), ('OE2', 'GLU', 'CG', 'TYR', 11.6), ('OE2', 'GLU', 'CD1', 'TYR', 10.48), ('OE2', 'GLU', 'CD2', 'TYR', 11.61), ('OE2', 'GLU', 'CE1', 'TYR', 9.24), ('OE2', 'GLU', 'CE2', 'TYR', 10.53), ('OE2', 'GLU', 'CZ', 'TYR', 9.28), ('OE2', 'GLU', 'OH', 'TYR', 8.27)]]}
LYS_TYR = { 
	'distances':
		[[14.73, 13.87, 12.48, 14.55, 11.79, 13.97, 12.61, 12.2], [13.22, 12.38, 10.99, 13.09, 10.34, 12.56, 11.22, 10.9], [12.79, 12.05, 10.66, 12.85, 10.13, 12.43, 11.12, 10.93], [13.1, 12.28, 10.91, 12.98, 10.28, 12.47, 11.15, 10.85], [13.71, 13.02, 11.68, 13.8, 11.19, 13.4, 12.14, 11.93]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 14.73), ('CB', 'LYS', 'CG', 'TYR', 13.87), ('CB', 'LYS', 'CD1', 'TYR', 12.48), ('CB', 'LYS', 'CD2', 'TYR', 14.55), ('CB', 'LYS', 'CE1', 'TYR', 11.79), ('CB', 'LYS', 'CE2', 'TYR', 13.97), ('CB', 'LYS', 'CZ', 'TYR', 12.61), ('CB', 'LYS', 'OH', 'TYR', 12.2)], [('CG', 'LYS', 'CB', 'TYR', 13.22), ('CG', 'LYS', 'CG', 'TYR', 12.38), ('CG', 'LYS', 'CD1', 'TYR', 10.99), ('CG', 'LYS', 'CD2', 'TYR', 13.09), ('CG', 'LYS', 'CE1', 'TYR', 10.34), ('CG', 'LYS', 'CE2', 'TYR', 12.56), ('CG', 'LYS', 'CZ', 'TYR', 11.22), ('CG', 'LYS', 'OH', 'TYR', 10.9)], [('CD', 'LYS', 'CB', 'TYR', 12.79), ('CD', 'LYS', 'CG', 'TYR', 12.05), ('CD', 'LYS', 'CD1', 'TYR', 10.66), ('CD', 'LYS', 'CD2', 'TYR', 12.85), ('CD', 'LYS', 'CE1', 'TYR', 10.13), ('CD', 'LYS', 'CE2', 'TYR', 12.43), ('CD', 'LYS', 'CZ', 'TYR', 11.12), ('CD', 'LYS', 'OH', 'TYR', 10.93)], [('CE', 'LYS', 'CB', 'TYR', 13.1), ('CE', 'LYS', 'CG', 'TYR', 12.28), ('CE', 'LYS', 'CD1', 'TYR', 10.91), ('CE', 'LYS', 'CD2', 'TYR', 12.98), ('CE', 'LYS', 'CE1', 'TYR', 10.28), ('CE', 'LYS', 'CE2', 'TYR', 12.47), ('CE', 'LYS', 'CZ', 'TYR', 11.15), ('CE', 'LYS', 'OH', 'TYR', 10.85)], [('NZ', 'LYS', 'CB', 'TYR', 13.71), ('NZ', 'LYS', 'CG', 'TYR', 13.02), ('NZ', 'LYS', 'CD1', 'TYR', 11.68), ('NZ', 'LYS', 'CD2', 'TYR', 13.8), ('NZ', 'LYS', 'CE1', 'TYR', 11.19), ('NZ', 'LYS', 'CE2', 'TYR', 13.4), ('NZ', 'LYS', 'CZ', 'TYR', 12.14), ('NZ', 'LYS', 'OH', 'TYR', 11.93)]]}
GLU_ARG = { 
	'distances':
		[[13.24, 11.79, 11.14, 11.16, 11.83, 12.47, 12.06], [12.22, 10.79, 9.99, 9.94, 10.5, 11.09, 10.72], [11.69, 10.35, 9.47, 9.64, 10.2, 10.61, 10.64], [11.94, 10.64, 9.9, 10.27, 10.94, 11.3, 11.49], [11.26, 9.98, 8.93, 9.07, 9.47, 9.75, 9.93]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 13.24), ('CB', 'GLU', 'CG', 'ARG', 11.79), ('CB', 'GLU', 'CD', 'ARG', 11.14), ('CB', 'GLU', 'NE', 'ARG', 11.16), ('CB', 'GLU', 'CZ', 'ARG', 11.83), ('CB', 'GLU', 'NH1', 'ARG', 12.47), ('CB', 'GLU', 'NH2', 'ARG', 12.06)], [('CG', 'GLU', 'CB', 'ARG', 12.22), ('CG', 'GLU', 'CG', 'ARG', 10.79), ('CG', 'GLU', 'CD', 'ARG', 9.99), ('CG', 'GLU', 'NE', 'ARG', 9.94), ('CG', 'GLU', 'CZ', 'ARG', 10.5), ('CG', 'GLU', 'NH1', 'ARG', 11.09), ('CG', 'GLU', 'NH2', 'ARG', 10.72)], [('CD', 'GLU', 'CB', 'ARG', 11.69), ('CD', 'GLU', 'CG', 'ARG', 10.35), ('CD', 'GLU', 'CD', 'ARG', 9.47), ('CD', 'GLU', 'NE', 'ARG', 9.64), ('CD', 'GLU', 'CZ', 'ARG', 10.2), ('CD', 'GLU', 'NH1', 'ARG', 10.61), ('CD', 'GLU', 'NH2', 'ARG', 10.64)], [('OE1', 'GLU', 'CB', 'ARG', 11.94), ('OE1', 'GLU', 'CG', 'ARG', 10.64), ('OE1', 'GLU', 'CD', 'ARG', 9.9), ('OE1', 'GLU', 'NE', 'ARG', 10.27), ('OE1', 'GLU', 'CZ', 'ARG', 10.94), ('OE1', 'GLU', 'NH1', 'ARG', 11.3), ('OE1', 'GLU', 'NH2', 'ARG', 11.49)], [('OE2', 'GLU', 'CB', 'ARG', 11.26), ('OE2', 'GLU', 'CG', 'ARG', 9.98), ('OE2', 'GLU', 'CD', 'ARG', 8.93), ('OE2', 'GLU', 'NE', 'ARG', 9.07), ('OE2', 'GLU', 'CZ', 'ARG', 9.47), ('OE2', 'GLU', 'NH1', 'ARG', 9.75), ('OE2', 'GLU', 'NH2', 'ARG', 9.93)]]}
LYS_GLU = { 
	'distances':
		[[6.55, 6.34, 7.73, 8.69, 8.08], [5.92, 5.66, 7.1, 8.03, 7.55], [7.17, 6.81, 8.16, 9.1, 8.5], [8.03, 7.3, 8.45, 9.54, 8.51], [9.44, 8.79, 9.95, 11.03, 9.99]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 6.55), ('CB', 'LYS', 'CG', 'GLU', 6.34), ('CB', 'LYS', 'CD', 'GLU', 7.73), ('CB', 'LYS', 'OE1', 'GLU', 8.69), ('CB', 'LYS', 'OE2', 'GLU', 8.08)], [('CG', 'LYS', 'CB', 'GLU', 5.92), ('CG', 'LYS', 'CG', 'GLU', 5.66), ('CG', 'LYS', 'CD', 'GLU', 7.1), ('CG', 'LYS', 'OE1', 'GLU', 8.03), ('CG', 'LYS', 'OE2', 'GLU', 7.55)], [('CD', 'LYS', 'CB', 'GLU', 7.17), ('CD', 'LYS', 'CG', 'GLU', 6.81), ('CD', 'LYS', 'CD', 'GLU', 8.16), ('CD', 'LYS', 'OE1', 'GLU', 9.1), ('CD', 'LYS', 'OE2', 'GLU', 8.5)], [('CE', 'LYS', 'CB', 'GLU', 8.03), ('CE', 'LYS', 'CG', 'GLU', 7.3), ('CE', 'LYS', 'CD', 'GLU', 8.45), ('CE', 'LYS', 'OE1', 'GLU', 9.54), ('CE', 'LYS', 'OE2', 'GLU', 8.51)], [('NZ', 'LYS', 'CB', 'GLU', 9.44), ('NZ', 'LYS', 'CG', 'GLU', 8.79), ('NZ', 'LYS', 'CD', 'GLU', 9.95), ('NZ', 'LYS', 'OE1', 'GLU', 11.03), ('NZ', 'LYS', 'OE2', 'GLU', 9.99)]]}
LYS_ARG = { 
	'distances':
		[[14.73, 13.28, 12.45, 11.82, 12.07, 12.89, 11.7], [13.49, 12.02, 11.31, 10.72, 11.11, 12.02, 10.81], [13.12, 11.67, 11.06, 10.31, 10.68, 11.71, 10.22], [12.55, 11.17, 10.43, 9.5, 9.69, 10.7, 9.08], [13.24, 11.93, 11.27, 10.2, 10.28, 11.35, 9.48]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 14.73), ('CB', 'LYS', 'CG', 'ARG', 13.28), ('CB', 'LYS', 'CD', 'ARG', 12.45), ('CB', 'LYS', 'NE', 'ARG', 11.82), ('CB', 'LYS', 'CZ', 'ARG', 12.07), ('CB', 'LYS', 'NH1', 'ARG', 12.89), ('CB', 'LYS', 'NH2', 'ARG', 11.7)], [('CG', 'LYS', 'CB', 'ARG', 13.49), ('CG', 'LYS', 'CG', 'ARG', 12.02), ('CG', 'LYS', 'CD', 'ARG', 11.31), ('CG', 'LYS', 'NE', 'ARG', 10.72), ('CG', 'LYS', 'CZ', 'ARG', 11.11), ('CG', 'LYS', 'NH1', 'ARG', 12.02), ('CG', 'LYS', 'NH2', 'ARG', 10.81)], [('CD', 'LYS', 'CB', 'ARG', 13.12), ('CD', 'LYS', 'CG', 'ARG', 11.67), ('CD', 'LYS', 'CD', 'ARG', 11.06), ('CD', 'LYS', 'NE', 'ARG', 10.31), ('CD', 'LYS', 'CZ', 'ARG', 10.68), ('CD', 'LYS', 'NH1', 'ARG', 11.71), ('CD', 'LYS', 'NH2', 'ARG', 10.22)], [('CE', 'LYS', 'CB', 'ARG', 12.55), ('CE', 'LYS', 'CG', 'ARG', 11.17), ('CE', 'LYS', 'CD', 'ARG', 10.43), ('CE', 'LYS', 'NE', 'ARG', 9.5), ('CE', 'LYS', 'CZ', 'ARG', 9.69), ('CE', 'LYS', 'NH1', 'ARG', 10.7), ('CE', 'LYS', 'NH2', 'ARG', 9.08)], [('NZ', 'LYS', 'CB', 'ARG', 13.24), ('NZ', 'LYS', 'CG', 'ARG', 11.93), ('NZ', 'LYS', 'CD', 'ARG', 11.27), ('NZ', 'LYS', 'NE', 'ARG', 10.2), ('NZ', 'LYS', 'CZ', 'ARG', 10.28), ('NZ', 'LYS', 'NH1', 'ARG', 11.35), ('NZ', 'LYS', 'NH2', 'ARG', 9.48)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_TYR, d, 'A_1d6m_5_99_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_TYR, d, 'A_1d6m_5_99_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_TYR, d, 'A_1d6m_5_99_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_ARG, d, 'A_1d6m_5_99_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LYS_GLU, d, 'A_1d6m_5_99_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_ARG, d, 'A_1d6m_5_99_1_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_TYR' :  match1,
		'GLU_TYR' :  match2,
		'LYS_TYR' :  match3,
		'GLU_ARG' :  match4,
		'LYS_GLU' :  match5,
		'LYS_ARG' :  match6}