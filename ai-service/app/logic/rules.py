from typing import Dict, Iterable, Tuple


SEVERE_FLAGS = {"chảy máu", "lan rộng rất nhanh", "đau nhức dữ dội"}


def decide_risk(cv_scores: Dict[str, float], selected_symptoms: Iterable[str]) -> Tuple[str, str]:
    sel = {s.strip().lower() for s in selected_symptoms if s and s.strip()}

    # Ưu tiên 1: Cờ đỏ từ triệu chứng
    if sel & SEVERE_FLAGS:
        return "CAO 🔴", "Phát hiện triệu chứng nghiêm trọng."

    # Ưu tiên 2: Cờ đỏ từ CV
    if cv_scores.get("melanoma", 0.0) > 0.3:
        return "CAO 🔴", "Hình ảnh có đặc điểm của tổn thương ác tính."

    # Ưu tiên 3: Cờ vàng - Kết hợp
    if cv_scores.get("melanoma", 0.0) > 0.1 and ("mới xuất hiện" in sel):
        return "TRUNG BÌNH 🟡", "Phát hiện nốt ruồi mới xuất hiện có đặc điểm đáng ngờ."

    if cv_scores.get("eczema", 0.0) > 0.6 and ("ngứa" in sel):
        return "TRUNG BÌNH 🟡", "Các triệu chứng và hình ảnh tương đồng với viêm da/chàm."

    # Mặc định: Cờ xanh
    return "THẤP 🟢", "Các đặc điểm tương tự với tình trạng da thông thường."
