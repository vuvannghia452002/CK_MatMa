

Cho $x_1, x_2, \ldots, x_n$ là một cơ sở của $\mathbb{R}^n$ và $x_1^*, x_2^*, \ldots, x_n^*$ là trực giao hóa Gram-Schmidt của nó. Ta có:

\[
|\det(X)| \leq \|x_1\|\|x_2\|\cdots\|x_n\|.
\]

\textbf{Chứng minh:}

Ta có $|\det(X^*)|$ là thể tích hình hộp $n$ chiều căng bởi các vector trực giao $x_1^*, x_2^*, \ldots, x_n^*$. Do đó:

\[
|\det(X^*)| = \|x_1^*\|\|x_2^*\|\cdots\|x_n^*\|.
\]

Theo Định lý 2.2, ta có:

\[
\|x_k^*\| \leq \|x_k\| \quad \text{với mọi } k = 1, 2, \ldots, n.
\]

Vì $\det(X) = \det(X^*)$ (do $X$ và $X^*$ chỉ khác nhau bởi một ma trận tam giác dưới với các phần tử đường chéo bằng 1), ta suy ra:

\[
|\det(X)| = |\det(X^*)|.
\]

Kết hợp với bất đẳng thức trên, ta có:

\[
|\det(X)| = |\det(X^*)| \leq \|x_1^*\|\|x_2^*\|\cdots\|x_n^*\| \leq \|x_1\|\|x_2\|\cdots\|x_n\|.
\]

Do đó, ta có điều cần chứng minh:

\[
|\det(X)| \leq \|x_1\|\|x_2\|\cdots\|x_n\|.
\]

