//Leer un .txt 
//Termina cuando escriba "salir"
//Muestra cada línea convertida a mayúsculas en consola 

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;


class Ejercicios {
    public static void main(String[] args) {
        File archivo = null; 
        FileReader rd = null; 
        BufferedReader br = null;

        //Se supone que con este código no debería de estar en Finally, Java internamente se encarga de cerrarlos
        // try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
        //     String linea;
        //     while ((linea = br.readLine()) != null) {
        //         System.out.println(linea.toUpperCase());
        //     }
        // } catch (IOException e) {
        //     e.printStackTrace();
        // }


        try{

            archivo = new File("C:\\Users\\danie\\Desktop\\DAM\\JAVA\\Ejercicios01\\texto.txt"); 
            rd = new FileReader (archivo); 
            br = new BufferedReader(rd); 

            String linea; 
            while( (linea = br.readLine()) != null){
                //Si contiene la palabra "salir", no imprime la línea. Con equals compara la linea entera y da fallo.
                if(linea.contains("salir")) {
                    break; 
                } else {
                    System.out.println(linea.toUpperCase()); 
                }
            }

        }catch(IOException e){
            e.printStackTrace();
 
        }finally{
            try{
                if (br != null) br.close();
                if (rd != null) rd.close();
            } catch (IOException e2){
                e2.printStackTrace();
            }
        }
    }
}