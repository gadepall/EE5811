import string
import numpy as np
import cvxpy
import matplotlib.pyplot as plt
import os
import time

def init(A):
	for i in range(len(A)):
		A[i] = A[i] + '0'
	return A

def noof(A,f):
	q = 0
	for f in range(0,len(A)-1):
		if (A[f] == f):
			q+=1
	return q
	
def order(B):
	for i in range(1,len(B)):
		key = noof(B[i],'1')
		st = B[i]
		j = i -1	
		while j >=0 and key < noof(B[j],'1'):
			B[j+1] = B[j]
			j -=1
		B[j+1] = st
	return B

def common(A,B):
	count = 0
	C = ''
	for i in range(len(A) - 1):
		if(A[i] != B[i]):
			C += '-'
			count +=1
		else:
			C +=A[i]
	if (count ==1):
		C +='0'
		return C
	else:
		return None
		
def status(A,B):
	if(common(A,B)):
		A = A[:-1] 
		B = B[:-1]
		A += '1'
		B += '1'
	return A,B

def nxtbl(A):   ####m ------ no of tures for output
	C =[]
	for i in range(len(A)-1):
		for j in range(i,len(A)):
			if(common(A[i],A[j])):
				C.append(common(A[i],A[j]))
			A[i],A[j] = status(A[i],A[j])
	return C

def primertr(A):
	C = []
	for i in range(len(A)):
		for l in A[i]:
			if (l[-1] == '0'):
				C.append(l)
	if(nxtbl(C)):
		for i in range(len(nxtbl(C))):
			nxtbl(C)[i] = nxtbl(C)[i][:-1]
		return nxtbl(C)
	else:
		for i in range(len(C)):
			C[i] = C[i][:-1]
		return C

def expressiongnr(A):
	c = ""
	s = string.ascii_lowercase[0:len(A)]
	for i in range(len(A)):
		if (A[i] == '0'):
			c += s[i] +"'"
		elif (A[i] == '1'):
			c += s[i]
	return c

	
def samechk(A): 
	C =[]
	for i in range(0, len(A)): 
		d = 0
		for j in range(0, i): 
			if (A[i] == A[j]): 
				d = 1
				break
		if (d == 0): 
			C.append(A[i])
	return C
	
def numbr_fndr(A,n):
	cnt = 0
	for i in range(len(A)):
		if(A[i] == n):
			cnt +=1
			k = i
		else:
			continue
	if(cnt ==1):
		return k,True
	else:
		return None,False

def minimizer(A):
	A = np.asmatrix(A)
	b = -1*np.ones(A.shape[1])
	x = cvxpy.Variable(A.shape[0],boolean = True)
	constraint = [-1*A.transpose()*x <=b.transpose()]
	cost_function = A.transpose()*x
	s=0
	for i in range(cost_function.shape[0]):
		s  +=cost_function[i]
	knapsack_problem = cvxpy.Problem(cvxpy.Minimize(s), constraint)
	knapsack_problem.solve(solver=cvxpy.GLPK_MI)
	f =[]
	for j in range(len(x.value)):
		if(x.value[j] == 1):
			f.append(j)
	return f

def eg(A):
	c = ""
	s = string.ascii_lowercase[0:len(A)]
	for i in range(len(A)):
		if (A[i] == '0'):
			c += s[i] +"'"
		elif (A[i] == '1'):
			c += s[i]
	return c

def arreg(x):
	for i in range(len(x)):
		x[i] = eg(x[i])
	
	return x

def dec(x):
	for i in range(len(x)):
		x[i] = int(x[i],2)

	return x

# ~ def arrange(pi,inp):
	# ~ x = inp
	# ~ (dec(x)).sort()
	# ~ f =[]
	# ~ for i in range(len(x)):
		# ~ f.append('0'*(len(pi[0])-len(bin(x[i])[2:])) +(bin(x[i])[2:]))  
	# ~ return f
	
def pos(s):
	arr = []
	x = 0
	for i in range(len(s)):
		if(s[i] == "-"):
			arr.insert(x,i)
			x+=1
	return arr

def rewrite(p,q):	# rewriting p
	for i in range(len(q)):
		p = p[:q[i]] + '-' + p[(q[i]+1):]
		
	return p

def rowforcheap(p,inp):	#for getting any row of the chart.  p = prime implicant , inp = given input numbers
	row = []
	new_inp = []
	x = 0
	inp_copy = inp
	for i in range(len(inp)):
		new_inp.insert(i,rewrite(inp_copy[i],pos(p)))
		#print(new_inp)
	
	for i in range(len(inp)):
		if(p == new_inp[i]):
			row.insert(x,'✓')
			x+=1
		else:
			row.insert(x,'X')
			x+=1
	
	return row		
	
