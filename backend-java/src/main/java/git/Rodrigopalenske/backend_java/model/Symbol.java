package git.Rodrigopalenske.backend_java.model;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Data
public class Symbol {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String description;

    private String market;

    private String weekDayInit;

    private LocalTime timeInit;

    private String weekDayEnd;

    private LocalTime timeEnd;

    @OneToMany(mappedBy = "symbol", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Candle> candles = new ArrayList<>();
}
