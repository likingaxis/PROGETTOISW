public class RitiroDomicilio extends Prenotazione {

	private String indirizzoRitiro;

	// RitiroDomicilio * --- 1 SedeAMA
	private SedeAMA sede;

	// RitiroDomicilio 1 --- 0..1 Assegnazione
	private Assegnazione assegnazione;

}
