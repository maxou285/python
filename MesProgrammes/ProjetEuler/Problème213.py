from numpy import *

N = 30
Niter = 50

def ProbaMapFlea(Fi,Fj):
	# Probability matrix
	P1 = zeros((N,N), dtype='f8')
	P1[Fi, Fj] = 1.
	for k in range(0, Niter):
		P2 = zeros((N,N), dtype='f8')
		# Inside
		w = 1/float64(4.)
		for i in range(1, N-1):
			for j in range(1, N-1):
				P2[i+1,j] += P1[i,j] * w
				P2[i-1,j] += P1[i,j] * w
				P2[i,j+1] += P1[i,j] * w
				P2[i,j-1] += P1[i,j] * w
		# Border
		w = 1/float64(3.)
		for i in range(1, N-1):
			P2[i+1,0] += P1[i,0] * w
			P2[i-1,0] += P1[i,0] * w
			P2[i,1]   += P1[i,0] * w
			P2[i+1,N-1] += P1[i,N-1] * w
			P2[i-1,N-1] += P1[i,N-1] * w
			P2[i,N-2]   += P1[i,N-1] * w
			P2[0,i+1] += P1[0,i] * w
			P2[0,i-1] += P1[0,i] * w
			P2[1,i]   += P1[0,i] * w
			P2[N-1,i+1] += P1[N-1,i] * w
			P2[N-1,i-1] += P1[N-1,i] * w
			P2[N-2,i]   += P1[N-1,i] * w
		# Corner
		w = 1/float64(2.)
		P2[0,1] += P1[0,0] * w
		P2[1,0] += P1[0,0] * w
		P2[N-1,1] += P1[N-1,0] * w
		P2[N-2,0] += P1[N-1,0] * w
		P2[1,N-1] += P1[0,N-1] * w
		P2[0,N-2] += P1[0,N-1] * w
		P2[N-1,N-2] += P1[N-1,N-1] * w
		P2[N-2,N-1] += P1[N-1,N-1] * w
		
		P1 = P2.copy()
	
	return P1

# Let's take fleas only in the upper left quarter
P = ones((N,N), dtype="f8")
for fi in range(0,int(N/2)):
	print(fi, "/", N/2)
	for fj in range(0,int(N/2)):
		P *= 1.-ProbaMapFlea(fi,fj)

P *= P[::-1,:].copy()
P *= P[:,::-1].copy()

print(P.sum())