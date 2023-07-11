from input import parse_cmd_line, parse_file
from graph import Graph


def main():
    in_file, plot_graph = parse_cmd_line()
    vertices, edges = parse_file(in_file)
    print(f"#E={len(edges)}, #V={len(vertices)}")
    graph = Graph(vertices, edges)
    if plot_graph:
        graph.plot()

    print("adjacence \n", graph.adjacence)  
    print("edjes \n", graph.edges)  
    print("vertices \n", graph.vertices)  

    print("******************************** \n") 
    print(" taille edges ", len(graph.edges)) 
    print("******************************** \n") 

  

    if(graph.connexe()):
      if(graph.eulerien()):
         graph.chaine_eulerienne_poids_min() 
      else:
        graph.ajouter_arretes_artificielles()
 
   
    #print("eulérien",graph.eulerien())
    #graph.ajouter_arretes_artificielles()
    print("******************************** \n") 
    print(" taille edges ", len(graph.edges)) 
    
   


    
    

  




if __name__ == "__main__":
    main()

