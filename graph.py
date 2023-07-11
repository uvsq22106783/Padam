from __future__ import annotations, print_function
from inspect import _empty
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


class Graph:
    def __init__(self, vertices: list[tuple], edges: list[tuple]):
        """
        Parameters
        ----------
        vertices : list[tuple]
            list of vertices coordinates.
        edges : list[tuple]
            list of edges as tuple (id 1, id 2, weight, coordinates 1, coordinates 2).
        """
        self.vertices = vertices
        self.edges = edges
        self.adjacence = self.adjacence()

    def plot(self):
        """
        Plot the graph.
        """
        weights = list(set(edge[2] for edge in self.edges))
        colors = plt.cm.get_cmap("viridis", len(weights))
        _, ax = plt.subplots()
        for i, weight in enumerate(weights):
            lines = [[edge[-2][::-1], edge[-1][::-1]] for edge in self.edges if edge[2] == weight]
            ax.add_collection(LineCollection(lines, colors=colors(i), alpha=0.7, label=f"weight {weight}"))
        ax.plot()
        ax.legend()
        plt.title(f"#E={len(self.edges)}, #V={len(self.vertices)}")
        plt.show()

    def adjacence(self):

        adjacence = {}
        for edge in self.edges:
            vertex1, vertex2, _, _, _ = edge
            if vertex1 not in adjacence:
                adjacence[vertex1] = []
            if vertex2 not in adjacence:
                adjacence[vertex2] = []
            adjacence[vertex1].append(vertex2)
            adjacence[vertex2].append(vertex1)
        return adjacence

    def connexe(self):

      visited = set()
      stack = []

      start_node = 0
      stack.append(start_node)

      while stack:
          node = stack.pop()
          visited.add(node)

          for neighbor in self.adjacence[node]:
              if neighbor not in visited:
                  stack.append(neighbor)

      return len(visited) == len(self.vertices)
      
    def eulerien(self):

      if self.connexe() == False:
        return -1
      else:
        impair=0
        noeud_impair=0
        for i in self.adjacence:
          if (len(self.adjacence[i]) % 2 != 0):
            impair=impair+1
            noeud_impair=i
            if impair>2:
              return len(self.adjacence)
        if impair==0:
          #print("graphe eulerien \n")
          return 0 
        else:
          print("chaine eulerienne \n")
          return noeud_impair      

   
    def chaine_eulerienne_poids_min(self):
        
        eulerien = self.eulerien()
        if eulerien == -1:
            print("graphe non connexe \n")
            return []
        elif eulerien == len(self.adjacence):
            print("graphe non eulerien \n")
            return []
        
        eulerian_path = []
        stack = []
        current_vertex = eulerien
        stack.append(current_vertex)
        
        
        while stack:
            if not self.adjacence[current_vertex]:
                eulerian_path.append(current_vertex)
                current_vertex = stack.pop()
            else:
                next_vertex = self.adjacence[current_vertex][0]
                eulerian_path.append(current_vertex)
                self.adjacence[current_vertex].remove(next_vertex)
                self.adjacence[next_vertex].remove(current_vertex)
                stack.append(next_vertex)
                current_vertex = next_vertex
        poids = 0
        chain = eulerian_path  
        for i in range(len(chain) - 1):
            weight = self.get_edge_weight(chain[i], chain[i + 1])
            if weight is not None: 
                poids += weight        
        print("poids", poids)
        print("liste eulerienne",eulerian_path)
        
        return eulerian_path, poids
        

    def get_edge_weight(self, u, v):
      
      min_weight = float('inf')
      
      for edge in self.edges:
          if (edge[0] == u and edge[1] == v) or (edge[1] == u and edge[0] == v):
              weight = edge[2] 
              
              if weight < min_weight:
                  min_weight = weight


      if min_weight == float('inf'):
          return None  
      
      return min_weight

    def ajouter_arretes_artificielles(self):

      sommets_impairs = []
      for i in self.adjacence:
          if (len(self.adjacence[i]) % 2 != 0):
            sommets_impairs.append(i)
      poids_artificiel = 0  

      
      nouvelles_arretes = []
      temp=0

      
      for i in range(len(sommets_impairs)):
          for j in range(i + 1, len(sommets_impairs)):
              
              u = sommets_impairs[i]
              v = sommets_impairs[j]
              edge = (u, v, poids_artificiel, self.vertices[u], self.vertices[v])
              nouvelles_arretes.append(edge)
              for k in self.adjacence:
                if (len(self.adjacence[k]) % 2 != 0):
                  temp=1
                  break
          if temp==1:
            break        

      
      self.edges.extend(nouvelles_arretes)

      for u, v, _, _, _ in nouvelles_arretes:
          self.adjacence[u].append(v)
          self.adjacence[v].append(u)
      print("imapir", sommets_impairs) 
      print("taille", len(sommets_impairs)) 


      return self







        






        
