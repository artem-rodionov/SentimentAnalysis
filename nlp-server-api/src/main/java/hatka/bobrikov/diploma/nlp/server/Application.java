package hatka.bobrikov.diploma.nlp.server;

import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * @author Artem
 * @created 14.05.2024 1:14
 */
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        try {
            org.springframework.boot.SpringApplication.run(Application.class, args);
        } catch (Throwable e) {
            e.printStackTrace();
        }
    }
}
