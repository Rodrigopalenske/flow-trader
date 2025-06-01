package git.Rodrigopalenske.backend_java.repository;

import git.Rodrigopalenske.backend_java.model.Trade;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TradeRepository extends JpaRepository<Trade, Long> {
}
