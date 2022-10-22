from enum import Enum
from lib2to3.pgen2 import token
import re
import math
import webbrowser





class Analizador:
    def __init__(self, archivoimp):
        self.linea = 1
        self.columna = 0
        self.tmp_cadena = ""
        self.lista_cadena = []
        self.archivoimp=archivoimp
        self.EstadoActual = 0
        self.op=[]
        self.num=0
        global tokenlist
        tokenlist=[]
        global numtoken
        numtoken=[]
        global lexema
        lexema = []
        global controles
        controles=[]
        global idlist
        idlist=[]
        global tamañoletra 
        tamañoletra=[]
        global hola
        hola=""
        global errores 
        errores=[]

    def aumentarLinea(self):
        # _tmp = self.lista_cadena[self.linea]
        # #print(_tmp , " == ", self.tmp_cadena)
        # if _tmp == self.tmp_cadena:
            self.linea += 1
            self.tmp_cadena = ""
            self.columna = 0 

    def verificarToken(self, entrada:str, token:str):
        count = 0

        for i in range(0, len(token)):
            if count >= len(entrada):
                return {"result":None, "count":count}
            if entrada[i] != token[i]:
                return {"result":None, "count":count}
            count += 1

        nueva_cadena = ""
        count_1 = 0
        lista = entrada.split(token)
        for j in lista:
            if count_1 == len(lista) - 1:
                nueva_cadena += j
            elif count_1 > 0:
                nueva_cadena += j + token

            count_1 += 1

        self.tmp_cadena += token

        return {"result":nueva_cadena, "count":count}

    def quitar(self, entrada:str, token:str):
        nueva_cadena = ""
        count_1 = 0
        lista = entrada.split(token)
        for j in lista:
            if count_1 == len(lista) - 1:
                nueva_cadena += j
            elif count_1 > 0:
                nueva_cadena += j + token

            count_1 += 1
        return nueva_cadena


    def verificarID(self, entrada:str):
        count = 0
        llave = False
        alfabeto = ["A", "B", "C", "D", "E", "F", "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4","5","6","7","8","9", "_","(", ")",'"', ","]
        for i in entrada:
            llave = False
            for j in alfabeto:
                if i == j:
                    llave = True
                    break
            if llave == False:
                return {"result":None, "count":count}

            count += 1

        return {"result":True, "count":count}


    def comentariomultilinea(self, cadena : str):
        try:
            tmp = ""
            count = 0
            llave = False
            if cadena[0] == "/" and cadena[1] == "*":
                for i in cadena:
                    if llave:
                        tmp += i

                    if cadena[count - 1] == "*" and cadena[count] == "/":
                        llave = True
                    
                    count += 1
                print( self.linea, " | ", self.columna," | COMENTARIO",)
                self.columna += count
                self.aumentarLinea()
                return tmp
            return cadena
        except:
            return cadena


    def lecturaporEstados(self, cadena):
        cadena = self.comentariomultilinea(cadena)
        self.EstadoActual = "Q0"
        cont_numtoken=115
        cont_numtoken2=217
        cont_numvalor=250
        while cadena != "":

            if self.EstadoActual == "Q0":
                cadena = self.comentariomultilinea(cadena)
                token = "<"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "A"
                tokenlist.append("<")
                numtoken.append("101")
                lexema.append("<!--Controles")

            elif self.EstadoActual == "A":
                cadena = self.comentariomultilinea(cadena)
                token = "!"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "B"
                tokenlist.append("!")
                numtoken.append("102")
                lexema.append("<!--Controles")

            elif self.EstadoActual == "B":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "C"
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("<!--Controles")



            elif self.EstadoActual == "C":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "D"
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("<!--Controles")



            elif self.EstadoActual == "D":
                cadena = self.comentariomultilinea(cadena)
                token = "Controles"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "F"
                self.aumentarLinea()
                tokenlist.append("Controles")
                numtoken.append("104")
                lexema.append("<!--Controles")



            elif self.EstadoActual == "F":
                cadena = self.comentariomultilinea(cadena)
                token = "Controles"
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = ["Etiqueta", "Boton", "Check", "RadioBoton", "Texto", "AreaTexto", "Clave", "Contenedor"]
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            token = i
                            self.EstadoActual = "H"
                            tokenlist.append(token)
                            controles.append(token)
                            if token =="Etiqueta":
                                numtoken.append("105")
                            elif token =="Boton":
                                numtoken.append("106")
                            elif token =="Check":
                                numtoken.append("107")
                            elif token =="RadioBoton":
                                numtoken.append("108")
                            elif token =="Texto":
                                numtoken.append("109")
                            elif token =="AreaTexto":
                                numtoken.append("110")
                            elif token =="Clave":
                                numtoken.append("111")
                            elif token =="Contenedor":
                                numtoken.append("112")
                            break
                else:
                    self.EstadoActual = "I"
                    tokenlist.append("Controles")
                    numtoken.append("104")
                    lexema.append("Controles-->")

                
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break

                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]

                

            
            elif self.EstadoActual == "H":
                cadena = self.comentariomultilinea(cadena)
                tmp = cadena.split(";")
                id = tmp[0]
                res= self.verificarID(id)
                if res["result"] == None:
                    print("ERROR")
                    break
                cadena = self.quitar(cadena, id)
                print( self.linea, " | ", self.columna," | ",  id)
                self.columna += res["count"]
                self.EstadoActual = "J"
                tokenlist.append(id)
                numtoken.append(str(cont_numtoken))
                lexema.append(token+" "+id+";")
                lexema.append(token+" "+id+";")
                lexema.append(token+" "+id+";")
                idlist.append(id)
                cont_numtoken+=1


                


            elif self.EstadoActual=="J":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "F"
                #aumentar linea
                self.aumentarLinea()
                tokenlist.append(";")
                numtoken.append("113")


                
            
            elif self.EstadoActual == "I":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "K"
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("Controles-->")
                


            elif self.EstadoActual == "K":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "L"
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("Controles-->")
                
                

            elif self.EstadoActual == "L":
                cadena = self.comentariomultilinea(cadena)
                token = ">"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "M"
                #aumentar linea
                self.aumentarLinea()
                tokenlist.append(">")
                numtoken.append("114")
                lexema.append("Controles-->")



            if self.EstadoActual == "M":
                cadena = self.comentariomultilinea(cadena)
                token = "<"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "N"
                tokenlist.append("<")
                numtoken.append("201")
                lexema.append("<!--Propiedades")




            elif self.EstadoActual == "N":
                cadena = self.comentariomultilinea(cadena)
                token = "!"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "O"
                tokenlist.append("!")
                numtoken.append("202")
                lexema.append("<!--Propiedades")



            elif self.EstadoActual == "O":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "P"
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("<!--Propiedades")



            elif self.EstadoActual == "P":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "Q"
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("<!--Propiedades")



            elif self.EstadoActual == "Q":
                cadena = self.comentariomultilinea(cadena)
                token = "propiedades"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR Q")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "S"
                self.aumentarLinea()
                tokenlist.append("propiedades")
                numtoken.append("204")
                lexema.append("<!--propiedades")


            elif self.EstadoActual == "S":
                cadena = self.comentariomultilinea(cadena)
                token = "propiedades"
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = idlist
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            id = i
                            tokenlist.append(id)
                            numtoken.append(str(cont_numtoken2))
                            cont_numtoken2+=1
                            self.EstadoActual = "T"
                            print( self.linea, " | ", self.columna," | ",  id)
                            cadena = res["result"]
                            self.columna += res["count"]
                            break
                else:
                    self.EstadoActual = "Y"
                    tokenlist.append("propiedades")
                    numtoken.append("204")
                    lexema.append("propiedades-->")
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    self.columna += res["count"]
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break

                
                
                

                    


                
            elif self.EstadoActual == "T":
                cadena = self.comentariomultilinea(cadena)
                token = "."
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR T")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "U"
                tokenlist.append(".")
                numtoken.append("205")




            elif self.EstadoActual == "U":
                cadena = self.comentariomultilinea(cadena)
                tokens = ["setColorFondo", "setColorLetra", "setAlineacion", "setMarcada", "setTexto", "setGrupo", "setAncho", "setAlto"]   
                for i in tokens:
                    res = self.verificarToken(cadena, i)
                    if res["result"] != None:
                        token = i
                        self.EstadoActual = "H"
                        tokenlist.append(token)
                        controles.append(token)
                        if token =="setColorFondo":
                            numtoken.append("206")
                        elif token =="setColorLetra":
                            numtoken.append("207")
                        elif token =="setAlineacion":
                            numtoken.append("208")
                        elif token =="setMarcada":
                            numtoken.append("209")
                        elif token =="setTexto":
                            numtoken.append("210")
                        elif token =="setGrupo":
                            numtoken.append("211")
                        elif token =="setAncho":
                            numtoken.append("212")
                        elif token =="setAlto":
                            numtoken.append("213")
                        break
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR U")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "V"
                



            
            elif self.EstadoActual == "V":
                cadena = self.comentariomultilinea(cadena)
                tmp = cadena.split(";")
                id2 = tmp[0]
                res= self.verificarID(id2)
                if res["result"] == None:
                    print("ERROR V")
                    break
                cadena = self.quitar(cadena, id2)
                print( self.linea, " | ", self.columna," | ",  id2)
                self.columna += res["count"]
                self.EstadoActual = "W"
                tokenlist.append(id2)
                numtoken.append(str(cont_numvalor))
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                idlist.append(id2)
                cont_numvalor+=1


                


            elif self.EstadoActual=="W":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR W")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "S"
                #aumentar linea
                self.aumentarLinea()
                tokenlist.append(";")
                numtoken.append("214")


                
            
            elif self.EstadoActual == "Y":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR Y")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "Z"
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("Propiedades-->")
                


            elif self.EstadoActual == "Z":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR Z")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "AA"
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("Propiedades-->")
                
                

            elif self.EstadoActual == "AA":
                cadena = self.comentariomultilinea(cadena)
                token = ">"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR AA")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "BB"
                #aumentar linea
                self.aumentarLinea()
                tokenlist.append(">")
                numtoken.append("214")
                lexema.append("Propiedades-->")
    
            elif self.EstadoActual == "BB":
                cadena = self.comentariomultilinea(cadena)
                token = "<"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "CC"
                tokenlist.append("<")
                numtoken.append("301")
                lexema.append("<!--Colocacion")




            elif self.EstadoActual == "CC":
                cadena = self.comentariomultilinea(cadena)
                token = "!"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "DD"
                tokenlist.append("!")
                numtoken.append("302")
                lexema.append("<!--Colocacion")



            elif self.EstadoActual == "DD":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "EE"
                tokenlist.append("-")
                numtoken.append("303")
                lexema.append("<!--Colocacion")



            elif self.EstadoActual == "EE":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "FF"
                tokenlist.append("-")
                numtoken.append("303")
                lexema.append("<!--Colocacion")



            elif self.EstadoActual == "FF":
                cadena = self.comentariomultilinea(cadena)
                token = "Colocacion"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR FF")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "HH"
                self.aumentarLinea()
                tokenlist.append("Colocacion")
                numtoken.append("304")
                lexema.append("<!--Colocacion")


            elif self.EstadoActual == "HH":
                cadena = self.comentariomultilinea(cadena)
                token = "Colocacion"
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = idlist
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            id = i
                            tokenlist.append(id)
                            numtoken.append(str(cont_numtoken2))
                            cont_numtoken2+=1
                            self.EstadoActual = "II"
                            print( self.linea, " | ", self.columna," | ",  id)
                            cadena = res["result"]
                            self.columna += res["count"]
                            break
                else:
                    self.EstadoActual = "SS"
                    tokenlist.append("Colocacion")
                    numtoken.append("304")
                    lexema.append("Colocacion-->")
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    self.columna += res["count"]
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR HH")
                    break
                
                


                
            elif self.EstadoActual == "II":
                cadena = self.comentariomultilinea(cadena)
                token = "."
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR II")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "JJ"
                tokenlist.append(".")
                numtoken.append("305")




            elif self.EstadoActual == "JJ":
                cadena = self.comentariomultilinea(cadena)
                token = "setPosicion"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR JJ")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "KK"
                tokenlist.append("setPosicion")
                numtoken.append("306")
                



            
            elif self.EstadoActual == "KK":
                cadena = self.comentariomultilinea(cadena)
                tmp = cadena.split(";")
                id2 = tmp[0]
                res= self.verificarID(id2)
                if res["result"] == None:
                    print("ERROR KK")
                    break
                cadena = self.quitar(cadena, id2)
                print( self.linea, " | ", self.columna," | ",  id2)
                self.columna += res["count"]
                self.EstadoActual = "LL"
                tokenlist.append(id2)
                numtoken.append(str(cont_numvalor))
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                idlist.append(id2)
                cont_numvalor+=1


                


            elif self.EstadoActual=="LL":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR LL")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "MM"
                #aumentar linea
                self.aumentarLinea()
                tokenlist.append(";")
                numtoken.append("307")


            elif self.EstadoActual == "MM":
                cadena = self.comentariomultilinea(cadena)
                token = "Colocacion"
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = idlist
                    tokens.append("this")
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            id = i
                            tokenlist.append(id)
                            numtoken.append(str(cont_numtoken2))
                            cont_numtoken2+=1
                            self.EstadoActual = "NN"
                            print( self.linea, " | ", self.columna," | ",  id)
                            cadena = res["result"]
                            self.columna += res["count"]
                            break
                else:
                    self.EstadoActual = "SS"
                    tokenlist.append("Colocacion")
                    numtoken.append("304")
                    lexema.append("Colocacion-->")
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    self.columna += res["count"]
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR HH")
                    break
                
                


                
            elif self.EstadoActual == "NN":
                cadena = self.comentariomultilinea(cadena)
                token = "."
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR NN")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "OO"
                tokenlist.append(".")
                numtoken.append("305")




            elif self.EstadoActual == "OO":
                cadena = self.comentariomultilinea(cadena)
                token = "add"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR OO")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "PP"
                tokenlist.append("setPosicion")
                numtoken.append("306")
                



            
            elif self.EstadoActual == "PP":
                cadena = self.comentariomultilinea(cadena)
                tmp = cadena.split(";")
                id2 = tmp[0]
                res= self.verificarID(id2)
                if res["result"] == None:
                    print("ERROR PP")
                    break
                cadena = self.quitar(cadena, id2)
                print( self.linea, " | ", self.columna," | ",  id2)
                self.columna += res["count"]
                self.EstadoActual = "QQ"
                tokenlist.append(id2)
                numtoken.append(str(cont_numvalor))
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                idlist.append(id2)
                cont_numvalor+=1


                


            elif self.EstadoActual=="QQ":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR LL")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "HH"
                #aumentar linea
                self.aumentarLinea()
                tokenlist.append(";")
                numtoken.append("307")



                
            
            elif self.EstadoActual == "SS":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR SS")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "TT"
                tokenlist.append("-")
                numtoken.append("303")
                lexema.append("Colocacion-->")
                


            elif self.EstadoActual == "TT":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR TT")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "UU"
                tokenlist.append("-")
                numtoken.append("303")
                lexema.append("Colocacion-->")
                
                

            elif self.EstadoActual == "UU":
                cadena = self.comentariomultilinea(cadena)
                token = ">"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR UU")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                #aumentar linea
                self.aumentarLinea()
                tokenlist.append(">")
                numtoken.append("214")
                lexema.append("Colocacion-->")
                print("PROGRAMA LEÍDO CON EXITO")
                    

    def compile(self):
        # LEEMOS EL ARCHIVO DE ENTRADA
        archivo = open(self.archivoimp, "r", encoding="utf-8")
        contenido = archivo.readlines()
        archivo.close()

        # LIMPIAR MI ENTRADA
        nueva_cadena = ""
        lista_cadena = []

        for i in contenido:
            i = i.replace(' ', '') #QUITANDO ESPACIOS
            i = i.replace('\n', '') # QUITANDO SALTOS DE LINEA
            i= i.replace("(","")
            i= i.replace(")","")
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)

        # print("-------------------")
        # print(nueva_cadena)
        # print("-------------------")
        # print(lista_cadena)

        self.lista_cadena = lista_cadena
        self.lecturaporEstados(nueva_cadena)


    
    # def htmlanalizar():

    #     for j in contenido:
    #         if j!="":
    #             lista_cadena.append(j)

    #     r=0
        
    #     #hola=colortz[1]

    #     for x in range(len(lista_cadena)):

    #         if lista_cadena[x]=="<Texto>\n":
    #             nueva=lista_cadena[x+1]
    #             r=2
    #             while lista_cadena[x+r]!="</Texto>\n":
    #                 nueva+='<p style=color:'+hola+';font-size:'+tamañoletra[1]+'px;>'+lista_cadena[x+r]+"</p>\n"
    #                 r+=1

    #     titulo="Hola"
    #     r = open("Resultados_202109715.html","w+",encoding="utf-8")
    #     cadena="<!DOCTYPE html>\n"
    #     cadena+= "<html lang=\"es\">\n"
    #     cadena+= "  <head>\n"
    #     cadena+="       <meta charset=\"UTF-8\">\n"
    #     cadena+="       <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
    #     cadena+="       <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    #     cadena+="</head>\n"
    #     cadena += "    <body>\n"
    #     cadena += '         <h1 style=color:'+colortz[0]+';font-size:'+tamañoletra[0]+'px;>'+"<center>"+"<FONT FACE='arial'>"+titulo+"</center>"+"</FONT>"+"</h1>\n"
    #     cadena += '         <p style=color:'+colortz[1]+';font-size:'+tamañoletra[1]+'px;>'+"<FONT FACE='arial'>"+nueva+"</FONT>"+"</p>\n"
    #     for i in result:
    #         cadena +='          <p style="color:'+colortz[2]+';font-size:10px;">'+"<FONT FACE='arial'>"+str(i)+"</p>\n"
    #     cadena +="    <body>\n"
    #     cadena +="</html>\n"
    #     r.writelines(cadena)
    #     doc_analizador = 'Resultados_202109715.html'
    #     webbrowser.open_new(doc_analizador)
        
 


    def htmlerrores():
        lex="1"
        errorl="Error"
        errorc=""
        r = open("Errores_202109715.html","w+",encoding="utf-8")
        cadena="<!DOCTYPE html>\n"
        cadena+= "<html lang=\"es\">\n"
        cadena+= "  <head>\n"
        cadena+="       <meta charset=\"UTF-8\">\n"
        cadena+="       <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
        cadena+="       <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        cadena+="</head>\n"
        cadena += "    <body>\n"
        cadena+="<FONT FACE='arial'>"
        cadena += '''   <center>
                        <style>
                            .demo {
                                border:1px sólido #000000;
                                border-collapse:colapso;
                                padding:5px;
                            }
                            .demo th {
                                border:1px sólido #000000;
                                padding:5px;
                                background:#F0F0F0;
                            }
                            .demo td {
                                border:1px sólido #000000;
                                padding:5px;
                            }
                        </style>
                        <table class="demo">
                            <caption>Tabla de Errores</caption>
                            <thead>
                            <tr>
                                <th>No.</th>
                                <th>Tipo</th>
                                <th>Lexema</th>
                                <th>Fila</th>
                                <th>Columna</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                            <td>&nbsp;1</td>
                            <td>&nbsp;Error</td>'''
        cadena+="                        <td>&nbsp;"+lex+"</td>"
        cadena+="                        <td>&nbsp;"+errorl+"</td>"
        cadena+="                        <td>&nbsp;"+errorc+"</td>"
        cadena+='''                    </tr>
                            </tbody>
                        </table>
                        </center>'''
        cadena+="</FONT>"
        cadena +="    <body>\n"
        cadena +="</html>\n"
        r.writelines(cadena)
        doc_errores = 'Errores_202109715.html'
        webbrowser.open_new(doc_errores)


