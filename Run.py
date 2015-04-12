from flask import Flask,render_template,request
import os
import matplotlib.patches
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',title="Python Assignment")

@app.route('/about.html')
def about():
    return render_template('about.html',title="About")

@app.route('/rs.html')
def rs():
    return render_template('rs.html',title="Rishabh Sinha")

@app.route('/rj.html')
def rj():
    return render_template('rj.html',title="Rishabh Jain")

@app.route('/gj.html')
def gj():
    return render_template('gj.html',title="Gaurav Kumar Jaiswal")

@app.route('/q2.html')
def q2():
    return render_template('q2.html',title="Question 2")

@app.route('/int.html',methods=['GET', 'POST'])
def integrate():
    a = None
    b = None
    n = None
    fn = None
    sol = None
    k = None
    if request.method == 'POST' and 'a' in request.form and 'b' in request.form and 'n' in request.form and 'fn' in request.form:
        a = request.form['a']
        b = request.form['b']
        n = request.form['n']
        # fn = request.form['fn']
        fn = lambda x: eval(request.form['fn'])
        a = float(a)
        b = float(b)
        n=float(n)
        k = (b-a) / n
        sol = fn(a)
        q = []
        n=int(n)
        for i in range(1,n):
            i = float(i)
            q.append(i)
        for i in q:
            sol += 2 * fn(a + (i * k))
        sol = sol + fn(b)
        a = int(a)
        b = int(b)
        sol = (sol * k) / 2
        import matplotlib.pyplot as pt  # import plotting library
        from numpy import arange
        fig=pt.figure()


        x = [i for i in arange(a, b, (b - a) / (n * 1000.0))]  # list of values between a and b
        x = x + [b]
        y = [i for i in arange(a, b, (b - a) / (n * 1.0))]  # list of values of x
        y = y + [b]
        z = [fn(i) for i in x]  # list of function values
        pt.plot(x, z)  # plotting the curve
        for i in range(n + 1):
            pt.plot([y[i], y[i]], [0, fn(y[i])])  # parallel sides of the trapezium
        for i in range(n):
            pt.plot([y[i], y[i + 1]], [fn(y[i]), fn(y[i + 1])])  # non-parallel sides of trapezium
        #pt.show()  #output
        pt.axvline(0,color="k")
        pt.axhline(0,color="k")
        if os.path.exists("E:\\flaskapp\\app\\static\\graph.png"):
            os.remove("E:\\flaskapp\\app\\static\\graph.png")
            pt.savefig("E:\\flaskapp\\app\\static\\graph.png", dpi=fig.dpi)
        else :
            pt.savefig("E:\\flaskapp\\app\\static\\graph.png", format="png", dpi=fig.dpi)
    return render_template('int.html', sol=sol,title="Integrate" )

@app.route('/avg.html',methods=['GET', 'POST'])
def avg():
    a=None
    b=None
    c=None
    d=None
    e=None
    ans=None
    if request.method == 'POST' and 'a' in request.form and 'b' in request.form and 'c' in request.form and 'd' in request.form and 'e' in request.form:
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        e = request.form['e']
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        ans=(a+b+c+d+e)/5
    return render_template('avg.html',ans=ans)

if __name__ == '__main__':
  app.run(debug=True)
