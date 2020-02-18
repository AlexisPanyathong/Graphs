from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # Add vertex for parent and child
    g = Graph()

for (parent, child) in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)
    # Need to have to for loops for vertex and edge otherwise it throws an error.
        g.add_edge(parent, child)
    # Add edge for parent/child pair written as (parent, child).
    
    # New path list

    # For each parents, find path to starting node.
        # Set path to g.dfs that passes in the parent and starting_node.
        
        
        # If the path id not None & the length of the path is greater than the length of the new path.
            # Then the new path will replace the old path with the copy().
            
    # If the length of the new path is less than or equal to 1. Return -1.
   
    # Otherwise return the new path at the index of zero.
