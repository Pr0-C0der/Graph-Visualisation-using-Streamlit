import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import graphviz

st.title('Welcome to Graph Visualization\n')

st.header('Check if your graph is unidirectional or bidirectional')
type = st.radio('Enter the type of your graph',('Unidirectional','Bidirectional'))

bidirectional = False
unidirectional = False


if(type == 'Bidirectional'):
   bidirectional = True
else:
   unidirectional = True
st.header('Enter the edges in format a -> b form.')
text = st.text_input('Input Here')

text = str(text)
text = text.strip()

relation = text.split(' ')



if bidirectional:
    graph = graphviz.Graph()
    for x in relation:
        a_b = x.split('->')
        graph.edge(a_b[0],a_b[1])
    st.graphviz_chart(graph)
else:
    graph = graphviz.Digraph()
    for x in relation:
        a_b = x.split('->')
        graph.edge(a_b[0],a_b[1])
    st.graphviz_chart(graph)
