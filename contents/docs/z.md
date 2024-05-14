<!-- -->
<!-- Tổng quan về mật mã khóa công khai -->

<!-- Lịch sử -->

Ý tưởng về hệ thống mã hóa khóa công khai được Martin Hellman, Ralph Merkle và Whitfield Diffie tại Đại học Stanford giới thiệu vào năm 1976.

Sách: Diffie, W.; Hellman, M.E. (November 1976). "New directions in cryptography". IEEE Transactions on Information Theory

<!-- Khái niệm -->

Mật mã khóa công khai là hệ mã không đối xứng, nghĩa là sử dụng hai khóa liên đới cho việc mã hoá và giải mã thay vì một khóa duy nhất như trong các hệ mã cổ điển. Việc này đáp ứng được các yêu cầu trong các ứng dụng về bảo mật riêng tư, phân phối khóa, và xác thực điện tử.

Lưu ý:

Một hệ mật khóa công khai không bao giờ cung cấp độ mật vô điều kiện - thực tế, đó là hàm cửa sập một chiều (a trapdoor one-way function).

<!-- Mô hình tổng quát -->

![alt text](public.png)

<!-- Ý tưởng: -->
<!-- Mỗi người dùng: sử dụng một cặp khóa (khóa công khai, khóa bí mật) -->
<!-- Khóa công cộng: được công bố rộng rãi và được sử dụng trong mã hóa thông tin -->
<!-- Khóa riêng: chỉ do một người nắm giữ và được sử dụng để giải mã thông tin đã được mã hóa bằng khóa công cộng tương ứng -->
<!-- Mã hóa: A muốn gửi thông điệp cho B - mã hóa bằng khóa công khai của B ($$y = E(e_B, x)$$) -->
<!-- Giải mã: B giải mã bằng khóa bí mật của mình ($$x = D(d_B, y)$$) -->

<!--! Những hệ mật khóa công khai quan trọng nhất -->

<!-- RSA: dựa trên độ khó của phép phân tích các số nguyên lớn. -->

<!-- Merkle-Hellman Knapsack: dựa trên độ khó của bài toán subset sum (được biết là NP-complete). Tuy nhiên, có nhiều hệ mật dựa trên bài toán sắp ba lô đã được chứng minh là không bảo mật. -->

<!-- McEliece: dựa trên bài toán giải mã của một mã tuyến tính (cũng được cho là NP-complete). -->

<!-- ElGamal: dựa trên bài toán Logarit rời rạc trên trường hữu hạn. -->

<!-- Chor-Rivest: là một hệ sắp ba lô nhưng được xem là bảo mật. -->

<!-- Elliptic Curve: là sự cải tiến của các hệ mật khác, chẳng hạn tương tự ElGamal nhưng dựa trên các đường cong elíp thay vì trường hữu hạn. Ưu điểm của các hệ mật dạng này là có thể duy trì được độ bảo mật với khóa nhỏ hơn thông thường. -->

<!-- Hệ mật RSA -->

<!-- Lịch sử -->

Hệ mật RSA, được phát triển bởi Ron Rivest, Adi Shamir và Leonard Adleman (1977), có thể được sử dụng trong bảo mật dữ liệu và công nghệ chữ ký điện tử.

<!-- Ý tưởng -->
<!-- Bảo mật của RSA dựa trên giả thuyết không có các thuật toán đủ nhanh để khai triển luỹ thừa một số. Qui trình áp dụng RSA gồm hai bước: -->

<!-- Lựa chọn (sinh) cặp khóa công khai và khóa bí mật -->

<!-- Thực hiện thuật toán mã hoá và thuật toán giải mã -->

% \subsection{Mô tả hệ mật}

\begin{itemize}
\item Các phép tính được thực hiện trên $Z_n$ với $n = p \cdot q$.
\item $S = \langle P, C, K, E, D \rangle$
\begin{itemize}
\item $n = pq$ với $p$ và $q$ là hai số nguyên tố lẻ phân biệt. $\phi(n) = (p-1)(q-1)$
\item $P = C = Z_n$
\item $K = \{(n, p, q, a, b) : n = pq, p, q$ là số nguyên tố, $ab \equiv 1 \mod \phi(n) \}$
\end{itemize}
\end{itemize}

Với mỗi $k = (n, p, q, a, b) \in K$, định nghĩa:
\begin{align*}
e_k(x) &= x^b \mod n \\
d_k(y) &= y^a \mod n
\end{align*}
với $x, y \in Z_n$.

% \subsection{Sinh cặp khóa công khai - bí mật}

