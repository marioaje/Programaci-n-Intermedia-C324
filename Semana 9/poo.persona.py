# Estos es una clase POO

# Personas
# cedula
# nombre
# fechanacimiento
# nacionalidad
# altura
# apellidos

# ---Funciones
# Agregar
# Validar
# Eliminarlo
# ConsultarporId
# ConsultaGeneral
# ActualizarDatos
class Persona:
    #Esto es un constructor lo cual permite que la Clase Persona reciba los siguients parametros.
    def __init__(self,  cedula
                        ,nombre
                        ,fechanacimiento
                        ,nacionalidad
                        ,altura
                        ,apellidos):
        
        self.cedula = cedula
        self.nombre = nombre
        self.fechanacimiento = fechanacimiento
        self.nacionalidad = nacionalidad
        self.altura = altura
        self.apellidos =apellidos
        
    def Agregar(self,  cedula
                    ,nombre
                    ,fechanacimiento
                    ,nacionalidad
                    ,altura
                    ,apellidos):
        self.cedula = cedula
        self.nombre = nombre
        self.fechanacimiento = fechanacimiento
        self.nacionalidad = nacionalidad
        self.altura = altura
        self.apellidos =apellidos           
        
        
    def Validar(self,  cedula
                    ,nombre
                    ,fechanacimiento
                    ,nacionalidad
                    ,altura
                    ,apellidos):
        self.cedula = cedula
        self.nombre = nombre
        self.fechanacimiento = fechanacimiento
        self.nacionalidad = nacionalidad
        self.altura = altura
        self.apellidos =apellidos
        
        
        
        
    def NombreActualizar(self, nombre):
        self.nombre = nombre

    def setNombre(self, nombre):
        self.nombre = nombre
        
    def getNombre(self):
        return self.nombre        
        
    def Eliminarlo(self, id):        
        return "Se elimino: " + id
        
    def ActualizarDatos(self, nombre, fechanacimiento):
        self.fechanacimiento = fechanacimiento
        self.nombre = nombre          
        
    def ConsultaGeneral(self):
        return f"{self.cedula } { self.nombre } {self.fechanacimiento } {self.nacionalidad} {self.altura } {self.apellidos}"    
        #return "Test"
        
#fin class Persona:


usuarioMario = Persona(123,"Mario","12 setiembre","Apache","150cm",'Jimenez')
usuarioAlberto = Persona(1234,"Albertp","12 setiembre","Apache","150cm",'Jimenez')
usuarioMario.agre
print( usuarioMario.ConsultaGeneral() )
print( usuarioAlberto.ConsultaGeneral() )







            

# def Eliminarlo
# def ConsultarporId
# def ConsultaGeneral
# def ActualizarDatos
        
        