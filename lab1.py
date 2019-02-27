def TopologicalSort(V,Edge):
	n=len(V)
	s=[]
	degree=[0 for i in range(n)]
	sort=[]
	for v in range(n):
		degree[v]=get_in_degree(v,Edge)
	for i in range(n):
		if degree[i]==0:
			s.append(i)
	while (len(s)>0):
		v=s.pop()
		sort.append(v)
		for i in Edge[v]:
			degree[i]=degree[i]-1
			if degree[i]==0:
				s.append(i)
	return sort
def get_in_degree(v,Edge):
	degree=0
	for i in Edge:
		if v in i:
			degree=degree+1
	return degree
def main():
	print("Enter the no. of nodes and edges :")
	n=int(input())
	e=int(input())
	print("Enter the edges ")
	V=[i for i in range(n)]
	Edge=[[] for i in range(n)]
	for i in range(e):
		a=input().split()
		start=int(a[0])
		end=int(a[1])
		Edge[start].append(end)
	x=TopologicalSort(V,Edge)
	print("A linearisation is :",end=" ")
	for i in x:
		print(i,end=" ")
	print()
if __name__ == '__main__':
	main()

