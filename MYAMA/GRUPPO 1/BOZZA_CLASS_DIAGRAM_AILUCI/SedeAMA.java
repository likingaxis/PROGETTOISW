import java.util.List;

public class SedeAMA {

	private int idSede;
	private String nome;
	private String indirizzo;

	// SedeAMA * --- * ZonaCAP
	private List<ZonaCAP> zoneCAP;

	// SedeAMA 1 --- 0..* OperatoreSedeAMA
	private List<OperatoreSedeAMA> operatori;

	// SedeAMA 1 --- 0..* AmministratoreSedeAMA
	private List<AmministratoreSedeAMA> amministratori;

	// SedeAMA 1 --- 0..* Veicolo
	private List<Veicolo> veicoli;

	// SedeAMA 1 --- 0..* Disponibilita
	private List<Disponibilita> disponibilita;

	// SedeAMA 1 --- 0..* ConferimentoSede
	private List<ConferimentoSede> conferimenti;

	// SedeAMA 1 --- 0..* RitiroDomicilio
	private List<RitiroDomicilio> ritiri;

}
