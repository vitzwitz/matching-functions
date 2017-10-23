'''
FUNC:A_12as_6_3_1_1
PDB:12as
EC:6.3.1.1
RESI:asp,arg,gln
LOCI:a-46,100,116;
'''
import motifFunctions as cmd
ARG_ASP = { 
	'distances':
		[[11.5, 11.15, 11.5, 10.69, 10.16, 11.36, 12.17, 12.69], [10.04, 9.64, 9.97, 9.2, 8.72, 9.9, 10.71, 11.3], [9.21, 8.9, 9.42, 8.34, 8.33, 9.48, 10.06, 10.6], [9.18, 8.65, 9.18, 7.9, 8.68, 9.73, 10.19, 10.89], [8.24, 7.55, 8.07, 6.73, 7.99, 8.94, 9.33, 10.14], [8.6, 7.67, 7.98, 6.85, 8.27, 9.14, 9.63, 10.61], [7.7, 7.07, 7.78, 6.11, 7.99, 8.82, 8.95, 9.72], [14.13, 13.82, 14.07, 13.44, 12.47, 13.69, 14.64, 15.1], [13.31, 13.1, 13.36, 12.81, 11.55, 12.78, 13.74, 14.12], [11.97, 11.81, 12.16, 11.48, 10.4, 11.63, 12.49, 12.85], [12.33, 12.3, 12.8, 11.92, 10.98, 12.2, 12.92, 13.15]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 11.5), ('CB', 'ARG', 'CG', 'ASP', 11.15), ('CB', 'ARG', 'OD1', 'ASP', 11.5), ('CB', 'ARG', 'OD2', 'ASP', 10.69), ('CB', 'ARG', 'O', 'ASP', 10.16), ('CB', 'ARG', 'C', 'ASP', 11.36), ('CB', 'ARG', 'CA', 'ASP', 12.17), ('CB', 'ARG', 'N', 'ASP', 12.69)], [('CG', 'ARG', 'CB', 'ASP', 10.04), ('CG', 'ARG', 'CG', 'ASP', 9.64), ('CG', 'ARG', 'OD1', 'ASP', 9.97), ('CG', 'ARG', 'OD2', 'ASP', 9.2), ('CG', 'ARG', 'O', 'ASP', 8.72), ('CG', 'ARG', 'C', 'ASP', 9.9), ('CG', 'ARG', 'CA', 'ASP', 10.71), ('CG', 'ARG', 'N', 'ASP', 11.3)], [('CD', 'ARG', 'CB', 'ASP', 9.21), ('CD', 'ARG', 'CG', 'ASP', 8.9), ('CD', 'ARG', 'OD1', 'ASP', 9.42), ('CD', 'ARG', 'OD2', 'ASP', 8.34), ('CD', 'ARG', 'O', 'ASP', 8.33), ('CD', 'ARG', 'C', 'ASP', 9.48), ('CD', 'ARG', 'CA', 'ASP', 10.06), ('CD', 'ARG', 'N', 'ASP', 10.6)], [('NE', 'ARG', 'CB', 'ASP', 9.18), ('NE', 'ARG', 'CG', 'ASP', 8.65), ('NE', 'ARG', 'OD1', 'ASP', 9.18), ('NE', 'ARG', 'OD2', 'ASP', 7.9), ('NE', 'ARG', 'O', 'ASP', 8.68), ('NE', 'ARG', 'C', 'ASP', 9.73), ('NE', 'ARG', 'CA', 'ASP', 10.19), ('NE', 'ARG', 'N', 'ASP', 10.89)], [('CZ', 'ARG', 'CB', 'ASP', 8.24), ('CZ', 'ARG', 'CG', 'ASP', 7.55), ('CZ', 'ARG', 'OD1', 'ASP', 8.07), ('CZ', 'ARG', 'OD2', 'ASP', 6.73), ('CZ', 'ARG', 'O', 'ASP', 7.99), ('CZ', 'ARG', 'C', 'ASP', 8.94), ('CZ', 'ARG', 'CA', 'ASP', 9.33), ('CZ', 'ARG', 'N', 'ASP', 10.14)], [('NH1', 'ARG', 'CB', 'ASP', 8.6), ('NH1', 'ARG', 'CG', 'ASP', 7.67), ('NH1', 'ARG', 'OD1', 'ASP', 7.98), ('NH1', 'ARG', 'OD2', 'ASP', 6.85), ('NH1', 'ARG', 'O', 'ASP', 8.27), ('NH1', 'ARG', 'C', 'ASP', 9.14), ('NH1', 'ARG', 'CA', 'ASP', 9.63), ('NH1', 'ARG', 'N', 'ASP', 10.61)], [('NH2', 'ARG', 'CB', 'ASP', 7.7), ('NH2', 'ARG', 'CG', 'ASP', 7.07), ('NH2', 'ARG', 'OD1', 'ASP', 7.78), ('NH2', 'ARG', 'OD2', 'ASP', 6.11), ('NH2', 'ARG', 'O', 'ASP', 7.99), ('NH2', 'ARG', 'C', 'ASP', 8.82), ('NH2', 'ARG', 'CA', 'ASP', 8.95), ('NH2', 'ARG', 'N', 'ASP', 9.72)], [('O', 'ARG', 'CB', 'ASP', 14.13), ('O', 'ARG', 'CG', 'ASP', 13.82), ('O', 'ARG', 'OD1', 'ASP', 14.07), ('O', 'ARG', 'OD2', 'ASP', 13.44), ('O', 'ARG', 'O', 'ASP', 12.47), ('O', 'ARG', 'C', 'ASP', 13.69), ('O', 'ARG', 'CA', 'ASP', 14.64), ('O', 'ARG', 'N', 'ASP', 15.1)], [('C', 'ARG', 'CB', 'ASP', 13.31), ('C', 'ARG', 'CG', 'ASP', 13.1), ('C', 'ARG', 'OD1', 'ASP', 13.36), ('C', 'ARG', 'OD2', 'ASP', 12.81), ('C', 'ARG', 'O', 'ASP', 11.55), ('C', 'ARG', 'C', 'ASP', 12.78), ('C', 'ARG', 'CA', 'ASP', 13.74), ('C', 'ARG', 'N', 'ASP', 14.12)], [('CA', 'ARG', 'CB', 'ASP', 11.97), ('CA', 'ARG', 'CG', 'ASP', 11.81), ('CA', 'ARG', 'OD1', 'ASP', 12.16), ('CA', 'ARG', 'OD2', 'ASP', 11.48), ('CA', 'ARG', 'O', 'ASP', 10.4), ('CA', 'ARG', 'C', 'ASP', 11.63), ('CA', 'ARG', 'CA', 'ASP', 12.49), ('CA', 'ARG', 'N', 'ASP', 12.85)], [('N', 'ARG', 'CB', 'ASP', 12.33), ('N', 'ARG', 'CG', 'ASP', 12.3), ('N', 'ARG', 'OD1', 'ASP', 12.8), ('N', 'ARG', 'OD2', 'ASP', 11.92), ('N', 'ARG', 'O', 'ASP', 10.98), ('N', 'ARG', 'C', 'ASP', 12.2), ('N', 'ARG', 'CA', 'ASP', 12.92), ('N', 'ARG', 'N', 'ASP', 13.15)]]}
