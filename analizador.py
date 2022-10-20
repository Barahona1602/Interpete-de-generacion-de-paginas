from enum import Enum
from lib2to3.pgen2 import token
import re
import math
import webbrowser


class L_tokens(Enum):
    
    #Etiquetas 
    TK_E_AREATEXTO = "AreaTexto"
    TK_E_BOTON = "Boton"
    TK_E_CHECK = "Check"
    TK_E_CLAVE = "Clave"
    TK_E_COLOCACION = "Colocacion"
    TK_E_CONTENEDOR = "Contenedor"
    TK_E_CONTROLES="Controles"
    TK_E_ETIQUETA = "Etiqueta"
    TK_E_PROPIEDADES = "propiedades"
    TK_E_RADIOBOTON = "RadioBoton"
    TK_E_TEXTO = "Texto"
    TK_TEXTO = "[a-zA-Z,À-ÿ\u00f1\u00d1,'+'-'-',''.'*',0.0-9.0,':','%','=','/','^','√','(',')','âˆš']*"
   
   #Símbolos
    TK_A_PARENTESIS = "("
    TK_APERTURA = "<!--"
    TK_C_PARENTESIS = ")"
    TK_CIERRE = "-->"
    TK_COMA = ","
    TK_COMILLAS = '"'
    TK_MAYOR = ">"
    TK_MENOR = "<"
    TK_NUMERO = "[0-9]*[.]?[0-9]+"
    TK_PUNTO = "."
    TK_PUNTOYCOMA = ";"

    #Set y propiedades
    TK_ADD = "add"
    TK_ALINEACION = "[Centro|Izquierda|Derecha]"
    TK_COLORFONDO = "[0-9]+[,]?[0-9]+[,]?[0-9]+"
    TK_SETALINEACION = "setAlineacion"
    TK_SETALTO = "setAlto"
    TK_SETANCHO="setAncho"
    TK_SETCOLORFONDO = "setColorFondo"
    TK_SETCOLORLETRA = "setColorLetra"
    TK_SETGRUPO = "setGrupo"
    TK_SETMARCADA = "setMarcada"
    TK_SETPOSICION = "setPosicion"
    TK_SETTEXTO = "setTexto"
    TK_THIS = "this"




class Analizador:
    def __init__(self, archivoimp):
        self.linea = 0
        self.columna = 0
        self.tmp_cadena = ""
        self.lista_cadena = []
        self.archivoimp=archivoimp
        self.EstadoActual = 0
        self.op=[]
        self.num=0
        global result
        result=[]
        global datos
        datos=[]
        global funcion 
        funcion = []
        global tit
        tit=[]
        global colortz
        colortz=[]
        global tamañoletra 
        tamañoletra=[]
        global hola
        hola=""
        global errores 
        errores=[]

    def aumentarLinea(self):
        _tmp = self.lista_cadena[self.linea]
        #print(_tmp , " == ", self.tmp_cadena)
        if _tmp == self.tmp_cadena:
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
        alfabeto = ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "_"]
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


    def cometariomultilinea(self, cadena : str):
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
                print( self.linea, " | ", self.columna," | COMENTARIO MULTILINEA")
                self.columna += count
                self.aumentarLinea()
                return tmp
            return cadena
        except:
            return cadena


    def lecturaporEstados(self, cadena):
        self.EstadoActual = "Q0"

        while cadena != "":

            if self.EstadoActual == "Q0":
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
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "A":
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
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "B":
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
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "C":
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
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "D":
                token = "Controles"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "E"
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "E":
                token = ">"
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

            elif self.EstadoActual == "F":
                cadena = self.cometariomultilinea(cadena)
                print(cadena)
                token = "<"
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = ["Boton", "Texto", "Contenedor"]
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            token = i
                            self.EstadoActual = "H"
                            break
                else:
                    self.EstadoActual = "G"
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break

                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                #aumentar linea
                
                self.aumentarLinea()
                

            elif self.EstadoActual == "H":
                tmp = cadena.split(";")
                id = tmp[0]
                print(self.verificarID(id))
                cadena = self.quitar(cadena, id)
                print("--> ",cadena)
                break
                    

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
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)

        print("-------------------")
        print(nueva_cadena)
        print("-------------------")
        print(lista_cadena)

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


