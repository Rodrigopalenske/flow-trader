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
public class Trade {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String ticket;

    private LocalDateTime time;

    private String type;

    private Double volume;

    private BigDecimal priceOpening;

    private BigDecimal sl;

    private BigDecimal tp;

    private BigDecimal priceClosed;

    private BigDecimal profit;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "tick_id", nullable = false)
    private Tick tick;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "account_id", nullable = false)
    private Account account;

}
