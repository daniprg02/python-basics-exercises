import java.io.*;

public class LeerFichTextoBuf {
    public static void main(String[] args) {
        File fic = new File("fichero.txt");


        try {
            // Si no existe, lo creamos con contenido
            /*if (!fic.exists()) {
                try (BufferedWriter bw = new BufferedWriter(new FileWriter(fic))) {
                    bw.write("Hola, este es un fichero de prueba.\n");
                    bw.write("Segunda línea de texto.\n");
                }
                System.out.println("Archivo creado: " + fic.getAbsolutePath());
            }
            */
            // Ahora lo leemos
            try (BufferedReader fichero = new BufferedReader(new FileReader(fic))) {
                String linea;
                while ((linea = fichero.readLine()) != null) {
                    System.out.println(linea);
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
