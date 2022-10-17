##########---------pile--------#############


class pile :

    def __init__(self):
        self.p=[]

    def vide(self):
        return len(self.p)==0

    def empiler(self,x) :
        self.p.append(x)

    def depiler(self) :
        if  len(self.p)!= 0 :
          self.p.pop()

    def dernier(self) :
         if  len(self.p)!= 0 :
          return self.p[len(self.p)-1]
        
    def affiche_pile(self) :
        p1=self 
        print("----pile---------")
        while p1.p!=[] :
            print(p1.dernier())
            p1.depiler()
        print('---------------')