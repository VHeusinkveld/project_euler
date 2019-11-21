clear all; close all; clc;

i = 1:100;
sq = i.*i;

sumSq = zeros(1,numel(i));
sqSum = zeros(1,numel(i));


for j = 1:numel(i)
   sumSq(j) = sum(sq(1:j));
   sqSum(j) = (sum(i(1:j)))^2;
end

sumDif = sqSum - sumSq;
tot = sum(sumDif);
