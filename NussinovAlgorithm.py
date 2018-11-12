import sys
from numpy import *

def base_pair(l,m):
	delta = 0
	if (l=='A' and m=='U') or (l=='U' and m=='A'):
		return 1
	elif (l=='G' and m=='C') or (l=='C' and m=='G'):
		return 1
	else:
		return 0

def traceback(s,seq,i,j,pair):
	if i<j:
		if s[i,j]==s[i+1,j]:
			traceback(s,seq,i+1,j,pair)
		elif s[i,j]==s[i,j-1]:
			traceback(s,seq,i,j-1,pair)
		elif s[i,j]==str(s[i+1,j-1])+str(info([j][i])):
			pair.append([i,j,str(seq[i]),str(seq[j])])
			traceback(s,seq,i+1,j-1,pair)
		else:
			for k in range(i+1,j):
				if s[i,j]==s[i,k]+s[k+1,j]:
					traceback(s,seq,i,k,pair)
					traceback(s,seq,k+1,j,pair)
				break
		return pair

def score_matrix(seq,N):
	L=len(seq)
	s=zeros((L,L))
	for L in range(1,N):
		for i in range(0,N-L):
			j=i+L
			if j-i>=1:
				case1=str(s[i+1,j-1])+str(info([j][i]))
				case2=str(s[i+1,j])
				case3=str(s[i,j-1])
				case4=str(0)
				tmp=[]
				for k in range(i+1,j):
					tmp.append(str(s[i,k]+s[k+1,j]))
					case4=str(max(tmp))
				s[i,j]=str(max(str(case1),str(case2),str(case3),str(case4)))
			else:
				s[i,j]=0
	return s

def print_structure(seq):
	N=len(seq)
	s=score_matrix(seq,N)
	pair=traceback(s,seq,0,len(seq)-1,[])
	print(seq)
	for x in range(0,len(seq)):
		if True in (x==pair[y][0] for y in range(0,len(pair))):
			sys.stdout.write('(')
		elif True in (x==pair[y][1] for y in range(0,len(pair))):
			sys.stdout.write(')')
		else:
			sys.stdout.write('.')
	
seq="GAUCGAUUUACU"
print_structure(seq)
