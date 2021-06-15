def stablity(x_coords, y_coords, time_indices, scale, crd_x, crd_y):
  gs = 0
  gc = 0
  for node in x_coords[str(time_indices[-1])]:
    s = 0
    c = 0
    for t in time_indices:
      if node in x_coords[str(t)]:
        if str(t-1) in x_coords.keys() and node in x_coords[str(t-1)]:
          s += math.sqrt((x_coords[str(t)][node]-x_coords[str(t-1)][node])**2+(y_coords[str(t)][node]-y_coords[str(t-1)][node])**2)
          c += 1
    gs += s
    gc += 1

  label_area = 0
  for u in crd_x.keys():
    #print(u, G.nodes[u])
    cur_len = len(id_to_labels[u])
    label_len[u] = cur_len
    label_area += 0.6*scale*scale*cur_len
  total_area = (max(list(crd_x.values()))-min(list(crd_x.values())))*(max(list(crd_y.values()))-min(list(crd_y.values())))

  return (gs/gc)/total_area
