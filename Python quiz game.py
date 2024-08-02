#COMPUTER SCIENCE PROJECT
#Parneet Kaur and Kanishka Khanna

from tkinter import *
from PIL import ImageTk,Image
from random import randint,randrange,random
#Creating a new root window
root=Tk()
root.geometry('1000x1200')
root.title('THE STARNIGHT QUIZ')
root.configure(bg='sky blue')
root.resizable(0,0)
#Defining the answers
answers=[]
userans=[]


#Question 1(Euclid)

list1=[['107°and 121°','73°and 59°'],['51° and 83°','129°and 97°'],['155°and 105°','25°and 75°'],
       ['20°and 43°','137°and 160°'],['91°and 130°','50°and 89°'],['35°and 90°','145°and 90°'],
       ['166°and 41°','139°and 14°'],['148°and 18°','32°and 162°'],['106°and 120°','74°and 60°'],
       ['71°and 81°','109°and 99°']]
r1=randrange(0,10)
q1='Q1.When two lines are intersected by a transversal,what would be the measure of the pair of interior angles at the side at which the lines would meet'
Q1ans=[1,0,1,0,1,0,1,0,1,0]
we=Q1ans[r1]
answers.append(we)
def Check1():
    xz=r.get()
    Check.configure(state=DISABLED)
    Next['state']=NORMAL
    if xz==Q1ans[r1]:
        global lbA1
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
        
#Question 2(BODMAS)
lbA1=Label(text='')        
List1=['6[4(72-63)/3]','6[5(41-36)-(8+14)]','8+3(16-12)','(86-11)/(11+4)',
       '45-2(15-3)','37+26/2+2X25-80/2','7+[12+{8+3-(9X6-13X4+1)}]']
List2=[['72','70','71','56'],['11','9','18','15'],['45','20','56','19'],['3','4','5','6'],
       ['25','22','20','21'],['70','60','55','66'],['27','29','38','54']]
ri=randint(0,6)
q2='Q2.Solve the given equation:\n'+List1[ri]
x3=0
q2ans=[0,2,1,2,3,1,0]
answers.append(q2ans[ri])
def Check2():
    Check.configure(state=DISABLED)
    Next['state']=NORMAL
    xv=r.get()
    if xv==q2ans[ri]:
        global lbA1
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:        
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()

#Question 3(Area of triangle)
lbA1=Label(text='')
list3=['32,12','11,24','22,9','21,8','14,6','4,32','26,21','13,12']
list4=[['192','176','123','92'],['122','132','154','164'],['99','89','98','109'],
       ['54','68','78','84'],['52','42','48','44'],['68','61','64','54'],
       ['373','503','277','273'],['72','74','78','68']]
r3=randrange(0,8)
q3='Q3.Find the area of a triangle whose base and height are'+list3[r3]
q3ans=[0,1,0,3,1,2,3,2]
answers.append(q3ans[r3])
def Check3():
    Check.configure(state=DISABLED)
    Next['state']=NORMAL
    x=r.get()
    if x==q3ans[r3]:
        global lbA1
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()

    
#Question 4 Algebra
lbA1=Label(text='')   
listq4=[['3x+y=8','x+5y=-2'],['2x+5y=20','3x+6y=12'],['x-7y=-11','5x+2y=-18'],
        ['7x-8y=-12','-4x+2y=3'],['6x-5y=8','-12x+2y=0']]
options=[['x=3,y=-1','x=-1,y=3','x=5,y=-3','x=-3,y=5'],['y=8,x=15','x=20,y=-12','x=-20,y=12','y=-20,x=12'],
         ['x=4,y=-1','x=-4,y=1','x=-2,y=4','y=-4,x=1'],['x=1,y=0 ','y=3/2,x=2','x=-3/2,y=1','x=0,y=3/2'],
         ['x=1/3,y=1','x=-1/3,y=-2','x=1/2,y=-1/3','x=0,y=2/3']]
ri4=randint(0,4)
Q4='Q4.Solve the Linear Equations: '+listq4[ri4][0]+','+listq4[ri4][1]
q4ans=[0,2,1,3,1]
answers.append(q4ans[ri4])
def Check4():
    Check.configure(state=DISABLED)
    Next['state']=NORMAL
    x=r.get()
    if x==q4ans[ri4]:
        global lbA1
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:        
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()

