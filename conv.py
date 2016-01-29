#!/usr/bin/python
from pprint import pprint
data = open('orgchart.txt').read()
ppl = []
current = []
lvl = 0
def dataadd(name, pos, boss, img):
    pic = img and img or "http://directory.visionoss.int/photos/%s.jpg" % name.lower().replace(' ','.', 1).replace(' ', '')
    return [{'v':name,'f':'%s<div style="color:red; font-style:italic"><img src="%s" />%s</div>'%(name, pic, pos)}, boss and boss or '', pos]

for line in data.split('\n'):
    if not line:
        break
    if line.startswith('-'):
        img = None
        lvl = len(line.split()[0].split('-'))
        name = line[lvl:].split(',')[0]
        pos=''
        if ',' in line:
            pos = line[lvl:].split(',')[1]

        if ',' in line and len(line.split(',')) >2:
            img = line[lvl:].split(',')[2]
        if lvl > len(current):
            current.append(name)
        elif lvl == len(current):
            current[lvl-1] = name
        elif lvl < len(current):
            current = current[0:lvl-1:]
            current.append(name)
        boss = current[lvl-2]
        ppl.append(dataadd(name, pos, boss, img))
    else:
        name = line.split(',')[0]
        pos = line.split(',')[1]
        current = [name]
        ppl.append(dataadd(name, pos, None, None))

fhl = open('index.html', 'w')

fhl.write("""<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {packages:["orgchart"]});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');

        // For each orgchart box, provide the name, manager, and tooltip to show.
        data.addRows(""")
fhl.write(str(ppl))
fhl.write("""        );

        // Create the chart.
        var chart = new google.visualization.OrgChart(document.getElementById('chart_div'));
        // Draw the chart, setting the allowHtml option to true for the tooltips.
        chart.draw(data, {allowHtml:true, allowCollapse:true});
      }
   </script>
    </head>
  <body>
    <div id="chart_div"></div>
  </body>
</html>""")
