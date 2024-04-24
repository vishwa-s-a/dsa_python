# wrting code for playfair cipher
def create_matrix(txt):
	global matrix
	s=''
	for i in txt:
		if(i not in s):
			s+=i
	for i in range(97,123,1):
		if(chr(i) not in s):
			if(chr(i)=='j'):
				pass
			else:
				s+=chr(i)
	row=0
	col=0
	for i in s:
		if(i=='i'):
			matrix[row][col]='ij'
		else:
			matrix[row][col]=i
		col+=1
		if(col==5):
			col=0
			row+=1
	

def create_diagrams(t):
	global digrams
	txt=list(t)
	temp=[]
	for i in range(0,len(txt),2):
		try:
			u=txt[i]
			v=txt[i+1]
		except:
			u=txt[i]
			v='x'
		if(u==v):
			v='x'
			txt.insert(i+1,'x')
		temp.append(u)
		temp.append(v)
		digrams.append(list.copy(temp))
		temp.clear()
		
def find_index(z):
	global matrix
	if(z=='i' or z=='j'):
		z='ij'
	for ind,i in enumerate(matrix):
		try:
			u=i.index(z)
			return ind,u
		except:
			continue

def encrypt():
	enc=''
	#txt is diagrams
	global matrix,digrams
	for i in digrams:
		ind1=find_index(i[0])
		ind2=find_index(i[1])
		x1=ind1[0]
		y1=ind1[1]
		x2=ind2[0]
		y2=ind2[1]

		if(x1==x2):
			y1=(y1+1)%5
			y2=(y2+1)%5
		elif(y1==y2):
			x1=(x1+1)%5
			x2=(x2+1)%5
		else:
			y1,y2=y2,y1
		enc+=matrix[x1][y1]+matrix[x2][y2]
	for i in enc:
		if(i=='j'):
			pass
		else:
			print(i,end='')	

key=input('Enter the keyword: ').replace(' ','').lower()
pt=input('Enter the plainText: ').replace(' ','').lower()
print(key,pt)
matrix=[[None for i in range(5)] for j in range(5)]
digrams=[]
print(matrix)
create_matrix(key)
print(matrix)
create_diagrams(pt)
print(digrams)
encrypt()
