#encoding:utf-8


from users import app

if __name__ == '__main__':
    # print app.url_map
    app.run(host='0.0.0.0', port=9000, debug=True)
    #uwsgi --http 0.0.0.0:9000 --wsgi-file Manager.py --callable app --processes 4 --threads 4