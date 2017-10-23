'''
FUNC:A_1otg_5_3_3_10
PDB:1otg
EC:5.3.3.10
RESI:pro,phe,arg
LOCI:a-2,35,41;
'''
import motifFunctions as cmd
PRO_ARG = { 
	'distances':
		[[9.36, 10.19, 10.42, 9.39, 9.67, 10.91, 8.79], [9.25, 9.94, 10.29, 9.24, 9.55, 10.85, 8.64], [9.05, 9.48, 9.63, 8.43, 8.54, 9.79, 7.49]],
	'comparisons':
		[[('CB', 'PRO', 'CB', 'ARG', 9.36), ('CB', 'PRO', 'CG', 'ARG', 10.19), ('CB', 'PRO', 'CD', 'ARG', 10.42), ('CB', 'PRO', 'NE', 'ARG', 9.39), ('CB', 'PRO', 'CZ', 'ARG', 9.67), ('CB', 'PRO', 'NH1', 'ARG', 10.91), ('CB', 'PRO', 'NH2', 'ARG', 8.79)], [('CG', 'PRO', 'CB', 'ARG', 9.25), ('CG', 'PRO', 'CG', 'ARG', 9.94), ('CG', 'PRO', 'CD', 'ARG', 10.29), ('CG', 'PRO', 'NE', 'ARG', 9.24), ('CG', 'PRO', 'CZ', 'ARG', 9.55), ('CG', 'PRO', 'NH1', 'ARG', 10.85), ('CG', 'PRO', 'NH2', 'ARG', 8.64)], [('CD', 'PRO', 'CB', 'ARG', 9.05), ('CD', 'PRO', 'CG', 'ARG', 9.48), ('CD', 'PRO', 'CD', 'ARG', 9.63), ('CD', 'PRO', 'NE', 'ARG', 8.43), ('CD', 'PRO', 'CZ', 'ARG', 8.54), ('CD', 'PRO', 'NH1', 'ARG', 9.79), ('CD', 'PRO', 'NH2', 'ARG', 7.49)]]}
PRO_PHE = { 
	'distances':
		[[7.1, 6.73, 5.99, 7.64, 6.37, 7.94, 7.36], [5.95, 5.96, 5.58, 7.0, 6.39, 7.63, 7.35], [6.27, 6.58, 6.09, 7.84, 7.08, 8.59, 8.24]],
	'comparisons':
		[[('CB', 'PRO', 'CB', 'PHE', 7.1), ('CB', 'PRO', 'CG', 'PHE', 6.73), ('CB', 'PRO', 'CD1', 'PHE', 5.99), ('CB', 'PRO', 'CD2', 'PHE', 7.64), ('CB', 'PRO', 'CE1', 'PHE', 6.37), ('CB', 'PRO', 'CE2', 'PHE', 7.94), ('CB', 'PRO', 'CZ', 'PHE', 7.36)], [('CG', 'PRO', 'CB', 'PHE', 5.95), ('CG', 'PRO', 'CG', 'PHE', 5.96), ('CG', 'PRO', 'CD1', 'PHE', 5.58), ('CG', 'PRO', 'CD2', 'PHE', 7.0), ('CG', 'PRO', 'CE1', 'PHE', 6.39), ('CG', 'PRO', 'CE2', 'PHE', 7.63), ('CG', 'PRO', 'CZ', 'PHE', 7.35)], [('CD', 'PRO', 'CB', 'PHE', 6.27), ('CD', 'PRO', 'CG', 'PHE', 6.58), ('CD', 'PRO', 'CD1', 'PHE', 6.09), ('CD', 'PRO', 'CD2', 'PHE', 7.84), ('CD', 'PRO', 'CE1', 'PHE', 7.08), ('CD', 'PRO', 'CE2', 'PHE', 8.59), ('CD', 'PRO', 'CZ', 'PHE', 8.24)]]}
