import os

def is_equal(number, a, b):
	if a == b:
		print 'Test ' + str(number) + ' ok'
	else:
		print 'Test ' + str(number) + ' failed!'
		print 'First = ' + str(a)
		print 'Second = ' + str(b)

# returns the two lists intersection
def list_intersection(list1, list2):
	res = []
	for x in list1:
		if x in list2:
			res.append(x)
	return res

IMAGES_DIR = os.path.join("resource", "images")
SOUNDS_DIR = os.path.join("resource", "sounds")
