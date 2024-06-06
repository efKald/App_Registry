import Express from 'express' 
import Path from 'path' //Gets the pasth of current project folder. Better to use this one in case fodler is saved on another device path.
//Starting server with node.js backend. Insted of using npm start for react(frontend) server. FrontEnd running with the backend.
//npm install -g nodemon powershell Set-ExecutionPolicy Unrestricted
//npm run build to run the build of the front end, optimized for deployment.

const app = Express()
const dir = Path.resolve()
const dir_front = "frontend/build"
app.use(Express.static(dir_front))
app.use(Express.json())
app.use(Express.urlencoded({}))

app.listen ('5000', function(){
    console.log("Server has started.")
})

app.get('/', function(req, res){
    console.log(dir)
    res.sendFile(dir + "/" + dir_front + "/index.html")
})

app.get("/home", function(req, res){
    res.sendFile(dir + "/" + dir_front + "/index.html")
})

app.get("/login", (req, res)=>{
    res.sendFile(dir + "/" + dir_front + "/index.html")
})

app.get("/register", (req, res)=>{
    res.sendFile(dir + "/" + dir_front + "/index.html")
})

app.get("/search", (req, res)=>{
    res.sendFile(dir + "/" + dir_front + "/index.html")
})
//React(frontend) is making the pipeline.

app.post("/login_user", (req, res)=>{
    let {user, password} = req.body
    console.log(user + " " + password)
    res.redirect("/")
})