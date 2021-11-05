# Print O and H using 2 printstatments

HoleTag = "#"
TabTag = "#"+"\t"+"#"

# First i tried making the numbers using 2 varibles
print(HoleTag*9, TabTag, TabTag, TabTag, TabTag, TabTag, TabTag, TabTag, HoleTag*9, sep="\n")
print("\n", HoleTag*9, TabTag, TabTag, TabTag, HoleTag*9, TabTag, TabTag, TabTag, HoleTag*9, sep="\n")

# Then i tried making new varibles of the original 2 varibles
Zero = HoleTag*9+"\n"+TabTag+"\n"+TabTag+"\n"+TabTag+"\n"+TabTag+"\n"+TabTag+"\n"+TabTag+"\n"+TabTag+"\n"+HoleTag*9+"\n"
Eight = HoleTag*9+"\n"+TabTag+"\n"+TabTag+"\n"+TabTag+"\n"+HoleTag*9+"\n"+TabTag+"\n"+TabTag+"\n"+TabTag+"\n"+HoleTag*9+"\n"

print(Zero)
print(Eight)