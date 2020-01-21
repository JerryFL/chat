
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	for line in lines:
        if line == 'Jerry':
    		person = 'Jerry'
    		continue
    	elif line == 'Laurance':
    		person = 'Laurance'
    		continue
    	new.append(person + ':' + line)
        print(new)


def main():
    lines = read_file('chat.txt')
    convert(lines)
main()