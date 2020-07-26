from flask import Flask, request, render_template

developer_name = 'Mucahit Koca'

def converter(num):
    times = {"second": 1000, "minute": 60000, "hour": 3600000}
    hour = num // times["hour"]
    num -= hour * times["hour"]
    minute = num // times["minute"]
    num -= minute * times["minute"]
    second = num // times["second"] 
    result = f"{hour} hour/s " * (hour!=0) + f"{minute} minute/s " * (minute!=0) + f"{second} second/s" * (second!=0) or f"just {num} millisecond/s" 
    return result

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main_page():
    return render_template('index.html', developer_name = developer_name)

@app.route('/', methods = ['POST'])
def convert():
    number = str(request.form["number"])

    if number.isdecimal():
        number = int(number)
        if number < 1:
            not_valid = True
            return render_template("index.html", developer_name = developer_name, not_valid = not_valid)
        else:
            return render_template("result.html", developer_name = developer_name, result = converter(number), milliseconds = number)
    else:
        not_valid = True
        return render_template("index.html", developer_name = developer_name, not_valid = not_valid)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
