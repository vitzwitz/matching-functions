'''
FUNC:P_1hl2_4_1_3_3
PDB:1hl2
EC:4.1.3.3
RESI:tyr,arg,lys
LOCI:a-137,142,165;
'''
import motifFunctions as cmd
TYR_LYS = { 
	'distances':
		[[6.43, 7.04, 6.67, 7.6, 7.81], [6.51, 6.63, 6.0, 6.57, 6.68], [6.05, 5.88, 5.46, 5.82, 6.28], [7.59, 7.51, 6.56, 6.86, 6.55], [6.86, 6.24, 5.62, 5.37, 5.71], [8.2, 7.77, 6.68, 6.53, 6.03], [7.89, 7.21, 6.26, 5.8, 5.58], [8.92, 8.02, 7.02, 6.17, 5.78]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 6.43), ('CB', 'TYR', 'CG', 'LYS', 7.04), ('CB', 'TYR', 'CD', 'LYS', 6.67), ('CB', 'TYR', 'CE', 'LYS', 7.6), ('CB', 'TYR', 'NZ', 'LYS', 7.81)], [('CG', 'TYR', 'CB', 'LYS', 6.51), ('CG', 'TYR', 'CG', 'LYS', 6.63), ('CG', 'TYR', 'CD', 'LYS', 6.0), ('CG', 'TYR', 'CE', 'LYS', 6.57), ('CG', 'TYR', 'NZ', 'LYS', 6.68)], [('CD1', 'TYR', 'CB', 'LYS', 6.05), ('CD1', 'TYR', 'CG', 'LYS', 5.88), ('CD1', 'TYR', 'CD', 'LYS', 5.46), ('CD1', 'TYR', 'CE', 'LYS', 5.82), ('CD1', 'TYR', 'NZ', 'LYS', 6.28)], [('CD2', 'TYR', 'CB', 'LYS', 7.59), ('CD2', 'TYR', 'CG', 'LYS', 7.51), ('CD2', 'TYR', 'CD', 'LYS', 6.56), ('CD2', 'TYR', 'CE', 'LYS', 6.86), ('CD2', 'TYR', 'NZ', 'LYS', 6.55)], [('CE1', 'TYR', 'CB', 'LYS', 6.86), ('CE1', 'TYR', 'CG', 'LYS', 6.24), ('CE1', 'TYR', 'CD', 'LYS', 5.62), ('CE1', 'TYR', 'CE', 'LYS', 5.37), ('CE1', 'TYR', 'NZ', 'LYS', 5.71)], [('CE2', 'TYR', 'CB', 'LYS', 8.2), ('CE2', 'TYR', 'CG', 'LYS', 7.77), ('CE2', 'TYR', 'CD', 'LYS', 6.68), ('CE2', 'TYR', 'CE', 'LYS', 6.53), ('CE2', 'TYR', 'NZ', 'LYS', 6.03)], [('CZ', 'TYR', 'CB', 'LYS', 7.89), ('CZ', 'TYR', 'CG', 'LYS', 7.21), ('CZ', 'TYR', 'CD', 'LYS', 6.26), ('CZ', 'TYR', 'CE', 'LYS', 5.8), ('CZ', 'TYR', 'NZ', 'LYS', 5.58)], [('OH', 'TYR', 'CB', 'LYS', 8.92), ('OH', 'TYR', 'CG', 'LYS', 8.02), ('OH', 'TYR', 'CD', 'LYS', 7.02), ('OH', 'TYR', 'CE', 'LYS', 6.17), ('OH', 'TYR', 'NZ', 'LYS', 5.78)]]}
