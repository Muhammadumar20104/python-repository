from cgitb import text


fu = open('text.txt','w')
fu.write('umae write\n')
fu.close

fw = open('text.txt','r')
tex = fw.read()
print(tex)
fw.close()