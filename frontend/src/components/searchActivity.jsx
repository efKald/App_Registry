import image2 from './db_report.png'

function SearchActivity () {
    return(
        <div>
            <h1>Consulta de Actividades de Usuario</h1>
            <br/><br/>
            <form>
                <label> Consultar Usuario </label> <input />
                <br/><br/>
                <button> Consultar </button>
            </form>
            <br/><br/>
            <table className="table-consult">
                    <thead>
                        <tr>
                            <th colSpan="4">
                                Actividad
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <p>Hora Inicial</p>
                            </td>
                            <td>
                                <p>Hora  Final</p>
                            </td>
                            <td>
                                <p>Actividad</p>
                            </td>
                            <td>
                                <p>Descripción</p>                      
                            </td>
                        </tr>
                    </tbody>
                </table>
                <img src={image2} alt='cdb_report' width="300" height="300"></img>
        </div>
    )
}

export {SearchActivity}