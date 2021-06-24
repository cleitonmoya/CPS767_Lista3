% Exercício 3

close all;
clear;
clc;

% Parâmetros do modelo
n = 10;
p = 0.50;  

% Criação da matriz de transição
A(1:n-1,1) = 1-p;
B = p*eye(n-1);
C = zeros(1,n);
C(1) = 1-p;
C(n) = p;
P = [A, B; C];

% Criação do modelo
mc = dtmc(P);

% Distribição estacionária
pi = asymptotics(mc);


% Simulação
N = 1000;        % número de simulações
numSteps = 10;   % passos por simulação
x0 = zeros(1,n);
x0(1)=N;

rng(1); % For reproducibility
X = simulate(mc,numSteps,'X0',x0);

figure;
simplot(mc,X);

for x = 1:10
    pi_sim(x) = sum(X==x,'all')/(numel(X));
end

d_tv = 0.5*sum(abs(pi_sim-pi))