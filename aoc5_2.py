from hashlib import md5
from string import ascii_lowercase


door_id = 'ffykfhsq'
password_length = 8
password = ['-1'] * password_length

index = 0
while '-1' in password:
    m = md5(door_id+str(index))
    if m.hexdigest()[:5] == '00000' and m.hexdigest()[5:6] not in ascii_lowercase:
        potential = m.hexdigest()[6:7]
        position = int(m.hexdigest()[5:6])
        print 'Found a potential password character!: %s for postion %s' % (potential, position)

        if position < password_length and password[position] == '-1':
            password[position] = potential
    index += 1
    # print 'Password so far: %s' % password

print ''.join(password)