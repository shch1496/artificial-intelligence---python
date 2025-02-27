l1 = [33, 44, 22];
type(l1);

l2 = ['bhopal', 'indore', 'jaipur']
l3 = [4.5, True, 3+4];
l4 = [[1,2], [3,4], [5,6]]
print(l1[0]);
print(l4[0][0]);


for e in l2:
    print(e);

l1.append(55);
print(l1)
l1.insert(2,66)
print(l1)

print(sum(l1));
print(max(l1))
print(sorted(l1))
print(len(l1))

# Array
# supports only 1 d array
# Faster than list
import array;
a = array.array('i', [1,5,13,15]);
print(a)
print(a[0])
print(a[1])
print(a[2]);
for e in a:
    print(a)
print(a[-1])
print(a[-2])
print(*a) # To print only elements
a.insert(1,10);
a.append(20);
print(a);
del a[2];
print(a);
a.pop()
print(a);
a.pop(0);
print(a);
a.remove(13);
print(a)
a.insert(0, 20);
a.insert(0, 40);
a.append(50);
a.append(30);
a.append(70);
a.append(90);
a.append(60);
print(*a);
print(a[::]);
print(a[1:5]);
print(a[1:6:2]);
print(a[::-1]);
print(a[:3:-1]);
print(a.index(50));
print(30 in a);
print(a[0])
print(a);
print(a.count(50));
a.reverse();
print(a)
a.extend([1,2,3]); # Adding multiple values
print(*a);