#scrivere una pagina html/flask che visualizzi l'elenco delle regioni in un menu a tendina

from flask import Flask, render_template, request , jsonify
app = Flask(__name__)


@app.route('/')
@app.route('/select')
def select():
    import pandas as pd
    df=pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    nomi=df['denominazione_regione']
    nomi=nomi.drop_duplicates()
    return render_template('htend.html', tab=nomi)


@app.route('/ret', methods=['GET'])
def info():
    import pandas as pd
    regione=request.args['regione']
    df=pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    info=df[df.denominazione_regione == regione]
    info=info.drop_duplicates()
    return render_template('reg.html' ,tabella= info.to_html())












if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)