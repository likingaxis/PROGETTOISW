import java.util.List;

public class Cittadino extends UtenteSistema {

	private String codiceFiscale;
	private String telefono;
	private String indirizzo;
	private String CAP;

	// 1 Cittadino --- 0..* Prenotazione
	private List<Prenotazione> prenotazioni;

}
