#!/usr/bin/env python3
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL
############################################################################

from flask import (Flask, render_template, request, abort, )
from flask.json import jsonify
from datetime import datetime
import pytz
from time import sleep
from random import uniform

app = Flask(__name__)
############################################################################
LOCATIONS = {'Africa': ['Addis_Ababa', 'Blantyre', 'Djibouti',
                        'Tunis', 'Windhoek'],
             'America': ['Adak', 'Atka', 'Hermosillo', 'Menominee',
                         'New_York'],
             'Asia': ['Baku', 'Kabul', 'Jerusalem', 'Seoul', 'Tokyo'],
             'Australia': ['North', 'West', 'Sydney', 'South', 'Victoria'],
             'Europe': ['Prague', 'Berlin', 'Dublin', 'Kiev', 'Skopje'],
             }


@app.route('/calculate.json')
@app.route('/')
def index():
    c = '???'
    a = request.args.get('a')
    b = request.args.get('b')
    if a and b:
        try:
            c = float(a) + float(b)
        except:
            c = '???'
    if 'calculate' in request.path:
        return jsonify(result=c)
    else:
        return render_template('base.html', c=c)


@app.route('/time.json')
def makeAJAX():
    loc_timezone = pytz.timezone('Europe/Prague')
    loc_dt = loc_timezone.localize(datetime.now())
    data = {}
    location = request.args.get('location')
    if location is str:
        location = location.capitalize()
    # if location in LOCATIONS:
    #     for city in LOCATIONS[location]:
    #         timezone = pytz.timezone('{}/{}'.format(location, city))
    #         timezone_dt = loc_dt.astimezone(timezone)
    #         data[city] = timezone_dt.strftime('%H:%M:%S %Z%z')
    #     sleep(uniform(0.1, 1.8))
    #     return jsonify(data)

    if location in LOCATIONS:
        for timezone in pytz.common_timezones_set:
            if location in timezone:
                timezone_tz = pytz.timezone(timezone)
                timezone_dt = loc_dt.astimezone(timezone_tz)
                city = timezone[len(location)+1:]
                data[city] = timezone_dt.strftime('%H:%M:%S %Z%z')
        sleep(uniform(0.2, 1.1))
        return jsonify(location=location, data=data)
    return abort(400)


############################################################################
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
