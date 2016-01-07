import os

class HtmlOutputer() :
    def __init__(self) :
        self.data = []

    def collect_data(self, data) :
        if data == None :
            return
        self.data.append(data)

    def output_html(self, file_name) :
        dir_path = os.path.dirname(file_name)
        if len(dir_path) != 0 :
            os.makedirs(dir_path)

        f = open(file_name, 'w')

        f.write('<html>')
        f.write('<body>')
        f.write('<table border="8">')

        for item in self.data :
            f.write('<tr>')
            f.write('<td>%s</td>' % (item['url'].encode('utf-8')))
            f.write('<td>%s</td>' % (item['title'].encode('utf-8')))
            f.write('<td>%s</td>' % (item['summary'].encode('utf-8')))
            f.write('</tr>')

        f.write('</table>')
        f.write('</body>')
        f.write('</html>')

        f.close()
