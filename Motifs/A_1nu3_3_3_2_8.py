'''
FUNC:A_1nu3_3_3_2_8
PDB:1nu3
EC:3.3.2.8
RESI:arg,asp,asp
LOCI:a-99,101,132;
'''
import motifFunctions as cmd
ARG_ASP = { 
	'distances':
		[[8.54, 7.72, 6.57, 8.4], [7.94, 6.94, 5.88, 7.41], [8.19, 6.92, 5.85, 7.15], [7.25, 5.85, 5.0, 5.86], [7.68, 6.27, 5.75, 5.91], [8.98, 7.59, 7.07, 7.2], [7.13, 5.74, 5.61, 5.06], [11.12, 10.11, 9.56, 10.07], [9.74, 8.71, 8.19, 8.66], [9.59, 8.34, 7.75, 8.17], [8.62, 7.34, 6.96, 6.98], [7.35, 6.03, 5.66, 5.71], [7.0, 5.65, 4.9, 5.71], [6.79, 5.51, 5.54, 4.84]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 8.54), ('CB', 'ARG', 'CG', 'ASP', 7.72), ('CB', 'ARG', 'OD1', 'ASP', 6.57), ('CB', 'ARG', 'OD2', 'ASP', 8.4)], [('CG', 'ARG', 'CB', 'ASP', 7.94), ('CG', 'ARG', 'CG', 'ASP', 6.94), ('CG', 'ARG', 'OD1', 'ASP', 5.88), ('CG', 'ARG', 'OD2', 'ASP', 7.41)], [('CD', 'ARG', 'CB', 'ASP', 8.19), ('CD', 'ARG', 'CG', 'ASP', 6.92), ('CD', 'ARG', 'OD1', 'ASP', 5.85), ('CD', 'ARG', 'OD2', 'ASP', 7.15)], [('NE', 'ARG', 'CB', 'ASP', 7.25), ('NE', 'ARG', 'CG', 'ASP', 5.85), ('NE', 'ARG', 'OD1', 'ASP', 5.0), ('NE', 'ARG', 'OD2', 'ASP', 5.86)], [('CZ', 'ARG', 'CB', 'ASP', 7.68), ('CZ', 'ARG', 'CG', 'ASP', 6.27), ('CZ', 'ARG', 'OD1', 'ASP', 5.75), ('CZ', 'ARG', 'OD2', 'ASP', 5.91)], [('NH1', 'ARG', 'CB', 'ASP', 8.98), ('NH1', 'ARG', 'CG', 'ASP', 7.59), ('NH1', 'ARG', 'OD1', 'ASP', 7.07), ('NH1', 'ARG', 'OD2', 'ASP', 7.2)], [('NH2', 'ARG', 'CB', 'ASP', 7.13), ('NH2', 'ARG', 'CG', 'ASP', 5.74), ('NH2', 'ARG', 'OD1', 'ASP', 5.61), ('NH2', 'ARG', 'OD2', 'ASP', 5.06)], [('CB', 'ARG', 'CB', 'ASP', 11.12), ('CB', 'ARG', 'CG', 'ASP', 10.11), ('CB', 'ARG', 'OD1', 'ASP', 9.56), ('CB', 'ARG', 'OD2', 'ASP', 10.07)], [('CG', 'ARG', 'CB', 'ASP', 9.74), ('CG', 'ARG', 'CG', 'ASP', 8.71), ('CG', 'ARG', 'OD1', 'ASP', 8.19), ('CG', 'ARG', 'OD2', 'ASP', 8.66)], [('CD', 'ARG', 'CB', 'ASP', 9.59), ('CD', 'ARG', 'CG', 'ASP', 8.34), ('CD', 'ARG', 'OD1', 'ASP', 7.75), ('CD', 'ARG', 'OD2', 'ASP', 8.17)], [('NE', 'ARG', 'CB', 'ASP', 8.62), ('NE', 'ARG', 'CG', 'ASP', 7.34), ('NE', 'ARG', 'OD1', 'ASP', 6.96), ('NE', 'ARG', 'OD2', 'ASP', 6.98)], [('CZ', 'ARG', 'CB', 'ASP', 7.35), ('CZ', 'ARG', 'CG', 'ASP', 6.03), ('CZ', 'ARG', 'OD1', 'ASP', 5.66), ('CZ', 'ARG', 'OD2', 'ASP', 5.71)], [('NH1', 'ARG', 'CB', 'ASP', 7.0), ('NH1', 'ARG', 'CG', 'ASP', 5.65), ('NH1', 'ARG', 'OD1', 'ASP', 4.9), ('NH1', 'ARG', 'OD2', 'ASP', 5.71)], [('NH2', 'ARG', 'CB', 'ASP', 6.79), ('NH2', 'ARG', 'CG', 'ASP', 5.51), ('NH2', 'ARG', 'OD1', 'ASP', 5.54), ('NH2', 'ARG', 'OD2', 'ASP', 4.84)]]}
