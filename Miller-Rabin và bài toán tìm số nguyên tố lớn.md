---
date: 2026-04-13T09:03
tags:
  - "#math"
---
# Abstract

	Trong lĩnh vực mật mã học, phương pháp RSA dựa trên cơ sở các số nguyên tố lớn để triển khai. Tuy nhiên, trong use case thực tế, các số đó có thể lên tới 256 bit, hoặc 512 bit, điều này khiến việc kiểm tra các số nguyên tố lớn mất rất nhiều thời gian với độ phức tạp:
	
$$O(\sqrt n)$$
	Dựa vào định lý Fermat nhỏ từ thế kỉ XVII, Garry Miller và 
# I. Định lý Fermat nhỏ

Vào năm 1640, Fermat phát hiện ra rằng tất cả các số nguyên tố $p$ và một số $a$ trong khoảng $1 < a < p$ thì:
	$$a^{p-1}\equiv 1 (mod \; p)$$
Ví dụ $(p, a)=(17, 5)$, ta có:
$$5^{16} \equiv 1(mod \;17)$$

Và 17 đúng là số nguyên tố!


Tuy nhiên, điều ngược lại thì không đúng. Vẫn tồn tại hợp số a sao cho: $a^{p-1}\equiv 1 (mod \; p)$, ví dụ

$$n=561 \quad a = 100 \quad và \quad 100^{560}\equiv1(mod ~ 561)$$
Tuy nhiên:
$$561=3\times11\times17 $$

Do đó, đối với các số đặc biệt như 561, người ta gọi chúng là Carmichael Numbers (hay số giả nguyên tố), trong đó các số $a$ được cho là liar nếu chúng khiến các số composite $c$ thỏa mãn $a^{c-1}\equiv 1 (mod \; c)$


![[Pasted image 20260413093348.png]]
*Các số liar và witness*

# II. Sự mở rộng định lý của Miller và phát triển của Rabin

Sau khi Václav Simerka phát hiện 7 số Carmichael đầu tiên vào 1800s,
$$561, 1105, 1729, 2465, 2821, 6601, 8911$$
Paul Erdos chứng minh được rằng các số Carmichael tồn tại vô hạn và Robert Carmichael đồng ý với điều này (nên nó mới gọi là số Carmichael).


![[Pasted image 20260413093736.png|331]] ![[Pasted image 20260413093856.png|320]]


Năm 1994, William "RED" Alford, Andrew Granville, Carl Pomerance đã chứng minh sự tồn tại vô hạn của dãy số Carmichael


## 1. Thuật toán của Garry Miller 

Năm 1970s, Garry Miller cho ra một cách tiếp cận mở rộng để kiểm tra số nguyên tố dựa trên phương pháp kiểm tra của Fermat. Ông thực hiện như sau:
- Thay vì dừng lại ở 	$a^{p-1}\equiv 1 (mod \; p)$ , ông tiếp tục chia đôi $p_1 = p-1$, sau đó tiếp tục kiểm tra $a^{p_1}(mod \; p)$.

Hãy lấy ví dụ với $n = 561$, Miller cho ra chuỗi:
$$100^{35} \equiv 298 (mod \; 561)$$
$$100^{70} \equiv 166 (mod \; 561)$$
$$100^{140} \equiv 67 (mod \; 561)$$
$$100^{280} \equiv 1 (mod \; 561)$$
$$100^{560} \equiv 1 (mod \; 561)$$



Ông đưa ra mệnh đề như sau:

	Một số là số nguyên tố nếu nó thỏa mãn 2 điều kiện:
	- Chuỗi kiểm tra phải kết thúc bằng 1
	- Nếu chuỗi tồn tại số 1, thì số trước đó phải là 1 hoặc n-1


Với điều kiện thứ nhất, chúng tuân theo định luận của Fermat. Với Điều kiện thứ 2, trong trường số nguyên tố hữu hạn, ta có:
$$mod \; p$$
$$\sqrt{1} = 1 \quad or \quad p-1$$


VD2: $n = 41$
$$8^{5} \equiv 9 (mod \; 41)$$
$$8^{10} \equiv 40 (mod \; 41)$$
$$8^{20} \equiv 1 (mod \; 41)$$
$$8^{40} \equiv 1 (mod \; 41)$$




Có thể thấy, Miller test là một sự bổ sung cho Fermat test giúp phát hiện những số Carmichael. Tuy nhiên, test của Miller vẫn chưa hoàn hảo, có thể lấy ví dụ sau:

$n = 221, \; a = 174$
$$174^{55} \equiv 47 (mod \; 221)$$
$$174^{110} \equiv 220 (mod \; 221)$$
$$174^{220} \equiv 1 (mod \; 221)$$


Có thể thấy, case trên đáp ứng 2 điều kiện của Miller, tuy nhiên $$221 = 13 \times 17 $$

### 2. Sự cải tiến của Michael Rabin

Nhiều năm sau, nhận thấy sự quan trọng từ công trình của Miller, Michael Rabin đã tham gia và ông chứng minh được rằng tỷ lệ các số witnesses lớn hơn 75%. Do đó, phương pháp đề ra là sẽ test số đó bằng phương pháp của Miller nhiều lần, qua đó ta có tỉ lệ của trường hợp False-Positive sau k lần là:
$$P[False\;Positive] \leq (\frac{1}{4})^k$$

Với k = 10, xác suất sai xấp xỉ khoảng 1/ 1.000.000
# III. Triển khai thuật toán Miller - Rabin với Python


### Miller Iteration

``` Python
def millerRabinIteration(n):

	a = secrets.randbelow(n-3) + 2
	e = n - 1
	if Math.modExp(a, e, n) ! = 1:
		return False
	
	prevIs1 = True
	
	while e%2 == 0:
		e //= 2
		x = Math.modExp(a, e, n)
		if prevIs1:
			if x == n-1:
				prevIs1 = False
			elif x ! = 1:
				return False
	
	return True
```


### Miller Rabin Algorithm

``` Python
def millerRabin(n, k = 40):

	if n < 2:
		return False
	
	for _ in range (k):
		if not Math.millerRabinIteration(n):
			return False
	
	return True
```