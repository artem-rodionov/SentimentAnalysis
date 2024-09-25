package hatka.bobrikov.diploma.nlp.server.api.controllers;

import hatka.bobrikov.diploma.nlp.server.api.dto.ResultDTO;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.example.MLServiceGrpc;
import org.example.MLServiceOuterClass;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


import javax.transaction.Transactional;

/**
 * @author Artem
 * @created 16.05.2024 18:02
 */

@Log4j2
@RestController
@RequiredArgsConstructor
@Transactional
public class SentimentAnalysisController {

    private final String TARGET = "localhost:50051";
    private final ManagedChannel channel = ManagedChannelBuilder.forTarget(TARGET)
            .usePlaintext()
            .build();

    private final MLServiceGrpc.MLServiceBlockingStub stub = MLServiceGrpc.newBlockingStub(channel);

    public static final String GET_API_TELECOM = "/api/telecom";

    @PostMapping(GET_API_TELECOM)
    public ResultDTO getSentiment(@RequestParam String text) {

        MLServiceOuterClass.MLRequest request = MLServiceOuterClass.MLRequest
                .newBuilder()
                .setText(text)
                .build();

        log.info("sent: " + text);

        MLServiceOuterClass.MLResponse response = stub.classify(request);

        log.info("received: " + response);

        return new ResultDTO(response.getText(), response.getLabel(), response.getScore());
    }


}