TYR_ARG = { 
	'distances':
		[[11.94, 12.52, 13.75, 14.94, 15.58, 15.21, 16.72], [10.74, 11.19, 12.4, 13.62, 14.23, 13.81, 15.4], [10.23, 10.57, 11.86, 13.01, 13.5, 13.0, 14.64], [10.36, 10.78, 11.85, 13.16, 13.85, 13.45, 15.07], [9.26, 9.42, 10.69, 11.85, 12.28, 11.72, 13.45], [9.42, 9.69, 10.7, 12.04, 12.7, 12.24, 13.95], [8.83, 8.94, 10.06, 11.33, 11.86, 11.32, 13.1], [8.15, 8.02, 9.04, 10.33, 10.81, 10.19, 12.07]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 11.94), ('CB', 'TYR', 'CG', 'ARG', 12.52), ('CB', 'TYR', 'CD', 'ARG', 13.75), ('CB', 'TYR', 'NE', 'ARG', 14.94), ('CB', 'TYR', 'CZ', 'ARG', 15.58), ('CB', 'TYR', 'NH1', 'ARG', 15.21), ('CB', 'TYR', 'NH2', 'ARG', 16.72)], [('CG', 'TYR', 'CB', 'ARG', 10.74), ('CG', 'TYR', 'CG', 'ARG', 11.19), ('CG', 'TYR', 'CD', 'ARG', 12.4), ('CG', 'TYR', 'NE', 'ARG', 13.62), ('CG', 'TYR', 'CZ', 'ARG', 14.23), ('CG', 'TYR', 'NH1', 'ARG', 13.81), ('CG', 'TYR', 'NH2', 'ARG', 15.4)], [('CD1', 'TYR', 'CB', 'ARG', 10.23), ('CD1', 'TYR', 'CG', 'ARG', 10.57), ('CD1', 'TYR', 'CD', 'ARG', 11.86), ('CD1', 'TYR', 'NE', 'ARG', 13.01), ('CD1', 'TYR', 'CZ', 'ARG', 13.5), ('CD1', 'TYR', 'NH1', 'ARG', 13.0), ('CD1', 'TYR', 'NH2', 'ARG', 14.64)], [('CD2', 'TYR', 'CB', 'ARG', 10.36), ('CD2', 'TYR', 'CG', 'ARG', 10.78), ('CD2', 'TYR', 'CD', 'ARG', 11.85), ('CD2', 'TYR', 'NE', 'ARG', 13.16), ('CD2', 'TYR', 'CZ', 'ARG', 13.85), ('CD2', 'TYR', 'NH1', 'ARG', 13.45), ('CD2', 'TYR', 'NH2', 'ARG', 15.07)], [('CE1', 'TYR', 'CB', 'ARG', 9.26), ('CE1', 'TYR', 'CG', 'ARG', 9.42), ('CE1', 'TYR', 'CD', 'ARG', 10.69), ('CE1', 'TYR', 'NE', 'ARG', 11.85), ('CE1', 'TYR', 'CZ', 'ARG', 12.28), ('CE1', 'TYR', 'NH1', 'ARG', 11.72), ('CE1', 'TYR', 'NH2', 'ARG', 13.45)], [('CE2', 'TYR', 'CB', 'ARG', 9.42), ('CE2', 'TYR', 'CG', 'ARG', 9.69), ('CE2', 'TYR', 'CD', 'ARG', 10.7), ('CE2', 'TYR', 'NE', 'ARG', 12.04), ('CE2', 'TYR', 'CZ', 'ARG', 12.7), ('CE2', 'TYR', 'NH1', 'ARG', 12.24), ('CE2', 'TYR', 'NH2', 'ARG', 13.95)], [('CZ', 'TYR', 'CB', 'ARG', 8.83), ('CZ', 'TYR', 'CG', 'ARG', 8.94), ('CZ', 'TYR', 'CD', 'ARG', 10.06), ('CZ', 'TYR', 'NE', 'ARG', 11.33), ('CZ', 'TYR', 'CZ', 'ARG', 11.86), ('CZ', 'TYR', 'NH1', 'ARG', 11.32), ('CZ', 'TYR', 'NH2', 'ARG', 13.1)], [('OH', 'TYR', 'CB', 'ARG', 8.15), ('OH', 'TYR', 'CG', 'ARG', 8.02), ('OH', 'TYR', 'CD', 'ARG', 9.04), ('OH', 'TYR', 'NE', 'ARG', 10.33), ('OH', 'TYR', 'CZ', 'ARG', 10.81), ('OH', 'TYR', 'NH1', 'ARG', 10.19), ('OH', 'TYR', 'NH2', 'ARG', 12.07)]]}
ARG_LYS = { 
	'distances':
		[[13.97, 13.25, 12.71, 11.9, 11.85], [14.09, 13.2, 12.63, 11.63, 11.55], [15.42, 14.49, 13.82, 12.76, 12.54], [16.49, 15.55, 14.98, 13.9, 13.78], [16.76, 15.74, 15.24, 14.09, 14.04], [16.05, 14.95, 14.45, 13.22, 13.19], [17.84, 16.83, 16.41, 15.26, 15.28]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYS', 13.97), ('CB', 'ARG', 'CG', 'LYS', 13.25), ('CB', 'ARG', 'CD', 'LYS', 12.71), ('CB', 'ARG', 'CE', 'LYS', 11.9), ('CB', 'ARG', 'NZ', 'LYS', 11.85)], [('CG', 'ARG', 'CB', 'LYS', 14.09), ('CG', 'ARG', 'CG', 'LYS', 13.2), ('CG', 'ARG', 'CD', 'LYS', 12.63), ('CG', 'ARG', 'CE', 'LYS', 11.63), ('CG', 'ARG', 'NZ', 'LYS', 11.55)], [('CD', 'ARG', 'CB', 'LYS', 15.42), ('CD', 'ARG', 'CG', 'LYS', 14.49), ('CD', 'ARG', 'CD', 'LYS', 13.82), ('CD', 'ARG', 'CE', 'LYS', 12.76), ('CD', 'ARG', 'NZ', 'LYS', 12.54)], [('NE', 'ARG', 'CB', 'LYS', 16.49), ('NE', 'ARG', 'CG', 'LYS', 15.55), ('NE', 'ARG', 'CD', 'LYS', 14.98), ('NE', 'ARG', 'CE', 'LYS', 13.9), ('NE', 'ARG', 'NZ', 'LYS', 13.78)], [('CZ', 'ARG', 'CB', 'LYS', 16.76), ('CZ', 'ARG', 'CG', 'LYS', 15.74), ('CZ', 'ARG', 'CD', 'LYS', 15.24), ('CZ', 'ARG', 'CE', 'LYS', 14.09), ('CZ', 'ARG', 'NZ', 'LYS', 14.04)], [('NH1', 'ARG', 'CB', 'LYS', 16.05), ('NH1', 'ARG', 'CG', 'LYS', 14.95), ('NH1', 'ARG', 'CD', 'LYS', 14.45), ('NH1', 'ARG', 'CE', 'LYS', 13.22), ('NH1', 'ARG', 'NZ', 'LYS', 13.19)], [('NH2', 'ARG', 'CB', 'LYS', 17.84), ('NH2', 'ARG', 'CG', 'LYS', 16.83), ('NH2', 'ARG', 'CD', 'LYS', 16.41), ('NH2', 'ARG', 'CE', 'LYS', 15.26), ('NH2', 'ARG', 'NZ', 'LYS', 15.28)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_LYS, d, 'P_1hl2_4_1_3_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ARG, d, 'P_1hl2_4_1_3_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_LYS, d, 'P_1hl2_4_1_3_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_LYS' :  match1,
		'TYR_ARG' :  match2,
		'ARG_LYS' :  match3}