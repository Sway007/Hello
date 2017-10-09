import graphviz as gv

g1 = gv.Digraph(filename='test')

g1.edges([['A', 'B'], ['A', 'C'], ('B', 'D'), ('B', 'E')])

# g1.edge
# g1.edge('B', 'D')
# g1.edge('B', 'E')

g1.render(filename='test', view=True)
