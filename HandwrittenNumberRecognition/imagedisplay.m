k=1;
z=zeros(20,20);

for i=1:20;
    for j=1:20
        z(i,j) =X(4,k);
        k=k+1;
    end
end
colormap(gray)
contour(z')