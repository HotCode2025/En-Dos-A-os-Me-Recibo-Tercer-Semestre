
package Java.Clase02;

public class PersonaBloqueDinamico {

    private final int idPersonaBloqueDinamico;
    private static int contadorPersonas;

    // Bloque de inicialización ESTÁTICO (se mantiene)
    static {
        System.out.println("Ejecucion del bloque estatico");
        contadorPersonas = 1;
    }

    // CONSTRUCTOR (reemplaza el bloque NO static)
    public PersonaBloqueDinamico() {
        System.out.println("Inicializacion NO static usando constructor");
        this.idPersonaBloqueDinamico = contadorPersonas++;
    }

    public String toString() {
        return "Persona{idPersona=" + idPersonaBloqueDinamico + "}";
    }
}

