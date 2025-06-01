package git.Rodrigopalenske.backend_java.repository;

import git.Rodrigopalenske.backend_java.model.Tick;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TickRepository extends JpaRepository<Tick, Long> {
}
