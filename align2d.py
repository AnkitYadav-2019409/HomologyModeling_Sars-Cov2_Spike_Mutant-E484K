from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='7c2l', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='7c2lA', atom_files='7c2l.pdb')
aln.append(file='querySeq.ali', align_codes='e484k')
aln.align2d(max_gap_length=50)
aln.write(file='querySeq-7c2lA.ali', alignment_format='PIR')
aln.write(file='querySeq-7c2lA.pap', alignment_format='PAP')
