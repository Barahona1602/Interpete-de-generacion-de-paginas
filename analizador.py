from enum import Enum
from lib2to3.pgen2 import token
import re
import math
import webbrowser
from xml.dom.pulldom import PROCESSING_INSTRUCTION





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
        idlist=["this"]
        global errores 
        errores=[]
        global tokenlex
        tokenlex=[]
        global controles_list
        controles_list=[]
        global propiedades_list
        propiedades_list=[]
        global colocacion_list
        colocacion_list=[]

        



    def aumentarLinea(self):
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
        alfabeto = ["A", "B", "C", "D", "E", "F", "G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z", "a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4","5","6","7","8","9", "_","(", ")",'"', ","]
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
        global tipo_error
        tipo_error=""
        global linea_error
        linea_error=""
        global columna_error
        columna_error=""
        global token_error
        token_error=""
        global desc_error
        desc_error=""
        while cadena != "":

            if self.EstadoActual == "Q0":
                cadena = self.comentariomultilinea(cadena)
                token = "<"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "A"
                tokenlex.append("Apertura")
                tokenlist.append("<")
                numtoken.append("101")
                lexema.append("<!--Controles")

            elif self.EstadoActual == "A":
                cadena = self.comentariomultilinea(cadena)
                token = "!"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "B"
                tokenlex.append("Admiración")
                tokenlist.append("!")
                numtoken.append("102")
                lexema.append("<!--Controles")

            elif self.EstadoActual == "B":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "C"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("<!--Controles")



            elif self.EstadoActual == "C":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "D"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("<!--Controles")



            elif self.EstadoActual == "D":
                cadena = self.comentariomultilinea(cadena)
                token = "Controles"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "F"
                self.aumentarLinea()
                tokenlex.append("Controles")
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
                            tmp_controles=[]
                            tokenlex.append("Tipo")
                            tokenlist.append(token)
                            controles.append(token)
                            tmp_controles.append(token)
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
                    tokenlex.append("Controles")
                    tokenlist.append("Controles")
                    numtoken.append("104")
                    lexema.append("Controles-->")

                
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
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
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                cadena = self.quitar(cadena, id)
                print( self.linea, " | ", self.columna," | ",  id)
                self.columna += res["count"]
                self.EstadoActual = "J"
                tokenlex.append("ID")
                tokenlist.append(id)
                tmp_controles.append(id)
                numtoken.append(str(cont_numtoken))
                lexema.append(token+" "+id+";")
                lexema.append(token+" "+id+";")
                lexema.append(token+" "+id+";")
                idlist.append(id)
                cont_numtoken+=1
                controles_list.append(tmp_controles)


                


            elif self.EstadoActual=="J":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "F"
                #aumentar linea
                self.aumentarLinea()
                tokenlex.append("Punto y coma")
                tokenlist.append(";")
                numtoken.append("113")


                
            
            elif self.EstadoActual == "I":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "K"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("Controles-->")
                


            elif self.EstadoActual == "K":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "L"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("103")
                lexema.append("Controles-->")
                
                

            elif self.EstadoActual == "L":
                cadena = self.comentariomultilinea(cadena)
                token = ">"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "M"
                #aumentar linea
                self.aumentarLinea()
                tokenlex.append("Cierre")
                tokenlist.append(">")
                numtoken.append("114")
                lexema.append("Controles-->")



            if self.EstadoActual == "M":
                cadena = self.comentariomultilinea(cadena)
                token = "<"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "N"
                tokenlex.append("Apertura")
                tokenlist.append("<")
                numtoken.append("201")
                lexema.append("<!--Propiedades")




            elif self.EstadoActual == "N":
                cadena = self.comentariomultilinea(cadena)
                token = "!"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "O"
                tokenlex.append("Admiración")
                tokenlist.append("!")
                numtoken.append("202")
                lexema.append("<!--Propiedades")



            elif self.EstadoActual == "O":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "P"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("<!--Propiedades")



            elif self.EstadoActual == "P":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "Q"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("<!--Propiedades")



            elif self.EstadoActual == "Q":
                cadena = self.comentariomultilinea(cadena)
                token = "propiedades"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR Q")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "S"
                self.aumentarLinea()
                tokenlex.append("Propiedades")
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
                            tmp_propiedades=[]
                            id = i
                            tmp_propiedades.append(id)
                            tokenlex.append("ID")
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
                    tokenlex.append("Propiedades")
                    tokenlist.append("propiedades")
                    numtoken.append("204")
                    lexema.append("propiedades-->")
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    self.columna += res["count"]
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break

                
                
                

                    


                
            elif self.EstadoActual == "T":
                cadena = self.comentariomultilinea(cadena)
                token = "."
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR T")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "U"
                tokenlex.append("Punto")
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
                        tokenlex.append("Set")
                        tmp_propiedades.append(token)
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
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
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
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR V")
                    break
                cadena = self.quitar(cadena, id2)
                print( self.linea, " | ", self.columna," | ",  id2)
                self.columna += res["count"]
                self.EstadoActual = "W"
                tokenlex.append("Valor")
                tokenlist.append(id2)
                numtoken.append(str(cont_numvalor))
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                tmp_propiedades.append(id2)
                propiedades_list.append(tmp_propiedades)
                cont_numvalor+=1


                


            elif self.EstadoActual=="W":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR W")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "S"
                #aumentar linea
                self.aumentarLinea()
                tokenlex.append("Punto y coma")
                tokenlist.append(";")
                numtoken.append("214")


                
            
            elif self.EstadoActual == "Y":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR Y")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "Z"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("propiedades-->")
                


            elif self.EstadoActual == "Z":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR Z")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "AA"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("203")
                lexema.append("propiedades-->")
                
                

            elif self.EstadoActual == "AA":
                cadena = self.comentariomultilinea(cadena)
                token = ">"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR AA")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "BB"
                #aumentar linea
                self.aumentarLinea()
                tokenlex.append("Cierre")
                tokenlist.append(">")
                numtoken.append("214")
                lexema.append("propiedades-->")
    
            elif self.EstadoActual == "BB":
                cadena = self.comentariomultilinea(cadena)
                token = "<"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "CC"
                tokenlex.append("Apertura")
                tokenlist.append("<")
                numtoken.append("301")
                lexema.append("<!--Colocacion")




            elif self.EstadoActual == "CC":
                cadena = self.comentariomultilinea(cadena)
                token = "!"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "DD"
                tokenlex.append("Admiración")
                tokenlist.append("!")
                numtoken.append("302")
                lexema.append("<!--Colocacion")



            elif self.EstadoActual == "DD":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "EE"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("303")
                lexema.append("<!--Colocacion")



            elif self.EstadoActual == "EE":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "FF"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("303")
                lexema.append("<!--Colocacion")



            elif self.EstadoActual == "FF":
                cadena = self.comentariomultilinea(cadena)
                token = "Colocacion"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR FF")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "HH"
                self.aumentarLinea()
                tokenlex.append("Colocación")
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
                            tmp_colocacion=[]
                            id = i
                            tokenlex.append("ID")
                            tokenlist.append(id)
                            tmp_colocacion.append(id)
                            numtoken.append(str(cont_numtoken2))

                            cont_numtoken2+=1
                            self.EstadoActual = "II"
                            print( self.linea, " | ", self.columna," | ",  id)
                            cadena = res["result"]
                            self.columna += res["count"]
                            break
                else:
                    self.EstadoActual = "SS"
                    tokenlex.append("Colocación")
                    tokenlist.append("Colocacion")
                    numtoken.append("304")
                    lexema.append("Colocacion-->")
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    self.columna += res["count"]
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR HH")
                    break
                
                


                
            elif self.EstadoActual == "II":
                cadena = self.comentariomultilinea(cadena)
                token = "."
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR II")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "JJ"
                tokenlex.append("Punto")
                tokenlist.append(".")
                numtoken.append("305")




            elif self.EstadoActual == "JJ":
                cadena = self.comentariomultilinea(cadena)
                token = "setPosicion"
                res = self.verificarToken(cadena, token)
                if res["result"] == None:
                    token="add"
                    res = self.verificarToken(cadena, token)
                    if res["result"] != None:
                        id = token
                        self.EstadoActual = "PP"
                        tokenlex.append("Add")
                        tokenlist.append("add")
                        tmp_colocacion.append(token)
                        print( self.linea, " | ", self.columna," | ",  id)
                        cadena = res["result"]
                        self.columna += res["count"]
                else:
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    tmp_colocacion.append(token)
                    self.columna += res["count"]
                    self.EstadoActual = "KK"
                    tokenlex.append("Set")
                    tokenlist.append("setPosicion")
                    numtoken.append("306")
                        


                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR JJ")
                    break
                
                



            
            elif self.EstadoActual == "KK":
                cadena = self.comentariomultilinea(cadena)
                tmp = cadena.split(";")
                id2 = tmp[0]
                res= self.verificarID(id2)
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR KK")
                    break
                cadena = self.quitar(cadena, id2)
                print( self.linea, " | ", self.columna," | ",  id2)
                self.columna += res["count"]
                self.EstadoActual = "LL"
                tokenlex.append("Valor")
                tokenlist.append(id2)
                numtoken.append(str(cont_numvalor))
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                tmp_colocacion.append(id2)
                colocacion_list.append(tmp_colocacion)
                cont_numvalor+=1


                


            elif self.EstadoActual=="LL":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR LL")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "MM"
                #aumentar linea
                self.aumentarLinea()
                tokenlex.append("Punto y Coma")
                tokenlist.append(";")
                numtoken.append("307")




            elif self.EstadoActual == "MM":
                cadena = self.comentariomultilinea(cadena)
                token = "Colocacion"
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = idlist
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            id = i
                            tokenlex.append("ID")
                            tokenlist.append(id)
                            numtoken.append(str(cont_numtoken2))
                            tmp_colocacion=[]
                            tmp_colocacion.append(id)
                            cont_numtoken2+=1
                            self.EstadoActual = "NN"
                            print( self.linea, " | ", self.columna," | ",  id)
                            cadena = res["result"]
                            self.columna += res["count"]
                            break
                else:
                    self.EstadoActual = "SS"
                    tokenlex.append("Colocación")
                    tokenlist.append("Colocacion")
                    numtoken.append("304")
                    lexema.append("Colocacion-->")
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    self.columna += res["count"]
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR HH")
                    break
                
                


                
            elif self.EstadoActual == "NN":
                cadena = self.comentariomultilinea(cadena)
                token = "."
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR NN")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "JJ"
                tokenlex.append("Punto")
                tokenlist.append(".")
                numtoken.append("305")


                

            elif self.EstadoActual == "OO":
                cadena = self.comentariomultilinea(cadena)
                token = "add" 
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = idlist
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            id = i
                            tmp_colocacion=[]
                            tokenlex.append("ID")
                            tokenlist.append(id)
                            tmp_colocacion.append(id)
                            numtoken.append(str(cont_numtoken2))
                            cont_numtoken2+=1
                            self.EstadoActual = "II"
                            print( self.linea, " | ", self.columna," | ",  id)
                            cadena = res["result"]
                            self.columna += res["count"]
                            break
                else:
                    print( self.linea, " | ", self.columna," | ",  token)
                    cadena = res["result"]
                    self.columna += res["count"]
                    tmp_colocacion.append(token)
                    self.EstadoActual = "PP"
                    tokenlex.append("Set")
                    tokenlist.append("setPosicion")
                    numtoken.append("306")
                
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    token="Colocacion"
                    res = self.verificarToken(cadena, token)
                    if res["result"] != None:
                        self.EstadoActual="HH"
                    else:
                        tipo_error="Léxico"
                        linea_error=str(self.linea)
                        columna_error=str(self.columna)
                        token_error=str(token)
                        desc_error="Se esperaba "+token+" pero no se obtuvo"
                        print("ERROR OO")
                    



            
            elif self.EstadoActual == "PP":
                cadena = self.comentariomultilinea(cadena)
                tmp = cadena.split(";")
                id2 = tmp[0]
                res= self.verificarID(id2)
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(";")
                    desc_error="Se esperaba ; pero no se obtuvo"
                    print("ERROR PP")
                    break
                cadena = self.quitar(cadena, id2)
                print( self.linea, " | ", self.columna," | ",  id2)
                self.columna += res["count"]
                self.EstadoActual = "QQ"
                tokenlex.append("Valor")
                tokenlist.append(id2)
                numtoken.append(str(cont_numvalor))
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                lexema.append(id+"."+token+id2+";")
                tmp_colocacion.append(id2)
                colocacion_list.append(tmp_colocacion)
                cont_numvalor+=1


                


            elif self.EstadoActual=="QQ":
                cadena = self.comentariomultilinea(cadena)
                token = ";"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR QQ")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "OO"
                #aumentar linea
                self.aumentarLinea()
                tokenlex.append("Punto y Coma")
                tokenlist.append(";")
                numtoken.append("307")



                
            
            elif self.EstadoActual == "SS":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR SS")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "TT"
                tokenlex.append("Guión")
                tokenlist.append("-")
                numtoken.append("303")
                lexema.append("Colocacion-->")
                


            elif self.EstadoActual == "TT":
                cadena = self.comentariomultilinea(cadena)
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR TT")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "UU"
                tokenlist.append("-")
                tokenlex.append("Guión")
                numtoken.append("303")
                lexema.append("Colocacion-->")
                
                

            elif self.EstadoActual == "UU":
                cadena = self.comentariomultilinea(cadena)
                token = ">"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    tipo_error="Léxico"
                    linea_error=str(self.linea)
                    columna_error=str(self.columna)
                    token_error=str(token)
                    desc_error="Se esperaba "+token+" pero no se obtuvo"
                    print("ERROR UU")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                #aumentar linea
                self.aumentarLinea()
                tokenlex.append("Cierre")
                tokenlist.append(">")
                numtoken.append("214")
                lexema.append("Colocacion-->")
                tipo_error=""
                linea_error=""
                columna_error=""
                token_error=""
                desc_error=""
                print("PROGRAMA LEÍDO CON EXITO")
                # print(propiedades_list)
                # print(controles_list)
                # for i in colocacion_list:
                #     print(i)
                
                    

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
            i= i.replace('"',"")
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)

        # print("-------------------")
        # print(nueva_cadena)
        # print("-------------------")
        # print(lista_cadena)

        self.lista_cadena = lista_cadena
        self.lecturaporEstados(nueva_cadena)


    

    def htmlanalizar():
        controles_html=[]
        contenedor_lista=[]
        for i in controles_list:
            if i[0]=="Contenedor":
                print("Contenedor encontrado con id"+i[1])
                contenedor_lista.append(i[1])

            elif i[0]=="Etiqueta":
                for j in propiedades_list:
                    if j[0]==i[1] and j[1]=="setTexto":
                        tmp_html=[]
                        tmp_etiqueta=('<label id="'+i[1]+'">'+j[2]+'</label>')
                        tmp_html.append(i[1])
                        tmp_html.append(tmp_etiqueta)
                        controles_html.append(tmp_html)
                        
            
            elif i[0]=="Boton":
                tmp_alineacion="left"
                tmp_texto=""
                for j in propiedades_list:
                    tmp_html=[]
                    tmp_botones=[]
                    if j[0]==i[1]:
                        if j[1]=="setTexto":
                            tmp_texto=j[2]
                            tmp_botones.append(tmp_texto)

                    if j[0]==i[1] and j[1]=="setAlineacion":
                        if j[2]=="Centro":    
                            tmp_alineacion="center"
                        elif j[2]=="Izquierdo":
                            tmp_alineacion="left"
                        elif j[2]=="Derecho":
                            tmp_alineacion="right"

                tmp_boton=('<input type="submit" id="'+i[1]+'" value="'+tmp_texto+'" style="text-align:'+tmp_alineacion+'"/>')
                tmp_html.append(i[1])
                tmp_html.append(tmp_boton)
                controles_html.append(tmp_html)
            
            


            elif i[0]=="Check":
                tmp_texto=""
                for j in propiedades_list:
                    tmp_html=[]
                    tmp_check=[]
                    if j[0]==i[1]:
                        if j[1]=="setTexto":
                            tmp_texto=j[2]
                            tmp_check.append(tmp_texto)

                    if j[0]==i[1] and j[1]=="setMarcada":
                        if j[2]=="true":    
                            tmp_marca="checked"
                        else:
                            tmp_marca=""

                tmp_check=('<input type="checkbox" id="'+i[1]+'" '+tmp_marca+'/>'+tmp_texto)
                tmp_html.append(i[1])
                tmp_html.append(tmp_check)
                controles_html.append(tmp_html)

            elif i[0]=="RadioBoton":
                tmp_texto=""
                for j in propiedades_list:
                    tmp_html=[]
                    tmp_radio=[]

                    if j[0]==i[1]:
                        if j[1]=="setTexto":
                            tmp_texto=j[2]
                            tmp_radio.append(tmp_texto)

                    if j[0]==i[1]:
                        if j[1]=="setGrupo":
                            tmp_grupo=j[2]
                            tmp_radio.append(tmp_grupo)

                    if j[0]==i[1] and j[1]=="setMarcada":
                        if j[2]=="true":    
                            tmp_marca="checked"
                        else:
                            tmp_marca=""

                tmp_radio=('<input type="radio" name='+tmp_grupo+ ' id="'+i[1]+'" '+tmp_marca+'/>'+tmp_texto)
                tmp_html.append(i[1])
                tmp_html.append(tmp_radio)
                controles_html.append(tmp_html)

            elif i[0]=="Texto":
                tmp_alineacion="left"
                tmp_texto=""
                for j in propiedades_list:
                    tmp_html=[]
                    
                    if j[0]==i[1]:
                        if j[1]=="setTexto":
                            tmp_texto=j[2]
                            

                    if j[0]==i[1] and j[1]=="setAlineacion":
                        if j[2]=="Centro":    
                            tmp_alineacion="center"
                        elif j[2]=="Izquierdo":
                            tmp_alineacion="left"
                        elif j[2]=="Derecho":
                            tmp_alineacion="right"

                tmp_text=('<input type="text" id="'+i[1]+'" value="'+tmp_texto+'" style="text-align:'+tmp_alineacion+'"/>')
                tmp_html.append(i[1])
                tmp_html.append(tmp_text)
                controles_html.append(tmp_html)

            elif i[0]=="AreaTexto":
                for j in propiedades_list:
                    if j[0]==i[1] and j[1]=="setTexto":
                        tmp_html=[]
                        tmp_etiqueta=('<TEXTAREA id="'+i[1]+'">'+j[2]+'</TEXTAREA>')
                        tmp_html.append(i[1])
                        tmp_html.append(tmp_etiqueta)
                        controles_html.append(tmp_html)

            elif i[0]=="Clave":
                tmp_alineacion="left"
                tmp_texto=""
                for j in propiedades_list:
                    tmp_html=[]
                    
                    if j[0]==i[1]:
                        if j[1]=="setTexto":
                            tmp_texto=j[2]
        

                    if j[0]==i[1] and j[1]=="setAlineacion":
                        if j[2]=="Centro":    
                            tmp_alineacion="center"
                        elif j[2]=="Izquierdo":
                            tmp_alineacion="left"
                        elif j[2]=="Derecho":
                            tmp_alineacion="right"

                tmp_clave=('<input type="password" id="'+i[1]+'" value="'+tmp_texto+'" style="text-align:'+tmp_alineacion+'"/>')
                tmp_html.append(i[1])
                tmp_html.append(tmp_clave)
                controles_html.append(tmp_html)


        cadena=""
        listaFinal=[]
        for i in controles_list:
            if i[0]=="Contenedor":
                list_tmp=[]
                #cadena+='<div id="'+i[1]+'>'
                for j in colocacion_list:
                    if j[1]=="add" and i[1]==j[0]:
                        
                        for k in controles_html:
                            tmp_colocacion=[]
                            
                            if j[2]==k[0]:
                                cadena2=k[1]
                                tmp_colocacion.append(cadena2)
                                cadena+=cadena2
                #cadena+="</div>"
                list_tmp.append(i[1])
                list_tmp.append('<div id="'+i[1]+'>')
                list_tmp.append(cadena)
                list_tmp.append("</div>")
                listaFinal.append(list_tmp)

                            
                            # for p in tmp_colocacion:
                            #     cadena+=p

        # j = [this, add, contenedor1]
        # j = [contenedor1, add, contenedor2]
        # i = [contenedor1, div, lexema, div]
        # i = [contenedor2, div, lexema, div]
          
        # for i in listaFinal:   
        #     print("------------------------------")
        #     print(i)
        #     for j in colocacion_list:
        #         if i[0]==j[2] and j[1]=="add":
                    


        # cadena=[]
        # cadena2=""
        # i = contenedor1
        # j = [this, add, contenedor1]
        # j = [contenedor1, add, contenedor2]
        # k = [contenedor1, lexema]
        # k = [contenedor2, lexema]
        # j[1] =
        # for i in contenedor_lista:
        #     for j in colocacion_list:
        #         for k in listaFinal:
        #             if "this"==j[0]:
        #                     if i==k[0]:
        #                         print(j)
        #                         print(i)
        #                         cadena.append('<div id="'+i+'>')
        #                         cadena.append(k[1])
        #                         break
                # if i ==j[0]:
                #     for k in listaFinal:
                #         if j[2]==k[0]:
                #             cadena2+='<div id="'+j[2]+'>'
                #             cadena2+=(k[1])
                #             if 
                #             cadena2+="</div>"
                #             cadena.append(cadena2)
        # for i in cadena:
        #     print(i)                   
        # for i in controles_html:
        #     print(i[1])


        r = open("archivo.html","w+",encoding="utf-8")
        cadena="<!DOCTYPE html>\n"
        cadena+= "<html lang=\"es\">\n"
        cadena+= "  <head>\n"
        cadena+='<link href="prueba.css" rel="stylesheet"'
        cadena+= ' type="text/css" />'
        # cadena+="       <meta charset=\"UTF-8\">\n"
        # cadena+="       <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
        # cadena+="       <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        cadena+="</head>\n"
        cadena += "    <body>\n"
        for i in controles_list:
            if i[0]=="Contenedor":
                cadena+=('<div id="'+i[1]+'">')
                for j in colocacion_list:
                    if j[1]=="add" and i[1]==j[0]:
                        
                        for k in controles_html:
                            tmp_colocacion=[]
                            
                            if j[2]==k[0]:
                                cadena2=k[1]
                                tmp_colocacion.append(cadena2)
                                cadena+=(cadena2)
                cadena+=("</div>")
        cadena +="    </body>\n"
        cadena +="</html>\n"
        r.writelines(cadena)
        doc_analizador = 'archivo.html'
        webbrowser.open_new(doc_analizador)
        
    def css():
        r = open("prueba.css","w+",encoding="utf-8")
        cadena=""
        css_list=[] 
        for i in controles_list:
            setColorFondo=""
            setPosicion=""
            setAncho=""
            setAlto=""
            setColorLetra=""
            setTamañoLetra=""
            if i[0]=="Etiqueta":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')

                

            
            elif i[0]=="Boton":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')


            elif i[0]=="Check":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')

            elif i[0]=="RadioBoton":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')

            elif i[0]=="Texto":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')

            elif i[0]=="AreaTexto":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')

            elif i[0]=="Clave":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')

            elif i[0]=="Contenedor":
                for j in colocacion_list:
                    if j[1]=="setPosicion" and i[1]==j[0]:
                        tmp_posicion=j[2]
                        posicion = tmp_posicion.split(",")
                        x = posicion[0]
                        y = posicion[1]
                        setPosicion=('\n position:absolute; \n left: '+x+'px; \n top:'+y+'px; \n')
                for k in propiedades_list:
                    if k[1]=="setAncho" and i[1]==k[0]:
                        setAncho = ('\n width : '+k[2]+'px;')
                    if k[1]=="setAlto" and i[1]==k[0]:
                        setAlto = ('\n height : '+k[2]+'px;')
                    if k[1]=="setColorFondo" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorFondo = ('\n background-color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    if k[1]=="setColorLetra" and i[1]==k[0]:
                        tmp_bgcolor=k[2]
                        bgcolor = tmp_bgcolor.split(",")
                        bg1 = bgcolor[0]
                        bg2 = bgcolor[1]
                        bg3 = bgcolor[2]
                        setColorLetra = ('\n color: rgb'+'('+bg1+','+bg2+','+bg3+');')
                    setTamañoLetra=('\n font-size: 12px;')
                    

                
                
                css_list.append('#'+i[1]+'{'+setPosicion+ setAncho+setAlto+setColorFondo+setColorLetra+setTamañoLetra+'\n}')

        for l in css_list:
            cadena+=l 

        r.writelines(cadena)
        doc_css = 'prueba.css'
        webbrowser.open_new(doc_css)



 


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
                                <th>Tipo</th>
                                <th>Línea</th>
                                <th>Columna</th>
                                <th>Token esperado</th>
                                <th>Descripción </th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>'''
        cadena+="                    <td>&nbsp;"+tipo_error+"</td>"
        cadena+="                    <td>&nbsp;"+linea_error+"</td>"
        cadena+="                        <td>&nbsp;"+columna_error+"</td>"
        cadena+="                        <td>&nbsp;"+token_error+"</td>"
        cadena+="                        <td>&nbsp;"+desc_error+"</td>"
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


    def htmltokens():
        lex="1"
        errorl="Error"
        errorc=""
        r = open("Tokens_202109715.html","w+",encoding="utf-8")
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
                            <caption>Tabla de Tokens</caption>
                            <thead>
                            <tr>
                                <th>No.</th>
                                <th>Tipo</th>
                                <th>     Lexema    </th>
                            </tr>
                            </thead>
                            <tbody>'''
        cont_num=1
        cadena+=            "<tr>"
        print("|"+"NO."+"|"+"  TOKEN  "+"|"+"LEXEMA")
        for j,i in zip(tokenlex, tokenlist):
            cadena+="          <tr>"
            print("|"+str(cont_num)+"|"+j+"|"+i) 
            cadena+="                        <td>"+str(cont_num)+"</td>"
            cadena+="                        <td>"+j+"</td>"
            cont_num+=1
            cadena+="                        <td>&nbsp;"+i+"</td>"
        
        
        cadena+='''          </tr>
                            </tbody>
                        </table>
                        </center>'''
        cadena+="</FONT>"
        cadena +="    <body>\n"
        cadena +="</html>\n"
        r.writelines(cadena)
        doc_tokens = 'Tokens_202109715.html'
        webbrowser.open_new(doc_tokens)


