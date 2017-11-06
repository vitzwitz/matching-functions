'''
FUNC:A_1hzf_3_4_21_43
PDB:1hzf
EC:3.4.21.43
RESI:cys,gln
LOCI:a-991,994;
'''
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&r. gln'%(d*7.30))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&r. gln'%(d*7.12))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. CD&r. gln'%(d*8.42))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. OE1&r. gln'%(d*9.50))
cmd.select('cys5', 'n. CB&r. cys w. %s of n. NE2&r. gln'%(d*8.53))
cmd.select('cys6', 'n. SG&r. cys w. %s of n. CB&r. gln'%(d*6.35))
cmd.select('cys7', 'n. SG&r. cys w. %s of n. CG&r. gln'%(d*5.85))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. CD&r. gln'%(d*6.93))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. OE1&r. gln'%(d*8.10))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. NE2&r. gln'%(d*6.85))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.select('gln1', 'n. CB&r. gln w. %s of n. CB&cys'%(d*7.30))
cmd.select('gln2', 'n. CB&r. gln w. %s of n. SG&cys'%(d*6.35))
cmd.select('gln3', 'n. CG&r. gln w. %s of n. CB&cys'%(d*7.12))
cmd.select('gln4', 'n. CG&r. gln w. %s of n. SG&cys'%(d*5.85))
cmd.select('gln5', 'n. CD&r. gln w. %s of n. CB&cys'%(d*8.42))
cmd.select('gln6', 'n. CD&r. gln w. %s of n. SG&cys'%(d*6.93))
cmd.select('gln7', 'n. OE1&r. gln w. %s of n. CB&cys'%(d*9.50))
cmd.select('gln8', 'n. OE1&r. gln w. %s of n. SG&cys'%(d*8.10))
cmd.select('gln9', 'n. NE2&r. gln w. %s of n. CB&cys'%(d*8.53))
cmd.select('gln10', 'n. NE2&r. gln w. %s of n. SG&cys'%(d*6.85))
cmd.select('gln',' br. gln1&br. gln2&br. gln3&br. gln4&br. gln5&br. gln6&br. gln7&br. gln8&br. gln9&br. gln10')
cmd.delete('gln1')
cmd.delete('gln2')
cmd.delete('gln3')
cmd.delete('gln4')
cmd.delete('gln5')
cmd.delete('gln6')
cmd.delete('gln7')
cmd.delete('gln8')
cmd.delete('gln9')
cmd.delete('gln10')
cmd.select('A_1hzf_3_4_21_43', 'cys|gln')
cmd.delete('cys')
cmd.delete('gln')
