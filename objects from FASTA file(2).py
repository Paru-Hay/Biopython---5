from Bio import SeqIO
record = SeqIO.read("NC_005816.fna", "fasta")
print(record)

# print(record.seq)

record.dbxrefs
print("dbxrefs =", record.dbxrefs)