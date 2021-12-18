# Code for making Hashtagnumbers

# Creating buildingblocks for the numbers
Hashtagline = "#"*9+"\n"
TabTag = "#"+"\t"+"#"+"\n"
Righttag = " "+"\t"+"#"+"\n"
Lefttag = "#"+"\t"+" "+"\n"
Midtag = "   "+"#"+"   "+"\n"

# Creating numbers from the buildingblocks
Zero = Hashtagline + TabTag*7 + Hashtagline + "\n"
One = Righttag*9+ "\n"
Two = Hashtagline + Righttag*3 + Hashtagline + Lefttag*3 + Hashtagline+ "\n"
Tree = Hashtagline + Righttag*3 + Hashtagline + Righttag*3 + Hashtagline+ "\n"
Four = TabTag*3 + Hashtagline + Righttag*4+ "\n"
Five = Hashtagline + Lefttag*3 + Hashtagline + Righttag*3 + Hashtagline+ "\n"
Six = Hashtagline + Lefttag*3 + Hashtagline + TabTag*3 + Hashtagline+ "\n"
Seven = Hashtagline + Righttag*8+ "\n"
Eight = Hashtagline + TabTag*3 + Hashtagline + TabTag*3 + Hashtagline+ "\n"
Nine = Hashtagline + TabTag*3 + Hashtagline + Righttag*3 + Hashtagline+ "\n"

# Printing the numbers from 0-9
print(Zero+One+Two+Tree+Four+Five+Six+Seven+Eight+Nine)