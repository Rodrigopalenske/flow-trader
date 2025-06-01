package git.Rodrigopalenske.backend_java.repository;

import git.Rodrigopalenske.backend_java.model.Symbol;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SymbolRepository extends JpaRepository<Symbol, Long> {
}
