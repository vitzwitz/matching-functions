'''
FUNC:P_1gy0_2_4_2_31
PDB:1gy0
EC:2.4.2.31
RESI:ser,glu,arg,glu
LOCI:a-147,159,184,189;
'''
import motifFunctions as cmd
GLU_ARG = { 
	'distances':
		[[11.24, 11.03, 9.6, 9.73, 8.85, 7.54, 9.46], [10.89, 10.61, 9.16, 9.2, 8.27, 6.99, 8.83], [11.02, 10.5, 9.0, 8.73, 7.63, 6.46, 7.91], [10.41, 9.76, 8.25, 7.87, 6.7, 5.58, 6.94], [11.94, 11.36, 9.88, 9.49, 8.32, 7.29, 8.42], [10.0, 11.14, 11.54, 12.87, 13.62, 13.26, 14.84], [10.64, 11.6, 11.89, 13.13, 13.78, 13.39, 14.96], [10.0, 10.8, 11.12, 12.26, 12.94, 12.65, 14.04], [8.81, 9.57, 9.86, 11.01, 11.69, 11.43, 12.8], [10.85, 11.53, 11.89, 12.95, 13.62, 13.41, 14.66]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 11.24), ('CB', 'GLU', 'CG', 'ARG', 11.03), ('CB', 'GLU', 'CD', 'ARG', 9.6), ('CB', 'GLU', 'NE', 'ARG', 9.73), ('CB', 'GLU', 'CZ', 'ARG', 8.85), ('CB', 'GLU', 'NH1', 'ARG', 7.54), ('CB', 'GLU', 'NH2', 'ARG', 9.46)], [('CG', 'GLU', 'CB', 'ARG', 10.89), ('CG', 'GLU', 'CG', 'ARG', 10.61), ('CG', 'GLU', 'CD', 'ARG', 9.16), ('CG', 'GLU', 'NE', 'ARG', 9.2), ('CG', 'GLU', 'CZ', 'ARG', 8.27), ('CG', 'GLU', 'NH1', 'ARG', 6.99), ('CG', 'GLU', 'NH2', 'ARG', 8.83)], [('CD', 'GLU', 'CB', 'ARG', 11.02), ('CD', 'GLU', 'CG', 'ARG', 10.5), ('CD', 'GLU', 'CD', 'ARG', 9.0), ('CD', 'GLU', 'NE', 'ARG', 8.73), ('CD', 'GLU', 'CZ', 'ARG', 7.63), ('CD', 'GLU', 'NH1', 'ARG', 6.46), ('CD', 'GLU', 'NH2', 'ARG', 7.91)], [('OE1', 'GLU', 'CB', 'ARG', 10.41), ('OE1', 'GLU', 'CG', 'ARG', 9.76), ('OE1', 'GLU', 'CD', 'ARG', 8.25), ('OE1', 'GLU', 'NE', 'ARG', 7.87), ('OE1', 'GLU', 'CZ', 'ARG', 6.7), ('OE1', 'GLU', 'NH1', 'ARG', 5.58), ('OE1', 'GLU', 'NH2', 'ARG', 6.94)], [('OE2', 'GLU', 'CB', 'ARG', 11.94), ('OE2', 'GLU', 'CG', 'ARG', 11.36), ('OE2', 'GLU', 'CD', 'ARG', 9.88), ('OE2', 'GLU', 'NE', 'ARG', 9.49), ('OE2', 'GLU', 'CZ', 'ARG', 8.32), ('OE2', 'GLU', 'NH1', 'ARG', 7.29), ('OE2', 'GLU', 'NH2', 'ARG', 8.42)], [('CB', 'GLU', 'CB', 'ARG', 10.0), ('CB', 'GLU', 'CG', 'ARG', 11.14), ('CB', 'GLU', 'CD', 'ARG', 11.54), ('CB', 'GLU', 'NE', 'ARG', 12.87), ('CB', 'GLU', 'CZ', 'ARG', 13.62), ('CB', 'GLU', 'NH1', 'ARG', 13.26), ('CB', 'GLU', 'NH2', 'ARG', 14.84)], [('CG', 'GLU', 'CB', 'ARG', 10.64), ('CG', 'GLU', 'CG', 'ARG', 11.6), ('CG', 'GLU', 'CD', 'ARG', 11.89), ('CG', 'GLU', 'NE', 'ARG', 13.13), ('CG', 'GLU', 'CZ', 'ARG', 13.78), ('CG', 'GLU', 'NH1', 'ARG', 13.39), ('CG', 'GLU', 'NH2', 'ARG', 14.96)], [('CD', 'GLU', 'CB', 'ARG', 10.0), ('CD', 'GLU', 'CG', 'ARG', 10.8), ('CD', 'GLU', 'CD', 'ARG', 11.12), ('CD', 'GLU', 'NE', 'ARG', 12.26), ('CD', 'GLU', 'CZ', 'ARG', 12.94), ('CD', 'GLU', 'NH1', 'ARG', 12.65), ('CD', 'GLU', 'NH2', 'ARG', 14.04)], [('OE1', 'GLU', 'CB', 'ARG', 8.81), ('OE1', 'GLU', 'CG', 'ARG', 9.57), ('OE1', 'GLU', 'CD', 'ARG', 9.86), ('OE1', 'GLU', 'NE', 'ARG', 11.01), ('OE1', 'GLU', 'CZ', 'ARG', 11.69), ('OE1', 'GLU', 'NH1', 'ARG', 11.43), ('OE1', 'GLU', 'NH2', 'ARG', 12.8)], [('OE2', 'GLU', 'CB', 'ARG', 10.85), ('OE2', 'GLU', 'CG', 'ARG', 11.53), ('OE2', 'GLU', 'CD', 'ARG', 11.89), ('OE2', 'GLU', 'NE', 'ARG', 12.95), ('OE2', 'GLU', 'CZ', 'ARG', 13.62), ('OE2', 'GLU', 'NH1', 'ARG', 13.41), ('OE2', 'GLU', 'NH2', 'ARG', 14.66)]]}
