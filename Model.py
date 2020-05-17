import dataset


def create_db():
   db = dataset.connect('sqlite:///enquete.db')
   table = db.create_table('enquete_poo')
   table.insert(dict(title="outros"))
   print("BANCO CRIADO COM SUCESSO")

#create_db()

class Banco(object):
    def __init__(self,base=None,tabela=None):
        self.base = base 
        self.tabela = tabela
        self.db = dataset.connect('sqlite:///enquete.db')
        self.table = self.db.create_table('enquete_poo')

    def insert(self, query): 
        self.table.insert(dict(title=query))
        return " Obrigado por Votar ! "

    def list_itens(self,lista_sistemas):
        value = []
        for itens in lista_sistemas:
            query = 'SELECT COUNT(*) FROM enquete_poo where title = "%s"' % itens 
            valores = []
            for linhas in self.db.query(query):
                #print(linhas)
                valores.append(linhas["COUNT(*)"])
            value.append(valores)   
        return value

class Percent(object):
    def __init__(self):
        None
    def calcule(self):    
        model = Banco()
        dados =  model.list_itens(["Windows Server","Unix","Linux","Netware","Mac OS","Outro"])
        valores = {"Windows Server":dados[0][0],
                          "Unix":dados[1][0],
                          "Linux":dados[2][0],
                          "Netware":dados[3][0],
                          "Mac OS":dados[4][0],
                          "Outro":dados[5][0] }
        total = sum(valores.values())
        result = {
                     "Windows Server": (dados[0][0] * 100) / total,
                      "Unix":(dados[1][0] * 100) / total,
                      "Linux":(dados[2][0] * 100) / total,
                      "Netware":(dados[3][0] * 100) / total,
                      "Mac OS":(dados[4][0] * 100) / total,
                      "Outro":(dados[5][0] * 100) / total}
        return result                  
