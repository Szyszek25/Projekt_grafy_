
#!/usr/bin/env python3

"""
Algorytm Kruskala – minimalne drzewo rozpinające
Autorzy: Jakub Szych, Jakub Orchowski

Uruchomienie:
    python AlgKruskal.py graph.txt

Plik wejściowy graph.txt:
    V E
    u v w   (E wierszy)

Wynik:
    Plik mst.txt zawierający krawędzie MST i łączny koszt.
"""

import sys
from typing import List, Tuple


class DSU:
    """Disjoint Set Union z kompresją ścieżek i scalaniem według rangi."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """Zwraca reprezentanta zbioru zawierającego x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """Łączy zbiory zawierające a i b. Zwraca True jeżeli nastąpiło scalenie."""
        a_root, b_root = self.find(a), self.find(b)
        if a_root == b_root:
            return False
        if self.rank[a_root] < self.rank[b_root]:
            a_root, b_root = b_root, a_root
        self.parent[b_root] = a_root
        if self.rank[a_root] == self.rank[b_root]:
            self.rank[a_root] += 1
        return True


def load_graph(path: str) -> Tuple[int, List[Tuple[int, int, int]]]:
    """Wczytuje graf z pliku tekstowego w formacie opisanym wyżej."""
    with open(path, "r", encoding="utf-8") as f:
        first = f.readline()
        if not first:
            raise ValueError("Plik jest pusty.")
        V, E = map(int, first.split())
        edges = []
        for _ in range(E):
            u, v, w = map(int, f.readline().split())
            edges.append((u, v, w))
    return V, edges


def kruskal(V: int, edges: List[Tuple[int, int, int]]):
    """Zwraca listę krawędzi MST i jego łączny koszt."""
    edges.sort(key=lambda x: x[2])  # sortujemy rosnąco po wadze
    dsu = DSU(V)
    mst = []
    total = 0
    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == V - 1:  # można wcześniej zakończyć, gdy mamy V-1 krawędzi
                break
    return mst, total


def main():
    if len(sys.argv) < 2:
        print("Użycie: python AlgKruskal.py graph.txt")
        sys.exit(1)

    path = sys.argv[1]
    V, edges = load_graph(path)
    mst, total = kruskal(V, edges)

    with open("mst.txt", "w", encoding="utf-8") as out:
        for u, v, w in mst:
            out.write(f"{u} {v} {w}\n")
        out.write(f"Total = {total}\n")

    if len(mst) < V - 1:
        print("Uwaga: graf nie jest spójny – znaleziono tylko częściowe drzewo.")
    else:
        print(f"Zapisano MST (koszt całkowity = {total}) do pliku mst.txt")


if __name__ == "__main__":
    main()
