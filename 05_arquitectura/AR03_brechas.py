# -*- coding: utf-8 -*-
"""AR03 — Brechas EPS Aguas del Sur. Requiere pandas y networkx.
Los esfuerzos y TO-BE son propuestas académicas; verificar contra el PETI.
"""
from pathlib import Path
import pandas as pd, networkx as nx
A=Path(__file__).resolve().parent
df=pd.read_csv(A/'AR03_brechas.csv',encoding='utf-8-sig',dtype=str).fillna('')
p=pd.read_csv(A/'AR04_paquetes_de_trabajo.csv',encoding='utf-8-sig',dtype=str).fillna('')
assert len(df)>=10 and df.codigo.is_unique
G=nx.DiGraph();G.add_nodes_from(p.paquete)
for row in p.itertuples():
    for dep in [x.strip() for x in row.dependencias.split(';') if x.strip() and x.strip()!='Ninguna']:
        G.add_edge(dep,row.paquete)
assert nx.is_directed_acyclic_graph(G), 'Dependencias cíclicas'
orden=list(nx.topological_sort(G)); nivel={x:1 for x in G}
for x in orden:
    for y in G.successors(x): nivel[y]=max(nivel[y],nivel[x]+1)
p['fase_recalculada']=p.paquete.map(nivel)
p.to_csv(A/'AR04_paquetes_de_trabajo_recalculados.csv',index=False,encoding='utf-8-sig')
print('BRECHAS:',len(df))
print(df.groupby(['capa','tipo_brecha']).size().to_string())
print('\nPAQUETES Y FASES DE EJECUCIÓN')
print(p[['paquete','nombre','dependencias','fase_recalculada']].sort_values(['fase_recalculada','paquete']).to_string(index=False))
