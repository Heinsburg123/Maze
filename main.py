from tkinter import *
from tkinter import ttk
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

class node:
    def __init__(self, a_star,path, cur):
        self.a_star=a_star
        self.path=path
        self.cur=cur
    def __lt__(self,other):
        return self.a_star<other.a_star

node_fr=[(0,0),(1,0),(1,4),(2,4),(2,0),(5,0),(5,1),(3,1),(3,2),(5,2),(5,3),(3,3),(3,4),(6,4),(6,0),(9,0),(9,1),(7,1),(7,2),(9,2),(9,3),(7,3),(7,4),(10,4),(10,6)]
node_back=[(0,0),(-1,0),(-1,-1),(-10,-1),(-10,-6)]
vertice=[]
ans={}
dem=0

def cross(a,b):
    return (a.x*b.y-a.y*b.x)

def equal(a,b):
    if(a.x==b.x and a.y==b.y):
        return True
    else:
        return False

def check_inter(line1,line2,Click):
    det=line1.a*line2.b-line2.a*line1.b
    p1=point(line1.x1,line1.y1)
    p2=point(line1.x2,line1.y2)
    p3=point(line2.x1,line2.y1)
    p4=point(line2.x2,line2.y2)
    if(equal(p1,p3) or equal(p1,p4) or equal(p2,p3) or equal(p2,p4)):
        return False
    if(det==0):
        return False
    X=(line2.b*line1.c - line1.b*line2.c)/det
    Y=(line1.a*line2.c-line2.a*line1.c)/det

    if(min(line1.x1,line1.x2)<=X<=max(line1.x1,line1.x2) and min(line1.y1,line1.y2)<=Y<=max(line1.y1,line1.y2) and min(line2.x1,line2.x2)<=X<=max(line2.x1,line2.x2) and min(line2.y1,line2.y2)<=Y<=max(line2.y1,line2.y2) and Click==False):
        return True
    elif(min(line1.x1,line1.x2)<X<max(line1.x1,line1.x2) and min(line1.y1,line1.y2)<=Y<=max(line1.y1,line1.y2) and min(line2.x1,line2.x2)<=X<=max(line2.x1,line2.x2) and min(line2.y1,line2.y2)<Y<max(line2.y1,line2.y2) and Click==True):
        return True
    else:
        return False

