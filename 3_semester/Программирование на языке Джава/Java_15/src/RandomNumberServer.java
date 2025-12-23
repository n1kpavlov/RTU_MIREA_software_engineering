import java.io.*;
import java.net.*;
import java.util.Random;

public class RandomNumberServer {

    private static final int PORT = 2424;
    private static final Random random = new Random();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Random number server started on port " + PORT);

            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                     PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                    String line = in.readLine();
                    if (line == null || !line.startsWith("GET")) continue;

                    String query = line.split(" ")[1];

                    if (!query.contains("?")) {
                        sendError(out, 400, "<html><body><h1>Invalid request format</h1></body></html>");
                        continue;
                    }

                    String[] params = query.split("\\?");
                    String[] queryParameters = params[1].split("&");

                    int min = -1, max = -1;
                    for (String param : queryParameters) {
                        String[] parts = param.split("=");
                        if (parts.length == 2) {
                            String key = parts[0];
                            String value = parts[1];

                            if (key.equals("min")) {
                                try {
                                    min = Integer.parseInt(value);
                                } catch (NumberFormatException e) {
                                    sendError(out, 400, "<html><body><h1>Invalid 'min' parameter</h1></body></html>");
                                    return;
                                }
                            } else if (key.equals("max")) {
                                try {
                                    max = Integer.parseInt(value);
                                } catch (NumberFormatException e) {
                                    sendError(out, 400, "<html><body><h1>Invalid 'max' parameter</h1></body></html>");
                                    return;
                                }
                            }
                        }
                    }

                    if (min == -1 || max == -1) {
                        sendError(out, 400, "<html><body><h1>Missing parameters</h1></body></html>");
                        continue;
                    }

                    if (min > max) {
                        sendError(out, 400, "<html><body><h1>Min cannot be greater than Max</h1></body></html>");
                        continue;
                    }

                    int randomNumber = random.nextInt(max - min + 1) + min;
                    StringBuilder message = new StringBuilder();
                    message.append("<html><body><h1>Nikita Pavlov chose the number ");
                    message.append(randomNumber);
                    message.append("<h1></body></html>");
                    sendResponse(out, message.toString());

                } catch (IOException e) {
                    System.err.println("Error handling client: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Error starting server: " + e.getMessage());
        }
    }

    private static void sendResponse(PrintWriter out, String message) {
        out.println("HTTP/1.1 200 OK");
        out.println("Content-Type: text/html");
        out.println("Content-Length: " + message.length());
        out.println();
        out.println(message);
    }

    private static void sendError(PrintWriter out, int statusCode, String message) {
        out.println("HTTP/1.1 " + statusCode + " OK");
        out.println("Content-Type: text/html");
        out.println("Content-Length: " + message.length());
        out.println();
        out.println(message);
    }
}
