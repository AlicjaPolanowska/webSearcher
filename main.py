# This is a sample Python script.
import dfs
import content
import time
import cProfile
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def graph_from_page(root: str, page: str):
    graph = dfs.Graph()
    graph.add_vertex(root, None)
    hrefs = content.get_page_hrefs(page)
    for y in hrefs:
        idx = graph.add_vertex(y, 0)
        # if idx == -1:
        #     continue
        # page_inner = content.read_url(y)
        # hrefs_inner = content.get_page_hrefs(page_inner)
        # for z in hrefs_inner:
        #     graph.add_vertex(z, idx)
    return graph


def find_occurrences(graph, target_value):
    found = []
    for current_vertex in graph:
        current_content = content.plain_text_from_html(content.read_url(current_vertex.url))
        if current_content is None:
            continue
        found_index = current_content.find(target_value)
        if found_index != -1:
            found.append(f'I found value {target_value} at page {current_vertex} at possition {found_index}. The text: {current_content[found_index:found_index+len(target_value)+10]}')
    return found


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    url = 'https://www.onet.pl'
    page = content.read_url(url)
    g = graph_from_page(url, page)
    #start = time.time()
    print(g)
    #end = time.time()
    #print(end-start)
    #print(len(g.vertices))
    # print(find_occurrences(g, 'Kaczyński'))
    #cProfile.run('print(g)')
    #0.0030341148376464844
    #dfs.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
