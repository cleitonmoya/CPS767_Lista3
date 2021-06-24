% Exercício 3

close all;
clear;
clc;

% Parâmetros do modelo
n = 6;
p = 0.25;

% Criação da matriz de transição
A(1:n-1,1) = 1-p;
B = p*eye(n-1);
C = zeros(1,n);
C(1) = q;
C(n) = 1-q;
P = [A, B; C];

% Criação do modelo
mc = dtmc(P);

% Distribição estacionária
pi = asymptotics(mc)

% Vão espectral
e = sort(eig(P));
e2 = e(1:n-1,1);
lambmax = max(abs(e2));
delta = 1-lambmax

[pi_o,k]=min(pi)