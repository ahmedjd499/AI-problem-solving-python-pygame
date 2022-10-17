from cmath import rect
import pygame as p
import tkinter as t
from file import file 
from pile import pile 
import time

r=t.Tk()

p.init()

win=p.display.set_mode((r.winfo_screenwidth()-100,r.winfo_screenheight()-100))


class caracter :
    def __init__(self,name,pic,pos):
        self.name=name
        self.pic=p.image.load(pic)
        self.pos=(pos[0],pos[1])
        self.side='left'
        self.selected=False
        

farmer=caracter('f','farmer.png',(200,600))
wolf=caracter('l','wolf3.png',(100,500))
chou=caracter('o','hay.png',(100,700))
goat=caracter('c','goat4.png',(100,600))

boat=caracter('boat','boat.png',(350,700))

global pos1in,pos2in,pos3in,pos4in,pos4fi,pos3fi,pos2fi,pos1fi

pos1in=(200,600)
pos2in=(100,500)
pos3in=(100,700)
pos4in=(100,600)

pos1fi=(800,150)
pos2fi=(900,150)
pos3fi=(930,250)
pos4fi=(1000,150)

#----------------for user mode -------------------
def show(win) : ###  afficher les cars fil win
   
    win.blit(farmer.pic,farmer.pos)
    win.blit(wolf.pic,wolf.pos)
    win.blit(chou.pic,chou.pos)
    win.blit(goat.pic,goat.pos)

def how_to_play(msg,x,y) : ## afficher msg fil win
    font=p.font.Font('freesansbold.ttf',22)
    text=font.render(msg,True,'black')
    rect=text.get_rect()
    rect.center=(x,y)
    win.blit(text,rect)
    
def select(win) :  ## select the car
        if p.key.get_pressed()[p.K_f]:
            farmer.selected=True 
            wolf.selected=False
            goat.selected=False
            chou.selected=False

        if p.key.get_pressed()[p.K_w] and wolf.side==farmer.side:
            wolf.selected=True
            goat.selected=False
            chou.selected=False
            
            
        if p.key.get_pressed()[p.K_g] and goat.side==farmer.side:
            wolf.selected=False
            goat.selected=True
            chou.selected=False
        if p.key.get_pressed()[p.K_h] and chou.side==farmer.side:
            wolf.selected=False
            goat.selected=False
            chou.selected=True
        if p.key.get_pressed()[p.K_ESCAPE]:
            wolf.selected=False
            goat.selected=False
            chou.selected=False
            farmer.selected=False

def show_select(win) : ## dessiner rect 3la selected car 
    if farmer.selected==True :
            if farmer.side=='left' :
                     p.draw.rect(win,'blue',(200,600,52,160),2)
            elif farmer.side=='right' :
                    p.draw.rect(win,'blue',(800,150,52,160),2)
    if wolf.selected==True :
        rect=wolf.pic.get_rect()
        if wolf.side=='left':
            rect.center=(137,550)
            p.draw.rect(win,'blue',(200,600,52,160),2)
        elif   wolf.side=='right':
            rect.center=(937,200)
            p.draw.rect(win,'blue',(800,150,52,160),2)
        p.draw.rect(win,'blue',rect,2)

    elif chou.selected==True :
        rect=chou.pic.get_rect()
        if chou.side=='left':
           rect.center=(138,725)
           p.draw.rect(win,'blue',(200,600,52,160),2)
        elif   chou.side=='right':
            rect.center=(967,275)
            p.draw.rect(win,'blue',(800,150,52,160),2)
        p.draw.rect(win,'blue',rect,2)

    elif goat.selected==True :
        rect=goat.pic.get_rect()
        if goat.side=='left':
           rect.center=(134,638)
           p.draw.rect(win,'blue',(200,600,52,160),2)
        elif   goat.side=='right':
            rect.center=(1034,188)
            p.draw.rect(win,'blue',(800,150,52,160),2)
        p.draw.rect(win,'blue',rect,2)

