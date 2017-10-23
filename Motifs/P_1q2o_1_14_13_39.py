'''
FUNC:P_1q2o_1_14_13_39
PDB:1q2o
EC:1.14.13.39
RESI:cys,arg,trp,glu
LOCI:a-186,189,358,363;
'''
import motifFunctions as cmd
TRP_GLU = { 
	'distances':
		[[12.08, 11.76, 10.69, 9.54, 11.15], [12.54, 12.05, 11.03, 9.82, 11.58], [12.04, 11.48, 10.6, 9.35, 11.29], [13.83, 13.25, 12.2, 10.98, 12.69], [13.04, 12.36, 11.51, 10.26, 12.21], [14.09, 13.41, 12.44, 11.21, 13.03], [14.91, 14.35, 13.21, 12.03, 13.6], [15.34, 14.59, 13.62, 12.4, 14.19], [16.08, 15.44, 14.3, 13.11, 14.69], [16.27, 15.54, 14.48, 13.28, 14.95]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'GLU', 12.08), ('CB', 'TRP', 'CG', 'GLU', 11.76), ('CB', 'TRP', 'CD', 'GLU', 10.69), ('CB', 'TRP', 'OE1', 'GLU', 9.54), ('CB', 'TRP', 'OE2', 'GLU', 11.15)], [('CG', 'TRP', 'CB', 'GLU', 12.54), ('CG', 'TRP', 'CG', 'GLU', 12.05), ('CG', 'TRP', 'CD', 'GLU', 11.03), ('CG', 'TRP', 'OE1', 'GLU', 9.82), ('CG', 'TRP', 'OE2', 'GLU', 11.58)], [('CD1', 'TRP', 'CB', 'GLU', 12.04), ('CD1', 'TRP', 'CG', 'GLU', 11.48), ('CD1', 'TRP', 'CD', 'GLU', 10.6), ('CD1', 'TRP', 'OE1', 'GLU', 9.35), ('CD1', 'TRP', 'OE2', 'GLU', 11.29)], [('CD2', 'TRP', 'CB', 'GLU', 13.83), ('CD2', 'TRP', 'CG', 'GLU', 13.25), ('CD2', 'TRP', 'CD', 'GLU', 12.2), ('CD2', 'TRP', 'OE1', 'GLU', 10.98), ('CD2', 'TRP', 'OE2', 'GLU', 12.69)], [('NE1', 'TRP', 'CB', 'GLU', 13.04), ('NE1', 'TRP', 'CG', 'GLU', 12.36), ('NE1', 'TRP', 'CD', 'GLU', 11.51), ('NE1', 'TRP', 'OE1', 'GLU', 10.26), ('NE1', 'TRP', 'OE2', 'GLU', 12.21)], [('CE2', 'TRP', 'CB', 'GLU', 14.09), ('CE2', 'TRP', 'CG', 'GLU', 13.41), ('CE2', 'TRP', 'CD', 'GLU', 12.44), ('CE2', 'TRP', 'OE1', 'GLU', 11.21), ('CE2', 'TRP', 'OE2', 'GLU', 13.03)], [('CE3', 'TRP', 'CB', 'GLU', 14.91), ('CE3', 'TRP', 'CG', 'GLU', 14.35), ('CE3', 'TRP', 'CD', 'GLU', 13.21), ('CE3', 'TRP', 'OE1', 'GLU', 12.03), ('CE3', 'TRP', 'OE2', 'GLU', 13.6)], [('CZ2', 'TRP', 'CB', 'GLU', 15.34), ('CZ2', 'TRP', 'CG', 'GLU', 14.59), ('CZ2', 'TRP', 'CD', 'GLU', 13.62), ('CZ2', 'TRP', 'OE1', 'GLU', 12.4), ('CZ2', 'TRP', 'OE2', 'GLU', 14.19)], [('CZ3', 'TRP', 'CB', 'GLU', 16.08), ('CZ3', 'TRP', 'CG', 'GLU', 15.44), ('CZ3', 'TRP', 'CD', 'GLU', 14.3), ('CZ3', 'TRP', 'OE1', 'GLU', 13.11), ('CZ3', 'TRP', 'OE2', 'GLU', 14.69)], [('CH2', 'TRP', 'CB', 'GLU', 16.27), ('CH2', 'TRP', 'CG', 'GLU', 15.54), ('CH2', 'TRP', 'CD', 'GLU', 14.48), ('CH2', 'TRP', 'OE1', 'GLU', 13.28), ('CH2', 'TRP', 'OE2', 'GLU', 14.95)]]}
