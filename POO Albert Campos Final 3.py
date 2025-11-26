import sys

contador_universal_ids = 0
registro_total_empleados = []
registro_total_proyectos = []

class Empleado:
    def __init__(self, nombre_completo, sueldo_basico):
        global contador_universal_ids
        contador_universal_ids = contador_universal_ids + 1
        self.__id_propio = contador_universal_ids
        self.__nombre_empleado = nombre_completo
        self.__salario_base_mensual = float(sueldo_basico)
        self.lista_proyectos_asignados = []

    def recuperar_id(self):
        return self.__id_propio
    
    def recuperar_nombre(self):
        return self.__nombre_empleado
    
    def recuperar_salario_base(self):
        return self.__salario_base_mensual

    def calcular_salario_mensual(self):
        return 0.0

    def imprimir_datos_personales(self):
        monto = self.calcular_salario_mensual()
        ident = self.recuperar_id()
        nom = self.recuperar_nombre()
        print("ID Empleado: " + str(ident) + " | Nombre: " + str(nom) + " | Salario Final: " + str(monto))

    def intentar_asignar_proyecto(self, objeto_proyecto):
        clase_actual = str(type(self).__name__)
        tope_maximo = 0
        
        if clase_actual == "Desarrollador":
            tope_maximo = 3
        else:
            if clase_actual == "Diseñador":
                tope_maximo = 2
            else:
                if clase_actual == "Gerente":
                    tope_maximo = 0
        
        if clase_actual == "Gerente":
            print("ERROR FATAL: Un Gerente no puede ser obrero en un proyecto.")
            return False

        numero_proyectos_actuales = 0
        for p in self.lista_proyectos_asignados:
            numero_proyectos_actuales = numero_proyectos_actuales + 1
        
        if numero_proyectos_actuales < tope_maximo:
            self.lista_proyectos_asignados.append(objeto_proyecto)
            return True
        else:
            print("FALLO ASIGNACION: Limite de proyectos excedido (" + str(tope_maximo) + ")")
            return False

class Desarrollador(Empleado):
    def __init__(self, nombre_completo, sueldo_basico, listado_lenguajes, nivel_seniority):
        super().__init__(nombre_completo, sueldo_basico)
        self.lenguajes_programacion = listado_lenguajes
        self.nivel_experiencia = nivel_seniority

    def calcular_salario_mensual(self):
        acumulador = self.recuperar_salario_base()
        
        if self.nivel_experiencia == "Junior":
            acumulador = acumulador + 200
        else:
            if self.nivel_experiencia == "SemiSenior":
                acumulador = acumulador + 500
            else:
                if self.nivel_experiencia == "Senior":
                    acumulador = acumulador + 1000
        
        return acumulador

class Diseñador(Empleado):
    def __init__(self, nombre_completo, sueldo_basico, listado_herramientas, tipo_especialidad):
        super().__init__(nombre_completo, sueldo_basico)
        self.herramientas_diseño = listado_herramientas
        self.tipo_especialidad = tipo_especialidad

    def calcular_salario_mensual(self):
        pago_final = self.recuperar_salario_base()
        
        detectar_figma = False
        indice = 0
        largo = len(self.herramientas_diseño)
        while indice < largo:
            if self.herramientas_diseño[indice] == "Figma":
                detectar_figma = True
            indice = indice + 1
        
        if detecting_figma == True: 
            pago_final = pago_final + 300
        else:
            if detectar_figma == True:
                pago_final = pago_final + 300

        contador_suite_adobe = 0
        for herramienta in self.herramientas_diseño:
            if herramienta == "Photoshop":
                contador_suite_adobe = contador_suite_adobe + 1
            if herramienta == "Illustrator":
                contador_suite_adobe = contador_suite_adobe + 1
        
        conteo_total_items = len(self.herramientas_diseño)
        
        if conteo_total_items == 1:
            if contador_suite_adobe > 0:
                pago_final = pago_final + 200
        
        if conteo_total_items >= 3:
            pago_final = pago_final + 400
            
        return pago_final

