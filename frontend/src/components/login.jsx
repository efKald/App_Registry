

function Login () {
    return(
        <div id='log'>
            <h1>Ingreso</h1>
            <form action="/login_user" method="post">
                <label> Usuario </label> <input name="user"/><br/><br/>
                <label> Contraseña </label> <input name="password"/><br/><br/>
                <button> Ingresar </button><br/><br/>          
            </form>
        </div>
    )
}

export {Login}