CYS_TRP = { 
	'distances':
		[[14.24, 13.71, 13.39, 13.77, 13.26, 13.49, 14.25, 13.7, 14.44, 14.17], [12.51, 11.94, 11.65, 11.96, 11.49, 11.68, 12.43, 11.9, 12.62, 12.36]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'TRP', 14.24), ('CB', 'CYS', 'CG', 'TRP', 13.71), ('CB', 'CYS', 'CD1', 'TRP', 13.39), ('CB', 'CYS', 'CD2', 'TRP', 13.77), ('CB', 'CYS', 'NE1', 'TRP', 13.26), ('CB', 'CYS', 'CE2', 'TRP', 13.49), ('CB', 'CYS', 'CE3', 'TRP', 14.25), ('CB', 'CYS', 'CZ2', 'TRP', 13.7), ('CB', 'CYS', 'CZ3', 'TRP', 14.44), ('CB', 'CYS', 'CH2', 'TRP', 14.17)], [('SG', 'CYS', 'CB', 'TRP', 12.51), ('SG', 'CYS', 'CG', 'TRP', 11.94), ('SG', 'CYS', 'CD1', 'TRP', 11.65), ('SG', 'CYS', 'CD2', 'TRP', 11.96), ('SG', 'CYS', 'NE1', 'TRP', 11.49), ('SG', 'CYS', 'CE2', 'TRP', 11.68), ('SG', 'CYS', 'CE3', 'TRP', 12.43), ('SG', 'CYS', 'CZ2', 'TRP', 11.9), ('SG', 'CYS', 'CZ3', 'TRP', 12.62), ('SG', 'CYS', 'CH2', 'TRP', 12.36)]]}
ARG_GLU = { 
	'distances':
		[[17.52, 16.07, 15.24, 14.67, 15.32], [17.0, 15.54, 14.66, 14.19, 14.61], [17.74, 16.26, 15.45, 15.09, 15.34], [17.31, 15.8, 15.13, 14.84, 15.07], [18.12, 16.61, 16.01, 15.8, 15.94], [19.31, 17.81, 17.17, 16.97, 17.03], [17.83, 16.32, 15.85, 15.71, 15.81]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 17.52), ('CB', 'ARG', 'CG', 'GLU', 16.07), ('CB', 'ARG', 'CD', 'GLU', 15.24), ('CB', 'ARG', 'OE1', 'GLU', 14.67), ('CB', 'ARG', 'OE2', 'GLU', 15.32)], [('CG', 'ARG', 'CB', 'GLU', 17.0), ('CG', 'ARG', 'CG', 'GLU', 15.54), ('CG', 'ARG', 'CD', 'GLU', 14.66), ('CG', 'ARG', 'OE1', 'GLU', 14.19), ('CG', 'ARG', 'OE2', 'GLU', 14.61)], [('CD', 'ARG', 'CB', 'GLU', 17.74), ('CD', 'ARG', 'CG', 'GLU', 16.26), ('CD', 'ARG', 'CD', 'GLU', 15.45), ('CD', 'ARG', 'OE1', 'GLU', 15.09), ('CD', 'ARG', 'OE2', 'GLU', 15.34)], [('NE', 'ARG', 'CB', 'GLU', 17.31), ('NE', 'ARG', 'CG', 'GLU', 15.8), ('NE', 'ARG', 'CD', 'GLU', 15.13), ('NE', 'ARG', 'OE1', 'GLU', 14.84), ('NE', 'ARG', 'OE2', 'GLU', 15.07)], [('CZ', 'ARG', 'CB', 'GLU', 18.12), ('CZ', 'ARG', 'CG', 'GLU', 16.61), ('CZ', 'ARG', 'CD', 'GLU', 16.01), ('CZ', 'ARG', 'OE1', 'GLU', 15.8), ('CZ', 'ARG', 'OE2', 'GLU', 15.94)], [('NH1', 'ARG', 'CB', 'GLU', 19.31), ('NH1', 'ARG', 'CG', 'GLU', 17.81), ('NH1', 'ARG', 'CD', 'GLU', 17.17), ('NH1', 'ARG', 'OE1', 'GLU', 16.97), ('NH1', 'ARG', 'OE2', 'GLU', 17.03)], [('NH2', 'ARG', 'CB', 'GLU', 17.83), ('NH2', 'ARG', 'CG', 'GLU', 16.32), ('NH2', 'ARG', 'CD', 'GLU', 15.85), ('NH2', 'ARG', 'OE1', 'GLU', 15.71), ('NH2', 'ARG', 'OE2', 'GLU', 15.81)]]}
