n = int(input())
pmax, pmid, pmin = 1, 0, 0
for p in sorted(map(float, input().split()))[::-1]:
    pmid = pmax*p + pmid*(1-p)
    pmax *= 1-p
    pmin = max(pmin, pmid)
print(pmin)