def dis(a,b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

def dis_to_p(p,seg1):
    seg2=segment(0,0,1,1)
    seg2.a=-seg1.b
    seg2.b=seg1.a
    seg2.c=seg2.a*p.x+seg2.b*p.y
    det=seg1.a*seg2.b-seg2.a*seg1.b
    if(det==0):
        return min(dis(p,point(seg1.x1,seg1.y1)),dis(p,point(seg1.x2,seg1.y2)))
    X=(seg2.b*seg1.c - seg1.b*seg2.c)/det
    Y=(seg1.a*seg2.c - seg2.a*seg1.c)/det
    seg2.x1=100000
    if(seg2.b==0):
        seg2.y1==100000
    else:
        seg2.y1=(seg2.c-seg2.x1*seg2.a)/seg2.b
    seg2.x2=-100000
    if(seg2.b==0):
        seg2.y2==-100000
    else:
        seg2.y2=(seg2.c-seg2.x2*seg2.a)/seg2.b
    p_new=point(X,Y)
    if(check_inter(seg1,seg2,False)):
        return dis(p,p_new)
    else:
        return min(dis(p,point(seg1.x1,seg1.y1)),dis(p,point(seg1.x2,seg1.y2)))

def draw(x,y,k,size,add):
    if(add):
        vertice.append(point(x,y))
    for i in range(1,len(node_fr)):
        c.create_line(x+size*node_fr[i-1][0],y+size*node_fr[i-1][1],x+size*node_fr[i][0],y+size*node_fr[i][1])
        if(add):   
            vertice.append(point(x+size*node_fr[i][0],y+size*node_fr[i][1]))
    x_end,y_end=x+size*node_fr[len(node_fr)-1][0],y+size*node_fr[len(node_fr)-1][1]
    for i in range(k-1):
        for j in range(2,len(node_fr)):
            c.create_line(x_end+size*node_fr[j-1][0]-size,y_end+size*node_fr[j-1][1],x_end+size*node_fr[j][0]-size,y_end+size*node_fr[j][1])
            if(add):
                vertice.append(point(x_end+size*node_fr[j][0]-size,y_end+size*node_fr[j][1]))
        x_end,y_end=x_end+size*node_fr[len(node_fr)-1][0]-size,y_end+size*node_fr[len(node_fr)-1][1]
    for i in range(1,len(node_back)):
        c.create_line(x_end+size*node_back[i-1][0],y_end+size*node_back[i-1][1],x_end+size*node_back[i][0],y_end+size*node_back[i][1])
        if(add):
            vertice.append(point(x_end+size*node_back[i][0],y_end+size*node_back[i][1]))
    x_end,y_end=x_end+size*node_back[len(node_back)-1][0],y_end+size*node_back[len(node_back)-1][1]
    for i in range(k-1):
        for j in range(2,len(node_back)):
            c.create_line(x_end+size*node_back[j-1][0]+size,y_end+size*node_back[j-1][1],x_end+size*node_back[j][0]+size,y_end+size*node_back[j][1])
            if(add):
                vertice.append(point(x_end+size*node_back[j][0]+size,y_end+size*node_back[j][1]))
        x_end,y_end=x_end+size*node_back[len(node_back)-1][0]+size,y_end+size*node_back[len(node_back)-1][1]
    if(add):
        vertice.pop()

def check(heap,code,line):
    if(len(heap)==0):
        return False
    minn=heapq.nsmallest(1,heap)
    for line2 in code[minn[0]]:
        if(check_inter(line,code[minn[0]][line2],False)==True):
            return True
    return False

def check_taunt(s1,s2,prev,pos,convex):
    if(convex==1):
        return False
    if(cross(vec(s2,pos),vec(s1,s2))>0 and cross(vec(s2,prev),vec(s1,s2))<0):
        return False
    return True

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
            if(v1.y*v2.y>=0):
                if(abs(v1.y)<=abs(v2.y)):
                    return -1
                else:
                    return 1
            else:
                if(v1.y>=v2.y):
                    return -1
                else:
                    return 1
        if(v1.y==0 and v2.y==0):
            if(v1.x<=v2.x):
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
                if(ans[u].get(v)==None):
                    ans[u][v]=1
        if(check(heap,code,seg)==True and prev!=cen.id and pos!=cen.id):
            u,v=cen.id,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)==None):
                ans[u]={}
            ans[u][v]=0
        if(arr[j].id==-1 or arr[j].id==-2):
            continue
        if(prev!=cen.id and not (cross(vec(arr[start],cen),vec(arr[j],cen))>=0 and cross(vec(arr[start],cen),vec(vertice[prev],cen))<0 and cross(vec(arr[j],cen),vec(vertice[prev],cen))<0)):
            # if(arr[j].id==40):
            #     print(arr[start].id,arr[j].id)
            seg1=segment(arr[j].x,arr[j].y,vertice[prev].x,vertice[prev].y)
            dis1=dis_to_p(cen,seg1)
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
        if(pos!=cen.id and not (cross(vec(arr[start],cen),vec(arr[j],cen))>=0 and cross(vec(arr[start],cen),vec(vertice[pos],cen))<0 and cross(vec(arr[j],cen),vec(vertice[pos],cen))<0)):
            seg2=segment(arr[j].x,arr[j].y,vertice[pos].x,vertice[pos].y)
            dis2=dis_to_p(cen,seg2)
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
    for j in range(len(arr)):
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
                if(ans[u].get(v)==None):
                    ans[u][v]=1
        if(check(heap,code,seg)==True and prev!=cen.id and pos!=cen.id):
            u,v=cen.id,arr[j].id
            if(u>v):
                u,v=v,u
            if(ans.get(u)==None):
                ans[u]={}
            ans[u][v]=0
        if(arr[j].id==-1 or arr[j].id==-2):
            continue
        if(prev!=cen.id):
            seg1=segment(arr[j].x,arr[j].y,vertice[prev].x,vertice[prev].y)
            dis1=dis_to_p(cen,seg1)
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
            seg2=segment(arr[j].x,arr[j].y,vertice[pos].x,vertice[pos].y)
            dis2=dis_to_p(cen,seg2)
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

