#!/usr/bin/env python
class hand(object):
	category = None
	category_value = None

	def hand(self):
		self.category = "None"
		self.category_value = 11

	def get_category(self,cat):
		self.category = cat

	def return_category(self):
		return self.category

	def show_category(self):
		print self.category

	def get_category_value(self,value):
		self.category_value = value

	def return_category_value(self):
		return self.category_value

	def show_category_value(self):
		print self.category_value

infile = open("testcase.txt","r")
n = int(infile.readline())

for x in range(n):
	data = infile.readline().split(" ")

temp1 = data[0:5]
temp2 = data[5:]

hand_value_1 = []
hand_value_2 = []
hand_suit_1 = []
hand_suit_2 = []
for x in range(0,len(temp1)):
	stub1 = list(temp1[x])
	stub2 = list(temp2[x])

	if(stub1[0]=='a'):
		stub1[0]=1
	elif(stub1[0]=='k'):
		stub1[0]=13
	elif(stub1[0]=='q'):
		stub1[0]=12
	elif(stub1[0]=='j'):
		stub1[0]=11
	elif((stub1[0]=='1') and (stub1[1]=='0')):
		stub1[0]=10

	hand_value_1.append(stub1[0])
	if(hand_value_1[x]==10):
		hand_suit_1.append(stub1[2])
	else:
		hand_suit_1.append(stub1[1])

	if(stub2[0]=='a'):
		stub2[0]=1
	elif(stub2[0]=='k'):
		stub2[0]=13
	elif(stub2[0]=='q'):
		stub2[0]=12
	elif(stub2[0]=='j'):
		stub2[0]=11
	elif(stub2[0]=='1' and stub2[1]=='0'):
		stub2[0]=10
	hand_value_2.append(stub2[0])
	if(hand_value_2[x]==10):
		hand_suit_2.append(stub2[2])
	else:
		hand_suit_2.append(stub2[1])

hand_value_1 = map(int, hand_value_1)
hand_value_2 = map(int, hand_value_2)

hands = {'Royal Flush':1,
		'Straight Flush':2,
		'Four of a kind':3,
		'Full House':4,
		'Flush':5,
		'Straight':6,
		'Three of a kind':7,
		'Two pair':8,
		'Pair':9,
		'High Card':10,
		"None":11}

def util(hval,li):
	for x in range(0,5):
		li[hval[x]]+=1

def flush(hand_suit,h):
	flag=0
	value = 11
	for x in range(1,5):
		if(hand_suit[x]!=hand_suit[x-1]):
			flag=1
			break
	if(flag):
		pass
	else:
		h.get_category("Flush")
		value = hands[h.return_category()]
		h.get_category_value(value)

def straight(hand_value,h):
	flag=0
	temp=0
	print hand_value
	for x in range(1,5):
		if(hand_value[x]!=hand_value[x-1]+1):
			flag=1
			break
	
	for x in range(0,5):
		if(hand_value[x]>9):
			temp=1
	if(flag):
		pass
	elif(h.return_category()=="Flush"):
		if(temp):
			h.get_category("Royal Flush")
			value = hands[h.return_category()]
			h.get_category_value(value)
		else:
			h.get_category("Straight Flush")
			value = hands[h.return_category()]
			h.get_category_value(value)
	else:
		h.get_category("Straight")
		value = hands[h.return_category()]
		h.get_category_value(value)

def four_of_a_kind(hval,h):
	li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	util(hval,li)
	flag=0
	for x in range(0,len(li)):
		if(li[x]==4):
			flag=1
			break
	category_value_returned = h.return_category_value()

	if(flag):
		if(category_value_returned>3):
			h.get_category("Four of a kind")
			value = hands[h.return_category()]
			h.get_category_value(value)

def full_house(hval,h):
	li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	util(hval,li)
	count2=0
	count3=0
	print "li"
	print li
	for x in range(0,len(li)):
		if(li[x]==3):
			count3+=1
		elif(li[x]==2):
			count2+=1
	category_value_returned = h.return_category_value()

	if(count2==1 and count3==1):
		if(category_value_returned>4):
			h.get_category("Full House")
			value = hands[h.return_category()]
			h.get_category_value(value)

def three_of_a_kind(hval,h):
	li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	util(hval,li)
	count=0
	for x in range(0,len(li)):
		if(li[x]==3):
			count+=1
	category_value_returned = h.return_category_value()
	if(count==1):
		if(category_value_returned>7):
			h.get_category("Three of a kind")
			value = hands[h.return_category()]
			h.get_category_value(value)

def two_pair(hval,h):
	li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	util(hval,li)
	count=0
	for x in range(0,len(li)):
		if(li[x]==2):
			count+=1
	category_value_returned = h.return_category_value()
	if(count==2):
		if(category_value_returned>8):
			h.get_category("Two pair")
			value = hands[h.return_category()]
			h.get_category_value(value)
	elif(count==1):
		if(category_value_returned>9):
			h.get_category("Pair")
			value = hands[h.return_category()]
			h.get_category_value(value)