PHE_ARG = { 
	'distances':
		[[12.57, 13.0, 13.44, 12.33, 12.5, 13.75, 11.45], [13.05, 13.63, 14.03, 12.92, 13.09, 14.34, 12.02], [12.82, 13.43, 13.68, 12.51, 12.58, 13.79, 11.45], [13.97, 14.64, 15.14, 14.09, 14.33, 15.61, 13.3], [13.58, 14.3, 14.53, 13.38, 13.45, 14.65, 12.34], [14.66, 15.44, 15.9, 14.86, 15.1, 16.36, 14.06], [14.46, 15.26, 15.6, 14.51, 14.67, 15.9, 13.6]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ARG', 12.57), ('CB', 'PHE', 'CG', 'ARG', 13.0), ('CB', 'PHE', 'CD', 'ARG', 13.44), ('CB', 'PHE', 'NE', 'ARG', 12.33), ('CB', 'PHE', 'CZ', 'ARG', 12.5), ('CB', 'PHE', 'NH1', 'ARG', 13.75), ('CB', 'PHE', 'NH2', 'ARG', 11.45)], [('CG', 'PHE', 'CB', 'ARG', 13.05), ('CG', 'PHE', 'CG', 'ARG', 13.63), ('CG', 'PHE', 'CD', 'ARG', 14.03), ('CG', 'PHE', 'NE', 'ARG', 12.92), ('CG', 'PHE', 'CZ', 'ARG', 13.09), ('CG', 'PHE', 'NH1', 'ARG', 14.34), ('CG', 'PHE', 'NH2', 'ARG', 12.02)], [('CD1', 'PHE', 'CB', 'ARG', 12.82), ('CD1', 'PHE', 'CG', 'ARG', 13.43), ('CD1', 'PHE', 'CD', 'ARG', 13.68), ('CD1', 'PHE', 'NE', 'ARG', 12.51), ('CD1', 'PHE', 'CZ', 'ARG', 12.58), ('CD1', 'PHE', 'NH1', 'ARG', 13.79), ('CD1', 'PHE', 'NH2', 'ARG', 11.45)], [('CD2', 'PHE', 'CB', 'ARG', 13.97), ('CD2', 'PHE', 'CG', 'ARG', 14.64), ('CD2', 'PHE', 'CD', 'ARG', 15.14), ('CD2', 'PHE', 'NE', 'ARG', 14.09), ('CD2', 'PHE', 'CZ', 'ARG', 14.33), ('CD2', 'PHE', 'NH1', 'ARG', 15.61), ('CD2', 'PHE', 'NH2', 'ARG', 13.3)], [('CE1', 'PHE', 'CB', 'ARG', 13.58), ('CE1', 'PHE', 'CG', 'ARG', 14.3), ('CE1', 'PHE', 'CD', 'ARG', 14.53), ('CE1', 'PHE', 'NE', 'ARG', 13.38), ('CE1', 'PHE', 'CZ', 'ARG', 13.45), ('CE1', 'PHE', 'NH1', 'ARG', 14.65), ('CE1', 'PHE', 'NH2', 'ARG', 12.34)], [('CE2', 'PHE', 'CB', 'ARG', 14.66), ('CE2', 'PHE', 'CG', 'ARG', 15.44), ('CE2', 'PHE', 'CD', 'ARG', 15.9), ('CE2', 'PHE', 'NE', 'ARG', 14.86), ('CE2', 'PHE', 'CZ', 'ARG', 15.1), ('CE2', 'PHE', 'NH1', 'ARG', 16.36), ('CE2', 'PHE', 'NH2', 'ARG', 14.06)], [('CZ', 'PHE', 'CB', 'ARG', 14.46), ('CZ', 'PHE', 'CG', 'ARG', 15.26), ('CZ', 'PHE', 'CD', 'ARG', 15.6), ('CZ', 'PHE', 'NE', 'ARG', 14.51), ('CZ', 'PHE', 'CZ', 'ARG', 14.67), ('CZ', 'PHE', 'NH1', 'ARG', 15.9), ('CZ', 'PHE', 'NH2', 'ARG', 13.6)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(PRO_ARG, d, 'A_1otg_5_3_3_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(PRO_PHE, d, 'A_1otg_5_3_3_10')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_ARG, d, 'A_1otg_5_3_3_10')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'PRO_ARG' :  match1,
		'PRO_PHE' :  match2,
		'PHE_ARG' :  match3}