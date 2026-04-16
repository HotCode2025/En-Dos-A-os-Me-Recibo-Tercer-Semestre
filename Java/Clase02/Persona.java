package Java.Clase02;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;


    static { // Bloque de inicialización estático
        System.out.println("Ejecucion del bloque estatico");
        ++Persona.contadorPersonas; 
        //  idPersona = 10; // No se estatico por esto tenemos error
    }

    { //Bloque de inicializacion NO estatico (contexto dinamico)
        System.out.println("Ejecucion del bloque NO estatico");
        this.idPersona = Persona.contadorPersonas++; // Incrementamos el atributo    
    }

    //Los bloques de inicialización se ejecutan antes que el constructor

    public Persona() {
        System.out.println("Ejecucion del constructor");
    }

    public int idPersona() {
        return this.idPersona;
    }
}