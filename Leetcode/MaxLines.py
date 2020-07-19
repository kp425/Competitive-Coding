
def slope(point1,point2):
	ydiff = point2[1]-point1[1]
	xdiff = point2[0]-point1[0]
	if xdiff == 0:
		return "infinity"
	return ydiff/xdiff

def sol(points):
	if all(x==points[0] for x in points):
		return len(points)
	if len(points)==1:
		return 1
	if len(points)==0:
		return 0
	
	info = {"points":None,"max_no":None}
	m = 0
	l = {}
	points = sorted(points)
	for i in range(len(points)):
		for j in range(i+1,len(points)):
			s = slope(points[i],points[j])
			l[(points[j][0],points[j][1])] = s

		for x in set(l.values()):
			temp = list(l.values()).count(x)+1
			if temp>m:
				l[(points[i][0],points[i][1])] = x 
				info["points"] = [key for key in l if l[key]==x]
				info["max_no"] = temp
				m = temp
		
		l ={}
	
	for i in info["points"]:
		count = points.count([i[0],i[1]])
		if count>1:
			info["max_no"] = info["max_no"]+count-1
		
	return info["max_no"]




points = [[1,1],[2,2],[3,3]]
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
points = [[0,0],[1,1],[0,0]]
points = [[0,0],[0,0]]

k = sol(points)
print(k)















# def sol_1(points):
# 	m = [None,0]
# 	l = []
# 	points = sorted(points)
# 	print(points)
# 	for i in range(len(points)):
# 		for j in range(i+1,len(points)):
# 			s = slope(points[i],points[j])
# 			l.append(s)

# 		for x in set(l):
# 			temp = l.count(x)+1
# 			if temp>m[1]:
# 				m[0]=x
# 				m[1]=temp
# 		l =[]
	
# 	return m