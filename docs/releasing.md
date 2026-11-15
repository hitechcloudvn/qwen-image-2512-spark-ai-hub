# Releasing · Phát hành

Tiếng Việt · English

## Tiếng Việt

### Nguyên tắc

- **Không build local:** mọi ảnh container đều do CI/CD build và đăng lên GHCR.
- **Tag = nguồn sự thật:** mỗi phiên bản là một annotated tag `vX.Y.Z` (Semantic Versioning),
  được đẩy lên cả GitHub và GitLab.
- **Release tự động:** workflow `release.yml` tạo GitHub Release từ tag; GitLab tạo Release tương ứng.

### Các bước phát hành

1. Cập nhật `CHANGELOG.md`: chuyển mục `[Unreleased]` thành phiên bản mới với ngày phát hành.
2. Commit trên `main` (kèm trailer đồng tác giả) và đẩy lên GitHub + GitLab.
3. Tạo annotated tag và đẩy tag:

   ```bash
   git tag -a v1.0.0 -m "v1.0.0 — Initial public release"
   git push origin v1.0.0
   git push gitlab v1.0.0
   ```

4. CI/CD lo phần còn lại:
   - **GitHub Actions `publish.yml`:** build ảnh `linux/arm64` và đăng lên
     `ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub` với các tag `latest`, `sha-<sha>`, `v1.0.0`.
   - **GitHub Actions `release.yml`:** tạo GitHub Release với ghi chú trích từ `CHANGELOG.md`.
   - **GitLab CI:** job `release` tạo GitLab Release cho tag.

### Quy ước version

| Thay đổi | Version | Ví dụ |
| --- | --- | --- |
| Sửa lỗi, chỉnh sửa nhỏ | Patch | `v1.0.1` |
| Tính năng mới tương thích ngược | Minor | `v1.1.0` |
| Phá vỡ tương thích | Major | `v2.0.0` |

## English

### Principles

- **No local builds:** all container images are built and published to GHCR by CI/CD.
- **Tags are the source of truth:** each release is an annotated `vX.Y.Z` tag
  (Semantic Versioning), pushed to both GitHub and GitLab.
- **Automated releases:** the `release.yml` workflow creates the GitHub Release from the tag;
  GitLab creates the corresponding Release.

### Release steps

1. Update `CHANGELOG.md`: turn the `[Unreleased]` section into the new version with its date.
2. Commit on `main` (with the co-author trailers) and push to GitHub + GitLab.
3. Create an annotated tag and push it:

   ```bash
   git tag -a v1.0.0 -m "v1.0.0 — Initial public release"
   git push origin v1.0.0
   git push gitlab v1.0.0
   ```

4. CI/CD handles the rest:
   - **GitHub Actions `publish.yml`:** builds the `linux/arm64` image and publishes it to
     `ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub` with the `latest`, `sha-<sha>`, `v1.0.0` tags.
   - **GitHub Actions `release.yml`:** creates the GitHub Release with notes extracted from `CHANGELOG.md`.
   - **GitLab CI:** the `release` job creates the GitLab Release for the tag.

### Versioning convention

| Change | Version | Example |
| --- | --- | --- |
| Bug fixes, small edits | Patch | `v1.0.1` |
| Backward-compatible features | Minor | `v1.1.0` |
| Breaking changes | Major | `v2.0.0` |
