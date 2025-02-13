color=list(map(int, input().split()))
H=len(color)
color.sort()
Op=0 
for i in range(H - 1):
        if color[i]==color[i+1]:
                Op+=1
        else:
                Op+=0
print(Op)
