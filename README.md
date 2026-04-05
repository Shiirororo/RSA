

# Lưu ý cho các con vợ:

Khi cần sửa mã nguồn, đừng có git init lại nữa, không thì sửa merge history mệt lắm

# Cách làm đúng:
## Clone
```
git clone https://github.com/Shiirororo/RSA.git
```
## Tạo nhánh mới để làm tính năng
```
git checkout -b rsa-feature-xyz
```
## Code và Commit:
```
git add .
git commit -m "feat: mô tả tính năng vừa làm"
```
## Push nhánh lên GitHub:
```
git push origin rsa-feature-xyz
```
## Tạo Pull Request: Lên GitHub nhấn nút Compare & Pull Request.

Thanks