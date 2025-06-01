package git.Rodrigopalenske.backend_java.service;

import git.Rodrigopalenske.backend_java.repository.AccountRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AccountService {

    @Autowired
    private AccountRepository accountRepository;

    @Autowired
    private RestTemplate restTemplate;

    private volatile boolean isCollecting = false;

    private String currentAccountCode;

    public void collectFromApi() {
        String apiUrl = "http://localhost:8082/accounts/";
        try {
            ResponseEntity<String> response = restTemplate.getForEntity(apiUrl, String.class);
            System.out.println(response.getBody());
        } catch (Exception e) {
            System.out.println("API call failed: " + e.getMessage());
            throw new RuntimeException("API call failed: " + e.getMessage(), e);
        }
    }
}
