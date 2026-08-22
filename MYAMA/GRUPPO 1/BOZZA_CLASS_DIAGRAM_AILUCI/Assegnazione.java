import java.time.LocalDate;

public class Assegnazione {

	private LocalDate dataAssegnazione;

	// Assegnazione * --- 1 AutistaAMA
	private AutistaAMA autista;

	// Assegnazione * --- 1 Veicolo
	private Veicolo veicolo;

	// RitiroDomicilio 1 --- 0..1 Assegnazione (riferimento inverso)
	private RitiroDomicilio ritiro;

}
