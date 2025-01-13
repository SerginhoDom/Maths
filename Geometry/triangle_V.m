a = [0 1 0];
b = [0 2 -1];
c = [-1 2 2];
d = [7 2 3];

ab = b - a;
ac = c - a;
ad = d - a;

answer = (dot(cross(ab, ac), ad)) / 4