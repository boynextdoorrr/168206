void Dijkstra(MGraph g,int v)
{
    int dist[MAXV],path[MAXV];
    int s[MAXV];
    int i,j,min,u;
    for(i=0;i<g.n;i++)
    {
        dist[i]=g.edges[v][i];
        s[i] = 0;
        if(g.edges[v][i]<INF)
            path[i] = g.edges[v][i];
        else
            path[i] = -1;       
    }

    for(i=0;i<g.n;i++)
    {
        min = INF;
        for(j=0;j<g.n;j++)
        {
            if(s[j]==0 &&　dist[j]<min)
            {
                min = dist[j];
                u = j;
            }
        }
        s[u] = 1;
        for(j=0;j<g.n;j++)
        {
            if(s[u]==0)
                if(g.edges[u][j]<INF && dist[u]+g.edges[u][j]<dist[j])
                {
                    dist[j] = dist[u]+g.edges[u][j];
                    path[j] = u;
                }
        }
    }
}
