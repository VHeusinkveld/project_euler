close all; clear all; clc;

k = 1;
n = 2;
p = zeros(1,100);
p(1) = 2;
i = 2;
lp = 1;

while (lp ~= 100)
   for j = 1:lp
        if(mod(i,p(j))== 0)
            i = i + 1;
            break
            
        else   
            if(k==lp)
                p(n) = i;
                k = 1;
                n = n + 1;
                lp = lp+1;
                i = i+1;
                
            end
            k = k + 1;
            
        end
        
   end
   
end