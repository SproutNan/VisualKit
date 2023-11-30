# 命令行交互式创建
import os, sys, csv
import colorsys

def generate_rainbow_colors(n, alpha=1):
    colors = []
    for i in range(n):
        # 计算色相，等间隔采样
        hue = i / n
        # 将HSL转换为RGB，这里固定饱和度和亮度
        rgb = colorsys.hls_to_rgb(hue, 0.5, 1)
        # 将RGB转换为RGBA
        rgba = f'rgba({int(rgb[0]*255)}, {int(rgb[1]*255)}, {int(rgb[2]*255)}, {alpha})'
        colors.append(rgba)
    return colors

if __name__ == "__main__":
    # 使用方法：python setup.py [datafile.csv]
    if len(sys.argv) < 2:
        print("Usage: python setup.py [datafile.csv]")
        sys.exit(1)

    datafile = sys.argv[1]
    # 格式：第一列x，第二列y，第三列颜色，第四列大小，第五列标签   没有表头
    with open(datafile, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        x, y = [float(row[0]) for row in rows], [float(row[1]) for row in rows]
        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        x_range, y_range = x_max - x_min, y_max - y_min
        # 把颜色收录进一个set，然后建立从颜色到编号的映射
        colors = list(set([row[2] for row in rows]))
        color_use = generate_rainbow_colors(len(colors))
        color_to_id = {color: i for i, color in enumerate(colors)}
        # 大小：暂时默认
        point_num = len(rows)
        points = []
        for i in range(point_num):
            points.append('{ ' + f"name: '{rows[i][4]}', color: '{color_use[color_to_id[rows[i][2]]]}', data: [[{rows[i][0]}, {rows[i][1]}]]" + '}')

        with open("template.html", 'r') as f:
            template = f.read()
            template = template.replace("//TITLE//", datafile[:-4])
            template = template.replace("//SUBTITLE//", "我是副标题")
            template = template.replace("//XMIN//", str(x_min-x_range//10))
            template = template.replace("//XMAX//", str(x_max+x_range//10))
            template = template.replace("//YMIN//", str(y_min-y_range//10))
            template = template.replace("//YMAX//", str(y_max+y_range//10))
            template = template.replace("//INTX//", str(x_range//10))
            template = template.replace("//INTY//", str(y_range//10))
            template = template.replace("//POINTS//", ',\n'.join(points))

            with open(f"./projects/{datafile[:-4]}" + ".html", 'w') as f:
                f.write(template)
                print(f"Successfully created {datafile[:-4]}" + ".html")    

        