import java.util.List;

public class AmministratoreSedeAMA extends UtenteSistema {

	// SedeAMA 1 --- 0..* AmministratoreSedeAMA
	private SedeAMA sede;

	// AmministratoreSedeAMA 1 --- 0..* CodiceInvito
	private List<CodiceInvito> codiciInvito;

}
