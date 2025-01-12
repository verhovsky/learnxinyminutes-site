# CoffeeScript is een taal voor hipsters.
# Het gaat mee met alle trends van moderne talen.
# Commentaar begint dus met een hekje, net zoals bij Python en Ruby.

###
Blokken commentaar maak je zo, ze vertalen naar JavaScripts */ en /*
in de uitvoer van de CoffeeScript-compiler.

Het is belangrijk dat je ongeveer snapt hoe JavaScript
werkt voordat je verder gaat.
###

# Toewijzing:
getal         = 42 #=> var getal = 42;
tegengestelde = true #=> var tegengestelde = true;

# Voorwaarden:
getal = -42 if tegengestelde #=> if(tegengestelde) { getal = -42; }

# Functies:
kwadraat = (x) -> x * x #=> var kwadraat = function(x) { return x * x; }

vul = (houder, vloeistof = "koffie") ->
  "Nu de #{houder} met #{vloeistof} aan het vullen..."
#=>var vul;
#
#vul = function(houder, vloeistof) {
#  if (vloeistof == null) {
#    vloeistof = "koffie";
#  }
#  return "Nu de " + houder + " met " + vloeistof + " aan het vullen...";
#};

# Reeksen:
lijst = [1..5] #=> var lijst = [1, 2, 3, 4, 5];

# Objecten:
wiskunde =
  wortel:   Math.sqrt
  kwadraat: kwadraat
  derdemacht:   (x) -> x * kwadraat x
#=> var wiskunde = {
#  "wortel": Math.sqrt,
#  "kwadraat": kwadraat,
#  "derdemacht": function(x) { return x * kwadraat(x); }
#}

# "Splats":
wedstrijd = (winnaar, lopers...) ->
  print winnaar, lopers
#=>wedstrijd = function() {
#  var lopers, winnaar;
#  winnaar = arguments[0], lopers = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
#  return print(winnaar, lopers);
#};

# Aanwezigheid:
alert "Ik wist het!" if elvis?
#=> if(typeof elvis !== "undefined" && elvis !== null) { alert("I knew it!"); }

# Lijstabstracties:
derdemachten = (wiskunde.derdemacht num for num in lijst)
#=>derdemachten = (function() {
#	var _i, _len, _results;
#	_results = [];
# 	for (_i = 0, _len = lijst.length; _i < _len; _i++) {
#		num = list[_i];
#		_results.push(wiskunde.derdemacht(num));
#	}
#	return _results;
#  })();

etenswaren = ['broccoli', 'spinazie', 'chocolade']
eet eten for eten in etenswaren when eten isnt 'chocolade'
#=>etenswaren = ['broccoli', 'spinazie', 'chocolade'];
#
#for (_k = 0, _len2 = etenswaren.length; _k < _len2; _k++) {
#  eten = etenswaren[_k];
#  if (eten !== 'chocolade') {
#    eet(eten);
#  }
#}