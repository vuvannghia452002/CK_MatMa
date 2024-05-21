

Tìm video k có thì sách DA ...
Chứng minh 1 2 3....
tìm xong chắc là b1 thì ok
Thực hiện các bước bài toán ... latex
Code


<!-- !Bài toán tìm vector ngắn nhất (Shortest Vector Problem - SVP) -->

<!--! Độ dài =..... -->
<!-- \begin{frame}{Vector ngắn nhất} -->
<!-- -->
<!-- \begin{itemize} -->
<!-- \item Độ dài vector $v = (v_1, v_2, \dots, v_n)$ là: -->
<!-- -->
<!-- $$\|v\| = (v_1^2 + v_2^2 + \dots + v_n^2)^{\tfrac{1}{2}}$$ -->
<!-- -->
<!-- -->
<!-- \end{itemize} -->
<!-- -->
<!-- \end{frame} -->

<!-- @ Có nhiều vector ngắn nhất khi đi tìm gần như ngắn nhất (vì theo tg đa thức) -->
<!-- @ Là vector đầu tiên (Chưa học LLL?????) + chứng minh -->
<!-- @Có thể đưa xuống sau LLL -->

<!-- youtube -->
<!-- youtube -->
<!-- youtube -->
<!-- youtube -->
<!-- youtube -->
<!-- youtube -->
<!-- youtube -->
<!-- youtube -->
![alt text](new/nghia1/pictures/image.png)


An Introduction to Mathematical Cryptography (2014) - Hoffstein, Pipher, Silverman



Lecture-Intro_Lattices.pdf

<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->










<!-- Để phá vỡ mã hóa RSA ta cần giải x trong bài toán: -->
<!-- c = (T + x) ^ e mod N -->

Chúng ta có thể chuyển đổi vấn đề này thành bài toán vectơ ngắn nhất, sau đó sử dụng LLL để giải nó.

<!-- @ Thống nhất kí hiệu và biến -->
<!-- @ Thống nhất kí hiệu và biến -->

<!--! Phương pháp lưới -->

Để phá vỡ mã hóa RSA yêu cầu giải phương trình đồng dư $c \equiv (M + x)^e \quad (mod \ N)$

Ta có:
$$x^n + a_{n-1}x^{n-1} + \dots + a_2x^2 + a_1x + a_0 \equiv 0 \quad (mod \ N) $$

Ta có được lưới bởi cơ sở như sau:

<!-- $$
\begin{aligned}
&\Vec{v_1} = (N, 0, 0, \dots, 0, 0)\\
&\Vec{v_2} = (0, YN, 0, \dots, 0, 0)\\
&\vdots\\
&\Vec{v_n} = (0, 0, 0, \dots, Y^{n-1}N, 0)\\
&\Vec{v_{n+1} = (a_0, a_1Y, \dots, a_{n-1}Y^{n-1}, Y^{n})}
\end{aligned}
$$ -->

<!-- @ Tại sao lại có công thức lưới qui định ntn? -->

<!-- !Thực hiện giảm lưới -->

Dùng thuật toán LLL để thực hiện giảm lưới

Ta thu được cơ sở mới sau khi giảm lưới $b_0, b_1, b_2, \dots, b_{n+1}$

<!-- !Tìm vector ngắn nhất -->

Ta sử dụng vector $b_0$ như vector ngắn nhất của lưới và chuyển về dạng đa thức:

<!-- @ chia cho m^xxxxxx -->

$$b_0 + \frac{b_1}{Y}x + \dots + \frac{b_{n-1}}{Y^{n-1}}x^{n-1} + \frac{b_n}{Y^n}x^n $$

=> Cuối cùng, thực hiện giải phương trình đa thức tìm nghiệm nguyên bài toán

<!-- @tìm đc x1 x2 x3 xét thêm x<y để suy ra x -->

<!--@ Gauuusss... -->

<!-- !Ví dụ: https://www.youtube.com/watch?v=vxS0DZE_Lvs -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!--  -->
<!-- det L = |det(x_1, x_2,..., x_n)| -->

<!-- Bổ đề trang 26???? -->

<!-- Định thức của một lưới không phụ thuộc vào cách chọn cơ sở. -->


<!-- trang 40 -->

<!-- @ -->
<!-- # -->

 
<!-- @ Lý thuyết -->
<!-- @ Lịch sử -->
<!-- @ Giới thiệu -->
<!-- @ Mục đích công dụng -->

<!-- @ Hình ảnh liên quan -->

<!-- @ Thuật toán -->
<!-- @ Các bước -->
<!-- @ Sơ đồ thuật toán -->

<!-- @ Code mã nguồn mã giả.... -->

<!-- @ Ví dụ minh họa -->
<!-- @ Chạy tay -->
<!-- @ Chương trình lập trình -->



% <!-- Điều kiện 1 -->

% <!-- Điều kiện 2 -->

% <!-- Mã giả -->

% <!-- Ví dụ -->

% <!--! Thuật toán LLL -->

% <!-- quy trình Gram-Schmidt: -->
% <!--Nếu $x_1, x_2, \dots, x_n$ là một cơ sở của lưới $L$ thì sau khi trực giao hóa ta thu được các vector $x_1^*, x_2^*, \dots, x_n^*$ có thể không nằm trong lưới $L$. -->
% <!-- Vì num là phân số.... -->
% <!-- Xin chào! Bạn có thể vui lòng giải thích mục đích của dòng: bk = bk - [uk, j]bj là gì không? -->
% <!-- quy trình Gram Schmidt làm cho cơ sở trực giao -->
% <!-- Tuy nhiên, trong LLL chúng ta đang làm việc trong một mạng nên không thể đảm bảo tính trực giao. -->
% <!-- Để làm được điều đó, chúng ta cần u_{k, j} là một số nguyên. -->
% <!-- Điều này tạo ra một cơ sở "đủ trực giao" trong khi vẫn còn trong mạng -->

% <!-- 2 chiều -->
% <!-- n chiều -->
% <!-- Thuật toán LLL giảm lưới -->

