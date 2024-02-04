from tkinter import *
from functools import cmp_to_key
import heapq

root = Tk()

class point:
    def __init__(self,x,y):
        self.x,self.y,self.id=x,y,0

class vec:
    def __init__(self,a,b):
        self.x=a.x-b.x
        self.y=a.y-b.y 
class segment:
    def __init__(self,x1,y1,x2,y2):
        self.x1,self.y1,self.x2,self.y2,self.a,self.b=x1,y1,x2,y2,y1-y2,x2-x1
        if(self.a==0):
            self.b=1
        if(self.b==0):
            self.a=1
        self.c=self.a*x1+self.b*y1
        self.length=(x1-x2)**2+(y1-y2)**2

def cross(a,b):
    return (a.x*b.y-a.y*b.x)

def equal(a,b):
    if(a.x==b.x and a.y==b.y):
        return True
    else:
        return False

def check_inter(line1,line2):
    det=line1.a*line2.b-line2.a*line1.b
    if(det==0):
        return True
    X=(line2.b*line1.c - line1.b*line2.c)/det
    Y=(line1.a*line2.c-line2.a*line1.c)/det
    p1=point(line1.x1,line1.y1)
    p2=point(line1.x2,line1.y2)
    p3=point(line2.x1,line2.y1)
    p4=point(line2.x2,line2.y2)
    if(equal(p1,p3) or equal(p1,p4) or equal(p2,p3) or equal(p2,p4)):
        return False
    if(min(line1.x1,line1.x2)<X<max(line1.x1,line1.x2) and min(line1.y1,line1.y2)<Y<max(line1.y1,line1.y2)) or (min(line2.x1,line2.x2)<=X<=max(line2.x1,line2.x2) and min(line1.y1,line1.y2)<=Y<=max(line2.y1,line2.y2)):
        return True
    else:
        return False

def dis(a,b):
    return (a.x-b.x)**2+(a.y-b.y)**2

c=Canvas(root,bg='white',height=700,width=1500)

vertice=[]
edge=[]
c.place(x=0,y=80)

def draw(x,y,k):
    vertice.append(point(x,y))
    l1=c.create_line(x,y,x+29,y)
    vertice.append(point(x+29,y))
    c.create_line(x+29,y,x+29,y+29*4)
    vertice.append(point(x+29,y+29*4))
    c.create_line(x+29,y+29*4,x+29*2,y+29*4)
    vertice.append(point(x+29*2,y+29*4))
    c.create_line(x+29*2,y+29*4,x+29*2,y)
    vertice.append(point(x+29*2,y))
    c.create_line(x+29*2,y,x+29*5,y)
    vertice.append(point(x+29*5,y))
    c.create_line(x+29*5,y,x+29*5,y+29)
    vertice.append(point(x+29*5,y+29))
    c.create_line(x+29*5,y+29,x+29*3,y+29)
    vertice.append(point(x+29*3,y+29))
    c.create_line(x+29*3,y+29,x+29*3,y+29*2)
    vertice.append(point(x+29*3,y+29*2))
    c.create_line(x+29*3,y+29*2,x+29*5,y+29*2)
    vertice.append(point(x+29*5,y+29*2))
    c.create_line(x+29*5,y+29*2,x+29*5,y+29*3)
    vertice.append(point(x+29*5,y+29*3))
    c.create_line(x+29*5,y+29*3,x+29*3,y+29*3)
    vertice.append(point(x+29*3,y+29*3))
    c.create_line(x+29*3,y+29*3,x+29*3,y+29*4)
    vertice.append(point(x+29*3,y+29*4))
    c.create_line(x+29*3,y+29*4,x+29*6,y+29*4)
    vertice.append(point(x+29*6,y+29*4))
    c.create_line(x+29*6,y+29*4,x+29*6,y)
    vertice.append(point(x+29*6,y))
    c.create_line(x+29*6,y,x+29*9,y)
    vertice.append(point(x+29*9,y))
    c.create_line(x+29*9,y,x+29*9,y+29)
    vertice.append(point(x+29*9,y+29))
    c.create_line(x+29*9,y+29,x+29*7,y+29)
    vertice.append(point(x+29*7,y+29))
    c.create_line(x+29*7,y+29,x+29*7,y+29*2)
    vertice.append(point(x+29*7,y+29*2))
    c.create_line(x+29*7,y+29*2,x+29*9,y+29*2)
    vertice.append(point(x+29*9,y+29*2))
    c.create_line(x+29*9,y+29*2,x+29*9,y+29*3)
    vertice.append(point(x+29*9,y+29*3))
    c.create_line(x+29*9,y+29*3,x+29*7,y+29*3)
    vertice.append(point(x+29*7,y+29*3))
    c.create_line(x+29*7,y+29*3,x+29*7,y+29*4)
    vertice.append(point(x+29*7,y+29*4))
    c.create_line(x+29*7,y+29*4,x+29*10,y+29*4)
    vertice.append(point(x+29*10,y+29*4))
    c.create_line(x+29*10,y+29*4,x+29*10,y+29*6)
    vertice.append(point(x+29*10,y+29*6))
    l2=c.create_line(x+29*10,y+29*6,x+29*9,y+29*6)
    vertice.append(point(x+29*9,y+29*6))
    c.create_line(x+29*9,y+29*6,x+29*9,y+29*5)
    vertice.append(point(x+29*9,y+29*5))
    c.create_line(x+29*9,y+29*5,x,y+29*5)
    vertice.append(point(x,y+29*5))
    c.create_line(x,y+29*5,x,y)
    if(k==0):
        c.delete(l2)
    if(k==1):
        c.delete(l1)
        c.delete(l2)
    if(k==2):
        c.delete(l1)
    return (x+29*9,y+29*6)