class Gerente(Empleado):
    def __init__(self, nombre_completo, sueldo_basico, area_gerencia):
        super().__init__(nombre_completo, sueldo_basico)
        self.departamento_asignado = area_gerencia
        self.lista_subordinados = []

    def metodo_recursivo_suma(self, lista_empleados, posicion_actual):
        cantidad = len(lista_empleados)
        if posicion_actual == cantidad:
            return 0
        
        trabajador_actual = lista_empleados[posicion_actual]
        dinero_actual = trabajador_actual.calcular_salario_mensual()
        
        return dinero_actual + self.metodo_recursivo_suma(lista_empleados, posicion_actual + 1)

    def calcular_salario_mensual(self):
        total_salarios_equipo = self.metodo_recursivo_suma(self.lista_subordinados, 0)
        comision = total_salarios_equipo * 0.15
        base_gerente = self.recuperar_salario_base()
        resultado = base_gerente + comision
        return resultado

    def agregar_miembro_equipo(self, nuevo_subordinado):
        nombre_clase = str(type(nuevo_subordinado).__name__)
        
        permitido = False
        if nombre_clase == "Desarrollador":
            permitido = True
        elif nombre_clase == "Diseñador":
            permitido = True
            
        if permitido == True:
            self.lista_subordinados.append(nuevo_subordinado)
            print("Se agrego correctamente al equipo del gerente.")
        else:
            print("Error de Jerarquia: El Gerente solo supervisa Desarrolladores o Diseñadores.")
    
    def intentar_asignar_proyecto(self, proy):
        print("ACCION DENEGADA: Los gerentes solo supervisan, no trabajan en proyectos.")
        return False

class Proyecto:
    def __init__(self, titulo_proyecto, dinero_presupuesto):
        self.titulo = titulo_proyecto
        self.presupuesto_maximo = float(dinero_presupuesto)
        self.trabajadores_inscritos = []

    def inscribir_empleado(self, empleado_candidato):
        bandera_existe = False
        id_candidato = empleado_candidato.recuperar_id()
        
        for persona in self.trabajadores_inscritos:
            if persona.recuperar_id() == id_candidato:
                bandera_existe = True
        
        if bandera_existe == True:
            print("Aviso: El empleado ya se encuentra en la lista de este proyecto.")
        else:
            respuesta = empleado_candidato.intentar_asignar_proyecto(self)
            if respuesta == True:
                self.trabajadores_inscritos.append(empleado_candidato)
                print("Exito: Empleado vinculado al proyecto " + self.titulo)
            else:
                print("Fallo: El empleado rechazo la asignacion por sus limites.")

    def calcular_costo_mensual_total(self):
        suma_acumulada = 0
        for integrante in self.trabajadores_inscritos:
            valor = integrante.calcular_salario_mensual()
            suma_acumulada = suma_acumulada + valor
        return suma_acumulada

    def verificar_viabilidad_financiera(self):
        gasto_proyectado = self.calcular_costo_mensual_total()
        limite_seguro = self.presupuesto_maximo * 0.70
        
        if gasto_proyectado <= limite_seguro:
            return True
        else:
            return False

def rutina_procesamiento_masivo(listado):
    print("=== INICIO DE PROCESAMIENTO DE PLANILLA ===")
    contador_iteracion = 0
    for individuo in listado:
        contador_iteracion = contador_iteracion + 1
        individuo.imprimir_datos_personales()
        
        tipo_obj = str(type(individuo).__name__)
        
        num_proyectos = 0
        if tipo_obj != "Gerente":
            num_proyectos = len(individuo.lista_proyectos_asignados)
        
        print("Proyectos Activos: " + str(num_proyectos))
        print("--- Fin del registro " + str(contador_iteracion) + " ---")

