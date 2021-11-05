# Code for making Hashtagnumbers

# Creating buildingblocks for the numbers
Hashtagline = "#"*9+"\n"
TabTag = "#"+"\t"+"#"+"\n"
Righttag = " "+"\t"+"#"+"\n"
Lefttag = "#"+"\t"+" "+"\n"
Midtag = "   "+"#"+"   "+"\n"

# Creating numbers from the buildingblocks
Zero = Hashtagline + TabTag*7 + Hashtagline
One = Righttag*9
Two = Hashtagline + Righttag*3 + Hashtagline + Lefttag*3 + Hashtagline
Tree = Hashtagline + Righttag*3 + Hashtagline + Righttag*3 + Hashtagline
Four = TabTag*3 + Hashtagline + Righttag*4
Five = Hashtagline + Lefttag*3 + Hashtagline + Righttag*3 + Hashtagline
Six = Hashtagline + Lefttag*3 + Hashtagline + TabTag*3 + Hashtagline
Seven = Hashtagline + Righttag*8
Eight = Hashtagline + TabTag*3 + Hashtagline + TabTag*3 + Hashtagline
Nine = Hashtagline + TabTag*3 + Hashtagline + Righttag*3 + Hashtagline

# Printing the numbers from 0-9
print(Zero+One+Two+Tree+Four+Five+Six+Seven+Eight+Nine)