\begin{enumerate}
\item Chọn hai số nguyên tố đủ lớn, $p$ và $q$
\item Tính toán $n = pq$ và $\phi(n) = (p - 1)(q - 1)$
\item Chọn một số, $e$ $(1 < e < \phi(n))$ sao cho $\text{gcd}(e, \phi(n)) = 1$. Giá trị $e$ sẽ được sử dụng trong mã hoá
\item Tìm một số $d$ sao cho $ed - 1$ chia hết cho $\phi(n)$, hay nói cách khác $d = e^{-1} \mod \phi(n)$. Giá trị $d$ sẽ được sử dụng để giải mã
\item Công khai khóa $K^+_B$ = (n, e) và giữ bí mật khóa $K^-_B$ = (n, d)
\end{enumerate}

\begin{figure}[H]
\centering
\includegraphics[scale = 0.4]{pictures/Bob_Alice.jpg}
\caption{Thuật toán mã hoá (Alice) và thuật toán giải mã (Bob)}
\end{figure}

Mã hoá (Alice):

Giả sử Alice muốn gửi cho Bob một mẫu bit, hoặc một số $m$ sao cho $m < n$. Để mã hoá, Alice thực hiện tính luỹ thừa, $m^e$, sau đó tính toán số dư khi đem chia $m^e$ cho $n$. Vì vậy, giá trị được mã hoá ($c$) của bản tin $m$ là: $c = m^e \mod n $

Giải mã (Bob):

Để giải mã đoạn tin mã hoá nhận được ($c$), Bob tính toán: $ m = c^d \mod n $. Việc này đòi hỏi phải sử dụng khóa bí mật $(n, d)$.

Ví dụ:

Giả sử B chọn $p = 101$ và $q = 113$, khi đó $n = 11413$ và $\phi(n) = 11200$.

Giả sử B chọn $b = 3533$, khi đó bằng thuật toán Euclidean mở rộng ta tính được
\[a = b^{-1} \equiv 6597 \pmod{11200}.\]

B công khai bộ $(n = 11413, b = 3533)$.

Bây giờ giả sử A muốn gửi từ hiện $9726$ cho B, A sẽ tính
\[9726^{3533} \equiv 5761 \pmod{11413}, \]
là từ mã.

Khi B nhận được $5761$, B sẽ tính
\[5761^{6597} \equiv 9726 \pmod{11413}, \]
và thu được từ hiện A muốn gửi.

% \subsection{Áp dụng hệ mật RSA}

\begin{enumerate}
\item Sinh hai số nguyên tố có giá trị lớn: $p$ và $q$
\item Tính $n = pq$ và $\phi(n) = (p - 1)(q - 1)$
\item Chọn ngẫu nhiên một số nguyên $e$ $(1 < e < \phi(n))$ thỏa $\text{gcd}(e, \phi(n)) = 1$
\item Tính giá trị $d = e^{-1} \mod \phi(n)$ (bằng thuật toán Euclide mở rộng)
\item Công bố giá trị $(n, e)$ (khóa công khai)
\item Giữ bí mật giá trị $(p, q, d)$ (khóa bí mật)
\end{enumerate}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \section\*{References:}
Diffie, W.; Hellman, M.E. (November 1976). "New directions in cryptography". IEEE Transactions on Information Theory

https://ieeexplore.ieee.org/document/1055638

Slide mật mã thầy Hân

Slide mật mã thầy Nam

\end{document}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

<!-- Khái niệm hệ mật khóa công khai -->
<!-- Cách tấn công (phương thức/giao thức, cơ chế, lỗ hổng, ...) -->
<!-- Áp dụng: Hệ RSA -->
<!-- Lịch sử ra đời -->
<!-- Cơ chế hoạt động -->
<!-- Ưu điểm, nhược điểm -->
<!-- Ví dụ thực tế -->

<!-- asymmetric algorithm (RSA) -->
<!-- RSA -->
<!-- public -->
<!-- LLL -->

<!-- -->
<!-- https://web.microsoftstream.com/video/a677964a-d1a2-40a8-bb4d-dc7e70ad75a3 -->
<!-- https://web.microsoftstream.com/video/cbe08326-77fc-42a2-bd2d-eb693e6c8e49 -->
<!-- https://web.microsoftstream.com/video/25535150-2bf5-43a2-8ed6-94e7133dc4e9 -->
<!--! https://web.microsoftstream.com/video/2213acc3-a878-4d67-90ee-a4b5bbaf6756 -->

https://web.microsoftstream.com/video/6f4b3e1e-cdb7-4cb9-b50f-ae249b8d206c

<!-- https://web.microsoftstream.com/video/11bad894-f6cf-4f5a-9b44-4eaa5f33f194 -->

https://web.microsoftstream.com/video/b66de9dd-5c60-42f4-8f48-9d5bb0cb5906

<!-- Sardinas Patterson .. -->
<!-- https://web.microsoftstream.com/video/99b83abc-56d7-469c-ae1c-2109beb4e47a -->

https://web.microsoftstream.com/video/88acb276-cde0-4583-b6d8-29a39c333cd3
https://web.microsoftstream.com/video/0e063e14-db41-43c2-bb88-d64589a87d26
https://web.microsoftstream.com/video/a07fc02b-da90-44f7-a164-e257a380923a