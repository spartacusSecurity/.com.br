from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SPARTACUS Segurança Privada</title>
        <style>
            body { background-color: white; color: black; font-family: Arial, sans-serif; margin: 0; padding: 0; }
            header { background-color: black; color: white; padding: 20px; text-align: center; font-size: 28px; font-weight: bold; }
            .container { width: 90%; max-width: 1200px; margin: auto; text-align: center; padding: 40px 20px; }
            .logo img { width: 250px; margin: 20px 0; }
            h1 { color: black; font-size: 24px; margin-bottom: 20px; }
            .services { background-color: #f5f5f5; padding: 20px; border-radius: 10px; display: inline-block; text-align: left; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); }
            .services h2 { color: black; font-size: 22px; }
            .services ul { list-style: none; padding: 0; }
            .services li { background: #b71c1c; color: white; padding: 10px; margin: 8px 0; border-radius: 5px; font-size: 18px; transition: 0.3s; }
            .services li:hover { background: black; }
            .buttons { margin-top: 30px; }
            .button { display: inline-block; padding: 15px 40px; margin: 10px; font-size: 20px; font-weight: bold; color: white; background-color: black; border: none; border-radius: 8px; cursor: pointer; text-decoration: none; transition: 0.3s; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); }
            .button:hover { background-color: #b71c1c; }
            footer { background-color: black; color: white; text-align: center; padding: 15px; margin-top: 40px; font-size: 16px; }
        </style>
    </head>
    <body>
        <header>
            <div class="logo">
                <img src="/static/SEGURANÇA PRIVADA.png" alt="">
            </div>
            SPARTACUS SEGURANÇA
        </header>
        <div class="container">
            <div class="logo">
                <img src="/static/" alt="">
            </div>
            <h1>SPARTACUS SERVIÇOS DE APOIO E EVENTOS</h1>
            <div class="services">
                <h2>Serviços</h2>
                <ul>
                    <li>Serviços combinados para apoio a edifícios</li>
                    <li>Atividade de monitoramento de sistemas de segurança eletrônica</li>
                    <li>Serviços de organização de feiras, congressos, exposições e festas</li>
                </ul>
            </div>
            <div class="buttons">
                <a href="tel:1196368181" class="button">📞 Contato</a>
                <a href="https://www.google.com/maps/search/Rua+balaclava,+1066+-+jardim+santo+alberto+-+santo+andre+-+sp" target="_blank" class="button">📍 Endereço</a>
            </div>
        </div>
        <footer>
            <div class="logo">
            </div>
            </div>
            </div>
            </div>
            &copy; 2025 SPARTACUS Segurança - Todos os direitos reservados.
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

