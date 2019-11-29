clear all; close all; clc;

b = [10 11 12 13 14 15 16 17 18 19 20];
r = 20;
i = 0;

while(sum(mod(r,b)) ~= 0)
    r = r + 20;
end

disp(r);
