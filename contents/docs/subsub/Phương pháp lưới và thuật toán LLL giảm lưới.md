
\defi{\textbf{Định lý 2.5.} \textit{Nếu $x_1,x_2$ là cơ sở rút gọn của lưới $L$ thì $x_1$ là vector khác không ngắn nhất của lưới đó.}}
\textit{Chứng minh.}\\
Đặt $ax_1 + bx_2$ là vector khác không bất kì trong lưới $L$ (với $a,b \in Z$).\\
Ta có: \hspace{4cm}$ \quad \|ax_1 + bx_2\|^2 = a^2\|x_1\|^2 + b^2\|x_2\|^2 + 2abx_1x_2$\\
Vì $x_1,x_2$ là cơ sở giảm nên: $$-\frac{1}{2}x_1x_1 \leq x_1x_2 \leq \frac{1}{2}x_1x_1 \text{.}$$
Suy ra: \hspace{3cm} $\qquad 2abx_1x_2 \geq -|ab|\|x_1\|^2 . \quad \text{Do đó}$
$$
\begin{aligned}
    \|ax_1 + bx_2\|^2 &\geq a^2\|x_1\|^2 - |ab|\|x_1\|^2 + b^2\|x_2\|^2 \\
    & \geq a^2\|x_1\|^2 - |ab|\|x_1\|^2 + b^2\|x_1\|^2  \quad (\text{do }\|x_2\| \geq \|x_1\|)\\
    & = (a^2 - |ab| + b^2) \|x_1\|^2 \text{.}
\end{aligned}
$$
Ta thấy $a^2 - |ab| + b^2 \in N$ và bằng 0 khi và chỉ khi $a = b = 0$.\\
Nhưng \quad $ax_1 + bx_2 \ne 0$ \qquad $\Rightarrow$ \qquad Trường hợp $a = b = 0$ (loại).\\
\hspace*{3cm}$\Rightarrow a^2 - |ab| + b^2 \geq 1$\\
\hspace*{3cm}$ \Rightarrow \|ax_1 + bx_2\| \geq \|x_1\|^2$.\\
Do đó $x_1$ là vector khác không ngắn nhất của lưới.
\vspace{1cm}
