// Pide al usuario un número entero. Genera su tabla de multiplicar del 1 al 10.
// Guarda la tabla en un archivo llamado tabla.txt. 
// Al finalizar, muestra un mensaje indicando que el archivo fue creado. 

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.println("Hola, introduce un número entero");

        if(s.hasNextInt()){
            int num = s.nextInt(); 
            System.out.println("Número "+ num + " leído");
            //Creamos el archivo 
            try (FileWriter fw = new FileWriter("tabla.txt")) {
                for(int i = 1; i <= 10; i++){
                    int mul; 
                    mul = i*num; 
                    //Con el método de FileWriter vamos escribiendo línea a línea en el fichero tabla
                    fw.write(i + " x " + num + " = " + mul + "\n");
                }
                System.out.println("El archivo tabla.txt fue creado.");
            } catch (IOException e) {
                e.printStackTrace();
            } 
        } else {
            System.out.println("No es un número");
        }
    }
}
