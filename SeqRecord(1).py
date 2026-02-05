from Bio.Seq import Seq
simple_seq = Seq("AGCT")

from Bio.SeqRecord import SeqRecord
simple_seq_r = SeqRecord(simple_seq)
print(simple_seq_r)

simple_seq_r.id = 'AC12345'
print("id = ", simple_seq_r.id)

simple_seq_r.description = "Just a simple example"
print("description = ", simple_seq_r.description)

# Add annotations
simple_seq_r.annotations["evidence"] = 'none.'
print("annotations = ", simple_seq_r.annotations)
print(simple_seq_r.annotations["evidence"])

# Letter annotations
simple_seq_r.letter_annotations["phred_quality"] = [40, 39, 38, 37]
print("letter_annotations = ", simple_seq_r.letter_annotations)