def create_map(n):
    x,y=0,0
    if(n==1):
        draw(144,140,-1)
        return
    for i in range(0,n):
        if(i==0):
            x,y=draw(100,100,0)
        if(i>0 and i<n-1):
            x,y=draw(x,y,1)
        if(i==n-1):
            x,y=draw(x,y,2)
create_map(1)
b1=Button(root, text='find')
b2=Button(root,text='clear')
b1.place(x=20,y=20)
b2.place(x=100,y=20)

def cmp(a,b):
    v1=point(a.x-cen.x,a.y-cen.y)
    v2=point(b.x-cen.x,b.y-cen.y)
    if(v1.x==0 and v1.y==0):
        return -1
    if(v2.x==0 and v2.y==0):
        return 1
    if(v1.x<=0 and v2.x>0):
        return -1
    if(v1.x>0 and v2.x<=0):
        return 1
    if(v1.x==0 and v2.x==0):
        if(abs(v1.y)<=abs(v2.y)):
            return -1
        else:
            return 1
    if(v1.y==0 and v2.y==0):
        if(abs(v1.x)<=abs(v2.x)):
            return -1
        else:
            return 1

    det=cross(v1,v2)
    if(det>=0):
        return -1
    if(det<0):
        return 1

    d1=v1.x**2 + v1.y**2
    d2=v2.x**2 + v2.y**2
    if(d1>d2):
        return 1
    else:
        return -1

def check(heap,code,line):
    if(len(heap)==0):
        return False
    minn=heapq.nsmallest(1,heap)
    for line2 in code[minn[0]]:
        if(check_inter(line,code[minn[0]][line2])==True):
            return True
    return False

for i in range(len(vertice)):
    vertice[i].y=-vertice[i].y
    vertice[i].id=i