def clear_node():
    global dem
    if(dem<2):
        return
    for _ in range(2):
        for i in range(len(vertice)-1):
            if(ans[vertice[len(vertice)-1].id].get(vertice[i].id)!=None and ans[vertice[len(vertice)-1].id][vertice[i].id]==1):
                a[i].pop()
        a.pop()
        vertice.pop()
    ans.pop(-1)
    ans.pop(-2)
    c.delete('all')
    draw(144,140,1,29,0)
    dem=0

def show_visi():
    for i in range(len(vertice)):
        for j in a[i]:
            c.create_line(vertice[i].x,-vertice[i].y,vertice[j].x,-vertice[j].y,fill='red')

def show_path():
    v=len(vertice)-1
    u=len(vertice)-2
    while(cha[v]!=u):
        c.create_line(vertice[v].x,-vertice[v].y,vertice[cha[v]].x,-vertice[cha[v]].y,fill='blue')
        v=cha[v]
    c.create_line(vertice[v].x,-vertice[v].y,vertice[cha[v]].x,-vertice[cha[v]].y,fill='blue')

def raycast(p,extra):
    check=0
    ray=segment(p.x,p.y,100000,p.y)
    for i in range(1,len(vertice)-extra):
        seg=segment(vertice[(i-1)%(len(vertice)-extra)].x,vertice[(i-1)%(len(vertice)-extra)].y,vertice[i].x,vertice[i].y)
        if(check_inter(ray,seg,True)):
            check+=1
    if(check%2!=0):
        return True
    else:
        return False

def click(e):
    global dem,p1,p2
    if(dem>=2):
        return
    dem+=1
    if(dem==1):
        if(raycast(point(e.x,-e.y),1)==False):
            dem-=1
            return 
        p1=point(e.x,-e.y)
        p1.id=-1
        vertice.append(p1)
        a.append([])
        line_of_sight(p1,1)
        add_node(p1,-1,len(vertice)-1)
    else:
        if(raycast(point(e.x,-e.y),2)==False):
            dem-=1
            return 
        p2=point(e.x,-e.y)
        p2.id=-2
        vertice.append(p2)
        a.append([])
        line_of_sight(p2,2)
        add_node(p2,-2,len(vertice)-1)
        find_path()

def find_path():
    d=[100000000 for _ in range(len(vertice))]
    d[len(vertice)-2]=0
    close=[0 for _ in range(len(vertice))]
    for i in range(len(vertice)):
        cha[i]=0
    heap=[]
    heapq.heapify(heap)
    heapq.heappush(heap,node(0,0,len(vertice)-2))
    while len(heap)>0:
        cur_node=heapq.heappop(heap)
        u=cur_node.cur
        if(cur_node.path>d[u]):
            continue
        if(close[u]==1):
            continue
        close[u]=1
        for v in a[u]:
            if(d[u]+dis(vertice[u],vertice[v])+dis(vertice[v],vertice[len(vertice)-1])>d[len(vertice)-1]):
                continue
            if(d[v]>d[u]+dis(vertice[u],vertice[v])):
                d[v]=d[u]+dis(vertice[u],vertice[v])
                cha[v]=u
                heapq.heappush(heap,node(d[v]+dis(vertice[v],vertice[len(vertice)-1]),d[v],v))

c=Canvas(root,bg='white',height=700,width=1500)
c.place(x=0,y=80)
draw(144,140,1,29,1)

a=[[] for _ in range(len(vertice))]
cha=[0 for _ in range(len(vertice)+2)]

p1=point(0,0)
p2=point(0,0)
b1=ttk.Button(root, text='show graph',command=show_visi)
b2=ttk.Button(root,text='clear',command=clear_node)
b3=ttk.Button(root, text='show path', command=show_path)
b1.place(x=20,y=20)
b2.place(x=100,y=20)
b3.place(x=180,y=20)

for i in range(len(vertice)):
    vertice[i].y=-vertice[i].y
    vertice[i].id=i

for i in range(len(vertice)):
    cc=cross(vec(vertice[i],vertice[(i-1)%len(vertice)]),vec(vertice[(i+1)%len(vertice)],vertice[i]))
    if(cc>0):
        line_of_sight(vertice[i],0)

create_data()

c.bind('<Button 1>',click)
c.pack()
root.mainloop()
