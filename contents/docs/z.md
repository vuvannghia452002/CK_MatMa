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

<!--! Mô tả hệ mật -->

<!--! Bảng chữ cái -->

<!--! Sinh cặp khóa công khai  và bí mật -->

<!--! Ví dụ: -->

<!-- code? -->

<!--! Áp dụng hệ mật RSA -->

<!--! LLL -->

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
