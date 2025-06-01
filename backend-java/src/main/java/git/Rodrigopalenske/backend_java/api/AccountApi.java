package git.Rodrigopalenske.backend_java.api;

import git.Rodrigopalenske.backend_java.model.Account;
import git.Rodrigopalenske.backend_java.service.AccountService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
@RequestMapping("api/account")
public class AccountApi {

    private final AccountService accountService;

    @GetMapping
    public ResponseEntity collectFromApi() {
        accountService.collectFromApi();
        return ResponseEntity.ok().build();
    }

}