def row(p,inp):	#for getting any row of the chart.  p = prime implicant , inp = given input numbers
	row = []
	new_inp = []
	x = 0
	inp_copy = inp
	for i in range(len(inp)):
		new_inp.insert(i,rewrite(inp_copy[i],pos(p)))
		#print(new_inp)
	
	for i in range(len(inp)):
		if(p == new_inp[i]):
			row.insert(x,1)
			x+=1
		else:
			row.insert(x,0)
			x+=1
	
	return row		
				
def create_chart(pi,inp): #pi = prime implicants' array , inp = given input numbers in binary form(also array)
	chart = np.vstack((row(pi[0],inp),row(pi[1],inp)))
	for i in range(2,len(pi)):
		chart = np.vstack((chart,row(pi[i],inp)))					
	
	return chart
	
def create_chart_save(pi,inp): #pi = prime implicants' array , inp = given input numbers in binary form(also array)
	chart = np.vstack((rowforcheap(pi[0],inp),rowforcheap(pi[1],inp)))
	for i in range(2,len(pi)):
		chart = np.vstack((chart,rowforcheap(pi[i],inp)))					
	
	return chart

def table(pi,inp,x):
	fig = plt.figure()
	c = len(inp)+1
	r = len(pi)+1
    
	col_labels = dec(inp)
	row_labels = arreg(pi)
	table_vals = x.tolist()

	the_table = plt.table(cellText=table_vals,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc='center')
	the_table.auto_set_font_size(False)
	the_table.set_fontsize(20)
	the_table.scale(r,c)


	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
	for pos in ['right','top','bottom','left']:
		plt.gca().spines[pos].set_visible(False)
	plt.savefig('./Prime_Implecant_chart.png', bbox_inches='tight', pad_inches=0.05)
	#plt.show()	

def main(file_name):
	lines = open(file_name).readlines()
	A=open('newfile.txt', 'w').writelines(lines[4:])
	data = np.loadtxt("newfile.txt")
	B = []

	for i in range(len(data)):
		
		B.append([int(x) for x in data[i]])

	B = np.asarray(B)
	C = []
	inp = lines[:2][0][3]
	out = lines[:2][1][3]
	nv = int(inp)
	k=0
	inputs = B[:,0:4]
	for i in range(4, len(data[0])):
		out = B[:, i]
		sd = []
		for j in range(len(out)):
			tmp = ""
			if (out[j] == 1):
				for s in inputs[j,:]:
					tmp+= str(s)
				sd.append((tmp))
		C.append((sd))
	os.system("rm -rf newfile.txt")
	I =C
	start_time = time.time()
	C = samechk(C[0])
	C = init(C)
	m = len(C)
	k = len(C[0])
	#C = order(C)
	A = []
	A.append(C)
	A.append(nxtbl(C))
	for i in range(1,m-1):
		if(A[i] !=[]):
			A.append(nxtbl(A[i]))
			#print(A[i])
		else:
			break
	A = A[:-1]
	B = samechk(primertr(A))
	#print(B)
	#print(B)
	#print(I[0])
	M = create_chart(B,I[0])
	#print(M)
	f = minimizer(M)
	#print("--- %s seconds ---" % (time.time() - start_time))
	j = []
	for e in range(len(f)):	
		j.append(B[f[e]])
	W =[]
	#print(j)
	for a in B:
		W.append((expressiongnr(a)))
	#print(I[0])
	return j,B,I[0],k,(time.time() - start_time)
	
def main_without_txt(C):
	I =C
	start_time = time.time()
	C = samechk(C)
	C = init(C)
	m = len(C)
	k = len(C[0])
	#C = order(C)
	A = []
	A.append(C)
	A.append(nxtbl(C))
	for i in range(1,m-1):
		if(A[i] !=[]):
			A.append(nxtbl(A[i]))
			#print(A[i])
		else:
			break
	A = A[:-1]
	B = samechk(primertr(A))
	#print(B)
	#print(I)
	M = create_chart(B,I)
	#print(M)
	f = minimizer(M)
	#print("--- %s seconds ---" % (time.time() - start_time))
	j = []
	for e in range(len(f)):	
		j.append(B[f[e]])
	W =[]
	#print(j)
	for a in B:
		W.append((expressiongnr(a)))
	
	return j,W,I,k,(time.time() - start_time)

def expr(A):
	C =''
	B = []
	if(len(A[0]) <= 26):
		for i in range(len(A)):
			B.append(expressiongnr(A[i]))
		for i in range(len(B)):
			C +=(B[i] + ' + ')
		return C[:-2]
	else:
		return A
			
