from flask import Flask, request,render_template
app = Flask(__name__)

@app.route('/')
def index2():
   return render_template('index2.html')

@app.route('/tampilnama')
def index3():
   nama = request.args.get('nama_mhs', "flask 2")
   return render_template('index3.html', nama=nama)

if __name__ == '__main__':
   app.run(debug = True)