def high_card(hval1,hval2,h1,h2):
	temp=0
	for x in range(0,5):
		if(hval1[x]==hval2[x]):
			pass
		elif(hval1[x]>hval2[x]):
			temp=1
			flag=1
		elif(hval1[x]<hval2[x]):
			temp=2
			flag=1
	category_value_returned_1 = h1.return_category_value()
	category_value_returned_2 = h2.return_category_value()
	if(temp==1):
		if(category_value_returned_1>9):
			h1.get_category("High Card")
			value = hands[h1.return_category()]
			h1.get_category_value(value)
	elif(temp==2):
		if(category_value_returned_2>9):
			h2.get_category("High Card")
			value = hands[h2.return_category()]
			h2.get_category_value(value)

def find_highest_card(hval1,hval2):
	if(hval1[4]>hval2[4]):
		return 1
	else:
		return 2

def check_higher_rank(hval1,hval2,p,q):
	li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	util(hval1,li)
	temp4=0
	temp1=0
	for x in range (0,len(li)):
		if(li[x]==p):
			temp4=x
		elif(li[x]==q):
			if(x>temp1):
				temp1=x
		li[x]=0
	util(hval2,li)
	count4=0
	count1=0
	for x in range(0,len(li)):
		if(li[x]==p):
			count4=x
		elif(li[x]==q):
			if(x>count1):
				count1=x
		li[x]=0
	print temp4
	print temp1
	print count4
	print count1
	if(temp4>count4):
		return 1
	elif(temp4<count4):
		return 2
	elif(temp4==count4):
		if(temp1>count1):
			return 1
		else:
			return 2

def check_two_pair_rank(hval1,hval2):
	li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	util(hval1,li)
	temp1 = [0,0,0]
	i=0
	one1=0
	for x in range(0,len(li)):
		if(li[x]==2):
			temp1[i]=x
			i+=1
		elif(li[x]==1):
			one1=x
		li[x]=0
	temp1.sort()

	util(hval2,li)
	temp2 = [0,0,0]
	i=0
	one2=0
	for x in range(0,len(li)):
		if(li[x]==2):
			temp2[i]=x
			i+=1
		elif(li[x]==1):
			one2=x
		li[x]=0
	temp2.sort()
	count=0
	for x in range(0,2):
		if(temp1[x]>temp2[x]):
			return 1
		elif(temp1[x]<temp2[x]):
			return 2
		elif(temp1[x]==temp2[x]):
			count+=1
	if(count==2):
		if(one1>one2):
			return 1
		else:
			return 2 

def  compare_card_with_equal_ranks(hval1,hval2,h1,h2,rank):
	temp=0
	if(rank==1):
		print "Split the pot"
	elif(rank==2 or rank==5 or rank==6):
		temp=find_highest_card(hval1,hval2)
		
	elif(rank==3):
		temp=check_higher_rank(hval1,hval2,4,1)
		
	elif(rank==4):
		temp=check_higher_rank(hval1,hval2,3,2)
		
	elif(rank==7):
		temp=check_higher_rank(hval1,hval2,3,1)
		
	elif(rank==8):
		temp=check_two_pair_rank(hval1,hval2)
		
	elif(rank==9):
		temp=check_higher_rank(hval1,hval2,2,1)

	if(temp==1):
		print "First hand is better"
	elif(temp==2):
		print "Second hand is better"

			
h1 = hand()
h2 = hand()
h1.hand()
h2.hand()

hand_value_1_sorted = hand_value_1
hand_value_2_sorted = hand_value_2
hand_value_1_sorted.sort()
hand_value_2_sorted.sort()

flush(hand_suit_1,h1)
flush(hand_suit_2,h2)

straight(hand_value_1_sorted,h1)
straight(hand_value_2_sorted,h2)

four_of_a_kind(hand_value_1,h1)
four_of_a_kind(hand_value_2,h2)

full_house(hand_value_1,h1)
full_house(hand_value_2,h2)

three_of_a_kind(hand_value_1,h1)
three_of_a_kind(hand_value_2,h2)

two_pair(hand_value_1,h1)
two_pair(hand_value_2,h2)

high_card(hand_value_1_sorted,hand_value_2_sorted,h1,h2)

rank1 = h1.return_category_value()
rank2 = h2.return_category_value()

if(rank1<rank2):
	print "First card is {} and Second card is {}".format(h1.return_category(),h2.return_category())
	print "First card is better"
elif(rank1>rank2):
	print "First card is {} and Second card is {}".format(h1.return_category(),h2.return_category())
	print "Second card is better"
elif(rank1==rank2):
	print "First card is {} and Second card is {}".format(h1.return_category(),h2.return_category())
	compare_card_with_equal_ranks(hand_value_1_sorted,hand_value_2_sorted,h1,h2,rank1)