def action_user(enter) :

 
    if enter==True :
        
        if farmer.selected==True and goat.selected==False and wolf.selected==False and chou.selected==False:
            
            farmer.selected=False
            if farmer.side=='left' :
                    farmer.pos=pos1fi
                    farmer.side='right'
            elif farmer.side=='right' :
                    farmer.pos=pos1in
                    farmer.side='left'  

        elif wolf.selected==True and wolf.side==farmer.side :
            wolf.selected=False 
            farmer.selected=False
            if wolf.side=='left' :
                wolf.pos=pos2fi
                wolf.side='right'
                farmer.pos=pos1fi
                farmer.side='right'

            elif wolf.side=='right' :
                wolf.pos=pos2in
                wolf.side='left'
                farmer.pos=pos1in
                farmer.side='left'

        elif chou.selected==True and chou.side==farmer.side:
            chou.selected=False 
            farmer.selected=False
            if chou.side=='left' :
                chou.pos=pos3fi
                chou.side='right'
                farmer.pos=pos1fi
                farmer.side='right'
            elif chou.side=='right' :
                chou.pos=pos3in
                chou.side='left'
                farmer.pos=pos1in
                farmer.side='left'

        elif goat.selected==True and goat.side==farmer.side:
            goat.selected=False 
            farmer.selected=False
            if goat.side=='left' :
                goat.pos=pos4fi
                goat.side='right'
                farmer.pos=pos1fi
                farmer.side='right'
            elif goat.side=='right' :
                goat.pos=pos4in
                goat.side='left'
                farmer.pos=pos1in
                farmer.side='left' 



#-------------------for Ai mode -------------------------  

def etat():
    ch=""
    for c in [farmer,goat,wolf,chou] :
        if c.side=="left" :
            ch+=c.name
    ch+=";"
    for c in [farmer,goat,wolf,chou] :
        if c.side=="right" :
            ch+=c.name
    return ch

def admissible(etat) :
    if len(etat) !=5 :
        'flco;'
        return False
    for x in etat :
        if x!='c' and x!='l' and x!='o' and x!='f' and x!=';' :
             return False
    for x in etat :
        if etat.count(x)!=1 :    
             return False

    if etat.index('f')<etat.index(';'):
        if (etat.index('c')>etat.index(';') and  etat.index('l')>etat.index(';')) or (etat.index('c')>etat.index(';') and  etat.index('o')>etat.index(';'))  :
            return False
    if etat.index('f')>etat.index(';'):
        if (etat.index('c')<etat.index(';') and  etat.index('l')<etat.index(';')) or (etat.index('c')<etat.index(';') and  etat.index('o')<etat.index(';'))  :
            return False
    return True 

def action(etat_in,passager,sens) :
    etat=etat_in
    if passager==None :
        if sens=='gd' and etat.index('f')<etat.index(';') :
            etat=etat[:etat.index('f')]+etat[etat.index('f')+1:]
            etat=etat+'f'
            return etat
        elif  sens=='dg' and etat.index('f')>etat.index(';') :
            etat=etat[:etat.index('f')]+etat[etat.index('f')+1:]
            etat='f'+etat
            return etat
    elif sens=='gd'  and etat.index(passager)<etat.index(';') and etat.index('f')<etat.index(';') and len(passager)==1:
        etat=etat[:etat.index('f')]+etat[etat.index('f')+1:]
        etat=etat[:etat.index(passager)]+etat[etat.index(passager)+1:]
        etat=etat+passager+'f'
        return etat
    
    elif sens=='dg'  and etat.index(passager)>etat.index(';') and etat.index('f')>etat.index(';') and len(passager)==1:    
        etat=etat[:etat.index('f')]+etat[etat.index('f')+1:]
        etat=etat[:etat.index(passager)]+etat[etat.index(passager)+1:]
        etat=passager+'f'+etat
        return etat

def move(etat) :
    for c in [farmer,goat,wolf,chou] :
        if etat.index(c.name)<etat.index(';'):
            c.side='left'
        else :
            c.side='right'


    if farmer.side=='left' :
        farmer.pos=pos1in
    else :
        farmer.pos=pos1fi

    if wolf.side=='left' :
        wolf.pos=pos2in
    else :
        wolf.pos=pos2fi

    if chou.side=='left' :
        chou.pos=pos3in
    else :
        chou.pos=pos3fi

    if goat.side=='left' :
        goat.pos=pos4in
    else :
        goat.pos=pos4fi

    show(win)
     
def successeurs(etat) :
    succ=[]
    if etat.index('f')<etat.index(';') and admissible(action(etat,None,'gd')):
        succ.append(action(etat,None,'gd'))
    elif etat.index('f')>etat.index(';') and admissible(action(etat,None,'dg')) :
        succ.append(action(etat,None,'dg'))
    for x in 'clo':   
        if  etat.index('f')<etat.index(';') and etat.index(x)<etat.index(';') and admissible(action(etat,x,'gd')) :
            succ.append(action(etat,x,'gd'))
        elif etat.index('f')>etat.index(';') and etat.index(x)>etat.index(';') and admissible(action(etat,x,'dg')):
            succ.append(action(etat,x,'dg'))
            
    return(succ)         

def verif_etat(etat_re,list_etat_exp) :
   
   for i in list_etat_exp :
        test=0
        for x in etat_re:
           if   etat_re.index(x)< etat_re.index(';') and i.index(x) < i.index(';') :
               test+=1
           elif etat_re.index(x)> etat_re.index(';') and i.index(x) >i.index(';') :
                test+=1
       
        if test==4 :
                return 'ex'

   return 'de' 

