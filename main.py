import subprocess
import os
from config import sites, delete_files, result_file_name


def write_result_graph_file(node_set):
    uiq_node_file = open('./uiq.txt', 'w+')
    uiq_node_file.write('digraph G {\n')

    sorted_set = sorted(node_set)
    for node in sorted_set:
        uiq_node_file.write(node)
    uiq_node_file.write('}\n')
    uiq_node_file.close()


def write_graph_file(site, graph, node_set):
    print('Creating trace graph to %s-graph.txt ...' % site)
    # Opening the graph file
    graph_path = './%s-graph.txt' % site
    site_graph_writer = open(graph_path, 'w+')

    # Writing graph structure to the graph file
    site_graph_writer.write('digraph G {\n')
    node_format = '\t"%s" -> "%s"\n'
    for i in range(0, len(graph) - 1):
        node = node_format % (graph[i], graph[i + 1])
        site_graph_writer.write(node)
        node_set.add(node)
    node = node_format % (graph[len(graph) - 1], site)
    site_graph_writer.write(node)
    node_set.add(node)
    site_graph_writer.write('}\n')
    site_graph_writer.close()

    print('Done Creating trace graph to %s-graph.txt' % site)


def valid_ip(ip):
    nums = ip.split('.')
    if len(nums) != 4:
        return False
    for x in nums:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def site_trace_list(site):
    print('Writing result to %s.txt ...' % site)
    # Creating a file for tracert command output
    site_file_path = './%s.txt' % site
    site_file = open(site_file_path, 'w+')

    # Running tracert command to the site
    subprocess.run(['tracert', '-d', site], stdout=site_file)

    # List of output ips
    graph = []

    # Opening a file for the output graph
    file = open(site_file_path, 'r')

    # Getting out the ips
    for line in file:
        line = line.rstrip()    # Delete whitespaces at the end
        if len(line) > 1:
            last_word = line[line.rindex(' '):]
            ip = last_word.lstrip()
            if valid_ip(ip):
                graph.append(ip)

    file.close()
    print('Done Writing tracert result to %s.txt' % site)

    return graph


def main():
    node_set = set()
    for site in sites:
        print('Tracing %s ...' % site)

        graph = site_trace_list(site)
        write_graph_file(site, graph, node_set)

        print('Done Tracing %s' % site)

    write_result_graph_file(node_set)

    # Draw result graph to pdf file
    os.system('dot ./uiq.txt -Tpdf -o %s.pdf' % result_file_name)

    if delete_files:
        for site in sites:
            os.remove('%s.txt' % site)
            os.remove('%s-graph.txt' % site)
            os.remove('uiq.txt')


if __name__ == "__main__":
    main()
