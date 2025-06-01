package git.Rodrigopalenske.backend_java.repository;

import git.Rodrigopalenske.backend_java.model.Candle;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CandleRepository extends JpaRepository<Candle, Long> {
}
