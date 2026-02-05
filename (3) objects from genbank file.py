from Bio import SeqIO
record = SeqIO.read("NC_005816.gb", "genbank")
print(record)
print(record.seq)
print("id = ", record.id)
print("name = ", record.name)
print("description =", record.description)

print(record.letter_annotations)

print("len = ", len(record.annotations))
print(record.annotations["source"])

print("dbxrefs = ", record.dbxrefs)


print("features = ", len(record.features))