import strutils, math

let hex = readFile("day16input.txt").strip()
type
  PacketKind = enum
    literal,
    operator
  OperatorKind = enum
    sum,
    product,
    minimum,
    maximum,
    greater,
    less,
    equal
  Packet = object
    version, length: int
    case kind: PacketKind
    of literal:
      value: int
    of operator:
      subpackets: seq[Packet]
      opKind: OperatorKind
var
  binary = ""

for i in hex:
  binary &= toBin(fromHex[int]($i), 4)

proc parse(bits: string): Packet =
  if bits == "": echo "eeeeeeeeeeee"
  var
    pos = 0

  proc read(chars: int): string =
    result = bits[pos..<pos+chars]
    pos += chars

  result.version = fromBin[int](read(3))

  let typeID = fromBin[int](read(3))
  result.kind = if typeID == 4: literal else: operator

  if result.kind == literal:
    var binaryValue = ""
    while read(1) == "1":
      binaryValue &= read(4)
    binaryValue &= read(4)
    result.value = fromBin[int](binaryValue)
    result.length = pos

  else:
    result.opKind = case typeID
      of 0: sum
      of 1: product
      of 2: minimum
      of 3: maximum
      of 5: greater
      of 6: less
      of 7: equal
      else: raise newException(Exception, $typeID & " does not correspond to a valid operator")
    if read(1) == "0":
      let bitLength = fromBin[int](read(15))
      var totalLength = 0
      while totalLength < bitLength:
        result.subpackets &= parse(bits[pos+totalLength..<pos+bitLength])
        totalLength += result.subpackets[^1].length
      result.length = pos + totalLength
    else:
      let packetLength = fromBin[int](read(11))
      for i in 0..<packetLength:
        result.subpackets &= parse(bits[pos..bits.high])
        pos += result.subpackets[^1].length
      result.length = pos

proc versionSum(packet: Packet): int =
  if packet.kind == literal:
    return packet.version
  else:
    result = packet.version
    for i in packet.subpackets:
      result += versionSum(i)

proc eval(packet: Packet): int =
  if packet.kind == literal:
    return packet.value
  else:
    var subvalues: seq[int]
    for i in packet.subpackets:
      subvalues &= eval(i)
    return case packet.opKind
    of sum: math.sum(subvalues)
    of product: prod(subvalues)
    of minimum: min(subvalues)
    of maximum: max(subvalues)
    of greater:
      if subvalues[0] > subvalues[1]: 1
      else: 0
    of less:
      if subvalues[0] < subvalues[1]: 1
      else: 0
    of equal:
      if subvalues[0] == subvalues[1]: 1
      else: 0

echo eval(parse(binary))
