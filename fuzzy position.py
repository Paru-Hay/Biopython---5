# Creating location with fuzzy end points
from Bio import SeqFeature
start_pos = SeqFeature.AfterPosition(5)
end_pos = SeqFeature.BetweenPosition(9, left=8, right=9)
my_location = SeqFeature.SimpleLocation(start_pos, end_pos)

print(my_location)
print(my_location.start)
print(my_location.end)

# To just see the integer positions:
print(int(my_location.start))
print(int(my_location.end))

# To create a position without using fuzzy positions
exact_location = SeqFeature.SimpleLocation(5, 9)
print(exact_location)
print(int(exact_location.start))