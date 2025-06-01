package git.Rodrigopalenske.backend_java.repository;

import git.Rodrigopalenske.backend_java.model.Account;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AccountRepository extends JpaRepository<Account, Long> {
}
