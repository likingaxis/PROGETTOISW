import java.util.List;

public class Veicolo {

	private int idVeicolo;
	private String targa;
	private double capacitaPeso;
	private double capacitaVolume;

	// Veicolo 1 --- 0..* Disponibilita
	private List<Disponibilita> disponibilita;

	// Assegnazione * --- 1 Veicolo
	private List<Assegnazione> assegnazioni;

	// SedeAMA 1 --- 0..* Veicolo (riferimento inverso)
	private SedeAMA sede;

}