CYS_GLU = { 
	'distances':
		[[13.85, 12.41, 11.53, 11.33, 11.29], [13.23, 11.82, 10.82, 10.4, 10.69]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 13.85), ('CB', 'CYS', 'CG', 'GLU', 12.41), ('CB', 'CYS', 'CD', 'GLU', 11.53), ('CB', 'CYS', 'OE1', 'GLU', 11.33), ('CB', 'CYS', 'OE2', 'GLU', 11.29)], [('SG', 'CYS', 'CB', 'GLU', 13.23), ('SG', 'CYS', 'CG', 'GLU', 11.82), ('SG', 'CYS', 'CD', 'GLU', 10.82), ('SG', 'CYS', 'OE1', 'GLU', 10.4), ('SG', 'CYS', 'OE2', 'GLU', 10.69)]]}
CYS_ARG = { 
	'distances':
		[[7.11, 5.89, 6.19, 6.13, 7.1, 7.98, 7.49], [6.91, 5.98, 6.88, 7.07, 8.25, 9.17, 8.74]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 7.11), ('CB', 'CYS', 'CG', 'ARG', 5.89), ('CB', 'CYS', 'CD', 'ARG', 6.19), ('CB', 'CYS', 'NE', 'ARG', 6.13), ('CB', 'CYS', 'CZ', 'ARG', 7.1), ('CB', 'CYS', 'NH1', 'ARG', 7.98), ('CB', 'CYS', 'NH2', 'ARG', 7.49)], [('SG', 'CYS', 'CB', 'ARG', 6.91), ('SG', 'CYS', 'CG', 'ARG', 5.98), ('SG', 'CYS', 'CD', 'ARG', 6.88), ('SG', 'CYS', 'NE', 'ARG', 7.07), ('SG', 'CYS', 'CZ', 'ARG', 8.25), ('SG', 'CYS', 'NH1', 'ARG', 9.17), ('SG', 'CYS', 'NH2', 'ARG', 8.74)]]}
