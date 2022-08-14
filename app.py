from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def regex():
    if request.method=='POST':
        input_1 = request.form['input_1']
        input_2 = request.form['input_2']
        lst = []
        for i in range(len(input_1)):
            lst.append(input_1[i:i+len(input_2)])

        lst1 = []
        for j in range(len(lst)):
            if lst[j] == input_2:
                lst1.append(j)
        
        count = len(lst1)

        return render_template('index.html', count=count, lst1=lst1)
    
    return render_template('index.html', count=-1)

if __name__ == '__main__':
    app.run(debug=True)