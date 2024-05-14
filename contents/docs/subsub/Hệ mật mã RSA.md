![alt text](image-2.png)
Mã hóa: 
c = E (m, KB+) = m^e \mod n
Giải mã: 
m=  D (c, KB-) = c^d \mod n



<!--! Ví dụ: -->

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

<!-- code? -->



 



<!--! Mô tả hệ mật -->
<!--! Bảng chữ cái -->