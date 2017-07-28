a=10;
b=3;

V = linspace(-5,5);
I = (a.*V).*exp(b.*sqrt(V));
figure
plot(V,I)