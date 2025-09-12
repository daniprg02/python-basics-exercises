package Ficheros;
import java.io.File;
import java.io.IOException;


public class Ficheros
{
    public static void main(String[] args) {
        //CREA UN ARCHIVO EN NUESTRA CARPETA
        File miArchivo = new File(System.getProperty("user.home") + "/fichero.txt");


        //SI NO SE HA CREADO, CON ESTE IF LO CREARÁ 
        if(!miArchivo.exists()){
            try{
                miArchivo.createNewFile(); 
                System.out.println(miArchivo.getName() + " Ha sido creado. ");


            }catch(IOException ex){
                ex.printStackTrace();
            }
        }

        System.out.println("¿Nuestro documento se puede leer? " + miArchivo.canRead());
        System.out.println("Se puede escribir? " + miArchivo.canRead());
        System.out.println("Se puede ejecutar? " + miArchivo.canExecute());
        System.out.println("Es un directorio? " + miArchivo.isDirectory());
        System.out.println("Fecha de actualización: " + new java.util.Date(miArchivo.lastModified()));
        System.out.println("Tamaño del archivo: " + miArchivo.length());

    }
}
