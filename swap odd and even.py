a=input()
print(''.join([a[k:k+2][::-1] for k in range (0,len(a),2)]))
