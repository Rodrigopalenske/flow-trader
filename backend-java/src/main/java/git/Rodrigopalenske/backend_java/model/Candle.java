package git.Rodrigopalenske.backend_java.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Candle {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private LocalDateTime timestamp;

    private String timeframe;

    private BigDecimal open;

    private BigDecimal hight;

    private BigDecimal low;

    private BigDecimal close;

    @ManyToOne
    @JoinColumn(name = "symbol_id", nullable = false)
    private Symbol symbol;

    @OneToMany(mappedBy = "candle", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Tick> ticks = new ArrayList<>();
}