ASP_ASP = { 
	'distances':
		[[10.49, 9.82, 10.25, 9.0], [9.61, 8.74, 9.06, 7.9], [9.88, 8.88, 8.98, 8.17], [8.78, 7.88, 8.32, 6.92], [10.49, 9.61, 9.88, 8.78], [9.82, 8.74, 8.88, 7.88], [10.25, 9.06, 8.98, 8.32], [9.0, 7.9, 8.17, 6.92]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 10.49), ('CB', 'ASP', 'CG', 'ASP', 9.82), ('CB', 'ASP', 'OD1', 'ASP', 10.25), ('CB', 'ASP', 'OD2', 'ASP', 9.0)], [('CG', 'ASP', 'CB', 'ASP', 9.61), ('CG', 'ASP', 'CG', 'ASP', 8.74), ('CG', 'ASP', 'OD1', 'ASP', 9.06), ('CG', 'ASP', 'OD2', 'ASP', 7.9)], [('OD1', 'ASP', 'CB', 'ASP', 9.88), ('OD1', 'ASP', 'CG', 'ASP', 8.88), ('OD1', 'ASP', 'OD1', 'ASP', 8.98), ('OD1', 'ASP', 'OD2', 'ASP', 8.17)], [('OD2', 'ASP', 'CB', 'ASP', 8.78), ('OD2', 'ASP', 'CG', 'ASP', 7.88), ('OD2', 'ASP', 'OD1', 'ASP', 8.32), ('OD2', 'ASP', 'OD2', 'ASP', 6.92)], [('CB', 'ASP', 'CB', 'ASP', 10.49), ('CB', 'ASP', 'CG', 'ASP', 9.61), ('CB', 'ASP', 'OD1', 'ASP', 9.88), ('CB', 'ASP', 'OD2', 'ASP', 8.78)], [('CG', 'ASP', 'CB', 'ASP', 9.82), ('CG', 'ASP', 'CG', 'ASP', 8.74), ('CG', 'ASP', 'OD1', 'ASP', 8.88), ('CG', 'ASP', 'OD2', 'ASP', 7.88)], [('OD1', 'ASP', 'CB', 'ASP', 10.25), ('OD1', 'ASP', 'CG', 'ASP', 9.06), ('OD1', 'ASP', 'OD1', 'ASP', 8.98), ('OD1', 'ASP', 'OD2', 'ASP', 8.32)], [('OD2', 'ASP', 'CB', 'ASP', 9.0), ('OD2', 'ASP', 'CG', 'ASP', 7.9), ('OD2', 'ASP', 'OD1', 'ASP', 8.17), ('OD2', 'ASP', 'OD2', 'ASP', 6.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_ASP, d, 'A_1nu3_3_3_2_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'A_1nu3_3_3_2_8')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ASP' :  match1,
		'ASP_ASP' :  match2}