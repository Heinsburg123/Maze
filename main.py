from tkinter import *
from functools import cmp_to_key
from collections import deque 
import math
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
    if(min(line1.x1,line1.x2)<=X<=max(line1.x1,line1.x2) and min(line1.y1,line1.y2)<=Y<=max(line1.y1,line1.y2)) and (min(line2.x1,line2.x2)<=X<=max(line2.x1,line2.x2) and min(line1.y1,line1.y2)<=Y<=max(line2.y1,line2.y2)):
        return True
    else:
        return False

def dis(a,b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

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

def check_taunt(s1,s2,prev,pos,convex):
    if(convex==1):
        return False
    if(cross(vec(s2,pos),vec(s1,s2))>0 and cross(vec(s2,prev),vec(s1,s2))<0):
        return False
    return True

ans={}

def line_of_sight(cen,extra):
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
        if(det>0):
            return -1
        if(det<0):
            return 1

        d1=v1.x**2 + v1.y**2
        d2=v2.x**2 + v2.y**2
        if(d1>d2):
            return 1
        else:
            return -1
    convex=0
    if(cross(vec(cen,vertice[(i-1)%(len(vertice)-extra)]),vec(vertice[(i+1)%(len(vertice)-extra)],cen))<0):
        convex=1
    if(cen.id<0):
        convex=0
    if(convex==1):
        return
    arr=sorted(vertice,key=cmp_to_key(cmp))
    start=1
    min_dis=10000000
    for j in range(1,len(arr)):
        if(dis(arr[j],cen)<min_dis and arr[j].id!=-1 and arr[j].id!=-2):
            min_dis=dis(arr[j],cen)
            start=j
    code={}
    heap=[]
    heapq.heapify(heap)
    for j in range(start,len(arr)):
        if(arr[j].id==cen.id):
            continue
        seg=segment(cen.x,cen.y,arr[j].x,arr[j].y)
        prev=(arr[j].id-1)%(len(vertice)-extra)
        pos=(arr[j].id+1)%(len(vertice)-extra) 
        if(check(heap,code,seg)==False and prev!=cen.id and pos!=cen.id):
            if(((cen.id<0 and arr[j].id<0) or (cen.id<0 and check_taunt(cen,arr[j],vertice[prev],vertice[pos],convex))) or ((convex==1 and cross(vec(arr[j],cen),vec(vertice[(i-1)%(len(vertice)-extra)],cen))<0 and cross(vec(arr[j],cen),vec(vertice[(i+1)%(len(vertice)-extra)],cen))>0) or (convex==0 and (cross(vec(arr[j],cen),vec(vertice[(i+1)%(len(vertice)-extra)],cen))>0 or cross(vec(arr[j],cen),vec(vertice[(i-1)%(len(vertice)-extra)],cen))<0)) and check_taunt(arr[j],cen,vertice[i-1],vertice[(i+1)%(len(vertice)-extra)],0) and check_taunt(cen,arr[j],vertice[prev],vertice[pos],convex))):
                u,v=cen.id,arr[j].id
                if(u>v):
                    u,v=v,u
                if(ans.get(u)==None):
                    ans[u]={}
                ans[u][v]=1
        if(check(heap,code,seg)==True and prev!=cen.id and pos!=cen.id):
            u,v=cen.id,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)!=None and ans[u].get(v)!=None):
                ans[u].pop(v)
            if(ans.get(u)!=None and len(ans[u])==0):
                ans.pop(u)
        if(prev!=cen.id and not (cross(vec(arr[start],cen),vec(arr[j],cen))>=0 and cross(vec(arr[start],cen),vec(vertice[prev],cen))<0 and cross(vec(arr[j],cen),vec(vertice[prev],cen))<0)):
            dis1=min(dis(cen,vertice[prev]),dis(cen,arr[j]),dis(cen,point((vertice[prev].x+arr[j].x)/2,(vertice[prev].y+arr[j].y)/2)))
            seg1=segment(arr[j].x,arr[j].y,vertice[prev].x,vertice[prev].y)
            u,v=prev,arr[j].id
            if(u>v):
                u,v=v,u
            if(code.get(dis1)!=None and code[dis1].get(f'{u},{v}')!=None):
                code[dis1].pop(f'{u},{v}')
                if(len(code[dis1])==0):
                    code.pop(dis1)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis1)==None):
                    code[dis1]={}
                code[dis1][f'{u},{v}']=seg1
                heapq.heappush(heap,dis1)
        if(arr[j].id==-1 or arr[j].id==-2):
            continue
        if(pos!=cen.id and not (cross(vec(arr[start],cen),vec(arr[j],cen))>=0 and cross(vec(arr[start],cen),vec(vertice[pos],cen))<0 and cross(vec(arr[j],cen),vec(vertice[pos],cen))<0)):
            dis2=min(dis(cen,vertice[pos]),dis(cen,arr[j]),dis(cen,point((vertice[pos].x+arr[j].x)/2,(vertice[pos].y+arr[j].y)/2)))
            seg2=segment(arr[j].x,arr[j].y,vertice[pos].x,vertice[pos].y)
            u,v=arr[j].id,pos
            if(u>v):
                u,v=v,u
            if(code.get(dis2)!=None and code[dis2].get(f'{u},{v}')!=None):
                code[dis2].pop(f'{u},{v}')
                if(len(code[dis2])==0):
                    code.pop(dis2)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis2)==None):
                    code[dis2]={}
                code[dis2][f'{u},{v}']=seg2
                heapq.heappush(heap,dis2)
    for j in range(len(vertice)):
        if(arr[j].id==cen.id):
            continue
        seg=segment(cen.x,cen.y,arr[j].x,arr[j].y)
        prev=(arr[j].id-1)%(len(vertice)-extra)
        pos=(arr[j].id+1)%(len(vertice)-extra)  
        if(check(heap,code,seg)==False and prev!=cen.id and pos!=cen.id):
            if(((cen.id<0 and arr[j].id<0) or (cen.id<0 and check_taunt(cen,arr[j],vertice[prev],vertice[pos],convex))) or ((convex==1 and cross(vec(arr[j],cen),vec(vertice[(i-1)%(len(vertice)-extra)],cen))<0 and cross(vec(arr[j],cen),vec(vertice[(i+1)%(len(vertice)-extra)],cen))>0) or (convex==0 and (cross(vec(arr[j],cen),vec(vertice[(i+1)%(len(vertice)-extra)],cen))>0 or cross(vec(arr[j],cen),vec(vertice[(i-1)%(len(vertice)-extra)],cen))<0)) and check_taunt(arr[j],cen,vertice[i-1],vertice[(i+1)%(len(vertice)-extra)],0) and check_taunt(cen,arr[j],vertice[prev],vertice[pos],convex))):
                u,v=cen.id,arr[j].id
                if(u>v):
                    u,v=v,u
                if(ans.get(u)==None):
                    ans[u]={}
                ans[u][v]=1
        if(check(heap,code,seg)==True and prev!=cen.id and pos!=cen.id):
            u,v=cen.id,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)!=None and ans[u].get(v)):
                ans[u].pop(v)
            if(ans.get(u)!=None and len(ans[u])==0):
                ans.pop(u)
        if(arr[j].id==-1 or arr[j].id==-2):
            continue
        if(prev!=cen.id):
            dis1=min(dis(cen,vertice[prev]),dis(cen,arr[j]),dis(cen,point((vertice[prev].x+arr[j].x)/2,(vertice[prev].y+arr[j].y)/2)))
            seg1=segment(arr[j].x,arr[j].y,vertice[prev].x,vertice[prev].y)
            u,v=prev,arr[j].id
            if(u>v):
                u,v=v,u
            if(code.get(dis1)!=None and code[dis1].get(f'{u},{v}')!=None):
                code[dis1].pop(f'{u},{v}')
                if(len(code[dis1])==0):
                    code.pop(dis1)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis1)==None):
                    code[dis1]={}
                code[dis1][f'{u},{v}']=seg1
                heapq.heappush(heap,dis1)
        if(pos!=cen.id):
            dis2=min(dis(cen,vertice[pos]),dis(cen,arr[j]),dis(cen,point((vertice[pos].x+arr[j].x)/2,(vertice[pos].y+arr[j].y)/2)))
            seg2=segment(arr[j].x,arr[j].y,vertice[pos].x,vertice[pos].y)
            u,v=arr[j].id,pos
            if(u>v):
                u,v=v,u
            if(code.get(dis2)!=None and code[dis2].get(f'{u},{v}')!=None):
                code[dis2].pop(f'{u},{v}')
                if(len(code[dis2])==0):
                    code.pop(dis2)
                while(len(heap)>0 and code.get(heapq.nsmallest(1,heap)[0])==None ):
                        heapq.heappop(heap)
            else:
                if(code.get(dis2)==None):
                    code[dis2]={}
                code[dis2][f'{u},{v}']=seg2
                heapq.heappush(heap,dis2)

