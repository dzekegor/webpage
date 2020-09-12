from flask import Flask, request, render_template,redirect, url_for, flash, make_response
import socket
import os
app = Flask(__name__,static_folder="static",template_folder="jinja_templates")
@app.route('/')
def index():
    if not request.cookies.get('joined'):
        return render_template("index.html",name=socket.gethostbyname(os.environ.get("HOSTNAME")))
        #return render_template("index.html",name=os.environ.get('HOSTNAME'))
    else:
        return render_template("join.html",name=socket.gethostbyname(os.environ.get("HOSTNAME")))
        #return render_template("join.html",name=os.environ.get("HOSTNAME"))
@app.route('/join/', methods=['post', 'get'])
def join():
    if request.method == 'POST':
        joined = request.form.get('join')
        print(joined)
        if joined == "on":
            print(request.cookies.get('joined') is None)
            if request.cookies.get('joined') is None:
                res = make_response(redirect("/join/"))
                res.set_cookie('joined', 'true', 60*60*24)
                return res
            return render_template("join.html",name=socket.gethostbyname(os.environ.get("HOSTNAME")))
            #return render_template("join.html",name=os.environ.get("HOSTNAME"))
        else:
            res = make_response(redirect("/join/"))
            res.set_cookie('joined', 'true', 0)
            return render_template("not_joined.html",name=socket.gethostbyname(os.environ.get("HOSTNAME")))
            #return render_template("not_joined.html",name=os.environ.get("HOSTNAME"))
    else:
        if request.cookies.get('joined') is None:
            res = make_response(redirect("/join/"))
            res.set_cookie('joined', 'true', 0)
            return render_template("not_joined.html",name=socket.gethostbyname(os.environ.get("HOSTNAME")))
            #return render_template("not_joined.html",name=os.environ.get("HOSTNAME"))
        else:
            return render_template("join.html",name=socket.gethostbyname(os.environ.get("HOSTNAME")))
            #return render_template("join.html",name=os.environ.get("HOSTNAME"))
@app.errorhandler(404)
def http_404_handler(error):
    return render_template("error404.html")
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)
