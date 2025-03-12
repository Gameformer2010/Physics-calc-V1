While True:
    f=str(input('Choose Function:'))
    if f=='av':
        u=int(input('Initial velocity:'))
        v=int(input('Final Velocity:'))
        fv = (u + v) / 2
        print (fv, 'm/s')

    if f=='a':
        u=int(input('Initial velocity:'))
        v=int(input('Final Velocity:'))
        t=int(input('Time:'))
        fa = (v - u) / t
        print (fa,'m/s')