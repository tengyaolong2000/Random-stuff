def longestPalindrome(s):

	x = []
	s_list = list(s)
	s_list.insert(0, 0)
	for n in range(0, len(s_list)+1):
		for i in range(1,len(s_list)+1):
			
			if s_list[n:i] == s_list[i:n-1:-1]:
				x.append(s_list[n:i])


	return ''.join(max(x, key=len))
	
def longestPalindrome1(s):
	
	z = ''
	s_list = list(s)
	for n in range(0, len(s_list)+1):
		for i in range(1,len(s_list)+1):
			copy = s_list[n:i]
			copy.reverse()
			if s_list[n:i] == copy:
				x = ''.join(s_list[n:i])

			if len(x)>len(z):
				z = x
	return z

def longestPalindrome2(s):
	
	x = []
	s_list = list(s)
	for n in range(0, len(s_list)+1):
		for i in range(1,len(s_list)+1):
			copy = s_list[n:i]
			copy.reverse()
			if s_list[n:i] == copy:
				if ''.join(s_list[n:i]) != '':
					x.append(''.join(s_list[n:i]))


			
	return max(x, key=len)



	

y = longestPalindrome2("iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxzerakhmexuyeuhjfobrmkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfhevfesnwltekstsueefbrddxrmxokpaxsenwlgytdaexgfwtneurhxvjvpsliepgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrlspejqvzpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmaocesnpqaotamwofyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqxqobfsageysonuoagmmviozeouutsiecitrmkypwknorjjiaasxfhsftypspwhvqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacleqdxgrxbldcuxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexcybbjaxlfhyvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmucjlqpiolklmjxnscjcyiybdkgitxnuvtmoypcdldrvalxcxalpwumfx")
print(y)

l = ['a', 'b', 'c', 'd']
print(l[0:0])