ARG_GLN = { 
	'distances':
		[[12.38, 11.42, 10.93, 9.83, 11.87, 14.5, 14.34, 12.99, 12.2], [11.83, 10.86, 10.17, 9.03, 10.98, 14.08, 13.93, 12.62, 11.98], [10.43, 9.54, 8.84, 7.75, 9.62, 12.62, 12.51, 11.26, 10.62], [9.54, 8.5, 7.76, 6.61, 8.61, 11.99, 11.75, 10.43, 9.94], [9.24, 8.16, 7.2, 6.0, 7.91, 11.84, 11.57, 10.31, 10.02], [9.92, 8.71, 7.7, 6.48, 8.4, 12.69, 12.32, 11.02, 10.86], [8.12, 7.12, 6.05, 4.9, 6.65, 10.71, 10.47, 9.28, 9.1], [14.79, 13.84, 13.53, 12.46, 14.54, 16.74, 16.58, 15.22, 14.28], [14.66, 13.78, 13.38, 12.31, 14.31, 16.55, 16.47, 15.16, 14.22], [13.32, 12.49, 12.03, 10.98, 12.91, 15.21, 15.16, 13.88, 12.99], [12.85, 12.16, 11.84, 10.89, 12.73, 14.49, 14.51, 13.29, 12.27]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLN', 12.38), ('CB', 'ARG', 'CG', 'GLN', 11.42), ('CB', 'ARG', 'CD', 'GLN', 10.93), ('CB', 'ARG', 'OE1', 'GLN', 9.83), ('CB', 'ARG', 'NE2', 'GLN', 11.87), ('CB', 'ARG', 'O', 'GLN', 14.5), ('CB', 'ARG', 'C', 'GLN', 14.34), ('CB', 'ARG', 'CA', 'GLN', 12.99), ('CB', 'ARG', 'N', 'GLN', 12.2)], [('CG', 'ARG', 'CB', 'GLN', 11.83), ('CG', 'ARG', 'CG', 'GLN', 10.86), ('CG', 'ARG', 'CD', 'GLN', 10.17), ('CG', 'ARG', 'OE1', 'GLN', 9.03), ('CG', 'ARG', 'NE2', 'GLN', 10.98), ('CG', 'ARG', 'O', 'GLN', 14.08), ('CG', 'ARG', 'C', 'GLN', 13.93), ('CG', 'ARG', 'CA', 'GLN', 12.62), ('CG', 'ARG', 'N', 'GLN', 11.98)], [('CD', 'ARG', 'CB', 'GLN', 10.43), ('CD', 'ARG', 'CG', 'GLN', 9.54), ('CD', 'ARG', 'CD', 'GLN', 8.84), ('CD', 'ARG', 'OE1', 'GLN', 7.75), ('CD', 'ARG', 'NE2', 'GLN', 9.62), ('CD', 'ARG', 'O', 'GLN', 12.62), ('CD', 'ARG', 'C', 'GLN', 12.51), ('CD', 'ARG', 'CA', 'GLN', 11.26), ('CD', 'ARG', 'N', 'GLN', 10.62)], [('NE', 'ARG', 'CB', 'GLN', 9.54), ('NE', 'ARG', 'CG', 'GLN', 8.5), ('NE', 'ARG', 'CD', 'GLN', 7.76), ('NE', 'ARG', 'OE1', 'GLN', 6.61), ('NE', 'ARG', 'NE2', 'GLN', 8.61), ('NE', 'ARG', 'O', 'GLN', 11.99), ('NE', 'ARG', 'C', 'GLN', 11.75), ('NE', 'ARG', 'CA', 'GLN', 10.43), ('NE', 'ARG', 'N', 'GLN', 9.94)], [('CZ', 'ARG', 'CB', 'GLN', 9.24), ('CZ', 'ARG', 'CG', 'GLN', 8.16), ('CZ', 'ARG', 'CD', 'GLN', 7.2), ('CZ', 'ARG', 'OE1', 'GLN', 6.0), ('CZ', 'ARG', 'NE2', 'GLN', 7.91), ('CZ', 'ARG', 'O', 'GLN', 11.84), ('CZ', 'ARG', 'C', 'GLN', 11.57), ('CZ', 'ARG', 'CA', 'GLN', 10.31), ('CZ', 'ARG', 'N', 'GLN', 10.02)], [('NH1', 'ARG', 'CB', 'GLN', 9.92), ('NH1', 'ARG', 'CG', 'GLN', 8.71), ('NH1', 'ARG', 'CD', 'GLN', 7.7), ('NH1', 'ARG', 'OE1', 'GLN', 6.48), ('NH1', 'ARG', 'NE2', 'GLN', 8.4), ('NH1', 'ARG', 'O', 'GLN', 12.69), ('NH1', 'ARG', 'C', 'GLN', 12.32), ('NH1', 'ARG', 'CA', 'GLN', 11.02), ('NH1', 'ARG', 'N', 'GLN', 10.86)], [('NH2', 'ARG', 'CB', 'GLN', 8.12), ('NH2', 'ARG', 'CG', 'GLN', 7.12), ('NH2', 'ARG', 'CD', 'GLN', 6.05), ('NH2', 'ARG', 'OE1', 'GLN', 4.9), ('NH2', 'ARG', 'NE2', 'GLN', 6.65), ('NH2', 'ARG', 'O', 'GLN', 10.71), ('NH2', 'ARG', 'C', 'GLN', 10.47), ('NH2', 'ARG', 'CA', 'GLN', 9.28), ('NH2', 'ARG', 'N', 'GLN', 9.1)], [('O', 'ARG', 'CB', 'GLN', 14.79), ('O', 'ARG', 'CG', 'GLN', 13.84), ('O', 'ARG', 'CD', 'GLN', 13.53), ('O', 'ARG', 'OE1', 'GLN', 12.46), ('O', 'ARG', 'NE2', 'GLN', 14.54), ('O', 'ARG', 'O', 'GLN', 16.74), ('O', 'ARG', 'C', 'GLN', 16.58), ('O', 'ARG', 'CA', 'GLN', 15.22), ('O', 'ARG', 'N', 'GLN', 14.28)], [('C', 'ARG', 'CB', 'GLN', 14.66), ('C', 'ARG', 'CG', 'GLN', 13.78), ('C', 'ARG', 'CD', 'GLN', 13.38), ('C', 'ARG', 'OE1', 'GLN', 12.31), ('C', 'ARG', 'NE2', 'GLN', 14.31), ('C', 'ARG', 'O', 'GLN', 16.55), ('C', 'ARG', 'C', 'GLN', 16.47), ('C', 'ARG', 'CA', 'GLN', 15.16), ('C', 'ARG', 'N', 'GLN', 14.22)], [('CA', 'ARG', 'CB', 'GLN', 13.32), ('CA', 'ARG', 'CG', 'GLN', 12.49), ('CA', 'ARG', 'CD', 'GLN', 12.03), ('CA', 'ARG', 'OE1', 'GLN', 10.98), ('CA', 'ARG', 'NE2', 'GLN', 12.91), ('CA', 'ARG', 'O', 'GLN', 15.21), ('CA', 'ARG', 'C', 'GLN', 15.16), ('CA', 'ARG', 'CA', 'GLN', 13.88), ('CA', 'ARG', 'N', 'GLN', 12.99)], [('N', 'ARG', 'CB', 'GLN', 12.85), ('N', 'ARG', 'CG', 'GLN', 12.16), ('N', 'ARG', 'CD', 'GLN', 11.84), ('N', 'ARG', 'OE1', 'GLN', 10.89), ('N', 'ARG', 'NE2', 'GLN', 12.73), ('N', 'ARG', 'O', 'GLN', 14.49), ('N', 'ARG', 'C', 'GLN', 14.51), ('N', 'ARG', 'CA', 'GLN', 13.29), ('N', 'ARG', 'N', 'GLN', 12.27)]]}
ASP_GLN = { 
	'distances':
		[[11.92, 11.55, 10.13, 9.58, 9.67, 13.72, 13.9, 13.33, 13.45], [11.67, 11.12, 9.64, 8.99, 9.25, 13.79, 13.81, 13.13, 13.33], [12.72, 12.08, 10.59, 9.88, 10.25, 14.94, 14.92, 14.19, 14.41], [10.54, 9.93, 8.44, 7.79, 8.09, 12.78, 12.73, 12.01, 12.25], [13.55, 12.99, 11.65, 10.84, 11.51, 15.49, 15.64, 14.87, 14.75], [14.04, 13.54, 12.14, 11.41, 11.86, 15.94, 16.11, 15.41, 15.39], [13.43, 13.07, 11.66, 11.08, 11.21, 15.17, 15.39, 14.82, 14.9], [13.82, 13.6, 12.27, 11.76, 11.78, 15.27, 15.61, 15.15, 15.16]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 11.92), ('CB', 'ASP', 'CG', 'GLN', 11.55), ('CB', 'ASP', 'CD', 'GLN', 10.13), ('CB', 'ASP', 'OE1', 'GLN', 9.58), ('CB', 'ASP', 'NE2', 'GLN', 9.67), ('CB', 'ASP', 'O', 'GLN', 13.72), ('CB', 'ASP', 'C', 'GLN', 13.9), ('CB', 'ASP', 'CA', 'GLN', 13.33), ('CB', 'ASP', 'N', 'GLN', 13.45)], [('CG', 'ASP', 'CB', 'GLN', 11.67), ('CG', 'ASP', 'CG', 'GLN', 11.12), ('CG', 'ASP', 'CD', 'GLN', 9.64), ('CG', 'ASP', 'OE1', 'GLN', 8.99), ('CG', 'ASP', 'NE2', 'GLN', 9.25), ('CG', 'ASP', 'O', 'GLN', 13.79), ('CG', 'ASP', 'C', 'GLN', 13.81), ('CG', 'ASP', 'CA', 'GLN', 13.13), ('CG', 'ASP', 'N', 'GLN', 13.33)], [('OD1', 'ASP', 'CB', 'GLN', 12.72), ('OD1', 'ASP', 'CG', 'GLN', 12.08), ('OD1', 'ASP', 'CD', 'GLN', 10.59), ('OD1', 'ASP', 'OE1', 'GLN', 9.88), ('OD1', 'ASP', 'NE2', 'GLN', 10.25), ('OD1', 'ASP', 'O', 'GLN', 14.94), ('OD1', 'ASP', 'C', 'GLN', 14.92), ('OD1', 'ASP', 'CA', 'GLN', 14.19), ('OD1', 'ASP', 'N', 'GLN', 14.41)], [('OD2', 'ASP', 'CB', 'GLN', 10.54), ('OD2', 'ASP', 'CG', 'GLN', 9.93), ('OD2', 'ASP', 'CD', 'GLN', 8.44), ('OD2', 'ASP', 'OE1', 'GLN', 7.79), ('OD2', 'ASP', 'NE2', 'GLN', 8.09), ('OD2', 'ASP', 'O', 'GLN', 12.78), ('OD2', 'ASP', 'C', 'GLN', 12.73), ('OD2', 'ASP', 'CA', 'GLN', 12.01), ('OD2', 'ASP', 'N', 'GLN', 12.25)], [('O', 'ASP', 'CB', 'GLN', 13.55), ('O', 'ASP', 'CG', 'GLN', 12.99), ('O', 'ASP', 'CD', 'GLN', 11.65), ('O', 'ASP', 'OE1', 'GLN', 10.84), ('O', 'ASP', 'NE2', 'GLN', 11.51), ('O', 'ASP', 'O', 'GLN', 15.49), ('O', 'ASP', 'C', 'GLN', 15.64), ('O', 'ASP', 'CA', 'GLN', 14.87), ('O', 'ASP', 'N', 'GLN', 14.75)], [('C', 'ASP', 'CB', 'GLN', 14.04), ('C', 'ASP', 'CG', 'GLN', 13.54), ('C', 'ASP', 'CD', 'GLN', 12.14), ('C', 'ASP', 'OE1', 'GLN', 11.41), ('C', 'ASP', 'NE2', 'GLN', 11.86), ('C', 'ASP', 'O', 'GLN', 15.94), ('C', 'ASP', 'C', 'GLN', 16.11), ('C', 'ASP', 'CA', 'GLN', 15.41), ('C', 'ASP', 'N', 'GLN', 15.39)], [('CA', 'ASP', 'CB', 'GLN', 13.43), ('CA', 'ASP', 'CG', 'GLN', 13.07), ('CA', 'ASP', 'CD', 'GLN', 11.66), ('CA', 'ASP', 'OE1', 'GLN', 11.08), ('CA', 'ASP', 'NE2', 'GLN', 11.21), ('CA', 'ASP', 'O', 'GLN', 15.17), ('CA', 'ASP', 'C', 'GLN', 15.39), ('CA', 'ASP', 'CA', 'GLN', 14.82), ('CA', 'ASP', 'N', 'GLN', 14.9)], [('N', 'ASP', 'CB', 'GLN', 13.82), ('N', 'ASP', 'CG', 'GLN', 13.6), ('N', 'ASP', 'CD', 'GLN', 12.27), ('N', 'ASP', 'OE1', 'GLN', 11.76), ('N', 'ASP', 'NE2', 'GLN', 11.78), ('N', 'ASP', 'O', 'GLN', 15.27), ('N', 'ASP', 'C', 'GLN', 15.61), ('N', 'ASP', 'CA', 'GLN', 15.15), ('N', 'ASP', 'N', 'GLN', 15.16)]]}


flag = False
while True:
	match1, totTime1 = cmd.detect(ARG_ASP, d, 'A_12as_6_3_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_GLN, d, 'A_12as_6_3_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLN, d, 'A_12as_6_3_1_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ASP' :  match1,
		'ARG_GLN' :  match2,
		'ASP_GLN' :  match3}