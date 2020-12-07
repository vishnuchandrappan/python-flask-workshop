# A Set is a collection which is unordered and un-indexed. 
set1 = {4,5,6}
print(f"set1                => {set1}")

# No duplicate members.
set2 = {1,2,3,1,2}
print(f"set1                => {set2}")

# Check existence in set
print(f"check 1 in set2     => {1 in set2}")

# Add to set
set2.add(4)
print(f"add 4 to set2       => {set2}")

# Remove from set
set2.remove(2)
print(f"remove 2            => {set2}")

# Add duplicate
set2.add(1)
print(f"add 1 (dup)         => {set2}")

# Clear set
# set2.clear()
# print(f"clear set2          => {set2}")

# Delete
# del set2

# SET Operations

# union
print(f"Union               => {set1.union(set2)}")
print(f"Union |             => {set1 | set2}")

# intersection
print(f"intersection        => {set1.intersection(set2)}")
print(f"intersection &      => {set1 & set2}")

# difference
print(f"difference          => {set1.difference(set2)}")
print(f"difference -        => {set1 - set2}")

# xor (exactly in one of the two)
print(f"XOR                 => {set1.__xor__(set2)}")
print(f"XOR ^               => {set1 ^ set2}")
