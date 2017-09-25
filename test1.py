'''
FUNC:test1
PDB:1a0j
EC:3.4.21.4
RESI:his,asp,ser
LOCI:a-57,102,195;
'''
import motifFunctions as cmd
comparisons = \ 
{('HIS', 'SER'):
		[[('CB', 'HIS', 'CB', 'SER', 8.66), ('CB', 'HIS', 'OG', 'SER', 8.85)], [('CG', 'HIS', 'CB', 'SER', 7.2), ('CG', 'HIS', 'OG', 'SER', 7.34)], [('ND1', 'HIS', 'CB', 'SER', 6.65), ('ND1', 'HIS', 'OG', 'SER', 6.76)], [('CD2', 'HIS', 'CB', 'SER', 6.55), ('CD2', 'HIS', 'OG', 'SER', 6.59)], [('CE1', 'HIS', 'CB', 'SER', 5.48), ('CE1', 'HIS', 'OG', 'SER', 5.46)], [('NE2', 'HIS', 'CB', 'SER', 5.4), ('NE2', 'HIS', 'OG', 'SER', 5.31)]],
('ASP', 'HIS'):
		[[('CB', 'ASP', 'CB', 'HIS', 7.57), ('CB', 'ASP', 'CG', 'HIS', 7.69), ('CB', 'ASP', 'ND1', 'HIS', 6.91), ('CB', 'ASP', 'CD2', 'HIS', 8.98), ('CB', 'ASP', 'CE1', 'HIS', 7.87), ('CB', 'ASP', 'NE2', 'HIS', 9.01)], [('CG', 'ASP', 'CB', 'HIS', 6.21), ('CG', 'ASP', 'CG', 'HIS', 6.23), ('CG', 'ASP', 'ND1', 'HIS', 5.47), ('CG', 'ASP', 'CD2', 'HIS', 7.52), ('CG', 'ASP', 'CE1', 'HIS', 6.5), ('CG', 'ASP', 'NE2', 'HIS', 7.59)], [('OD1', 'ASP', 'CB', 'HIS', 5.68), ('OD1', 'ASP', 'CG', 'HIS', 5.97), ('OD1', 'ASP', 'ND1', 'HIS', 5.51), ('OD1', 'ASP', 'CD2', 'HIS', 7.29), ('OD1', 'ASP', 'CE1', 'HIS', 6.66), ('OD1', 'ASP', 'NE2', 'HIS', 7.57)], [('OD2', 'ASP', 'CB', 'HIS', 6.05), ('OD2', 'ASP', 'CG', 'HIS', 5.69), ('OD2', 'ASP', 'ND1', 'HIS', 4.68), ('OD2', 'ASP', 'CD2', 'HIS', 6.84), ('OD2', 'ASP', 'CE1', 'HIS', 5.54), ('OD2', 'ASP', 'NE2', 'HIS', 6.71)]],
('ASP', 'SER'):
		[[('CB', 'ASP', 'CB', 'SER', 10.59), ('CB', 'ASP', 'OG', 'SER', 10.81)], [('CG', 'ASP', 'CB', 'SER', 9.32), ('CG', 'ASP', 'OG', 'SER', 9.59)], [('OD1', 'ASP', 'CB', 'SER', 9.42), ('OD1', 'ASP', 'OG', 'SER', 9.84)], [('OD2', 'ASP', 'CB', 'SER', 8.42), ('OD2', 'ASP', 'OG', 'SER', 8.55)]]}

mtrx = \ 
{('HIS', 'SER'):
		[[8.66, 8.85], [7.2, 7.34], [6.65, 6.76], [6.55, 6.59], [5.48, 5.46], [5.4, 5.31]],
('ASP', 'HIS'):
		[[7.57, 7.69, 6.91, 8.98, 7.87, 9.01], [6.21, 6.23, 5.47, 7.52, 6.5, 7.59], [5.68, 5.97, 5.51, 7.29, 6.66, 7.57], [6.05, 5.69, 4.68, 6.84, 5.54, 6.71]],
('ASP', 'SER'):
		[[10.59, 10.81], [9.32, 9.59], [9.42, 9.84], [8.42, 8.55]]}