def recherche_enprofendeur(etat) :

    list_explore=[]
    pl=pile()
    pl.empiler(etat)
    
    
    while pl.vide()==False and verif_etat(';clof',list_explore)=='de':
        
        win.blit(p.image.load('river2.png'),(0,0))
        win.blit(boat.pic,boat.pos)
        p.draw.rect(win,'red',(50,100,420,300),2)

        
        how_to_play('welcom....  : ',150,130)
        how_to_play('  this game works with AI',250,155)
        
       
        x=pl.dernier()
        list_explore.append(x)
        pl.depiler()

        move(x)
        for i in successeurs(x) :
           
            if verif_etat(i,list_explore)=='de' : 
              pl.empiler(i)
            
        
        p.display.update()
        time.sleep(2)

        
        for event in p.event.get() :
                if event.type==p.QUIT :
                    p.quit()
                    

        if  farmer.side=='right' and goat.side=='right' and wolf.side=='right' and chou.side=='right' :
                 win.blit(p.image.load('river2.png'),(0,0))
                 win.blit(boat.pic,boat.pos)
                 p.draw.rect(win,'red',(50,100,420,300),2)
                 how_to_play('       WINNNNNERRRR   ',250,200) 
                 show(win )
                 p.display.update()
                 time.sleep(3)
                 p.quit()
                 break
        p.display.update()

    time.sleep(5)


         
test=True
mode=None 
while test==True :
        win.blit(p.image.load('river2.png'),(0,0))
        win.blit(boat.pic,boat.pos)
        p.draw.rect(win,'red',(50,100,420,300),2)

        how_to_play('welcom.... press : ',150,130)
        how_to_play('   the black rect  : to choose user mode',250,155)
        how_to_play('   the white rect  : to choose AI       ',250,180)

        p.draw.rect(win,'black',(500,140,100,100))
        p.draw.rect(win,'white',(500,280,100,100))

        r1=p.Rect(500,140,100,100)
        r2=p.Rect(500,280,100,100)

        show(win)

        for event in p.event.get() :
         if event.type==p.MOUSEBUTTONDOWN and event.button==1 :

            mp=p.mouse.get_pos()
            ##(50,100)
            if p.Rect.collidepoint(r1,mp):
                mode='user'
                test=False
            elif  p.Rect.collidepoint(r2,mp):
                    mode='AI'
                    test=False

        p.display.update()

if mode=='user' :
    run=True
    enter=False
    while run:
        win.blit(p.image.load('river2.png'),(0,0)) ## background  

        win.blit(boat.pic,boat.pos) ## boat 

        p.draw.rect(win,'red',(50,100,420,300),2) ## rect ta3 lektiba 

        
        how_to_play('welcom.... press : ',150,130)
        how_to_play('   w : to select the wolt to be trasported',250,155)
        how_to_play('   g : to select the goat to be trasported',250,180)
        how_to_play('   h : to select the hay to be trasported ',250,205)
        how_to_play('   f : to select  the farmer                ',250,230)
        how_to_play('   SPACE : to start transportation        ',250,260)
        how_to_play('   ECHAP : to remove selection            ',250,290)

        show(win)

        select(win)

        show_select(win)

        if p.key.get_pressed()[p.K_SPACE]:
            enter=True
            action_user(enter)
        enter=False

        if not admissible(etat()) :
                 
                 win.blit(p.image.load('river2.png'),(0,0))
                 win.blit(boat.pic,boat.pos)
                 p.draw.rect(win,'red',(50,100,420,300),2)

                 how_to_play('   you loooooose.....try again ',250,200) 
                 show(win )
                 p.display.update()
                 time.sleep(3) 

                 farmer.__init__('f','farmer.png',(200,600))
                 wolf.__init__('l','wolf3.png',(100,500))
                 chou.__init__('o','hay.png',(100,700))
                 goat.__init__('c','goat4.png',(100,600))
                 boat.__init__('boat','boat.png',(350,700))

        if  farmer.side=='right' and goat.side=='right' and wolf.side=='right' and chou.side=='right' :
                 win.blit(p.image.load('river2.png'),(0,0))
                 win.blit(boat.pic,boat.pos)
                 p.draw.rect(win,'red',(50,100,420,300),2)
                 how_to_play('       WINNNNNERRRR   ',250,200) 
                 show(win )
                 p.display.update()
                 time.sleep(3)
                 p.quit()
                 break
                 
                 


        p.display.update()


        for event in p.event.get() :
                if event.type==p.QUIT :
                    p.quit()
                    run=False
elif mode=='AI' :
    recherche_enprofendeur(etat())      
