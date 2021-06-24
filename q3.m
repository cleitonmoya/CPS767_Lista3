% Exercício 3

close all;
clear;
clc;

% Parâmetros do modelo
% N = [10];
N = [10 25 50 100];
prob = 0.10:0.01:0.90;

figure()
hold on

for j=1:numel(N)
    n = N(j);
    
    for k=1:numel(prob)

        p = prob(k);

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
        % pi = asymptotics(mc);

        % Vão espectral
        e = sort(eig(P));
        e2 = e(1:n-1,1);
        lambmax = max(abs(e2));
        delta(k) = 1-lambmax;
    end

    % Plotagem
    leg = sprintf('n = %d',n);
    plot(prob, delta, 'DisplayName', leg)
    
end

hold off
legend('Location', 'southwest')
box
xlim([0 1])
ylim([-inf 1.02])
xlabel('p')
ylabel('Spectral gap (\delta)')
save2pdf('q3-2.pdf');