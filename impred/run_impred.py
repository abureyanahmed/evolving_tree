import matplotlib.pyplot as plt
import os

def draw_graph(edges, crd_x, crd_y):
  for e in edges:
    x = [crd_x[e[0]], crd_x[e[1]]]
    y = [crd_y[e[0]], crd_y[e[1]]]
    plt.plot(x, y)
  plt.show()

edges = []
f = open("evolving_math.txt", "r")
file_lines = f.read().split('\n')
f.close()
for ln in file_lines[:-1]:
  print(ln)
  token1, token2 = ln.split("--")
  vertex1 = token1.split('"')[1]
  vertex2 = token2.split('"')[1]
  edge = [vertex1, vertex2]
  edges.append(edge)

cnt = 0
label_to_id = dict()
for e in edges:
  if e[0] not in label_to_id.keys():
    label_to_id[e[0]] = cnt
    cnt += 1
  if e[1] not in label_to_id.keys():
    label_to_id[e[1]] = cnt
    cnt += 1

edges2 = []
for e in edges:
  edges2.append([label_to_id[e[0]], label_to_id[e[1]]])

input_file = "input.dot"
output_file = "output.dot"

def create_input_file(input_file, edge_list, crd_x, crd_y):
  f = open(input_file, 'w')
  f.write('strict graph "" {\n')
  for i, edge in enumerate(edge_list):
    if i==0:
      f.write(str(edge[0]) + ' [pos="' + str(crd_x[0]) + ',' + str(crd_y[0]) + '"];\n')
    f.write(str(edge[1]) + ' [pos="' + str(crd_x[i+1]) + ',' + str(crd_y[i+1]) + '"];\n')
    f.write(str(edge[0]) + ' -- ' + str(edge[1]) + ' [weight=1.0];\n')
  f.write('}\n')
  f.close()

def get_coordinates(output_file):
  crd_x = dict()
  crd_y = dict()
  f = open(output_file, 'r')
  f_lines = f.read().split('\n')
  for ln in f_lines:
    if 'pos' in ln:
      vertex, coordinate = ln.split(' ')
      v = int(vertex)
      x_str, y_str = coordinate.split('=')[1].split(']')[0][1:-1].split(',')
      crd_x[v] = float(x_str)
      crd_y[v] = float(y_str)
  f.close()
  crd_x_arr = []
  crd_y_arr = []
  for i in range(len(crd_x.keys())):
    crd_x_arr.append(crd_x[i])
    crd_y_arr.append(crd_y[i])
  return crd_x_arr, crd_y_arr

create_input_file(input_file, edges2[:1], [0, 0], [0, 1])

for i in range(1, 100):
  os.system("java -jar ImPred.jar --inputgraph='" + input_file + "' --edgenoderepulsion=10 --iterations=500 --outputfile='" + output_file + "'")
  crd_x, crd_y = get_coordinates(output_file)
  draw_graph(edges2[:i], crd_x, crd_y)
  create_input_file(input_file, edges2[:i+1], crd_x + [crd_x[edges2[i][0]]+.000001], crd_y + [crd_y[edges2[i][0]]+.000001])

