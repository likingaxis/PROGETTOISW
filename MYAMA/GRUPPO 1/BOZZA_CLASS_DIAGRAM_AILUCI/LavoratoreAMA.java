import java.util.List;

public abstract class LavoratoreAMA extends UtenteSistema {

	private String idDipendente;
	private String telefono;

	// 1 LavoratoreAMA --- 0..* Disponibilita
	private List<Disponibilita> disponibilita;

}
