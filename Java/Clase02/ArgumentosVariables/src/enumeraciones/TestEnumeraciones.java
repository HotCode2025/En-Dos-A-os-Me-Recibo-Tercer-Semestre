/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package enumeraciones;

import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Día 1: " +Dias.DOMINGO);
        
        indicarDiaSemana(Dias.DOMINGO);
        
        //Enum CONTINENTES
        System.out.println("4 Continente: "+ Continentes.AMERICA);
        System.out.println("Paises: "+ Continentes.AMERICA.getPaises());
        System.out.println("Habitantes: "+ Continentes.AMERICA.getHabitantes());
    }
    
 public static void indicarDiaSemana(Dias dias) {
     switch(dias) {
         case DOMINGO: 
             System.out.println("Primer día de la semana");
             break;
         case LUNES: 
             System.out.println("Segundo día de la semana");
             break;
        case MARTES: 
             System.out.println("Tercer día de la semana");
             break;
        case MIERCOLES: 
             System.out.println("Cuarto día de la semana");
             break;
        case JUEVES: 
             System.out.println("Quinto día de la semana");
             break;
        case VIERNES: 
             System.out.println("Sexto día de la semana");
             break;
        case SABADO: 
             System.out.println("Septimo día de la semana");
             break;
        default: 
            System.out.println("El valor ingresado no corresponde a un día de la semana");
            break;
     }
 }
}
