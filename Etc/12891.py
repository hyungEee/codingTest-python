s,p=map(int,input().split()) # 원래 문자열 길이, 부분 문자열 길이
dna=list(input()) # 임의 문자열
cond=list(map(int,input().split())) # a,c,g,t 포함 조건

def validCheck():
    return (acgt['A']>=cond[0] and acgt['C']>=cond[1] and acgt['G']>=cond[2] and acgt['T']>=cond[3])

# 초기 윈도우 셋팅
total=0
acgt={'A':0,'C':0,'G':0,'T':0}
for i in range(p):
    acgt[dna[i]]+=1
if validCheck():
    total+=1

for i in range(p,s): # 윈도우를 한칸씩 옮겨가며 유효한지 확인해주는 작업
    acgt[dna[i-p]]-=1 # 이전 문자 갯수 --
    acgt[dna[i]]+=1 # 다음 문자 갯수 ++
    if validCheck():
        total+=1
    
print(total)