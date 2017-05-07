import sys
import regex

sys.stdin = "1,a\t1\n1,b\t1\n1,b\t1\n2,a\t1\n2,d\t1\n2,e\t1\n3,a\t1\n3,b\t1"
sys.stdin = sys.stdin.split('\n')
for i in range(len(sys.stdin) - 1):
    sys.stdin[i] += "\n"

############################################################################################################
# Parse newline
############################################################################################################

f = False
oF = ""
oG = ""
for line in sys.stdin:
    arr = line.strip().split('\t')[0].split(',')
    F = arr[0]
    G = arr[1]
    if (f):
        if (oF != F or oG != G):
            print('{0},{1}'.format(oF, oG))
    else:
        f = True
    if regex.search(r'.*\n', line) == None:
        if (oF != F or oG != G):
            print('{0},{1}'.format(F, G))
    oF = F
    oG = G

#############################################################################################################
# Make backup
#############################################################################################################

# f = False
# oF = ""
# oG = ""
# for line in sys.stdin:
#     arr = line.strip().split('\t')[0].split(',')
#     F = arr[0]
#     G = arr[1]
#     if (f):
#         if (oF != F or oG != G):
#             print('{0},{1}'.format(oF, oG))
#     else:
#         f = True
#     backup = oF, oG
#     oF = F
#     oG = G
# if (backup[0] != F or backup[1] != G):
#     print('{0},{1}'.format(F, G))