ARG_TRP = { 
	'distances':
		[[15.31, 14.31, 13.9, 13.85, 13.19, 13.14, 14.17, 12.75, 13.8, 13.09], [15.3, 14.44, 14.11, 14.07, 13.55, 13.52, 14.37, 13.25, 14.11, 13.57], [16.71, 15.88, 15.53, 15.56, 15.0, 15.01, 15.86, 14.77, 15.63, 15.09], [17.09, 16.25, 15.78, 16.04, 15.28, 15.43, 16.47, 15.27, 16.31, 15.72], [18.37, 17.54, 17.03, 17.34, 16.53, 16.71, 17.79, 16.55, 17.63, 17.02], [19.32, 18.49, 18.05, 18.23, 17.52, 17.62, 18.59, 17.39, 18.37, 17.77], [18.78, 17.96, 17.37, 17.85, 16.9, 17.19, 18.41, 17.1, 18.31, 17.67]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TRP', 15.31), ('CB', 'ARG', 'CG', 'TRP', 14.31), ('CB', 'ARG', 'CD1', 'TRP', 13.9), ('CB', 'ARG', 'CD2', 'TRP', 13.85), ('CB', 'ARG', 'NE1', 'TRP', 13.19), ('CB', 'ARG', 'CE2', 'TRP', 13.14), ('CB', 'ARG', 'CE3', 'TRP', 14.17), ('CB', 'ARG', 'CZ2', 'TRP', 12.75), ('CB', 'ARG', 'CZ3', 'TRP', 13.8), ('CB', 'ARG', 'CH2', 'TRP', 13.09)], [('CG', 'ARG', 'CB', 'TRP', 15.3), ('CG', 'ARG', 'CG', 'TRP', 14.44), ('CG', 'ARG', 'CD1', 'TRP', 14.11), ('CG', 'ARG', 'CD2', 'TRP', 14.07), ('CG', 'ARG', 'NE1', 'TRP', 13.55), ('CG', 'ARG', 'CE2', 'TRP', 13.52), ('CG', 'ARG', 'CE3', 'TRP', 14.37), ('CG', 'ARG', 'CZ2', 'TRP', 13.25), ('CG', 'ARG', 'CZ3', 'TRP', 14.11), ('CG', 'ARG', 'CH2', 'TRP', 13.57)], [('CD', 'ARG', 'CB', 'TRP', 16.71), ('CD', 'ARG', 'CG', 'TRP', 15.88), ('CD', 'ARG', 'CD1', 'TRP', 15.53), ('CD', 'ARG', 'CD2', 'TRP', 15.56), ('CD', 'ARG', 'NE1', 'TRP', 15.0), ('CD', 'ARG', 'CE2', 'TRP', 15.01), ('CD', 'ARG', 'CE3', 'TRP', 15.86), ('CD', 'ARG', 'CZ2', 'TRP', 14.77), ('CD', 'ARG', 'CZ3', 'TRP', 15.63), ('CD', 'ARG', 'CH2', 'TRP', 15.09)], [('NE', 'ARG', 'CB', 'TRP', 17.09), ('NE', 'ARG', 'CG', 'TRP', 16.25), ('NE', 'ARG', 'CD1', 'TRP', 15.78), ('NE', 'ARG', 'CD2', 'TRP', 16.04), ('NE', 'ARG', 'NE1', 'TRP', 15.28), ('NE', 'ARG', 'CE2', 'TRP', 15.43), ('NE', 'ARG', 'CE3', 'TRP', 16.47), ('NE', 'ARG', 'CZ2', 'TRP', 15.27), ('NE', 'ARG', 'CZ3', 'TRP', 16.31), ('NE', 'ARG', 'CH2', 'TRP', 15.72)], [('CZ', 'ARG', 'CB', 'TRP', 18.37), ('CZ', 'ARG', 'CG', 'TRP', 17.54), ('CZ', 'ARG', 'CD1', 'TRP', 17.03), ('CZ', 'ARG', 'CD2', 'TRP', 17.34), ('CZ', 'ARG', 'NE1', 'TRP', 16.53), ('CZ', 'ARG', 'CE2', 'TRP', 16.71), ('CZ', 'ARG', 'CE3', 'TRP', 17.79), ('CZ', 'ARG', 'CZ2', 'TRP', 16.55), ('CZ', 'ARG', 'CZ3', 'TRP', 17.63), ('CZ', 'ARG', 'CH2', 'TRP', 17.02)], [('NH1', 'ARG', 'CB', 'TRP', 19.32), ('NH1', 'ARG', 'CG', 'TRP', 18.49), ('NH1', 'ARG', 'CD1', 'TRP', 18.05), ('NH1', 'ARG', 'CD2', 'TRP', 18.23), ('NH1', 'ARG', 'NE1', 'TRP', 17.52), ('NH1', 'ARG', 'CE2', 'TRP', 17.62), ('NH1', 'ARG', 'CE3', 'TRP', 18.59), ('NH1', 'ARG', 'CZ2', 'TRP', 17.39), ('NH1', 'ARG', 'CZ3', 'TRP', 18.37), ('NH1', 'ARG', 'CH2', 'TRP', 17.77)], [('NH2', 'ARG', 'CB', 'TRP', 18.78), ('NH2', 'ARG', 'CG', 'TRP', 17.96), ('NH2', 'ARG', 'CD1', 'TRP', 17.37), ('NH2', 'ARG', 'CD2', 'TRP', 17.85), ('NH2', 'ARG', 'NE1', 'TRP', 16.9), ('NH2', 'ARG', 'CE2', 'TRP', 17.19), ('NH2', 'ARG', 'CE3', 'TRP', 18.41), ('NH2', 'ARG', 'CZ2', 'TRP', 17.1), ('NH2', 'ARG', 'CZ3', 'TRP', 18.31), ('NH2', 'ARG', 'CH2', 'TRP', 17.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_GLU, d, 'P_1q2o_1_14_13_39')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_TRP, d, 'P_1q2o_1_14_13_39')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_GLU, d, 'P_1q2o_1_14_13_39')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_GLU, d, 'P_1q2o_1_14_13_39')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_ARG, d, 'P_1q2o_1_14_13_39')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_TRP, d, 'P_1q2o_1_14_13_39')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_GLU' :  match1,
		'CYS_TRP' :  match2,
		'ARG_GLU' :  match3,
		'CYS_GLU' :  match4,
		'CYS_ARG' :  match5,
		'ARG_TRP' :  match6}