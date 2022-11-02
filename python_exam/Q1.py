"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""

import pandas as pd
import os

def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        # Enter your code here
        root = 'D:\\Desktop\\Personal-Projects\\Applications_Resume\\IISc-BLR-Winter-Internship-2022\\transit-routing\python_exam'
        netfile = os.path.join(root,'ChicagoSketch_net.tntp')
        net = pd.read_csv(netfile, skiprows=8, sep='\t')
        trimmed= [s.strip().lower() for s in net.columns]
        net.columns = trimmed
        net.drop(['~', ';'], axis=1, inplace=True)
        print("The target dataframe is: ")
        print(net.head())
        graph_object = net 
        return graph_object
    except:
        return graph_object

def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        # Enter your code here
        print(shortest_path_distance)

        return shortest_path_distance
    except:
        return shortest_path_distance


