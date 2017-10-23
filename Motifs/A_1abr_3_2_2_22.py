'''
FUNC:A_1abr_3_2_2_22
PDB:1abr
EC:3.2.2.22
RESI:glu,arg
LOCI:a-164,167;
'''
import motifFunctions as cmd
GLU_ARG = { 
	'distances':
		[[7.87, 7.81, 7.35, 7.88, 7.89, 7.36, 8.79, 10.19, 9.1, 8.63, 8.13],
		 [8.56, 8.24, 7.46, 7.69, 7.36, 6.67, 8.11, 11.17, 10.14, 9.54, 9.13],
		 [8.14, 7.81, 6.75, 7.01, 6.54, 5.59, 7.41, 10.82, 9.92, 9.34, 9.22],
		 [7.0, 6.76, 5.69, 6.19, 5.95, 5.04, 7.04, 9.67, 8.83, 8.27, 8.31],
		 [9.15, 8.75, 7.54, 7.64, 6.92, 5.79, 7.64, 11.83, 10.99, 10.43, 10.39],
		 [5.87, 6.47, 6.82, 7.88, 8.56, 8.42, 9.66, 7.36, 6.2, 6.04, 5.52],
		 [6.51, 6.73, 6.97, 7.77, 8.32, 8.22, 9.29, 8.38, 7.19, 6.75, 5.98],
		 [6.71, 6.56, 6.38, 6.94, 7.22, 7.01, 8.13, 9.15, 8.01, 7.35, 6.73],
		 [7.4, 6.9, 6.78, 6.95, 7.15, 7.18, 7.79, 10.01, 8.85, 7.95, 7.1]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 7.87), ('CB', 'GLU', 'CG', 'ARG', 7.81), ('CB', 'GLU', 'CD', 'ARG', 7.35), ('CB', 'GLU', 'NE', 'ARG', 7.88), ('CB', 'GLU', 'CZ', 'ARG', 7.89), ('CB', 'GLU', 'NH1', 'ARG', 7.36), ('CB', 'GLU', 'NH2', 'ARG', 8.79), ('CB', 'GLU', 'O', 'ARG', 10.19), ('CB', 'GLU', 'C', 'ARG', 9.1), ('CB', 'GLU', 'CA', 'ARG', 8.63), ('CB', 'GLU', 'N', 'ARG', 8.13)], [('CG', 'GLU', 'CB', 'ARG', 8.56), ('CG', 'GLU', 'CG', 'ARG', 8.24), ('CG', 'GLU', 'CD', 'ARG', 7.46), ('CG', 'GLU', 'NE', 'ARG', 7.69), ('CG', 'GLU', 'CZ', 'ARG', 7.36), ('CG', 'GLU', 'NH1', 'ARG', 6.67), ('CG', 'GLU', 'NH2', 'ARG', 8.11), ('CG', 'GLU', 'O', 'ARG', 11.17), ('CG', 'GLU', 'C', 'ARG', 10.14), ('CG', 'GLU', 'CA', 'ARG', 9.54), ('CG', 'GLU', 'N', 'ARG', 9.13)], [('CD', 'GLU', 'CB', 'ARG', 8.14), ('CD', 'GLU', 'CG', 'ARG', 7.81), ('CD', 'GLU', 'CD', 'ARG', 6.75), ('CD', 'GLU', 'NE', 'ARG', 7.01), ('CD', 'GLU', 'CZ', 'ARG', 6.54), ('CD', 'GLU', 'NH1', 'ARG', 5.59), ('CD', 'GLU', 'NH2', 'ARG', 7.41), ('CD', 'GLU', 'O', 'ARG', 10.82), ('CD', 'GLU', 'C', 'ARG', 9.92), ('CD', 'GLU', 'CA', 'ARG', 9.34), ('CD', 'GLU', 'N', 'ARG', 9.22)], [('OE1', 'GLU', 'CB', 'ARG', 7.0), ('OE1', 'GLU', 'CG', 'ARG', 6.76), ('OE1', 'GLU', 'CD', 'ARG', 5.69), ('OE1', 'GLU', 'NE', 'ARG', 6.19), ('OE1', 'GLU', 'CZ', 'ARG', 5.95), ('OE1', 'GLU', 'NH1', 'ARG', 5.04), ('OE1', 'GLU', 'NH2', 'ARG', 7.04), ('OE1', 'GLU', 'O', 'ARG', 9.67), ('OE1', 'GLU', 'C', 'ARG', 8.83), ('OE1', 'GLU', 'CA', 'ARG', 8.27), ('OE1', 'GLU', 'N', 'ARG', 8.31)], [('OE2', 'GLU', 'CB', 'ARG', 9.15), ('OE2', 'GLU', 'CG', 'ARG', 8.75), ('OE2', 'GLU', 'CD', 'ARG', 7.54), ('OE2', 'GLU', 'NE', 'ARG', 7.64), ('OE2', 'GLU', 'CZ', 'ARG', 6.92), ('OE2', 'GLU', 'NH1', 'ARG', 5.79), ('OE2', 'GLU', 'NH2', 'ARG', 7.64), ('OE2', 'GLU', 'O', 'ARG', 11.83), ('OE2', 'GLU', 'C', 'ARG', 10.99), ('OE2', 'GLU', 'CA', 'ARG', 10.43), ('OE2', 'GLU', 'N', 'ARG', 10.39)], [('O', 'GLU', 'CB', 'ARG', 5.87), ('O', 'GLU', 'CG', 'ARG', 6.47), ('O', 'GLU', 'CD', 'ARG', 6.82), ('O', 'GLU', 'NE', 'ARG', 7.88), ('O', 'GLU', 'CZ', 'ARG', 8.56), ('O', 'GLU', 'NH1', 'ARG', 8.42), ('O', 'GLU', 'NH2', 'ARG', 9.66), ('O', 'GLU', 'O', 'ARG', 7.36), ('O', 'GLU', 'C', 'ARG', 6.2), ('O', 'GLU', 'CA', 'ARG', 6.04), ('O', 'GLU', 'N', 'ARG', 5.52)], [('C', 'GLU', 'CB', 'ARG', 6.51), ('C', 'GLU', 'CG', 'ARG', 6.73), ('C', 'GLU', 'CD', 'ARG', 6.97), ('C', 'GLU', 'NE', 'ARG', 7.77), ('C', 'GLU', 'CZ', 'ARG', 8.32), ('C', 'GLU', 'NH1', 'ARG', 8.22), ('C', 'GLU', 'NH2', 'ARG', 9.29), ('C', 'GLU', 'O', 'ARG', 8.38), ('C', 'GLU', 'C', 'ARG', 7.19), ('C', 'GLU', 'CA', 'ARG', 6.75), ('C', 'GLU', 'N', 'ARG', 5.98)], [('CA', 'GLU', 'CB', 'ARG', 6.71), ('CA', 'GLU', 'CG', 'ARG', 6.56), ('CA', 'GLU', 'CD', 'ARG', 6.38), ('CA', 'GLU', 'NE', 'ARG', 6.94), ('CA', 'GLU', 'CZ', 'ARG', 7.22), ('CA', 'GLU', 'NH1', 'ARG', 7.01), ('CA', 'GLU', 'NH2', 'ARG', 8.13), ('CA', 'GLU', 'O', 'ARG', 9.15), ('CA', 'GLU', 'C', 'ARG', 8.01), ('CA', 'GLU', 'CA', 'ARG', 7.35), ('CA', 'GLU', 'N', 'ARG', 6.73)], [('N', 'GLU', 'CB', 'ARG', 7.4), ('N', 'GLU', 'CG', 'ARG', 6.9), ('N', 'GLU', 'CD', 'ARG', 6.78), ('N', 'GLU', 'NE', 'ARG', 6.95), ('N', 'GLU', 'CZ', 'ARG', 7.15), ('N', 'GLU', 'NH1', 'ARG', 7.18), ('N', 'GLU', 'NH2', 'ARG', 7.79), ('N', 'GLU', 'O', 'ARG', 10.01), ('N', 'GLU', 'C', 'ARG', 8.85), ('N', 'GLU', 'CA', 'ARG', 7.95), ('N', 'GLU', 'N', 'ARG', 7.1)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ARG, d, 'A_1abr_3_2_2_22')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ARG' :  match1}