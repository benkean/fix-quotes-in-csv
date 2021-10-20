import regex

r = regex.compile('(?<!^|,|(?<!^|,)")"(?!,|$|"(?!,|$))')

out = ''

with open('test.txt',"r") as f:
    for line in f.readlines():
        out += r.sub('""',line)

with open ('out.txt',"w") as f:
    f.write(out)