a=[[] for _ in range(1000)]

def create_data():
    for i in range(len(vertice)):
        for j in range(i+1,len(vertice)):
            if(ans.get(i)!=None and ans[i].get(j)!=None and ans[i][j]==1):
                a[i].append(j)
                a[j].append(i)
    for i in range(len(vertice)):
        convex1,convex2=0,0
        prev1=(i-1)%len(vertice)
        pos1=(i+1)%len(vertice)
        prev2=i
        pos2=(i+2)%len(vertice)
        if(cross(vec(vertice[prev1],vertice[i]),vec(vertice[i],vertice[pos1]))<0):
            convex1=1
        if(cross(vec(vertice[prev2],vertice[(i+1)%len(vertice)]),vec(vertice[(i+1)%len(vertice)],vertice[pos2]))<0):
            convex2=1
        if(check_taunt(vertice[i],vertice[(i+1)%len(vertice)],vertice[prev2],vertice[pos2],convex2)==True and check_taunt(vertice[(i+1)%len(vertice)],vertice[i],vertice[prev1],vertice[pos1],convex1)==True):
            a[i].append(i+1)
            a[i+1].append(i)
        
def add_node(p,ind,size):
    for i in range(size):
        if(ans.get(ind)!=None and ans[ind].get(vertice[i].id)!=None and ans[ind][vertice[i].id]==1):
            a[size].append(i)
            a[i].append(size)