def menu_principal_consola():
    bandera_menu = True
    while bandera_menu == True:
        print("\n################################################")
        print("   SISTEMA CORPORATIVO DE GESTION DE RRHH")
        print("################################################")
        print("1 -> Dar de alta: DESARROLLADOR")
        print("2 -> Dar de alta: DISEÑADOR")
        print("3 -> Dar de alta: GERENTE")
        print("4 -> Crear nuevo PROYECTO")
        print("5 -> Asignar RECURSO a PROYECTO (por ID)")
        print("6 -> Asignar RECURSO a EQUIPO DE GERENTE (por ID)")
        print("7 -> EJECUTAR REPORTE (Procesar Empleados)")
        print("8 -> CONSULTAR VIABILIDAD DE PROYECTOS")
        print("9 -> EJECUTAR CASO DE PRUEBA OBLIGATORIO (PDF)")
        print("0 -> CERRAR APLICACION")
        
        entrada_usuario = input("Ingrese el digito de su opcion: ")

        if entrada_usuario == "1":
            nom = input("Nombre completo: ")
            sal = input("Salario Base Mensual: ")
            print("Ingrese lenguajes separados solo por coma (ej: Python,C#):")
            texto_lenguajes = input("Lenguajes: ")
            array_lenguajes = texto_lenguajes.split(",")
            niv = input("Nivel (Junior/SemiSenior/Senior): ")
            obj_dev = Desarrollador(nom, sal, array_lenguajes, niv)
            registro_total_empleados.append(obj_dev)
            print("Desarrollador registrado. ID Asignado: " + str(obj_dev.recuperar_id()))

        elif entrada_usuario == "2":
            nom = input("Nombre completo: ")
            sal = input("Salario Base Mensual: ")
            print("Ingrese herramientas separadas solo por coma:")
            texto_herra = input("Herramientas: ")
            array_herra = texto_herra.split(",")
            esp = input("Especialidad (UI/UX/Gráfico): ")
            obj_dis = Diseñador(nom, sal, array_herra, esp)
            registro_total_empleados.append(obj_dis)
            print("Diseñador registrado. ID Asignado: " + str(obj_dis.recuperar_id()))

        elif entrada_usuario == "3":
            nom = input("Nombre completo: ")
            sal = input("Salario Base Mensual: ")
            dep = input("Departamento: ")
            obj_ger = Gerente(nom, sal, dep)
            registro_total_empleados.append(obj_ger)
            print("Gerente registrado. ID Asignado: " + str(obj_ger.recuperar_id()))

        elif entrada_usuario == "4":
            t = input("Titulo del Proyecto: ")
            p = input("Presupuesto Total: ")
            obj_proy = Proyecto(t, p)
            registro_total_proyectos.append(obj_proy)
            print("Proyecto creado.")

        elif entrada_usuario == "5":
            try:
                id_e = int(input("ID del Empleado: "))
            except:
                id_e = -1
            
            tit_p = input("Titulo exacto del Proyecto: ")
            
            sujeto = None
            obra = None
            
            for e in registro_total_empleados:
                if e.recuperar_id() == id_e:
                    sujeto = e
            
            for p in registro_total_proyectos:
                if p.titulo == tit_p:
                    obra = p
            
            if sujeto != None:
                if obra != None:
                    obra.inscribir_empleado(sujeto)
                else:
                    print("Proyecto no hallado en la base de datos.")
            else:
                print("Empleado no hallado en la base de datos.")

        elif entrada_usuario == "6":
            try:
                id_g = int(input("ID del Gerente: "))
                id_sub = int(input("ID del Subordinado: "))
            except:
                id_g = 0
                id_sub = 0
            
            jefe = None
            peon = None
            
            for x in registro_total_empleados:
                if x.recuperar_id() == id_g:
                    if str(type(x).__name__) == "Gerente":
                        jefe = x
                if x.recuperar_id() == id_sub:
                    peon = x
            
            if jefe != None and peon != None:
                jefe.agregar_miembro_equipo(peon)
            else:
                print("Error: IDs invalidos o el primero no es Gerente.")

        elif entrada_usuario == "7":
            rutina_procesamiento_masivo(registro_total_empleados)

        elif entrada_usuario == "8":
            for pr in registro_total_proyectos:
                print(">>> Proyecto: " + pr.titulo)
                costo = pr.calcular_costo_mensual_total()
                presu = pr.presupuesto_maximo
                print("Costo Nomina: " + str(costo) + " / Presupuesto: " + str(presu))
                
                es_posible = pr.verificar_viabilidad_financiera()
                if es_posible == True:
                    print("ESTADO: VIABLE")
                else:
                    print("ESTADO: NO VIABLE (Riesgo Financiero)")
                print(" ")

        elif entrada_usuario == "9":
            print("--- INICIANDO PROTOCOLO DE PRUEBA AUTOMATICO ---")
            
            g_test = Gerente("Carlos Manager", 4000, "IT")
            d1_test = Desarrollador("Ana Python", 1800, ["Python", "Django"], "Senior")
            d2_test = Desarrollador("Pepe Java", 1200, ["Java"], "Junior")
            dis_test = Diseñador("Lucia Arts", 1400, ["Figma", "Photoshop"], "UI")
            
            registro_total_empleados.append(g_test)
            registro_total_empleados.append(d1_test)
            registro_total_empleados.append(d2_test)
            registro_total_empleados.append(dis_test)
            
            print("Asignando equipo al gerente...")
            g_test.agregar_miembro_equipo(d1_test)
            g_test.agregar_miembro_equipo(d2_test)
            g_test.agregar_miembro_equipo(dis_test)
            
            py1 = Proyecto("Sistema Web", 30000)
            py2 = Proyecto("App Movil", 6000)
            registro_total_proyectos.append(py1)
            registro_total_proyectos.append(py2)
            
            print("Asignando empleados a proyectos...")
            py1.inscribir_empleado(d1_test)
            py1.inscribir_empleado(dis_test)
            py2.inscribir_empleado(d2_test)
            
            print("Forzando error de 4to proyecto en Desarrollador...")
            py3 = Proyecto("Extra 1", 1000)
            py4 = Proyecto("Extra 2", 1000)
            py_fail = Proyecto("Extra 3", 1000)
            
            py2.inscribir_empleado(d1_test) 
            py3.inscribir_empleado(d1_test)
            py4.inscribir_empleado(d1_test) 
            
            rutina_procesamiento_masivo(registro_total_empleados)

        elif entrada_usuario == "0":
            print("Apagando sistema...")
            bandera_menu = False
        
        else:
            print("Opcion no reconocida.")

if __name__ == "__main__":
    menu_principal_consola()