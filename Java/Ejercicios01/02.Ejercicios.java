//Pedir al usuario que escriba texto linea por linea y leer con BufferedReader
//Termina cuando escriba "salir"
//Muestra cada línea convertida a mayúsculas en consola 

import java.util.Scanner;

class Ejercicios {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String linea;

        System.out.println("Escribe texto (escribe 'salir' para terminar):");

        while (true) {
            linea = s.nextLine();
            if (linea.equalsIgnoreCase("salir")) {
                break;
            } else {
                System.out.println(linea.toUpperCase());
            }
            
        }
        System.out.println("Adiós!");
    }
}