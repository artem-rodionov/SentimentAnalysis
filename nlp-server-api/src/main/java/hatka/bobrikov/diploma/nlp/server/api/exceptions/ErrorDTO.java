package hatka.bobrikov.diploma.nlp.server.api.exceptions;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;
import lombok.experimental.FieldDefaults;
/**
 * @author Artem
 * @created 16.05.2024 18:46
 */

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
public class ErrorDTO {

    String error;

    @JsonProperty("error_description")
    String errorDescription;
}
