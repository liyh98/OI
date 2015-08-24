#include <cstdio>
#pragma warning (disable : 4996)

struct
{
	int a, b, c1, c2;
}e[20001];

int fa[10001], n, k, m;

inline void reset()
{
	for (int i = 1; i <= n; i++)
		fa[i] = i;
}

int find(int x)
{
	return x == fa[x] ? x : fa[x] = find(fa[x]);
}
inline bool check(int x)
{
	int cnt = 0;
	reset();
	for (int i = 1; i <= m; i++)
		if (e[i].c1 <= x)
		{
			int p = find(e[i].a), q = find(e[i].b);
			if (p != q)
			{
				fa[p] = q;
				cnt++;
			}
		}
	if (cnt < k) return 0;
	reset();
	cnt = 0;
	for (int i = 1; i <= m; i++)
		if (e[i].c2 <= x)
		{
			int p = find(e[i].a), q = find(e[i].b);
			if (p != q)
			{
				fa[p] = q;
				cnt++;
			}
		}
	return cnt == n - 1;
}

int main()
{
	scanf("%d%d%d", &n, &k, &m);
	for (int i = 1; i < m; i++)
		scanf("%d%d%d%d", &e[i].a, &e[i].b, &e[i].c1, &e[i].c2);
	int l = 1, r = 30000, ans = r;
	while (l <= r)
	{
		int mid = (l + r) >> 1;
		if (check(mid)) ans = mid, r = mid - 1;
		else l = mid + 1;
	}
	printf("%d", ans);
	return 0;
}