SER_ARG = { 
	'distances':
		[[12.64, 13.18, 13.09, 14.03, 14.36, 13.84, 15.35], [12.75, 13.14, 12.87, 13.7, 13.89, 13.31, 14.81]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 12.64), ('CB', 'SER', 'CG', 'ARG', 13.18), ('CB', 'SER', 'CD', 'ARG', 13.09), ('CB', 'SER', 'NE', 'ARG', 14.03), ('CB', 'SER', 'CZ', 'ARG', 14.36), ('CB', 'SER', 'NH1', 'ARG', 13.84), ('CB', 'SER', 'NH2', 'ARG', 15.35)], [('OG', 'SER', 'CB', 'ARG', 12.75), ('OG', 'SER', 'CG', 'ARG', 13.14), ('OG', 'SER', 'CD', 'ARG', 12.87), ('OG', 'SER', 'NE', 'ARG', 13.7), ('OG', 'SER', 'CZ', 'ARG', 13.89), ('OG', 'SER', 'NH1', 'ARG', 13.31), ('OG', 'SER', 'NH2', 'ARG', 14.81)]]}
SER_GLU = { 
	'distances':
		[[13.58, 14.64, 15.34, 14.74, 16.59], [12.74, 13.88, 14.54, 13.92, 15.77], [7.4, 5.92, 5.66, 6.27, 5.43], [8.46, 7.05, 6.64, 6.96, 6.51]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 13.58), ('CB', 'SER', 'CG', 'GLU', 14.64), ('CB', 'SER', 'CD', 'GLU', 15.34), ('CB', 'SER', 'OE1', 'GLU', 14.74), ('CB', 'SER', 'OE2', 'GLU', 16.59)], [('OG', 'SER', 'CB', 'GLU', 12.74), ('OG', 'SER', 'CG', 'GLU', 13.88), ('OG', 'SER', 'CD', 'GLU', 14.54), ('OG', 'SER', 'OE1', 'GLU', 13.92), ('OG', 'SER', 'OE2', 'GLU', 15.77)], [('CB', 'SER', 'CB', 'GLU', 7.4), ('CB', 'SER', 'CG', 'GLU', 5.92), ('CB', 'SER', 'CD', 'GLU', 5.66), ('CB', 'SER', 'OE1', 'GLU', 6.27), ('CB', 'SER', 'OE2', 'GLU', 5.43)], [('OG', 'SER', 'CB', 'GLU', 8.46), ('OG', 'SER', 'CG', 'GLU', 7.05), ('OG', 'SER', 'CD', 'GLU', 6.64), ('OG', 'SER', 'OE1', 'GLU', 6.96), ('OG', 'SER', 'OE2', 'GLU', 6.51)]]}
