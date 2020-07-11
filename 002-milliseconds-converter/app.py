from flask import Flask, request, render_template

developer_name = 'Mucahit Koca'

def converter(num):
    times = {"second": 1000, "minute": 60000, "hour": 3600000}
    if num < 1000:
        result = f"just {num} milisecond/s"
        return result
    else:
        hour = num // times["hour"]
        num -= hour * times["hour"]
        minute = num // times["minute"]
        num -= minute * times["minute"]
        second = num // times["second"] 
        if hour == 0:
            hour = "" 
        else:
            hour = str(hour) + " hour/s "  
        if minute == 0:
            minute = "" 
        else:
            minute = str(minute) + " minute/s "
        if second == 0:
            second = "" 
        else:
            second = str(second) + " second/s"
        result = f"{hour}{minute}{second}" 
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
