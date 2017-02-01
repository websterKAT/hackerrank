class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linklist:
	def __init__(self):
		self.current = None

	def add(self,data):
		tmp = Node(data)
		tmp.next = self.current
		self.current = tmp	
	
	def addQueue(self):
		queue = []
		p = self.current
		while p != None:
			queue.append(p.data)
			p = p.next
		return queue

	

class graph:
	def __init__(self):
		self.dic = {}
		self.color = {}
		self.count = {}


	def _add(self,v1,v2):
		if v1 not in self.dic:
			self.dic[v1] = linklist()
		self.dic[v1].add(v2)
		self.color[v1] = 'w'
		self.count[v1] = 0
		
	
	def add(self,v1,v2):
		self._add(v1,v2)
		self._add(v2,v1)

	def bfs(self,start):
		queue = []
		queue.append(start)
		self.color[start] = 'g'
		while len(queue) != 0:
			tmp = queue.pop(0)
			secret = self.count[tmp]
			if self.color[tmp] == 'g':
				#print tmp
				self.color[tmp] = 'b'
				p = self.dic[tmp]
				sur = p.current
				while sur != None:
					if self.color[sur.data] == 'w':
						queue.append(sur.data)
						self.color[sur.data] = 'g'
						self.count[sur.data] = secret + 1	
					sur= sur.next
					
				
		return self.count


q = int(raw_input())
for a in xrange(q):
	g = graph()
	n,e = raw_input().strip().split(' ')
	n,e = [int(n),int(e)]
	for b in xrange(e):
		a,b = raw_input().strip().split(' ')
		a,b = [int(a),int(b)]
		g.add(a,b)
	s = int(raw_input())
	web = g.bfs(s)
	for c in xrange(1,n+1):
		if c == s:
			continue
		elif c not in web or web[c] == 0:
			print "-1",
		else:
			print(str(web[c]*6)),
		if c == n:
			print ""


