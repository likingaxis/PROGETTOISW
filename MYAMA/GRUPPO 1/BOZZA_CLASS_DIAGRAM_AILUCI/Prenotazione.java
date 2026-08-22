import java.time.LocalDate;

public abstract class Prenotazione {

	private int idPrenotazione;
	private LocalDate data;
	private String fasciaOraria;
	private String stato;

	// Prenotazione 1 --- 1 Rifiuto
	private Rifiuto rifiuto;

	// Cittadino 1 --- 0..* Prenotazione (riferimento inverso)
	private Cittadino cittadino;

	// Prenotazione 1 --- 0..1 Valutazione
	private Valutazione valutazione;

}
