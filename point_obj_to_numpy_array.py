listarray = []
for pp in points_list:
    listarray.append([pp.x, pp.y])

pts_array = np.array(listarray)

return pts_array
