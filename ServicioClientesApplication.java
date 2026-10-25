import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class ServicioClientesApplication {

    public static void main(String[] args) throws IOException {
        HttpServer servidor = HttpServer.create(new InetSocketAddress(8080), 0);
        servidor.createContext("/api/clientes/estado", new ManejadorClientes());
        servidor.setExecutor(null);
        System.out.println("=== MICROSERVICIO DE CLIENTES ACTIVADO ===");
        System.out.println("Escuchando peticiones en http://localhost:8080/api/clientes/estado");
        servidor.start();
    }

    static class ManejadorClientes implements HttpHandler {
        @Override
        public void handle(HttpExchange intercambio) throws IOException {
            String respuestaJson = "{\"cliente_id\": 5001, \"estado\": \"Activo\", \"limite_credito\": 15000}";
            intercambio.getResponseHeaders().set("Content-Type", "application/json");
            intercambio.sendResponseHeaders(200, respuestaJson.length());
            OutputStream cuerpo = intercambio.getResponseBody();
            cuerpo.write(respuestaJson.getBytes());
            cuerpo.close();
        }
    }
}