#Question 5(Percentage)
lbA1=Label(text='')       
list8=['25% of 200','38% of 500','55% of 50','90% of 90','60% of 250']
list9=[['50','25','100','55'],['170','190','210','165'],['29','29.5','27.5','27'],
       ['9','90','27','81'],['150','180','210','170']]
r8=randrange(0,5)
Q5='Q5.Calculate the following:'+list8[r8]
q5ans=[0,1,2,3,0]
answers.append(q5ans[r8])
def Check5():
    Check.configure(state=DISABLED)
    Next['state']=NORMAL
    global lbA1
    x=r.get()
    if x==q5ans[r8]:
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    
  
#Question 6(pythagoras)
lbA1=Label(text='')
triplets=[[['3','4','x'],['12','35','x'],['5','12','x']],
          [['20','x','29'],['8','x','17'],['28','x','53']],
          [['x','24','25'],['x','60','61'],['x','40','41']]]
xes=[[['x=5','x=7','x=6','x=8'],['x=43','x=37','x=13','x=45'],['x=13','x=15','x=16','x=14']],
     [['x=25','x=23','x=21','x=19'],['x=9','x=6','x=4','x=15'],['x=33','x=44','x=45','x=32']],
     [['x=22','x=21','x=25','x=9'],['x=7','x=12','x=13','x=11'],['x=33','x=9','x=11','x=13']]]
ri6q=randint(0,2)
ri6o=randint(0,2)
q6=''
w=0
if ri6q==0:
    q6s='Q6.Three sides of a right angled triangle are given. Find the third side(x is the greatest):'
    q6=q6s+triplets[ri6q][ri6o][0]+', '+triplets[ri6q][ri6o][1]+', '+triplets[ri6q][ri6o][2]
    if ri6o==0:
        w1=xes[0][0]
        w=w1.index('x=5')
        answers.append(w)
    elif ri6o==1:
        w1=xes[0][1]
        w=w1.index('x=37')
        answers.append(w)
    elif ri6o==2:
        w1=xes[0][2]
        w=w1.index('x=13')
        answers.append(w)
elif ri6q==1:
    q6s='Q6.Three sides of a right angled triangle are given. Find the third side(x is not the greatest):'
    q6=q6s+triplets[ri6q][ri6o][0]+','+triplets[ri6q][ri6o][1]+','+triplets[ri6q][ri6o][2]
    if ri6o==0:
        w1=xes[1][0]
        w=w1.index('x=21')
        answers.append(w)
    elif ri6o==1:
        w1=xes[1][1]
        w=w1.index('x=15')
        answers.append(w)
    elif ri6o==2:
        w1=xes[1][2]
        w=w1.index('x=45')
        answers.append(w)
elif ri6q==2:
    q6s='Q6.Three sides of a right angled triangle are given. Find the third side(x is not the greatest):'
    q6=q6s+triplets[ri6q][ri6o][0]+','+triplets[ri6q][ri6o][1]+','+triplets[ri6q][ri6o][2]
    if ri6o==0:
        w1=xes[2][0]
        w=w1.index('x=9')
        answers.append(w)
    elif ri6o==1:
        w1=xes[2][1]
        w=w1.index('x=11')
        answers.append(w)
    elif ri6o==2:
        w1=xes[2][2]
        w=w1.index('x=9')
        answers.append(w)
def Check6():
    Check.configure(state=DISABLED)
    Next['state']=NORMAL
    x=r.get()
    if x==w:
        global lbA1
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:
        
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()

#Question 7(AP)
lbA1=Label(text='')
r7=randrange(6,18)
q7='Q7.Find the '+str(r7)+'th term of the AP- 29,35,41....'
List4=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],['59','69','65','55'],['74','75','85','54'],
       ['71','84','81','82'],['78','79','85','87'],['93','91','97','95'],['100','99','101','103'],['102','103','105','99'],
       ['117','113','109','111'],['117','109','127','107'],['133','123','103','97'],
       ['139','108','129','107'],['125','143','102','135']]
q7ans=[0,0,0,0,0,0,0,1,2,3,0,1,2,3,0,1,2,3]
answers.append(q7ans[r7])
def Check7():
    Check.configure(state=DISABLED)
    Next['state']=NORMAL
    global lbA1
    x=r.get()
    if x==q7ans[r7]:
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
        
