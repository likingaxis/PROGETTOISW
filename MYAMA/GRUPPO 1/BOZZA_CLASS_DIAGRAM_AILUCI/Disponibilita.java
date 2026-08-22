import java.time.LocalDate;
import java.time.LocalTime;

public class Disponibilita {

	private LocalDate data;
	private LocalTime oraInizio;
	private LocalTime oraFine;

	// Disponibilita riferimenti inversi (navigabilità opzionale)
	// LavoratoreAMA 1 --- 0..* Disponibilita
	private LavoratoreAMA lavoratore;

	// SedeAMA 1 --- 0..* Disponibilita
	private SedeAMA sede;

	// Veicolo 1 --- 0..* Disponibilita
	private Veicolo veicolo;

}