index=[0 for i in range(len(vertice))]
ans={}
for i in range(28):
    global cen
    cen=vertice[i]
    arr=sorted(vertice,key=cmp_to_key(cmp))
    start=1
    for j in range(len(arr)):
        index[arr[j].id]=j
    min_dis=10000000
    for j in range(1,len(arr)):
        if(dis(arr[j],cen)<min_dis):
            min_dis=dis(arr[j],cen)
            start=j
    code={}
    heap=[]
    heapq.heapify(heap)
    for j in range(start,28):
        if(arr[j].id==i):
            continue
        seg=segment(cen.x,cen.y,arr[j].x,arr[j].y)
        prev=arr[j].id-1
        if(prev==-1):
            prev=27
        pos=(arr[j].id+1)%len(vertice)  
        minn=heapq.nsmallest(1,heap)
        # if(len(heap)>0):
        #     for line2 in code[minn[0]]:
        #         line=code[minn[0]][line2]
        #         print(line.x1,line.y1,line.x2,line.y2)
        #     print()
        if(check(heap,code,seg)==False and prev!=i and pos!=i):
            u,v=i,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)==None):
                ans[u]={}
            ans[u][v]=1
        if(check(heap,code,seg)==True and prev!=i and pos!=i):
            u,v=i,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)!=None and ans[u].get(v)!=None):
                ans[u].pop(v)
            if(ans.get(u)!=None and len(ans[u])==0):
                ans.pop(u)
        if(prev!=i and not (cross(vec(arr[start],cen),vec(arr[j],cen))>=0 and cross(vec(arr[start],cen),vec(vertice[prev],cen))<0 and cross(vec(arr[j],cen),vec(vertice[prev],cen))<0)):
            dis1=min(dis(cen,vertice[prev]),dis(cen,arr[j]),dis(cen,point((vertice[prev].x+arr[j].x)/2,(vertice[prev].y+arr[j].y)/2)))
            seg1=segment(arr[j].x,arr[j].y,vertice[prev].x,vertice[prev].y)
            if(code.get(dis1)!=None and code[dis1].get(f'{prev},{arr[j].id}')!=None):
                code[dis1].pop(f'{prev},{arr[j].id}')
                if(len(code[dis1])==0):
                    code.pop(dis1)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis1)==None):
                    code[dis1]={}
                code[dis1][f'{prev},{arr[j].id}']=seg1
                heapq.heappush(heap,dis1)
        if(pos!=i and not (cross(vec(arr[start],cen),vec(arr[j],cen))>=0 and cross(vec(arr[start],cen),vec(vertice[pos],cen))<0 and cross(vec(arr[j],cen),vec(vertice[pos],cen))<0)):
            dis2=min(dis(cen,vertice[pos]),dis(cen,arr[j]),dis(cen,point((vertice[pos].x+arr[j].x)/2,(vertice[pos].y+arr[j].y)/2)))
            seg2=segment(arr[j].x,arr[j].y,vertice[pos].x,vertice[pos].y)
            if(code.get(dis2)!=None and code[dis2].get(f'{arr[j].id},{pos}')!=None):
                code[dis2].pop(f'{arr[j].id},{pos}')
                if(len(code[dis2])==0):
                    code.pop(dis2)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis2)==None):
                    code[dis2]={}
                code[dis2][f'{arr[j].id},{pos}']=seg2
                heapq.heappush(heap,dis2)
    for j in range(0,28):
        if(arr[j].id==i):
            continue
        seg=segment(cen.x,cen.y,arr[j].x,arr[j].y)
        prev=arr[j].id-1
        if(prev==-1):
            prev=27
        pos=(arr[j].id+1)%len(vertice)
        minn=heapq.nsmallest(1,heap)
        # print(ans)
        # if(arr[j].id==26):
        #     print(arr[j].id)
        # if(len(heap)>0):
        #     for line2 in code[minn[0]]:
        #         line=code[minn[0]][line2]
        #         print(line.x1,line.y1,line.x2,line.y2,j)
        #     print()
        if(check(heap,code,seg)==False and prev!=i and pos!=i):
            u,v=i,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)==None):
                ans[u]={}
            ans[u][v]=1
        # print(u,v)
        if(check(heap,code,seg)==True and prev!=i and pos!=i):
            u,v=i,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)!=None and ans[u].get(v)):
                ans[u].pop(v)
            if(ans.get(u)!=None and len(ans[u])==0):
                ans.pop(u)
        if(prev!=i):
            dis1=min(dis(cen,vertice[prev]),dis(cen,arr[j]),dis(cen,point((vertice[prev].x+arr[j].x)/2,(vertice[prev].y+arr[j].y)/2)))
            seg1=segment(arr[j].x,arr[j].y,vertice[prev].x,vertice[prev].y)
            if(code.get(dis1)!=None and code[dis1].get(f'{prev},{arr[j].id}')!=None):
                code[dis1].pop(f'{prev},{arr[j].id}')
                if(len(code[dis1])==0):
                    code.pop(dis1)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis1)==None):
                    code[dis1]={}
                code[dis1][f'{prev},{arr[j].id}']=seg1
                heapq.heappush(heap,dis1)
        if(pos!=i):
            dis2=min(dis(cen,vertice[pos]),dis(cen,arr[j]),dis(cen,point((vertice[pos].x+arr[j].x)/2,(vertice[pos].y+arr[j].y)/2)))
            seg2=segment(arr[j].x,arr[j].y,vertice[pos].x,vertice[pos].y)
            if(code.get(dis2)!=None and code[dis2].get(f'{arr[j].id},{pos}')!=None):
                code[dis2].pop(f'{arr[j].id},{pos}')
                if(len(code[dis2])==0):
                    code.pop(dis2)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis2)==None):
                    code[dis2]={}
                code[dis2][f'{arr[j].id},{pos}']=seg2
                heapq.heappush(heap,dis2)
for i in range(len(vertice)):
    for j in range(i+1,len(vertice)):
        if(ans.get(i)!=None and ans[i].get(j)!=None and ans[i][j]==1):
            c.create_line(vertice[i].x,-vertice[i].y,vertice[j].x,-vertice[j].y,fill='red')
root.mainloop()
