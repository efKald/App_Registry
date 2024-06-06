import image1 from './color_folders.png'

function RegisterActivity () {
    return(
        <div>
            <h1>Registro de Actividades Diarias</h1>
            <br/><br/>
            <form>
                <table className="table-register">
                    <thead>
                        <tr>
                            <th colSpan="4">
                                <h2>Ingrese la Actividad</h2>
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
                        <tr>
                            <td>
                                <input/>
                            </td>
                            <td>
                                <input/>
                            </td>
                            <td>
                                <input/>
                            </td>
                            <td>
                                <input/>
                            </td>
                        </tr>
                    </tbody>
                </table>              
                <button> Registrar Actividad </button><br/><br/>
                <img src={image1} alt='color_folders' width="300" height="300"></img>
            </form>
        </div>
    )
}

export {RegisterActivity}