dem=0
p1=point(0,0)
p2=point(0,0)

for i in range(len(vertice)):
    line_of_sight(vertice[i],0)

create_data()
def click(e):
    global dem,p1,p2
    if(dem>=2):
        return
    dem+=1
    if(dem==1):
        p1=point(e.x,-e.y)
        p1.id=-1
        vertice.append(p1)
        line_of_sight(p1,1)
        add_node(p1,-1,len(vertice)-1)
    else:
        p2=point(e.x,-e.y)
        p2.id=-2
        vertice.append(p2)
        line_of_sight(p2,2)
        add_node(p2,-2,len(vertice)-1)
        for i in range(len(vertice)):
            for j in a[i]:
                c.create_line(vertice[i].x,-vertice[i].y,vertice[j].x,-vertice[j].y,fill='red')
        find_path()
def find_path():
    d=[100000000 for _ in range(1000)]
    close=[0 for _ in range(1000)]
    d[len(vertice)-2]=0
    cha=[0 for _ in range(1000)]
    code={}
    heap=[]
    code[0]=deque([len(vertice)-2])
    heapq.heapify(heap)
    heapq.heappush(heap,0)
    while len(heap)>0:
        dd=heapq.heappop(heap)
        u=code[dd][0]
        code[dd].popleft()
        if(dd>d[u]):
            continue
        if(close[u]==1):
            continue
        close[u]=1
        for v in a[u]:
            if(d[u]+dis(vertice[u],vertice[v])>d[len(vertice)-1]):
                continue
            if(d[v]>d[u]+dis(vertice[u],vertice[v])):
                if(v==13):
                    print(u)
                d[v]=d[u]+dis(vertice[u],vertice[v])
                cha[v]=u
                heapq.heappush(heap,d[v])
                if(code.get(d[v])==None):
                    code[d[v]]=deque([])
                code[d[v]].append(v)
    v=len(vertice)-1
    u=len(vertice)-2
    # print(d[v])
    while(cha[v]!=u):
        c.create_line(vertice[v].x,-vertice[v].y,vertice[cha[v]].x,-vertice[cha[v]].y,fill='blue')
        v=cha[v]
    c.create_line(vertice[v].x,-vertice[v].y,vertice[cha[v]].x,-vertice[cha[v]].y,fill='blue')




c.bind('<Button 1>',click)
c.pack()
root.mainloop()
