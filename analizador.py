from enum import Enum
from lib2to3.pgen2 import token
import re
import math
import webbrowser


class L_tokens(Enum):
    TK_MENOR = "<"
    TK_E_NUMERO = "Numero"
    TK_MAYOR = ">"
    TK_NUMERO = "[0-9]*[.]?[0-9]+"
    TK_BARRAINV = "/"
    TK_E_OPERACION = "Operacion"
    TK_IGUAL = "="
    TK_OP_SUMA = "SUMA",
    TK_OP_RESTA = "RESTA"
    TK_OP_MULTIPLICACION= "MULTIPLICACION"
    TK_OP_DIVISION= "DIVISION"
    TK_OP_POTENCIA="POTENCIA"
    TK_OP_RAIZ="RAIZ"
    TK_OP_INVERSO="INVERSO"
    TK_OP_SENO="SENO"
    TK_OP_COSENO="COSENO"
    TK_OP_TANGENTE="TANGENTE"
    TK_OP_MOD="MOD"
    TK_E_TIPO = "Tipo"
    TK_E_TEXTO = "Texto"
    TK_TEXTO = "[a-zA-Z,À-ÿ\u00f1\u00d1,'+'-'-',''.'*',0.0-9.0,':','%','=','/','^','√','(',')','âˆš']*"
    TK_E_FUNCION = "Funcion"
    TK_ESCRIBIR = "ESCRIBIR"
    TK_E_TITULO = "Titulo"
    TK_TITULO = "[a-zA-Z,À-ÿ\u00f1\u00d1,'+'-'-',''.'*',0.0-9.0,':','%','=','/','^','√','(',')','âˆš']*"
    TK_E_COLOR = "Color"
    TK_COLOR = "[a-z]*"
    TK_E_TAMANIO = "Tamanio"
    TK_TAMANIO ="[0-9]*"
    TK_E_DESCRIPCION="Descripcion"
    TK_DESCRIPCION = "TEXTO"
    TK_E_CONTENIDO = "Contenido"
    TK_CONTENIDO = "TIPO"
    TK_E_ESTILO = "Estilo"


