'''
FUNC:M_1hto_6_3_1_2
PDB:1hto
EC:6.3.1.2
RESI:asp,glu,arg,mn
LOCI:a-50,327,339;a-470;
'''
import motifFunctions as cmd
ARG_MN = { 
	'distances':
		[[10.11], [9.2], [9.45], [8.83], [9.05], [8.83], [9.83]],
	'comparisons':
		[[('CB', 'ARG', 'MN', 'MN', 10.11)], [('CG', 'ARG', 'MN', 'MN', 9.2)], [('CD', 'ARG', 'MN', 'MN', 9.45)], [('NE', 'ARG', 'MN', 'MN', 8.83)], [('CZ', 'ARG', 'MN', 'MN', 9.05)], [('NH1', 'ARG', 'MN', 'MN', 8.83)], [('NH2', 'ARG', 'MN', 'MN', 9.83)]]}
ARG_GLU = { 
	'distances':
		[[7.14, 7.79, 7.15, 6.17, 7.93], [8.53, 9.09, 8.26, 7.18, 8.93], [8.81, 9.17, 8.14, 6.96, 8.72], [10.26, 10.61, 9.53, 8.35, 10.04], [11.22, 11.52, 10.4, 9.29, 10.8], [12.48, 12.78, 11.65, 10.52, 12.02], [11.08, 11.32, 10.21, 9.2, 10.53]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 7.14), ('CB', 'ARG', 'CG', 'GLU', 7.79), ('CB', 'ARG', 'CD', 'GLU', 7.15), ('CB', 'ARG', 'OE1', 'GLU', 6.17), ('CB', 'ARG', 'OE2', 'GLU', 7.93)], [('CG', 'ARG', 'CB', 'GLU', 8.53), ('CG', 'ARG', 'CG', 'GLU', 9.09), ('CG', 'ARG', 'CD', 'GLU', 8.26), ('CG', 'ARG', 'OE1', 'GLU', 7.18), ('CG', 'ARG', 'OE2', 'GLU', 8.93)], [('CD', 'ARG', 'CB', 'GLU', 8.81), ('CD', 'ARG', 'CG', 'GLU', 9.17), ('CD', 'ARG', 'CD', 'GLU', 8.14), ('CD', 'ARG', 'OE1', 'GLU', 6.96), ('CD', 'ARG', 'OE2', 'GLU', 8.72)], [('NE', 'ARG', 'CB', 'GLU', 10.26), ('NE', 'ARG', 'CG', 'GLU', 10.61), ('NE', 'ARG', 'CD', 'GLU', 9.53), ('NE', 'ARG', 'OE1', 'GLU', 8.35), ('NE', 'ARG', 'OE2', 'GLU', 10.04)], [('CZ', 'ARG', 'CB', 'GLU', 11.22), ('CZ', 'ARG', 'CG', 'GLU', 11.52), ('CZ', 'ARG', 'CD', 'GLU', 10.4), ('CZ', 'ARG', 'OE1', 'GLU', 9.29), ('CZ', 'ARG', 'OE2', 'GLU', 10.8)], [('NH1', 'ARG', 'CB', 'GLU', 12.48), ('NH1', 'ARG', 'CG', 'GLU', 12.78), ('NH1', 'ARG', 'CD', 'GLU', 11.65), ('NH1', 'ARG', 'OE1', 'GLU', 10.52), ('NH1', 'ARG', 'OE2', 'GLU', 12.02)], [('NH2', 'ARG', 'CB', 'GLU', 11.08), ('NH2', 'ARG', 'CG', 'GLU', 11.32), ('NH2', 'ARG', 'CD', 'GLU', 10.21), ('NH2', 'ARG', 'OE1', 'GLU', 9.2), ('NH2', 'ARG', 'OE2', 'GLU', 10.53)]]}
ASP_MN = { 
	'distances':
		[[43.28], [42.78], [41.69], [43.52]],
	'comparisons':
		[[('CB', 'ASP', 'MN', 'MN', 43.28)], [('CG', 'ASP', 'MN', 'MN', 42.78)], [('OD1', 'ASP', 'MN', 'MN', 41.69)], [('OD2', 'ASP', 'MN', 'MN', 43.52)]]}
GLU_MN = { 
	'distances':
		[[14.06], [15.1], [14.64], [13.46], [15.57]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 14.06)], [('CG', 'GLU', 'MN', 'MN', 15.1)], [('CD', 'GLU', 'MN', 'MN', 14.64)], [('OE1', 'GLU', 'MN', 'MN', 13.46)], [('OE2', 'GLU', 'MN', 'MN', 15.57)]]}
