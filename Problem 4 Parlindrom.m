clear all; close all; clc;

a = (100:1:999);
Product = zeros(900,900);
Flip = zeros(900,900);


for i = 1:numel(a)
    Product(:,i) = a(i).*a;
end

Flip = str2num(fliplr(num2str(Product)));
k = 1;
for i = 1:900
    for j = 1:900
        
        if Product(i,j)==Flip(i,901-j);
            Palindroom(k) = Product(i,j);
            k = k+1;
        end
    end
end

LPalindroom = max(Palindroom);
