from tkinter import *
import tkinter.font as font
from tkinter import ttk
from datetime import datetime
from tkinter import filedialog
import os
import time
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.figure import Figure
from datetime import datetime
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPy import IP
import re
from tkinter import messagebox
import h5py
import pandas as pd
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.utils import ImageReader
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import string
from netgraph import Graph # pip install netgraph


class visual_screen(Frame):
    

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.colors = self.master.colors
        self.fonts = self.master.fonts
        #self.settings_dict = self.master.prog_settings
        self.configure(bg=self.colors["bg"])

        self.s = ttk.Style()
        self.s.configure('my.TButton', bordercolor=self.colors["red_2"], font=self.fonts["bold"], foreground=self.colors["red_2"], background="white")

        self.configure(highlightbackground="black", highlightthickness=2)
        arr = self.master.dict["matrix"]
        G = nx.Graph()
        
        #dic = dict(zip(string.ascii_uppercase, np.arange(0,26)))
        #key_list = list(dic.keys())
        #val_list = list(dic.values())

        fixed_lst = [(0.5 + 0.0,0.5 + 0.0) , (0.5 + 0.1,0.5 + 0.1) , (0.5 - 0.1,0.5 + 0.1) , (0.5 + 0.1,0.5 - 0.1) , (0.5 - 0.1,0.5 - 0.1),
                     (0.5 + 0.2,0.5 + 0.2) , (0.5 - 0.2,0.5 + 0.2) , (0.5 + 0.2,0.5 - 0.2) , (0.5 - 0.2,0.5 - 0.2),
                     (0.5 + 0.3,0.5 + 0.3) , (0.5 - 0.3,0.5 + 0.3) , (0.5 + 0.3,0.5 - 0.3) , (0.5 - 0.3,0.5 - 0.3),
                     (0.5 + 0.4,0.5 + 0.4) , (0.5 - 0.4,0.5 + 0.4) , (0.5 + 0.4,0.5 - 0.4) , (0.5 - 0.4,0.5 - 0.4),
                     (0.5 + 0.5,0.5 + 0.5) , (0.5 - 0.5,0.5 + 0.5) , (0.5 + 0.5,0.5 - 0.5) , (0.5 - 0.5,0.5 - 0.5),
                     (0.5 + 0.6,0.5 + 0.6) , (0.5 - 0.6,0.5 + 0.6) , (0.5 + 0.6,0.5 - 0.6) , (0.5 - 0.6,0.5 - 0.6),
                     (0.5 + 0.7,0.5 + 0.7)]
        fixed_positions = {}
        labeldict = {}
        alphabets = string.ascii_uppercase
        size = self.master.dict["nodes"]
        #nd = [100] * int(size)
        tup = []
        for row in range(1, size + 1):
            labeldict[row] = str(alphabets[row - 1])
            fixed_positions[row] = fixed_lst[row - 1]
        for row in range(1, size + 1):
            G.add_node(alphabets[row -1], pos = fixed_lst[row - 1])   #######################################
        for row in range(1, size + 1):
            for col in range(1, size + 1):
                if(arr[row - 1][col - 1] == 1):
                    if(alphabets[row - 1] == alphabets[col -1]):
                        G.add_edge(alphabets[row - 1], alphabets[col -1])
                        tup.append((alphabets[row - 1], alphabets[col -1]))
                    else:
                        G.add_edge(alphabets[row - 1], alphabets[col -1])
        
        G.to_undirected()
        fixed_nodes = fixed_positions.keys()
        edges = G.edges()
        #colors = [G[u][v]['color'] for u,v in edges]
        #weights = [G[u][v]['weight'] for u,v in edges]
        
        fr = Frame(self, relief=RAISED, borderwidth=0, bg=self.colors["panel_1"])
        #fr.grid(row=0, column=0, columnspan=2)
        fr.pack(side = TOP, fill = BOTH, expand = 1)

        fig = plt.figure(figsize=(14.9,6))
        #axes = fig.add_axes([0.5,1,0.5,1])
        canvas = FigureCanvasTkAgg(fig, master=fr)  # A tk.DrawingArea.
        #canvas.bind("<Configure>", self.onCanvasConfigure)
        #canvas.configure(highlightthickness=0, borderwidth=0)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, fr)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        a = fig.add_subplot(111)
        #a = fig.add_axes([0,0,1,1])
        #pos = (1, 1)
        #pos = nx.spring_layout(G, scale = 0.5, k =0.15, pos=fixed_positions, fixed = fixed_nodes, center = (0,0))
        #pos = nx.spring_layout(G, pos=fixed_positions, fixed = fixed_nodes, center = (0,0))    ##########################################
        #pos=nx.spectral_layout(G)
        #pos = nx.circular_layout(G)
        # displacement "force"
        #displacement = np.einsum('ijk,ij->ik', delta, (k * k / distance**2 - A * distance / k))
        # ADD THIS LINE - prevent things from flying off into infinity if not connected
        #displacement = displacement - pos / ( k * np.sqrt(nnodes))
        #self.draw()
        a.cla()
        a.set_xlim(0.25,0.75)
        a.set_ylim(0.25,0.75)
        #nx.draw(G, pos, ax = a, labels = labeldict,  with_labels = True, node_size = nd, node_shape = 'o', alpha = 0.7, font_size = 8, font_color = "blue", edge_color = "red", node_color = "green")  # ax = a
        #self.a.plot(self.pos[0], self.pos[1], 'r.')
        #print(colors)
        layout = dict((n, G.nodes[n]["pos"]) for n in G.nodes())
        
        
        #nx.draw(G, pos=layout, with_labels=True, node_size=100, font_size = 7, font_color = "blue", edge_color = colors, width=weights, node_color = "green", alpha = 0.6)
        print(tup)
        nx.draw_networkx_nodes(G, pos=layout, nodelist = G.nodes(), node_size = 100, node_color = 'green', alpha = 0.6)
        nx.draw_networkx_labels(G, pos=layout, font_size = 7, font_color = "blue", alpha = 0.6)
        nx.draw_networkx_edges(G, pos=layout, edgelist = tup, edge_color = 'r', style = 'solid', alpha = 0.6)
        ax = plt.gca()
        print(edges)
        for edge in edges:
            ax.annotate("",
                    xy=layout[edge[0]], xycoords='data',
                    xytext=layout[edge[1]], textcoords='data',
                    arrowprops=dict(arrowstyle="-",color='r',alpha = 0.6, 
                                    shrinkA=2, shrinkB=2,
                                    patchA=None, patchB=None,
                                    connectionstyle="arc3,rad=-0.3",
                                    ),
                        )
        #plt.show()
        
        #plt.tight_layout()
        plt.axis('off')
        canvas.draw()

        self.res = nx.is_tree(G)
        if(self.res):
            self.display = "The graph of the provided adjacency matrix is a Tree"
        else:
            '''if(nx.number_of_nodes(G) != nx.number_of_edges(G) + 1):
                self.err = 1
            if(nx.is_connected(G) != True):
                self.err = 2
            if(nx.number_of_nodes(G) != nx.number_of_edges(G) + 1 and nx.is_connected(G) != True):
                self.err = 3

            if( self.err == 1):'''
            self.display = "The graph of the provided adjacency matrix is a NOT a Tree"

        self.resultFrame = Frame(self, bg=self.colors["title_bg"])  
        if(self.res):     
            self.labl = Label(self.resultFrame, text=self.display, font=self.fonts["bold"], pady=10, bg=self.colors["panel_1"], fg="green") 
        else:
            self.labl = Label(self.resultFrame, text=self.display, font=self.fonts["bold"], pady=10, bg=self.colors["panel_1"], fg="red") 
        self.labl.pack(side=TOP, pady=0, expand=True, fill=X, anchor=S)
        self.resultFrame.pack(side=TOP, expand=True, fill=X, anchor=S)
            

        self.button_frame = Frame(self, bg=self.colors["bg"])
        
        self.b_home = Button(self.button_frame, text="Home", font=self.fonts["bold"], command=self.gohome, bg="white", fg=self.colors["blue"])
        self.b_set = Button(self.button_frame, text="Settings", font=self.fonts["bold"], command=self.goset, bg="white", fg=self.colors["blue"]) 
        self.b_exit = Button(self.button_frame, text="Exit", font=self.fonts["bold"], command=self.exit_callback, bg="white", fg=self.colors["blue"])
               

        self.b_home.pack(padx=20, pady=20, side=LEFT)
        self.b_set.pack(padx=20, pady=20, side=LEFT)
        self.b_exit.pack(padx=20, pady=20, side=LEFT)

        self.button_frame.pack()


    '''def onCanvasConfigure(self, event):
        # width is tweaked to account for window borders
        width = event.width - 4
        self.canvas.itemconfigure("self.frame", width=width)'''

    def gohome(self):
        self.master.show_startup_screen()

    def goset(self):
        self.master.show_settings_screen()

    def exit_callback(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.quit()
            self.destroy()


        
    def isCyclicUtil(self, v, visited, parent):
 
        # Mark current node as visited
        visited[v] = True
 
        # Recur for all the vertices adjacent
        # for this vertex
        for i in self.graph[v]:
            # If an adjacent is not visited,
            # then recur for that adjacent
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v) == True:
                    return True
 
            # If an adjacent is visited and not
            # parent of current vertex, then there
            # is a cycle.
            elif i != parent:
                return True
 
        return False
 
    # Returns true if the graph is a tree,
    # else false.
    def isaTree(self):
        # Mark all the vertices as not visited
        # and not part of recursion stack
        visited = [False] * self.V
 
        # The call to isCyclicUtil serves multiple
        # purposes. It returns true if graph reachable
        # from vertex 0 is cyclcic. It also marks
        # all vertices reachable from 0.
        if self.isCyclicUtil(0, visited, -1) == True:
            return False
 
        # If we find a vertex which is not reachable
        # from 0 (not marked by isCyclicUtil(),
        # then we return false
        for i in range(self.V):
            if visited[i] == False:
                return False
 
        return True
