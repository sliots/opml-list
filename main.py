from lxml import etree

# 解析XML文件
tree = etree.parse('1.xml')
root = tree.getroot()

# 获取需要排序的节点列表
outlines = root.findall('.//outline[@type="rss"]')

# 根据ID进行排序
sorted_outlines = sorted(outlines, key=lambda x: int(x.get('xmlUrl').split('/')[-1]))

# 替换原始节点顺序
for i, outline in enumerate(sorted_outlines):
    parent = outline.getparent()
    parent.remove(outline)
    parent.insert(i, outline)

# 保存修改后的XML文件
tree.write('sorted_xml_file.xml', encoding='UTF-8', xml_declaration=True)
