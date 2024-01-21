from flask import Flask, render_template, request
from bin.Leibniz_pi import calculate_pi
from bin.pixelate import recreate_image_with_n_pixels
import math


app = Flask(__name__)
pie_img = "pie.png"


@app.route('/')
def pass_n():
    n = int(request.args.get('n', '1'))
    pie_file = recreate_image_with_n_pixels(pie_img, n)
    pi, time = calculate_pi(n)
    time = round(time, 6)
    pi = round(pi, 10)
    accuracy = round(100 - abs(math.pi - pi) / math.pi * 100, 8)
    return render_template('calculation.html', n=n, pi=pi, t=time, a=accuracy, filename=pie_file)


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
