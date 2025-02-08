from flask import Flask
import.random 
pipenv shell
 pip install pipenv
app = Flask(__name__)
facts_list = ["Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas","Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos", "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna]
@app.route("/")
 
def hello_world():
    return f'<h1>Hello, World!</h1>'
def index():
  return f'<h1>ver un dato randomizado!!</h1>'
@app.route("/random_fact")
def facts():
  return  f'<p>{random.choice(facts_list)}</p>'
app.run(debug=True)
