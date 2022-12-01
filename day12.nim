import strutils, tables, sequtils

var
  connections = newTable[string, seq[string]]()

for l in lines("day12input.txt"):
  var caves = split(l, '-')
  connections.mgetOrPut(caves[0], @[]) &= caves[1]
  connections.mgetOrPut(caves[1], @[]) &= caves[0]

proc paths(ps: seq[seq[string]]): seq[seq[string]] =
  var newPaths: seq[seq[string]]
  for p in ps:
    let
      lastCave = p[p.high]
      visitedSmallTwice = any(p, proc (x: string): bool = return p.count(x) >= 2 and x != x.toUpper)
    if lastCave != "end":
      for c in connections[lastCave]:
        if c != "start" and not visitedSmallTwice or not (c in p) or c.toUpper == c:
          newPaths &= p & c
    else:
      newPaths &= p
  if newPaths != ps:
    return paths(newPaths)
  else:
    return newPaths

echo paths(@[@["start"]]).len
