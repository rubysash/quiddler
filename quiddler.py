import json							# to read our json dictionary
import sys							# for the argv
import time							# to time our requests

from colorama import init			# for colors
init()

# quiddler is a card game where you build words
# you score points for longest words, most words, or hard letters
# sometimes, you just cant see which word to pick from the cards you have
# so.... I wrote a "helper" to search through 466k dictionary words
# if any permutation of any of the letters input matches, it saves
# that to a unique list and then shows you the list at the end

# other keywords/modules:  iterations, permulations, yield, itertools

# surely there is a more pythonic way to do this, though


# class ripped from geeks for geeks colorama tutorial
class colors: 
	reset='\033[0m'
	bold='\033[01m'
	disable='\033[02m'
	underline='\033[04m'
	reverse='\033[07m'
	strikethrough='\033[09m'
	invisible='\033[08m'
	class fg: 
		black='\033[30m'
		red='\033[31m'
		green='\033[32m'
		orange='\033[33m'
		blue='\033[34m'
		purple='\033[35m'
		cyan='\033[36m'
		lightgrey='\033[37m'
		darkgrey='\033[90m'
		lightred='\033[91m'
		lightgreen='\033[92m'
		yellow='\033[93m'
		lightblue='\033[94m'
		pink='\033[95m'
		lightcyan='\033[96m'
		white='\033[37m'
	class bg: 
		black='\033[40m'
		red='\033[41m'
		green='\033[42m'
		orange='\033[43m'
		blue='\033[44m'
		purple='\033[45m'
		cyan='\033[46m'
		lightgrey='\033[47m'

def print_sorted_list(data, rows=0, columns=0, ljust=10):
	"""
	Prints sorted item of the list data structure formated using
	the rows and columns parameters
	ripped from dopstar: https://stackoverflow.com/questions/33463758/python-printing-list-in-columns
	"""

	if not data:
		return

	if rows:
		# column-wise sorting
		# we must know the number of rows to print on each column
		# before we print the next column. But since we cannot
		# move the cursor backwards (unless using ncurses library)
		# we have to know what each row with look like upfront
		# so we are basically printing the rows line by line instead
		# of printing column by column
		lines = {}
		for count, item in enumerate(sorted(data)):
			lines.setdefault(count % rows, []).append(item)
		for key, value in sorted(lines.items()):
			for item in value:
				print(colors.fg.yellow,item.ljust(ljust),end="")
			print()
	elif columns:
		# row-wise sorting
		# we just need to know how many columns should a row have
		# before we print the next row on the next line.
		for count, item in enumerate(sorted(data), 1):
			print(colors.fg.yellow,item.ljust(ljust),end="")
			if count % columns == 0:
				print()
	else:
		print(sorted(data))  # the default print behaviour

def allperm(inputstr):
	for i in range(len(inputstr)):
		yield(inputstr[i])        
		for s in allperm(inputstr[:i] + inputstr[i+1:]):
			yield(inputstr[i] + s)


