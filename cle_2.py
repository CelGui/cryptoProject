#!/usr/bin/env python2.7
with open('private.pem','w') as kf:
	kf.write(k)
	kf.close()

with open('public.pem','w') as pf:
	pf.write(p)
	pf.close()
