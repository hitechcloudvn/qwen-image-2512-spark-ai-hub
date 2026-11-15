# Contributing · Đóng góp

Tiếng Việt · English

## Tiếng Việt

Cảm ơn bạn đã quan tâm đóng góp cho **qwen-image-2512-spark-ai-hub**!

### Quy trình

1. Fork kho mã trên GitHub: <https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub>.
2. Tạo nhánh đặc tả: `git checkout -b feature/<ten-tinh-nang>`.
3. Thực hiện thay đổi, giữ mã nguồn và tài liệu **song ngữ Việt–Anh**.
4. Kiểm tra cục bộ: `python -m py_compile app.py`.
5. Commit với thông điệp rõ ràng, kết thúc bằng trailer đồng tác giả:

   ```
   Co-authored-by: @pgt-vn <nguyenthanhan92f1@gmail.com>
   Co-authored-by: @agent-hitechcloud <agent@hitechcloud.vn>
   ```

6. Đẩy nhánh và mở Pull Request (GitHub) hoặc Merge Request (GitLab).

### Nguyên tắc

- **Song ngữ / Bilingual:** mọi chú thích, nhãn UI và tài liệu mới phải có cả tiếng Việt và tiếng Anh (VI trước, EN sau).
- **Không build local để phát hành:** ảnh container được CI/CD build và đăng lên GHCR; không commit ảnh build cục bộ.
- **Tôn trọng tổ chức:** tham chiếu kho mã, ảnh và tài liệu dùng namespace `hitechcloudvn` trên cả GitHub và GitLab.
- **Tuân thủ versioning:** đánh tag `vX.Y.Z` theo Semantic Versioning; cập nhật `CHANGELOG.md` trước khi phát hành.

## English

Thank you for contributing to **qwen-image-2512-spark-ai-hub**!

### Workflow

1. Fork the repository on GitHub: <https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub>.
2. Create a topic branch: `git checkout -b feature/<name>`.
3. Make your changes, keeping code and docs **bilingual Vietnamese–English**.
4. Check locally: `python -m py_compile app.py`.
5. Commit with a clear message ending in the co-author trailers:

   ```
   Co-authored-by: @pgt-vn <nguyenthanhan92f1@gmail.com>
   Co-authored-by: @agent-hitechcloud <agent@hitechcloud.vn>
   ```

6. Push the branch and open a Pull Request (GitHub) or Merge Request (GitLab).

### Principles

- **Bilingual:** every new comment, UI label, and doc must carry both Vietnamese and English (VI first, EN second).
- **No local builds for releases:** container images are built and published to GHCR by CI/CD; do not commit locally built images.
- **Respect the org:** reference repos, images, and docs under the `hitechcloudvn` namespace on both GitHub and GitLab.
- **Follow versioning:** tag `vX.Y.Z` per Semantic Versioning; update `CHANGELOG.md` before each release.
