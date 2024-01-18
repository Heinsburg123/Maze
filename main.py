from tkinter import *
from functools import cmp_to_key
import heapq

root = Tk()

class point:
    def __init__(self,x,y):
        self.x,self.y,self.id=x,y,0

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

def check_inter(line1,line2):
    X=(line2.b*line1.c - line1.b*line2.c)/(line1.a*line2.b-line2.a*line1.b)
    Y=(line1.a*line2.c-line2.a*line1.c)/(line1.a*line2.b-line2.a*line1.b)
    if(min(line1.x1,line1.x2)<=X<=max(line1.x1,line1.x2) and min(line1.y1,line1.y2)<=Y<=max(line1.y1,line1.y2)):
        return True
    else:
        return False

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
        draw(100,100,-1)
        return
    for i in range(0,n):
        if(i==0):
            x,y=draw(100,100,0)
        if(i>0 and i<n-1):
            x,y=draw(x,y,1)
        if(i==n-1):
            x,y=draw(x,y,2)
create_map(1)
c.pack()
b1=Button(root, text='find')
b2=Button(root,text='clear')
b1.place(x=20,y=20)
b2.place(x=100,y=20)

def cmp(a,b):
    v1=point(a.x-cen.x,a.y-cen.y)
    v2=point(b.x-cen.x,b.y-cen.y)
    if(v1.x<0 and v2.x>=0):
        return -1
    if(v1.x>=0 and v2.x<0):
        return 1
    if(v1.x==0 and v2.x==0):
        if(v1.y<=v2.y):
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

def check(heap,code,line):
    minn=heapq.nsmallest(1,heap)
    for i in range(len(code[minn[0]])):
        if(check_inter(line,code[minn[0]][i])):
            return True
        else:
            return False

for i in range(len(vertice)):
    vertice[i].y=-vertice[i].y
    vertice[i].id=i

index=[0 for i in range(len(vertice))]
for i in range(len(vertice)):
    global cen
    cen=vertice[i]
    arr=sorted(vertice,key=cmp_to_key(cmp))
    for j in range(len(arr)):
        index[arr[j].id]=j
    code={}
    heap=[]
    heapq.heapify(heap)
    for j in range(len(vertice)):
        if(arr[j].id==i):
            continue
        prev=arr[j].id-1
        pos=(arr[j].id+1)%len(vertice)
        print(prev,arr[j].id,pos)
        if(prev!=i):
            dis1=(cen.x-vertice[prev].x)**2+(cen.y-vertice[prev].y)**2
            seg1=segment(arr[j].x,arr[j].y,vertice[prev].x,vertice[prev].y)
            if(index[prev]>j):
                if(code.get(dis1)==None):
                    code[dis1]=[]
                code[dis1].append(seg1)
                heapq.heappush(heap,dis1)
            else:
                #print(dis1)
                #print(prev,pos,arr[j].id)
                code.pop(dis1)
                while(code.get(heapq.nsmallest(1,heap))==None):
                    heapq.heappop(heap)
        if(pos!=i):
            dis2=(cen.x-vertice[pos].x)**2+(cen.y-vertice[pos].y)**2
            seg2=segment(arr[j].x,arr[j].y,vertice[pos].x,vertice[pos].y)
            if(index[pos]>j):
                if(code.get(dis2)==None):
                    code[dis2]=[]
                code[dis2].append(seg2)
                heapq.heappush(heap,dis2)
            else:
                code.pop(seg2.length)
                while(code.get(heapq.nsmallest(1,heap))==None):
                    heapq.heappop()
        seg=segment(cen.x,cen.y,arr[j].x,arr[j].y)
        if(check(heap,code,seg)==False):
            c.create_line(arr[j].x,arr[j].y,cen.x,cen.y)

root.mainloop()
