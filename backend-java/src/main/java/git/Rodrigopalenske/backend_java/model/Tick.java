package git.Rodrigopalenske.backend_java.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Tick {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime timestamp;

    private double bid;

    private double ask;

    @ManyToOne
    @JoinColumn(name = "candle_id", nullable = false)
    private Candle candle;

    @OneToMany(mappedBy = "tick", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Trade> Trade = new ArrayList<>();
}