class Analizador:
    def __init__(self, archivoimp):
        self.cadena = ""
        self.linea = 0
        self.columna = 0  
        self.lista_cadena = []
        self.tmp_cadena = ""
        self.archivoimp=archivoimp
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



    def quitar(self, _cadena :str, _num : int):
        _tmp = ""
        count = 0
        for i in _cadena:
            if count >= _num:
                _tmp += i
            else:
                self.tmp_cadena += i 
            count += 1
        return _tmp

    def aumentarLinea(self):
        _tmp = self.lista_cadena[self.linea]
        #print(_tmp , " == ", self.tmp_cadena)
        if _tmp == self.tmp_cadena:
            self.linea += 1
            self.tmp_cadena = ""
            self.columna = 0 

    def esLaetiqueta(self, _cadena : str, _etiqueta : str):
        tmp = ""
        count = 0
        for i in _cadena:
            if count < len(_etiqueta):
                tmp += i
            count += 1

        if tmp == _etiqueta:
            return True
        else:
            return False

    def Numero(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_NUMERO.value,         # 10
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value     # >
        ]
        _numero = ""

        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                global errorl
                global errorc
                global lex
                errorl=""
                errorc=""
                lex=""
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                self.columna += int(s.end())

                # GUARDAR EL TOKEN
                if i == L_tokens.TK_NUMERO.value:
                    _numero = s.group()
                    self.op.append(_numero)
                    self.num+=1


                    #SUMA
                    if self.op[0]=="SUMA" and self.num==2:
                        print(float(self.op[1])+float(self.op[2]))
                        results=(float(self.op[1])+float(self.op[2]))
                        num1=(self.op[1])
                        num2=(self.op[2])
                        operacion=self.op[0]
                        locacion=(operacion +": " + num1 + " + " + num2 + " = " + str(results))
                        result.append(locacion)

                    #RESTA
                    if self.op[0]=="RESTA" and self.num==2:
                        print(float(self.op[1])-float(self.op[2]))
                        results=(float(self.op[1])-float(self.op[2]))
                        num1=(self.op[1])
                        num2=(self.op[2])
                        operacion=self.op[0]
                        locacion=(operacion +": " + num1 + " - " + num2 + " = " + str(results))
                        result.append(locacion)



                    #MULTIPLICACION
                    if self.op[0]=="MULTIPLICACION" and self.num==2:
                        print(float(self.op[1])*float(self.op[2]))
                        results=(float(self.op[1])*float(self.op[2]))
                        num1=(self.op[1])
                        num2=(self.op[2])
                        operacion=self.op[0]
                        locacion=(operacion +": " + num1 + " * " + num2 + " = " + str(results))
                        result.append(locacion)





                    #DIVISION
                    if self.op[0]=="DIVISION" and self.num==2:
                        print(float(self.op[1])/(float(self.op[2])))
                        results=(float(self.op[1])/(float(self.op[2])))
                        num1=(self.op[1])
                        num2=(self.op[2])
                        operacion=self.op[0]
                        locacion=(operacion +": " + num1 + " / " + num2 + " = " + str(results))
                        result.append(locacion)



                    #POTENCIA
                    if self.op[0]=="POTENCIA" and self.num==2:
                        print((float(self.op[2]))**(float(self.op[1])))
                        results=((float(self.op[2]))**(float(self.op[1])))
                        num1=(self.op[1])
                        num2=(self.op[2])
                        operacion=self.op[0]
                        locacion=(operacion +": " + num2 + " ^ " + num1 + " = " + str(results))
                        result.append(locacion)


                    
                    #RAIZ
                    if self.op[0]=="RAIZ" and self.num==2:
                        print((float(self.op[2]))**(1/(float(self.op[1]))))
                        results=((float(self.op[2]))**(1/(float(self.op[1]))))
                        num1=(self.op[1])
                        num2=(self.op[2])
                        operacion=self.op[0]
                        locacion=(operacion +": " + num1 + " √ " + num2 + " = " + str(results))
                        result.append(locacion)



                    #INVERSO
                    if self.op[0]=="INVERSO" and self.num==1:
                        print(1/(float(self.op[1])))
                        results=(1/(float(self.op[1])))
                        num1=(self.op[1])
                        operacion=self.op[0]
                        locacion=(operacion +": "+"1/" + num1 + " = " + str(results))
                        result.append(locacion)


                    
                    #SENO
                    if self.op[0]=="SENO" and self.num==1:
                        print(math.sin(float(self.op[1])))
                        results=(math.sin(math.radians((float(self.op[1])))))
                        num1=(self.op[1])
                        operacion=self.op[0]
                        if results<=0.00000001:
                            results=0
                        locacion=(operacion +": " + " SIN(" + num1 + ")"+" = " + str(results))
                        result.append(locacion)



                    #COSENO
                    if self.op[0]=="COSENO" and self.num==1:
                        print(math.cos(float(self.op[1])))
                        results=(math.cos(math.radians((float(self.op[1])))))
                        num1=(self.op[1])
                        operacion=self.op[0]
                        if results<=0.00000001:
                            results=0
                        locacion=(operacion +": " + " COS(" + num1 + ")"+" = " + str(results))
                        result.append(locacion)



                    #TANGENTE
                    if self.op[0]=="TANGENTE" and self.num==1:
                        print(math.tan(float(self.op[1])))
                        results=(math.tan(math.radians((float(self.op[1])))))
                        num1=(self.op[1])
                        operacion=self.op[0]
                        if results<=0.00000001:
                            results=0
                        locacion=(operacion +": " + " TAN(" + num1 + ")"+" = " + str(results))
                        result.append(locacion)



                    #MOD
                    if self.op[0]=="MOD" and self.num==2:
                        print(float(self.op[1])%float(self.op[2]))
                        results=(float(self.op[1])%float(self.op[2]))
                        num1=(self.op[1])
                        num2=(self.op[2])
                        operacion=self.op[0]
                        locacion=(operacion +": " + num1 + " % " + num2 + " = " + str(results))
                        result.append(locacion)


                    # GRANDES
                    # if self.num==3 and self.op[0]=="SUMA" and self.op[2]=="SUMA":
                    #     print(float(self.op[1])+float(self.op[3])+float(self.op[4]))
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()

            except:
                # GUARDAR ERROR
                errorl=str(self.linea)
                
                errorc=str(self.columna)
                
                lex=str(s.group())
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}

        return {'resultado':_numero, "cadena":_cadena, "Error":False}

    def Operacion(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_OPERACION.value,  # Operacion
            L_tokens.TK_IGUAL.value,              # =
            "OPERADOR",                     # OPERADOR
            L_tokens.TK_MAYOR.value,        # >
            "NUMERO",                       # NUMERO
            "NUMERO",                       # NUMERO
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_OPERACION.value,  # Operacion
            L_tokens.TK_MAYOR.value,        # >
        ]
        _numero = ""
        _operador = None
        for i in tokens:
            try:
                if "NUMERO" == i:
                    if self.esLaetiqueta(_cadena, "<Numero>"):
                        _result = self.Numero(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            print("Ocurrio un error")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}

                    elif self.esLaetiqueta(_cadena, "<Operacion="):
                        _result = self.Operacion(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            print("Ocurrio un error")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}
                    else:
                        # GUARDAR ERROR
                        print("Ocurrio un error")
                        return {'resultado':_numero, "cadena":_cadena, "Error": True}
                
                else:
                    if "OPERADOR" == i:
                        # SUMA
                        spatron = re.compile(f'^SUMA')
                        t = spatron.search(_cadena)
                        #print("OPERADOR -> ", t)
                        if t != None:
                            i = "SUMA"
                            _operador = L_tokens.TK_OP_SUMA
                            self.op.append("SUMA")

                        # RESTA
                        spatron = re.compile(f'^RESTA')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "RESTA"
                            _operador = L_tokens.TK_OP_RESTA
                            self.op.append("RESTA")

                        # MULTIPLICACION
                        spatron = re.compile(f'^MULTIPLICACION')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "MULTIPLICACION"
                            _operador = L_tokens.TK_OP_MULTIPLICACION
                            self.op.append("MULTIPLICACION")
                        
                        # DIVISION
                        spatron = re.compile(f'^DIVISION')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "DIVISION"
                            _operador = L_tokens.TK_OP_DIVISION
                            self.op.append("DIVISION")
                        
                        # POTENCIA
                        spatron = re.compile(f'^POTENCIA')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "POTENCIA"
                            _operador = L_tokens.TK_OP_POTENCIA
                            self.op.append("POTENCIA")

                        # RAIZ
                        spatron = re.compile(f'^RAIZ')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "RAIZ"
                            _operador = L_tokens.TK_OP_RAIZ
                            self.op.append("RAIZ")

                        # INVERSO
                        spatron = re.compile(f'^INVERSO')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "INVERSO"
                            _operador = L_tokens.TK_OP_INVERSO
                            tokens.pop(6)
                            self.op.append("INVERSO")

                        # SENO
                        spatron = re.compile(f'^SENO')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "SENO"
                            _operador = L_tokens.TK_OP_SENO
                            tokens.pop(6)
                            self.op.append("SENO")

                        # COSENO
                        spatron = re.compile(f'^COSENO')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "COSENO"
                            _operador = L_tokens.TK_OP_COSENO
                            tokens.pop(6)
                            self.op.append("COSENO")
                        
                        # TANGENTE
                        spatron = re.compile(f'^TANGENTE')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "TANGENTE"
                            _operador = L_tokens.TK_OP_TANGENTE
                            tokens.pop(6)
                            self.op.append("TANGENTE")
                        
                        # MOD
                        spatron = re.compile(f'^MOD')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "MOD"
                            _operador = L_tokens.TK_OP_MOD
                            self.op.append("MOD")

                        if _operador == None:
                            # GUARDAR ERROR
                            print("Ocurrio un error Operacion")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}

                    patron = re.compile(f'^{i}')
                    s = patron.search(_cadena)
                    global errorl
                    global errorc
                    global lex
                    errorl=""
                    errorc=""
                    lex=""
                    # GUARDAR EL TOKEN
                    print("| ", self.linea, " | ", self.columna, " | ", s.group())
                    self.columna += int(s.end())
                    _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                errorl=str(self.linea)
                
                errorc=str(self.columna)
                
                lex=str(s.group())
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}

        # NUMERO1 OPERADOR NUMERO2
        return {'resultado':_numero, "cadena":_cadena, "Error":False}


    def Texto(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_TEXTO.value, # Texto
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_TEXTO.value,         # Hola como estas
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_TEXTO.value, # Texto
            L_tokens.TK_MAYOR.value     # >
        ]
        _numero = ""

        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                global errorl
                global errorc
                global lex
                errorl=""
                errorc=""
                lex=""
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                if i == L_tokens.TK_TEXTO.value:
                    datos.append(s.group())
                self.columna += int(s.end())
                # GUARDAR EL TOKEN
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                errorl=str(self.linea)
                
                errorc=str(self.columna)
                
                lex=str(s.group())
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}
        self.Funcion(_cadena)
    
    def Funcion(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_FUNCION.value, # Funcion
            L_tokens.TK_IGUAL.value, # =
            L_tokens.TK_ESCRIBIR.value, #Escribir
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_TITULO.value,  #Titulo
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_TITULO.value,   #Operaciones simples
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_TITULO.value, # Titulo
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_DESCRIPCION.value, # Descripcion
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_DESCRIPCION.value,
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_DESCRIPCION.value, # Descripcion
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_CONTENIDO.value, # Contenido
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_CONTENIDO.value,
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_CONTENIDO.value, # Contenido
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_FUNCION.value, # Funcion
            L_tokens.TK_MAYOR.value     # >
        ]
        _numero = ""
        global titulo
        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                global errorl
                global errorc
                global lex
                errorl=""
                errorc=""
                lex=""
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                
                if i == L_tokens.TK_TITULO.value:
                    titulo=s.group()
                self.columna += int(s.end())
                # GUARDAR EL TOKEN
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                print("Ocurrio un error")
                
                errorl=str(self.linea)
                
                errorc=str(self.columna)
                
                lex=str(s.group())
                
                
                return {'resultado':_numero, "cadena":_cadena, "Error": True}
            continue
                
        self.Estilo(_cadena)

    def Estilo(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_ESTILO.value, # Estilo
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_TITULO.value,  #Titulo
            L_tokens.TK_E_COLOR.value,  #Color
            L_tokens.TK_IGUAL.value,    #=
            L_tokens.TK_COLOR.value,    #AZUL
            L_tokens.TK_E_TAMANIO.value,  #TAMAÑO
            L_tokens.TK_IGUAL.value,  #=
            L_tokens.TK_TAMANIO.value,  #20
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_DESCRIPCION.value,  #Titulo
            L_tokens.TK_E_COLOR.value,  #Color
            L_tokens.TK_IGUAL.value,    #=
            L_tokens.TK_COLOR.value,    #AZUL
            L_tokens.TK_E_TAMANIO.value,  #TAMAÑO
            L_tokens.TK_IGUAL.value,  #=
            L_tokens.TK_TAMANIO.value,  #20
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_CONTENIDO.value,  #Titulo
            L_tokens.TK_E_COLOR.value,  #Color
            L_tokens.TK_IGUAL.value,    #=
            L_tokens.TK_COLOR.value,    #AZUL
            L_tokens.TK_E_TAMANIO.value,  #TAMAÑO
            L_tokens.TK_IGUAL.value,  #=
            L_tokens.TK_TAMANIO.value,  #20
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_MAYOR.value,     # >
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_ESTILO.value, # Estilo
            L_tokens.TK_MAYOR.value,    # >
        ]
        _numero = ""
        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                global errorl
                global errorc
                global lex
                errorl=""
                errorc=""
                lex=""
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                self.columna += int(s.end())


                if i == L_tokens.TK_COLOR.value:
                    colortz.append(s.group())


                if i == L_tokens.TK_TAMANIO.value:
                    tamañoletra.append(s.group())


                # GUARDAR EL TOKEN
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                errorl=str(self.linea)
                
                errorc=str(self.columna)
                
                lex=str(s.group())
                # GUARDAR ERROR
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}

    def Tipo(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_TIPO.value,       # Tipo
            L_tokens.TK_MAYOR.value,        # >
            L_tokens.TK_TITULO.value,
            "OPERACIONES",                  # OPERACIONES
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_TIPO.value,       # Tipo
            L_tokens.TK_MAYOR.value,        # >
        ]
        _numero = ""
    
        for i in tokens:
            try:
                
                if "OPERACIONES" == i:
                    salida = True
                    while salida:
                        print("--------------------------------")
                        self.num=0
                        self.op=[]
                        _result = self.Operacion(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            print("Ocurrio un error")
                            break
                        
                        if self.esLaetiqueta(_cadena, "</Tipo>"):
                            salida = False
                else:
                    patron = re.compile(f'^{i}')
                    s = patron.search(_cadena)
                    global errorl
                    global errorc
                    global lex
                    errorl=""
                    errorc=""
                    lex=""
                    # GUARDAR EL TOKEN
                    print("| ", self.linea, " | ", self.columna, " | ", s.group())
                    self.columna += int(s.end())
                    _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                errorl=str(self.linea)
                
                errorc=str(self.columna)
                
                lex=str(s.group())
                # GUARDAR ERROR
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}

        
        self.Texto(_cadena)

        return {'resultado':_numero, "cadena":_cadena, "Error": False}

    def compile(self):
        # LEEMOS EL ARCHIVO DE ENTRADA
        archivo = open(self.archivoimp, "r", encoding="utf-8")
        global contenido
        contenido = archivo.readlines()
        archivo.close()

        

        # LIMPIAR MI ENTRADA
        global nueva_cadena
        nueva_cadena = ""
        global lista_cadena
        lista_cadena = []
        global nueva
        

        

        for i in contenido:
            i = i.replace(' ', '') #QUITANDO ESPACIOS
            i = i.replace('\n', '') # QUITANDO SALTOS DE LINEA
            i = i.replace('[','') 
            i = i.replace(']','') 
            i = i.replace('"','')
            i = i.replace('AZUL','blue')
            i = i.replace('ANARANJADO','orange')
            i = i.replace('NARANJA','orange')
            i = i.replace('ROJO','red')
            i = i.replace('AMARILLO','yellow')
            i = i.replace('VERDE','green')
            i = i.replace('MORADO','purple')
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)
       
        

        print(nueva_cadena)
        print(lista_cadena)

        self.lista_cadena = lista_cadena

        print(self.Tipo(nueva_cadena))
    
    def htmlanalizar():

        for j in contenido:
            if j!="":
                lista_cadena.append(j)

        r=0
        
        hola=colortz[1]

        for x in range(len(lista_cadena)):

            if lista_cadena[x]=="<Texto>\n":
                nueva=lista_cadena[x+1]
                r=2
                while lista_cadena[x+r]!="</Texto>\n":
                    nueva+='<p style=color:'+hola+';font-size:'+tamañoletra[1]+'px;>'+lista_cadena[x+r]+"</p>\n"
                    r+=1


        r = open("Resultados_202109715.html","w+",encoding="utf-8")
        cadena="<!DOCTYPE html>\n"
        cadena+= "<html lang=\"es\">\n"
        cadena+= "  <head>\n"
        cadena+="       <meta charset=\"UTF-8\">\n"
        cadena+="       <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
        cadena+="       <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        cadena+="</head>\n"
        cadena += "    <body>\n"
        cadena += '         <h1 style=color:'+colortz[0]+';font-size:'+tamañoletra[0]+'px;>'+"<center>"+"<FONT FACE='arial'>"+titulo+"</center>"+"</FONT>"+"</h1>\n"
        cadena += '         <p style=color:'+colortz[1]+';font-size:'+tamañoletra[1]+'px;>'+"<FONT FACE='arial'>"+nueva+"</FONT>"+"</p>\n"
        for i in result:
            cadena +='          <p style="color:'+colortz[2]+';font-size:10px;">'+"<FONT FACE='arial'>"+str(i)+"</p>\n"
        cadena +="    <body>\n"
        cadena +="</html>\n"
        r.writelines(cadena)
        doc_analizador = 'Resultados_202109715.html'
        webbrowser.open_new(doc_analizador)
        
 


    def htmlerrores():
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