GLU_GLU = { 
	'distances':
		[[14.14, 14.03, 13.75, 12.81, 14.6], [14.67, 14.72, 14.43, 13.41, 15.33], [15.51, 15.53, 15.08, 14.01, 15.92], [15.07, 15.02, 14.45, 13.36, 15.22], [16.71, 16.76, 16.32, 15.24, 17.16], [14.14, 14.67, 15.51, 15.07, 16.71], [14.03, 14.72, 15.53, 15.02, 16.76], [13.75, 14.43, 15.08, 14.45, 16.32], [12.81, 13.41, 14.01, 13.36, 15.24], [14.6, 15.33, 15.92, 15.22, 17.16]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 14.14), ('CB', 'GLU', 'CG', 'GLU', 14.03), ('CB', 'GLU', 'CD', 'GLU', 13.75), ('CB', 'GLU', 'OE1', 'GLU', 12.81), ('CB', 'GLU', 'OE2', 'GLU', 14.6)], [('CG', 'GLU', 'CB', 'GLU', 14.67), ('CG', 'GLU', 'CG', 'GLU', 14.72), ('CG', 'GLU', 'CD', 'GLU', 14.43), ('CG', 'GLU', 'OE1', 'GLU', 13.41), ('CG', 'GLU', 'OE2', 'GLU', 15.33)], [('CD', 'GLU', 'CB', 'GLU', 15.51), ('CD', 'GLU', 'CG', 'GLU', 15.53), ('CD', 'GLU', 'CD', 'GLU', 15.08), ('CD', 'GLU', 'OE1', 'GLU', 14.01), ('CD', 'GLU', 'OE2', 'GLU', 15.92)], [('OE1', 'GLU', 'CB', 'GLU', 15.07), ('OE1', 'GLU', 'CG', 'GLU', 15.02), ('OE1', 'GLU', 'CD', 'GLU', 14.45), ('OE1', 'GLU', 'OE1', 'GLU', 13.36), ('OE1', 'GLU', 'OE2', 'GLU', 15.22)], [('OE2', 'GLU', 'CB', 'GLU', 16.71), ('OE2', 'GLU', 'CG', 'GLU', 16.76), ('OE2', 'GLU', 'CD', 'GLU', 16.32), ('OE2', 'GLU', 'OE1', 'GLU', 15.24), ('OE2', 'GLU', 'OE2', 'GLU', 17.16)], [('CB', 'GLU', 'CB', 'GLU', 14.14), ('CB', 'GLU', 'CG', 'GLU', 14.67), ('CB', 'GLU', 'CD', 'GLU', 15.51), ('CB', 'GLU', 'OE1', 'GLU', 15.07), ('CB', 'GLU', 'OE2', 'GLU', 16.71)], [('CG', 'GLU', 'CB', 'GLU', 14.03), ('CG', 'GLU', 'CG', 'GLU', 14.72), ('CG', 'GLU', 'CD', 'GLU', 15.53), ('CG', 'GLU', 'OE1', 'GLU', 15.02), ('CG', 'GLU', 'OE2', 'GLU', 16.76)], [('CD', 'GLU', 'CB', 'GLU', 13.75), ('CD', 'GLU', 'CG', 'GLU', 14.43), ('CD', 'GLU', 'CD', 'GLU', 15.08), ('CD', 'GLU', 'OE1', 'GLU', 14.45), ('CD', 'GLU', 'OE2', 'GLU', 16.32)], [('OE1', 'GLU', 'CB', 'GLU', 12.81), ('OE1', 'GLU', 'CG', 'GLU', 13.41), ('OE1', 'GLU', 'CD', 'GLU', 14.01), ('OE1', 'GLU', 'OE1', 'GLU', 13.36), ('OE1', 'GLU', 'OE2', 'GLU', 15.24)], [('OE2', 'GLU', 'CB', 'GLU', 14.6), ('OE2', 'GLU', 'CG', 'GLU', 15.33), ('OE2', 'GLU', 'CD', 'GLU', 15.92), ('OE2', 'GLU', 'OE1', 'GLU', 15.22), ('OE2', 'GLU', 'OE2', 'GLU', 17.16)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ARG, d, 'P_1gy0_2_4_2_31')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_ARG, d, 'P_1gy0_2_4_2_31')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_GLU, d, 'P_1gy0_2_4_2_31')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_GLU, d, 'P_1gy0_2_4_2_31')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ARG' :  match1,
		'SER_ARG' :  match2,
		'SER_GLU' :  match3,
		'GLU_GLU' :  match4}