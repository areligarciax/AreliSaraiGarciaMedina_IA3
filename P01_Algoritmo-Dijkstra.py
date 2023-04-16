import heapq
import networkx as nx
import matplotlib.pyplot as plt

grafo = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

def algoritmo_dijkstra(grafo, origen, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    padres = {nodo: None for nodo in grafo}

    vertices = [(0, origen)]
    G = nx.Graph()

    while vertices:
        actual = heapq.heappop(vertices)[1]

        if actual == destino:
            ruta = []
            while actual:
                ruta.append(actual)
                actual = padres[actual]
            ruta.reverse()
            print(f"La ruta más corta desde {origen} hasta {destino} es {ruta} con una distancia de {distancias[destino]}")
            return ruta

        for vecino, peso in grafo[actual].items():
            nueva_distancia = distancias[actual] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                padres[vecino] = actual
                heapq.heappush(vertices, (nueva_distancia, vecino))
                G.add_edge(actual, vecino, weight=peso)

        # Dibujar el grafo
        posicion = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, posicion, node_color='lightgreen', node_size=500)
        nx.draw_networkx_edges(G, posicion, edge_color='black')
        nx.draw_networkx_edge_labels(G, posicion, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
        nx.draw_networkx_labels(G, posicion, font_size=20, font_family='sans-serif')
        plt.axis('off')
        plt.show()
        plt.pause(2)

    print(f"No se encontró una ruta desde {origen} hasta {destino}")
    return None

algoritmo_dijkstra(grafo, 'A', 'F')