#Question 8(Decimals)
lbA1=Label(text='')
list6=['8.2/2.4','98.8/49.9','6.5/5','90/41.5','42.5/8','55.8/27.9']
list7=[['3.41','4.41','5.44','3.31'],['4','2','6','5'],['2.3','1.43','1.3','2.54'],
       ['4.2','3.4','5.2','2.1'],['5.3','4.2','3.3','3.2'],['4','2','6','3']]
r4=randrange(0,6)
q8='Q8.Solve the following'+list6[r4]
q8ans=[0,1,2,3,0,1]
answers.append(q8ans[r4])
def Check8():
    global lbA1
    x=r.get()
    if x==q8ans[r4]:
        lbA1=Label(text='Your Answer is Correct.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    else:
        lbA1=Label(text='Your Answer is Wrong.',bg='orange',font=('Californian FB',30,'bold'))
        lbA1.pack()
    Check.configure(state=DISABLED)

def showresultmaths(scoremaths):
    if scoremaths>60:
        img=ImageTk.PhotoImage(Image.open('perfect.jpg'))
        label=Label(image=img)
        label.image=img
        label.pack()
        Excel=['You did an EXCELLENT work','You Got the PERFECT score','Its time to CELEBRATE your Perfect score.']
        er=randint(0,2)
        Excellent=Label(text=Excel[er],bg='orange',font=('Imprint MT Shadow',30,'bold'),justify='center')
        Excellent.pack()
    elif 30<scoremaths<80:
        imga=ImageTk.PhotoImage(Image.open('smiley.jpg'))
        label1=Label(image=imga,bg='orange')
        label1.image=imga
        label1.pack()
        ok=['You did a GOOD work.','You were quite close to the Perfect Score','You did a NICE job']
        okr=randint(0,2)
        OkOk=Label(text=ok[okr],bg='orange',font=('Imprint MT Shadow',30,'bold'),justify='center')
        OkOk.pack()
    else:
        imgae=ImageTk.PhotoImage(Image.open('mickey mouse.jpg'))
        label2=Label(image=imgae,bg='orange')
        label2.image=imgae
        label2.pack()
        tryh=['Try Harder Next Time.','Better Luck for next time','Brush up your Knowledge']
        rand=randint(0,2)
        harder=Label(text=tryh[rand],bg='orange',font=('Imprint MT Shadow',30,'bold'),justify='center')
        harder.pack()

    

def scoremaths():
    global userans,answers,M,time
    x=r.get()
    userans.append(x)
    time.destroy()
    global end
    end.destroy()
    A1.destroy()
    A2.destroy()
    A3.destroy()
    A4.destroy()
    Next.destroy()
    Check.destroy()
    Q.destroy()
    lbA1.destroy()
    
    M=0
    scoremaths=0
    for i in range(len(answers)):
        if answers[i]==userans[M]:
            scoremaths+=10
        M+=1
    lbSCM=Label(text='Your score is '+str(scoremaths),bg='orange',font=('Imprint MT Shadow',30,'bold'),justify='center')
    lbSCM.pack()
    showresultmaths(scoremaths)


def timeup():
    global time,end
    time=Label(text='Your time is up. Please press the END QUIZ button',bg='orange',font=('Californian FB',30,'bold'),wraplength=600)
    time.pack()
    Check.configure(state=DISABLED)
    Next.configure(state=DISABLED)
    end=Button(text='END QUIZ',bg='pink',width=20,height=1,font=('Arial',16,'bold'),command=scoremaths)
    end.pack()


def oneleft():
    global threeup
    threeup.destroy()
    nst=Label(text='')
    nst.after(55000,timeup)
    
def threeup():
    global threeup
    threeup=Label(text='You Have 1 mins left',bg='orange',font=('Californian FB',30,'bold'),wraplength=600)
    threeup.pack()
    threeup.after(5000,oneleft)

def twoleft():
    global twoup
    twoup.destroy()
    mst=Label(text='')
    mst.after(55000,threeup)
    
def twoup():
    global twoup
    twoup=Label(text='You Have 2 mins left',bg='orange',font=('Californian FB',30,'bold'),wraplength=600)
    twoup.pack()
    twoup.after(5000,twoleft)

def threeleft():
    global oneup
    oneup.destroy()
    lst=Label(text='')
    lst.after(55000,twoup)
    
def oneup():
    global oneup
    oneup=Label(text='You Have 3 mins left',bg='orange',font=('Californian FB',30,'bold'),wraplength=600)
    oneup.pack()
    oneup.after(5000,threeleft)

def selected7():
    x=r.get()
    userans.append(x)
    r.set(-1)
    lbA1.destroy()
    Q.config(text=q8)
    A1['text']=list7[r4][0]
    A2['text']=list7[r4][1]
    A3['text']=list7[r4][2]
    A4['text']=list7[r4][3]
    Check['state']=NORMAL
    Check.configure(command=Check8)
    Next.configure(state=DISABLED)
    global time
    time=Label(text='Please press the END QUIZ button.',bg='orange',font=('Californian FB',30,'bold'),wraplength=600)
    time.pack()
    global end
    end=Button(text='END QUIZ',bg='pink',width=20,height=1,font=('Arial',16,'bold'),command=scoremaths)
    end.pack()



def selected6():
    x=r.get()
    userans.append(x)
    r.set(-1)
    lbA1.destroy()
    Q.config(text=q7)
    A1['text']=List4[r7][0]
    A2['text']=List4[r7][1]
    A3['text']=List4[r7][2]
    A4['text']=List4[r7][3]
    Check['state']=NORMAL
    Next.configure(state=DISABLED)
    Check.configure(command=Check7)
    Next.configure(command=selected7)


def selected5():
    x=r.get()
    userans.append(x)
    r.set(-1)
    lbA1.destroy()
    Q.config(text=q6)
    A1['text']=xes[ri6q][ri6o][0]
    A2['text']=xes[ri6q][ri6o][1]
    A3['text']=xes[ri6q][ri6o][2]
    A4['text']=xes[ri6q][ri6o][3]
    Check['state']=NORMAL
    Next.configure(state=DISABLED)
    Check.configure(command=Check6)
    Next.configure(command=selected6)


def selected4():
    x=r.get()
    userans.append(x)
    r.set(-1)
    lbA1.destroy()
    Q.config(text=Q5)
    A1['text']=list9[r8][0]
    A2['text']=list9[r8][1]
    A3['text']=list9[r8][2]
    A4['text']=list9[r8][3]
    Check['state']=NORMAL
    Next.configure(state=DISABLED)
    Check.configure(command=Check5)
    Next.configure(command=selected5)


def selected3():
    x=r.get()
    userans.append(x)
    r.set(-1)
    lbA1.destroy()
    Q.config(text=Q4)
    A1['text']=options[ri4][0]
    A2['text']=options[ri4][1]
    A3['text']=options[ri4][2]
    A4['text']=options[ri4][3]
    Check['state']=NORMAL
    Next.configure(state=DISABLED)
    Check.configure(command=Check4)
    Next.configure(command=selected4)


def selected2():
    x=r.get()
    userans.append(x)
    r.set(-1)
    lbA1.destroy()
    Q.config(text=q3)
    A1['text']=list4[r3][0]
    A2['text']=list4[r3][1]
    A3['text']=list4[r3][2]
    A4['text']=list4[r3][3]
    Check['state']=NORMAL
    Next.configure(state=DISABLED)
    Check.configure(command=Check3)
    Next.configure(command=selected3)
    


def selected1():
    x=r.get()
    userans.append(x)
    r.set(-1)
    lbA1.destroy()
    Q.config(text=q2)
    Q.pack()
    A1['text']=List2[ri][0]
    A2['text']=List2[ri][1]
    A3['text']=List2[ri][2]
    A4['text']=List2[ri][3]
    Check['state']=NORMAL
    Next.configure(state=DISABLED)
    Check.configure(command=Check2)
    Next.configure(command=selected2)



def maths():
    root.destroy()
    global maths
    maths=Tk()
    maths.configure(bg='orange')
    maths.geometry('1000x1000')
    maths.title('MATHS QUIZ')
    maths.resizable(0,0)
    global Q
    Q=Label(text=q1,bg='orange',font=('Californian FB',30,'bold'),wraplength=600)
    Q.pack()
    global r,A1,A2,A3,A4,Next,Check
    r=IntVar()
    r.set(-1)
    A1=Radiobutton(padx=100,pady=10,text=list1[r1][0],height=1,width=20,value=0,variable=r,bg='yellow',font=('Bernard MT Condensed',16,'bold'))
    A1.pack()
    A2=Radiobutton(padx=100,pady=10,text=list1[r1][1],height=1,width=20,value=1,variable=r,bg='yellow',font=('Bernard MT Condensed',16,'bold'))
    A2.pack()
    A3=Radiobutton(padx=100,pady=10,text='None',height=1,width=20,value=2,variable=r,bg='yellow',font=('Bernard MT Condensed',16,'bold'))
    A3.pack()
    A4=Radiobutton(padx=100,pady=10,text='Both',height=1,width=20,value=3,variable=r,bg='yellow',font=('Bernard MT Condensed',16,'bold'))
    A4.pack()
    Check=Button(text='CHECK',bg='pink',width=20,height=1,font=('Arial',16,'bold'),command=Check1)
    Check.pack()
    Next=Button(text='NEXT',bg='pink',width=20,height=1,font=('Arial',16,'bold'),command=selected1)
    Next.pack()
    Next.configure(state=DISABLED)
    Q.after(60000,oneup)


#STARS
indexes=[]
starsus=[]
def showresult(score):
    if score>60:
        img=ImageTk.PhotoImage(Image.open('perfect.jpg'))
        label=Label(image=img)
        label.image=img
        label.pack()
        excel=['You did an EXCELLENT work','You Got the PERFECT score','Its time to CELEBRATE your Perfect score.']
        er=randint(0,2)
        excellent=Label(text=excel[er],bg='violet',font=('Imprint MT Shadow',30,'bold'),justify='center')
        excellent.pack()
    elif 30<score<80:
        imga=ImageTk.PhotoImage(Image.open('smiley.jpg'))
        label1=Label(image=imga)
        label1.image=imga
        label1.pack()
        ok=['You Did a GOOD work.','You were quite close to the Perfect Score','You did a NICE job']
        okr=randint(0,2)
        okok=Label(text=ok[okr],bg='violet',font=('Imprint MT Shadow',30,'bold'),justify='center')
        okok.pack()
    else:
        imgae=ImageTk.PhotoImage(Image.open('mickey mouse.jpg'))
        label2=Label(image=imgae)
        label2.image=imgae
        label2.pack()
        tryh=['Try Harder Next Time.','Better Luck for next time','Brush up your Knowledge']
        rand=randint(0,2)
        harder=Label(text=tryh[rand],bg='violet',font=('Imprint MT Shadow',30,'bold'),justify='center')
        harder.pack()
        
        
def score():
    SA1.destroy()
    SA2.destroy()
    SA3.destroy()
    SA4.destroy()
    ext.destroy()
    Cor.destroy()
    starsques.destroy()
    lbSA.destroy()
    global indexes,starsans,starsus
    x=0
    score=0
    for i in indexes:
        if starsans[i]==starsus[x]:
            score+=10
        x+=1
    lbSC=Label(text='Your score is '+str(score),bg='violet',font=('Imprint MT Shadow',30,'bold'),justify='center')
    lbSC.pack()
    showresult(score)
    

ques1=0
def correct():
    ext['state']=NORMAL
    global ques1,lbSA
    Cor.configure(state=DISABLED)
    st=r.get()
    CH=starsans[indexes[ques1]]
    if CH==st:
        lbSA=Label(text='Your answer is CORRECT',bg='violet',font=('Castellar',24,'bold'))
        lbSA.pack()
    else:
        lbSA=Label(text='Your answer is WRONG',bg='violet',font=('Castellar',24,'bold'))
        lbSA.pack()
    ques1+=1


def timup():
    global tim,end
    tim=Label(text='Your time is up. Please press the END QUIZ button',bg='violet',font=('Californian FB',30,'bold'),wraplength=600)
    tim.pack()
    Check.configure(state=DISABLED)
    Next.configure(state=DISABLED)
    end=Button(text='END QUIZ',bg='pink',width=20,height=1,font=('Arial',16,'bold'),command=score)
    end.pack()


def Oneleft():
    global Threeup
    Threeup.destroy()
    Nst=Label(text='')
    Nst.after(55000,timup)
    
def Threeup():
    global Threeup
    Threeup=Label(text='You Have 1 min left',bg='violet',font=('Californian FB',30,'bold'),wraplength=600)
    Threeup.pack()
    Threeup.after(5000,oneleft)

def Twoleft():
    global Twoup
    Twoup.destroy()
    Mst=Label(text='')
    Mst.after(55000,Threeup)
    
def Twoup():
    global Twoup
    Twoup=Label(text='You Have 2 mins left',bg='violet',font=('Californian FB',30,'bold'),wraplength=600)
    Twoup.pack()
    Twoup.after(5000,Twoleft)

def Threeleft():
    global Oneup
    Oneup.destroy()
    Lst=Label(text='')
    Lst.after(55000,Twoup)
    
def Oneup():
    global Oneup
    Oneup=Label(text='You Have 3 mins left',bg='violet',font=('Californian FB',30,'bold'),wraplength=600)
    Oneup.pack()
    Oneup.after(5000,Threeleft)
    
ques=1
def sel():
    lbSA.destroy()
    Cor["state"] = NORMAL
    st=r.get()    
    global starsus
    global ques
    starsus.append(st)
    if ques<8:
        r.set(-1)
        starsques.config(text='Q'+str(ques+1)+'.'+starsq[indexes[ques]])
        SA1['text']=starsops[indexes[ques]][0]
        SA2['text']=starsops[indexes[ques]][1]
        SA3['text']=starsops[indexes[ques]][2]
        SA4['text']=starsops[indexes[ques]][3]
        ques=ques+1
        ext.configure(state=DISABLED)
    else:
        score()
        
def stars():
    root.destroy()
    global indexes
    while len(indexes)<8:
        xy=randint(0,23)
        if xy in indexes:
            continue
        else:
            indexes.append(xy)
    stars=Tk()
    stars.configure(bg='violet')
    stars.geometry('1000x1200')
    stars.title('SKY QUIZ')
    stars.resizable(0,0)
    global starsq,starsops,starsans
    starsq=['Name the closest large spiral galaxy to our Milky Way Galaxy.',
            'The demon star(Algol) is a part of which constellation?',
            'Name the constellation whose shape is of a bull.',
            'Name the largest constellation in the night sky.',
            'How many stars are there in the big dipper?',
            'What is the other name of the little dipper constellation?',
            'Which was the first star to be named?',
            'Which Constellation is named after the wife of Perseus?',
            'Which constellation which contains two of the brightest stars in the night sky(Rigel and Betlguese)?',
            'Name the bightest star in the night sky.',
            "The air shaft of the King's Chamber in The Great Pyramid lead to Alnitak in which constellation",
            'Name the supermassive blackhole at the centre of our galaxy.',
            'Who in greek mythology is known for placing constellations in the sky?',
            'Which was the earliest named constellations in the sky?',
            'Which is the nearest Nebula to the Earth?',
            'Name the constellation whose biggest stars are Castor and Pollux.',
            'A star cluster of about 800 stars and 7 major stars which make a constellation',
            'What is the name of our galaxy?',
            'What is the other name of our moon?',
            'Name the asteroid belt that seperates Neptune and Pluto',
            'Which Planet is also known as the red planet?',
            'Which Planet cuts through the orbit of Neptune?',
            'Which is the nearest star to earth in the night sky?',
            'Which planet in the solar system has the highest number of moons?']
    starsops=[['a)Draco II','b)Andromeda','c)Hydrus I','Tucana III'],
              ['a)Perseus','b)Cassiopeia','c)Big Dipper','d)Orion'],
              ['a)Capricorn','b)Small Dipper','c)Leo','d)Taurus'],
              ['a)Hydra','b)Virgo','c)Ursa Major','d)Aries'],
              ['a)7','b)12','c)8','d)6'],
              ['a)Yurusa','b)Orsya Minora','c)Canis Minor','d)Ursa Minor'],
              ['a)Algol','b)Arctures','c)Rigel','d)Vega'],
              ['a)Cassiopeia','b)Hera','c)Andromeda','d)Amara'],
              ['a)Canis Major','b)Pleiades','c)Cancer','d)Orion'],
              ['a)Sirius A','b)North Star(Polaris)','c)Vega','d)Rigel'],
              ['a)Ursa Major','b)Orion','c)Scorpio','d)Cancer'],
              ['a)Powehi','b)Centaurus A','c)Sagittarius A','d)Fornax A'],
              ['a)Posiedon','b)Hera','c)Uranus','d)Zeus'],
              ['a)Taurus','b)Cancer','c)Orion','d)Pleiades'],
              ['a)Orion','b)Eagle','c)Helix','d)Mz3'],
              ['a)Virgo','b)Gemini','c)Canis','d)Aries'],
              ['a)Centaurus','b)Libra','c)Gemini','d)Pleiades'],
              ['a)Aakash Ganga','b)Andromeda','c)Cygnus','d)Pinwheel'],
              ['a)Ganymede','b)Callisto','c)Luna','d)Titan'],
              ['a)Kepler belt','b)Newton Belt','c)Gallilleo Belt','d)Kuiper Belt'],
              ['a)Venus','b)Mars','c)Mercury','d)Jupiter'],
              ['a)Uranus','b)Saturn','c)Pluto','d)Jupiter'],
              ['a)Proxima Centauri','b)Sun','c)Sirius A','d)Alnitak'],
              ['a)Neptune','b)Uranus','c)Saturn','d)Jupiter']]
    starsans=[1,0,3,0,2,3,1,2,3,0,1,2,3,0,2,1,3,0,2,3,1,2,0,2]
    global starsques,SA1,SA2,SA3,SA4,ext,Cor
    starsques=Label(stars,text='Q1.'+starsq[indexes[0]],bg='violet',font=('Californian FB',30,'bold'),justify='center',wraplength=600)
    starsques.pack()
    global r
    r=IntVar()
    r.set(-1)
    SA1=Radiobutton(padx=100,pady=10,text=starsops[indexes[0]][0],height=1,width=20,value=0,variable=r,bg='light green',font=('Californian FB',16,'bold'))
    SA1.pack()
    SA2=Radiobutton(padx=100,pady=10,text=starsops[indexes[0]][1],height=1,width=20,value=1,variable=r,bg='light green',font=('Californian FB',16,'bold'))
    SA2.pack()
    SA3=Radiobutton(padx=100,pady=10,text=starsops[indexes[0]][2],height=1,width=20,value=2,variable=r,bg='light green',font=('Californian FB',16,'bold'))
    SA3.pack()
    SA4=Radiobutton(padx=100,pady=10,text=starsops[indexes[0]][3],height=1,width=20,value=3,variable=r,bg='light green',font=('Californian FB',16,'bold'))
    SA4.pack()
    Cor=Button(text='CHECK',bg='pink',width=20,height=1,font=('Arial',16,'bold'),command=correct)
    Cor.pack()
    ext=Button(text='NEXT',bg='pink',width=20,height=1,font=('Arial',16,'bold'),command=sel)
    ext.pack()
    ext.configure(state=DISABLED)
    starsques.after(60000,Oneup)
              
def choice():
    l2=Label(text='You have a choice between two quizes. Choose your quiz wisely.The same rules apply to both of the quizes',wraplength=500,bg='sky blue',font=('Arial',16,'bold'))
    l2.grid(row=0,column=0,columnspan=2)
    b1=Button(text='Maths Quiz',width=25,command=maths,bg='pink',font=('Arial',16,'bold'))
    b1.grid(row=1, column=0)
    lbl=Label(text='You will get 8 questions and 4 minute to answer all questions.',wraplength=200,background='sky blue',font=('Times',18,'bold'))
    lbl.grid(row=2, column=0)
    b2=Button(text='Sky Quiz',width=25,command=stars,bg='pink',font=('Arial',16,'bold'))
    b2.grid(row=1, column=1)
    lbla=Label(text='You will get 8 questions and 3 minutes to nswer all questions.',wraplength=200,background='sky blue',font=('Times',18,'bold'))
    lbla.grid(row=2, column=1)
#Coding for the command when the button is clicked
def open1():
    l.destroy()
    l1.destroy()
    btn.destroy()
    choice()

img=ImageTk.PhotoImage(Image.open('star.jpg'))
l=Label(image=img)
l.pack()
l1=Label(text="THE STARNIGHT QUIZ",width=50,bg='sky blue',font=('Arial',16,'bold'))
l1.pack()
btn=Button(root, text="START",padx=50,pady=20,border=10,relief=RAISED,command=open1,bg="pink")
btn.pack()
root.mainloop()    

    




