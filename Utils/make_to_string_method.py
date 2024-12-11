
strng = [
"LIST",
"OF",
"YOUR",
"OBJECT",
"PROPERTIES"
]

for s in strng:
    s = """f\"#- {name}: {{self.{name}}}\\n\"""".format(name = s)
    print(s)