ARG_ASP = { 
	'distances':
		[[48.57, 48.17, 47.04, 49.02], [48.7, 48.28, 47.15, 49.1], [49.41, 48.95, 47.81, 49.75], [49.48, 49.0, 47.87, 49.78], [49.97, 49.5, 48.39, 50.28], [50.03, 49.55, 48.45, 50.31], [50.45, 50.03, 48.93, 50.83]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 48.57), ('CB', 'ARG', 'CG', 'ASP', 48.17), ('CB', 'ARG', 'OD1', 'ASP', 47.04), ('CB', 'ARG', 'OD2', 'ASP', 49.02)], [('CG', 'ARG', 'CB', 'ASP', 48.7), ('CG', 'ARG', 'CG', 'ASP', 48.28), ('CG', 'ARG', 'OD1', 'ASP', 47.15), ('CG', 'ARG', 'OD2', 'ASP', 49.1)], [('CD', 'ARG', 'CB', 'ASP', 49.41), ('CD', 'ARG', 'CG', 'ASP', 48.95), ('CD', 'ARG', 'OD1', 'ASP', 47.81), ('CD', 'ARG', 'OD2', 'ASP', 49.75)], [('NE', 'ARG', 'CB', 'ASP', 49.48), ('NE', 'ARG', 'CG', 'ASP', 49.0), ('NE', 'ARG', 'OD1', 'ASP', 47.87), ('NE', 'ARG', 'OD2', 'ASP', 49.78)], [('CZ', 'ARG', 'CB', 'ASP', 49.97), ('CZ', 'ARG', 'CG', 'ASP', 49.5), ('CZ', 'ARG', 'OD1', 'ASP', 48.39), ('CZ', 'ARG', 'OD2', 'ASP', 50.28)], [('NH1', 'ARG', 'CB', 'ASP', 50.03), ('NH1', 'ARG', 'CG', 'ASP', 49.55), ('NH1', 'ARG', 'OD1', 'ASP', 48.45), ('NH1', 'ARG', 'OD2', 'ASP', 50.31)], [('NH2', 'ARG', 'CB', 'ASP', 50.45), ('NH2', 'ARG', 'CG', 'ASP', 50.03), ('NH2', 'ARG', 'OD1', 'ASP', 48.93), ('NH2', 'ARG', 'OD2', 'ASP', 50.83)]]}
ASP_GLU = { 
	'distances':
		[[49.13, 50.63, 51.36, 50.74, 52.61], [48.73, 50.22, 50.94, 50.3, 52.18], [47.56, 49.05, 49.77, 49.13, 51.01], [49.62, 51.1, 51.81, 51.15, 53.05]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 49.13), ('CB', 'ASP', 'CG', 'GLU', 50.63), ('CB', 'ASP', 'CD', 'GLU', 51.36), ('CB', 'ASP', 'OE1', 'GLU', 50.74), ('CB', 'ASP', 'OE2', 'GLU', 52.61)], [('CG', 'ASP', 'CB', 'GLU', 48.73), ('CG', 'ASP', 'CG', 'GLU', 50.22), ('CG', 'ASP', 'CD', 'GLU', 50.94), ('CG', 'ASP', 'OE1', 'GLU', 50.3), ('CG', 'ASP', 'OE2', 'GLU', 52.18)], [('OD1', 'ASP', 'CB', 'GLU', 47.56), ('OD1', 'ASP', 'CG', 'GLU', 49.05), ('OD1', 'ASP', 'CD', 'GLU', 49.77), ('OD1', 'ASP', 'OE1', 'GLU', 49.13), ('OD1', 'ASP', 'OE2', 'GLU', 51.01)], [('OD2', 'ASP', 'CB', 'GLU', 49.62), ('OD2', 'ASP', 'CG', 'GLU', 51.1), ('OD2', 'ASP', 'CD', 'GLU', 51.81), ('OD2', 'ASP', 'OE1', 'GLU', 51.15), ('OD2', 'ASP', 'OE2', 'GLU', 53.05)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_MN, d, 'M_1hto_6_3_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_GLU, d, 'M_1hto_6_3_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_MN, d, 'M_1hto_6_3_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_MN, d, 'M_1hto_6_3_1_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_ASP, d, 'M_1hto_6_3_1_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_GLU, d, 'M_1hto_6_3_1_2')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_MN' :  match1,
		'ARG_GLU' :  match2,
		'ASP_MN' :  match3,
		'GLU_MN' :  match4,
		'ARG_ASP' :  match5,
		'ASP_GLU' :  match6}