hyphen_rule = ['et-ic','al-is-tic','s-tic','p-tic','-lyt-ic','ot-ic','an-tic','n-tic','c-tic','at-ic','h-nic','n-ic','m-ic','l-lic','b-lic','-clic','l-ic','h-ic','f-ic','d-ic','-bic','a-ic','-mac','i-ac']
def test_hyphen(word):
	for rule in hyphen_rule:
		r_len = len(rule)
		if word[r_len*-1:] == rule:
			r = rule
			break
		else:
			r = 'No matched rule!'
	return r