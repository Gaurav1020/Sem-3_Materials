#include<bits/stdc++.h>
using namespace std;

struct edge{
	int src,dst,wt;
};
int V,E;

void bellmanFord(vector<edge>& Edges)
{
	int parent[V];
	int cost_parent[V];
	vector<int> value(V,INT_MAX);
	parent[0] = -1;
	value[0] = 0;

	bool updated;
	for(int i=0;i<V-1;++i)
	{
		updated = false;
		for(int j=0;j<E;++j)
		{
			int U = Edges[j].src;
			int V = Edges[j].dst;
			int wt = Edges[j].wt;
			if(value[U]!=INT_MAX and value[U]+wt<value[V])
			{
				value[V] = value[U]+wt;
				parent[V] = U;
				cost_parent[V] = value[V];
				updated = true;
			}
		}
		if(updated==false)
			break;
	}

	for(int j=0;j<E and updated==true;++j)
		{
			int U = Edges[j].src;
			int V = Edges[j].dst;
			int wt = Edges[j].wt;
			if(value[U]!=INT_MAX and value[U]+wt<value[V])
			{
				cout<<"Graph has -VE edge cycle\n";
				return;
			}
		}

	for(int i=1;i<V;++i)
		cout<<"U->V: "<<parent[i]<<"->"<<i<<"  Cost to reach "<<i<<" from source 0 = "<<value[i]<<"\n";
}

int main()
{
    cout<<"Enter no. of vertices and edges:\n";
	cin>>V>>E;
	vector<edge> Edges(E);

	int src,dst,wt;
	cout<<"\nEnter the edges with their weight in the format `Source Destination Weight` in a directed manner: \n";
	for(int i=0;i<E;++i)
	{

		cin>>src>>dst>>wt;
		Edges[i].src = src;
		Edges[i].dst = dst;
		Edges[i].wt = wt;
	}

	bellmanFord(Edges);
	return 0;
}


