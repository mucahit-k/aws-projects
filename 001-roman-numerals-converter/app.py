from flask import Flask, request, render_template
import requests

ip_address = requests.get('https://checkip.amazonaws.com').text.strip()
developer_name = 'Mucahit Koca'

roman_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

app=Flask(__name__)


@app.route('/', methods = ['GET'])
def main_page():
    return render_template('index.html', developer_name = developer_name)

@app.route('/', methods = ['POST'])
def convert():
    number = str(request.form['number'])

    if number.isnumeric():
        if int(number) > 0 and int(number) < 4000:
            roman_list = []
            num = int(number)
            for i in range(len(roman_nums)):
                rom = num // roman_nums[i]
                num = num % roman_nums[i]
                value = rom * roman_values[i]
                roman_list.append(value)
            roman_value = ''.join(roman_list)
            return render_template('result.html',developer_name = developer_name, number_decimal = number, number_roman = roman_value)
        else:
            not_valid = True
            return render_template('index.html', not_valid = not_valid, developer_name = developer_name)
    else:
        not_vali d = True
        return render_template('index.html', not_valid = not_valid, developer_name = developer_name)

if __name__ == '__main__':
    app.run(host:'0.0.0.0', port=80)