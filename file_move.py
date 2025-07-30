import os
import shutil

source_root = r"D:\개인프로젝트\fall_detection\dataset\라벨링"
target_folder = r"D:\개인프로젝트\fall_detection\dataset\label"

# 목적지 폴더가 없으면 생성
os.makedirs(target_folder, exist_ok=True)

count = 0

# source_root 아래 폴더 순회
for folder_name in os.listdir(source_root):
    folder_path = os.path.join(source_root, folder_name)

    # 폴더가 아니면 무시
    if not os.path.isdir(folder_path):
        continue

    # 그 폴더 내 파일 목록 가져오기
    files = os.listdir(folder_path)

    # 내부가 비어 있거나 내부 파일이 여러 개인 폴더 확인
    if len(files) != 1:
        print(f"{folder_name}: contains {len(files)} files")

    # 파일 전체 경로
    file_name = files[0]  # 한 폴더 안에 하나의 파일만 들어 있으므로
    source_file = os.path.join(folder_path, file_name)
    destination_file = os.path.join(target_folder, file_name)

    # 이동
    shutil.move(source_file, destination_file)

    count += 1
    # 매 1000개마다 진행 상황 출력
    if count % 1000 == 0:
        print(f"\t{count} files moved...")

print(f"✅ Done. Total files moved: {count}")