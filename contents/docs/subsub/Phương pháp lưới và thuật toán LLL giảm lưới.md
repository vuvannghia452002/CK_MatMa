
\textit{Chứng minh.}\\
i) Theo Định nghĩa 2.7 ta có : 
$$\|x_i^*\| \geq (\alpha - \mu_{i,i-1}^2)\|x_{i-1}^*\|^2 \geq (\alpha - \frac{1}{4}).\|x_{i-1}^*\|^2 = \frac{1}{\beta}\|x_{i-1}^*\|^2 \text{.}$$
Khi đó \quad $\|x_{i-1}^*\|^2 \leq \beta.\|x_{i}^*\|^2$ ,và $$\|x_{j}^*\|^2 \leq \beta^{i-j}\|x_{i}^*\|^2  \qquad (1 \leq j \leq i \leq n)\text{.} \qquad (1)$$
Mặt khác, ta có : $$x_i = x_i^* + \displaystyle\sum_{j=1}^{i-1} \mu_{ij}x_j^*\text{,}$$ và vì $x_1^*,x_2^*,...,x_n^*$ là trực giao nên:
$$
\begin{aligned}
    \|x_i\|^2 & = \|x_i^*\|^2 + \displaystyle\sum_{j=1}^{i-1} (\mu_{ij})^2\|x_j^*\|^2  \leq \|x_i^*\|^2 + \displaystyle\sum_{j=1}^{i-1} \frac{1}{4}\beta^{i-j}\|x_i^*\|^2\\
    & \leq (1 + \frac{1}{4}\displaystyle\sum_{j=1}^{i-1} \beta^{i-j})\|x_i^*\|^2 = (1 + \frac{1}{4}\frac{\beta^i - \beta}{\beta - 1})\|x_i^*\|^2 \text{.}
\end{aligned}
$$
Bằng quy nạp, ta có thể dễ chứng minh $$1 + \frac{1}{4}\frac{\beta^i - \beta}{\beta - 1} \leq \beta^{i-1}.$$
Vì vậy,
$$ \|x_i\|^2 \leq \beta^{i-1}\|x_i^*\|^2 \text{.} \qquad\qquad (2)$$
Từ (1), (2) ta có:\\
\hspace*{4cm} $\|x_j\|^2 \leq \beta^{j-1}\|x_j^*\|^2 \leq \beta^{i-1}\|x_i\|^2 \text{.}$\\
ii) Theo Bổ đề 2.3. ta có :
$$det(L) = \|x_1^*\|.\|x_2^*\|...\|x_n^*\| \leq \|x_1\|.\|x_2\|...\|x_n\|\text{.}$$
Từ (2) ta có: \\
\hspace*{2cm}$\qquad \|x_1\|.\|x_2\|...\|x_n\| \leq \beta^{\tfrac{n(n-1)}{4}}\|x_1^*\|.\|x_2^*\|...\|x_n^*\| = \beta^{\tfrac{n(n-1)}{4}}.det(L)$\\
iii) Xét $j = 1$ trong i), ta có $$\|x_1\|^2 \leq \beta^{i-1}\|x_i^*\|^2 $$  với $1\leq i \leq n$.

\noindent Khi đó:  $$\qquad \|x_1\|^{2n} \leq \beta^{0 + 1 +2 + ... +(n-1)}\|x_1^*\|^2.\|x_2^*\|^2...\|x_n^*\|^2 \leq \beta^{\tfrac{n(n-1)}{2}}.det(L)^2\text{.}$$

 \noindent Suy ra:
$$ \qquad \|x_1\| \leq \beta^{\tfrac{n-1}{4}}.det(L)^{\tfrac{1}{n}}\text{.}$$
\hspace{2cm}