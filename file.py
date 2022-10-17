##########---------file--------#############


class file :

    def __init__(self):
        self.p=[]

    def vide(self):
        return len(self.p)==0

    def emfiler(self,x) :
        self.p=[x]+self.p

    def defiler(self) :
        assert self.p!=[]
        self.p.pop()

    def premier(self) :
        return self.p[0]
 
    def premier(self) :
        return self.p[len(self.p)-1]   

    def affiche_file(self) :
        p1=self
        print("----file---------")
        while p1.p!=[] :
            print(p1.dernier())
            p1.defiler()
        print('---------------')