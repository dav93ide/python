
strng = [
"LIST",
"OF",
"YOUR",
"OBJECT",
"PROPERTIES"
]


gts = []
sts = []

for s in strng:
    gt = "def get"
    st = "def set"
    name = ""
    first = False

    for i in range(0, len(s)):
        c = s[i]
        if (s[i-1] == "_" and c == "m") or c == "_":
            pass
        elif c.isupper():
            if not first:
                name += c.lower()
            else:
                name += c
            first = True
            gt += "_" + c.lower()
            st += "_" + c.lower()    
        else:
            gt += c
            st += c
            name += c

    gt += "(self):\n\t" + "return self." + s + "\n"
    st += "(self, {name}):\n\tself.{prop} = {name}\n".format(name = name, prop = s)  


    gts.append(gt)
    sts.append(st)

print("#region - Get Methods")

for gt in gts:
    print(gt)

print("#endregion")
print("\n\n\n\n\n\n\n")
print("#region - Set Methods")

for st in sts:
    print(st)

print("#endregion")