def main():
	# load our dictionary of words as keys
	with open('words_dictionary.json', 'r') as infile:
		d = json.load(infile)

	# refactored to scan smaller dictionaries instead of full dictionary.
	# based on letter it starts with and this greatly increased run time
	# but ... it's ugly.

	# needed to substantiate some dictionaries
	a2z = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	dic = {}
	for abc in a2z: dic[abc] = {}
	for w in d:
		if w[0] == 'a':		dic['a'][w] = 1
		elif w[0] == 'b':	dic['b'][w] = 1
		elif w[0] == 'c':	dic['c'][w] = 1
		elif w[0] == 'd':	dic['d'][w] = 1
		elif w[0] == 'e':	dic['e'][w] = 1
		elif w[0] == 'f':	dic['f'][w] = 1
		elif w[0] == 'g':	dic['g'][w] = 1
		elif w[0] == 'h':	dic['h'][w] = 1
		elif w[0] == 'i':	dic['i'][w] = 1
		elif w[0] == 'j':	dic['j'][w] = 1
		elif w[0] == 'k':	dic['k'][w] = 1
		elif w[0] == 'l':	dic['l'][w] = 1
		elif w[0] == 'm':	dic['m'][w] = 1
		elif w[0] == 'n':	dic['n'][w] = 1
		elif w[0] == 'o':	dic['o'][w] = 1
		elif w[0] == 'p':	dic['p'][w] = 1
		elif w[0] == 'q':	dic['q'][w] = 1
		elif w[0] == 'r':	dic['r'][w] = 1
		elif w[0] == 's':	dic['s'][w] = 1
		elif w[0] == 't':	dic['t'][w] = 1
		elif w[0] == 'u':	dic['u'][w] = 1
		elif w[0] == 'v':	dic['v'][w] = 1
		elif w[0] == 'w':	dic['w'][w] = 1
		elif w[0] == 'x':	dic['x'][w] = 1
		elif w[0] == 'y':	dic['y'][w] = 1
		elif w[0] == 'z':	dic['z'][w] = 1


	# what word did they want us to check? normalize it
	inputstr = sys.argv[1].lower()

	# figure out all the ways it can be arranged
	permutations = allperm(inputstr)
	
	# build a matching dictionary
	results = {}

	# only check a smaller list than our full list 
	for p in permutations:
		if p[0] == 'a':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'b':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'c':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'd':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'e':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'f':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'g':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'h':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'i':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'j':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'k':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'l':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'm':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'n':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'o':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'p':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'q':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'r':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 's':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 't':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'u':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'v':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'w':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'x':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'y':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		elif p[0] == 'z':
			for w in dic[ p[0]]:
				if w == p: results[p] = 1

		else:
			pass

	# this def wants a list, not a dict  convert from dict keys
	uniques = []
	for k in results:
		if len(k) > 1:
			uniques.append(k)

	# display as we desire
	print_sorted_list(uniques, columns=6)

if __name__ == '__main__':
	print(colors.fg.red,"LONGER SETS TAKE LONGER TO COMPUTE!")
	tic = time.perf_counter()
	main()
	toc = time.perf_counter()
	print(colors.fg.green,f"\nCOMPLETED IN {toc - tic:0.4f}s ")

'''
C:\git\pygame>python quiddler2.py dkeaty
 LONGER SETS TAKE LONGER TO COMPUTE!

 a          ad         ade        adet       ady        ae
 aet        ak         ake        aked       akey       at
 ate        ated       ay         aye        d          da
 dae        dak        dat        date       day        de
 dea        det        dey        dk         dt         dy
 dyak       dye        dyke       e          ea         ead
 eat        ed         et         eta        ety        ey
 k          ka         kae        kat        kate       katy
 kay        kea        keat       ked        ket        keta
 key        kt         ky         kyat       kyd        kye
 kyte       t          ta         tad        tade       tae
 take       taked      taky       tay        td         te
 tea        tead       teak       ted        teda       tekya
 tk         tye        tyke       y          ya         yad
 yade       yak        yat        yate       yd         ye
 yea        yeat       yed        yet        yeta       yt

COMPLETED 2.3193

C:\git\pygame>python quiddler2.py dkeatyh
 LONGER SETS TAKE LONGER TO COMPUTE!


 a          ad         ade        adet       ady        ae
 aet        ah         ahet       ahey       aht        ak
 ake        aked       akey       at         ate        ated
 ay         aye        d          da         dae        dah
 dak        dat        date       day        de         dea
 death      deathy     det        dey        dha        dhak
 dk         dt         dy         dyak       dye        dyke
 e          ea         ead        eat        eath       ed
 edh        eh         et         eta        eth        ety
 ey         eyah       h          ha         had        hade
 hae        haed       haet       hak        hake       hat
 hate       hated      hay        haye       hayed      hd
 he         head       heady      heat       hed        het
 hey        ht         hy         hyd        hyde       hye
 hyke       hyte       k          ka         kae        kat
 kate       kath       kathy      katy       kay        kea
 keat       ked        ket        keta       key        kha
 khat       kheda      khet       kt         ky         kyah
 kyat       kyd        kye        kyte       kythe      kythed
 t          ta         tad        tade       tae        take
 taked      taky       tay        td         te         tea
 tead       teak       ted        teda       tekya      th
 tha        thad       thae       thak       the        thea
 thed       they       theyd      thy        tk         tye
 tyke       y          ya         yad        yade       yah
 yak        yat        yate       yd         ye         yea
 yeah       yeat       yed        yeh        yet        yeta
 yeth       yt
COMPLETED 5.1986
'''