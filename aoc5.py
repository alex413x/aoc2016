from hashlib import md5


door_id = 'ffykfhsq'
password = ''

index = 0
while len(password) < 8:
    m = md5(door_id+str(index))
    if m.hexdigest()[:5] == '00000':
        print 'Found a password character!: %s' % m.hexdigest()[5:6]
        password += m.hexdigest()[5:6]
    index += 1

print password