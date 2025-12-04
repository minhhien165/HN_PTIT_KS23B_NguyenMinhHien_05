import numpy as np
import csv
import matplotlib.pyplot as plt

PlayerList = []
DATA_FILE = "data.csv"


def save_to_csv():
    try:
        if len(PlayerList) == 0:
            print("Không có dữ liệu để lưu.")
            return

        with open(DATA_FILE, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ['ma_ct', 'ten_ct', 'so_tran', 'ban_thang',
                          'kien_tao', 'diem_thanh_tich', 'danh_hieu']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(PlayerList)
        print(f"Đã lưu dữ liệu vào {DATA_FILE}")
    except Exception as e:
        print(f"Lỗi khi lưu CSV: {e}")

def displayAllPlayers():
    if len(PlayerList) == 0:
        print("\nDanh sách cầu thủ trống!")
        return
    else:
        print("\n" + "="*110)
        print(f"{'STT':<5} {'Mã CT':<10} {'Tên CT':<20} {'Số trận':<8} "
              f"{'Bàn thắng':<10} {'Kiến tạo':<9} {'Điểm thành tích':<20} {'Danh hiệu':<12}")
        print("="*110)

        for idx, player in enumerate(PlayerList, 1):
            print(f"{idx:<5} {player['ma_ct']:<10} {player['ten_ct']:<25} "
                  f"{player['so_tran']:<8} {player['ban_thang']:<8} "
                  f"{player['kien_tao']:<8} "
                  f"{player['diem_thanh_tich']:<20} "
                  f"{player['danh_hieu']:<12}")

        print("="*110)

def findPlayerById(playerId: str):
    for player in PlayerList:
        if player["ma_ct"] == playerId:
            return player
    return None

def findPlayersByName(name: str):
    result = []
    nameLower = name.lower()
    for player in PlayerList:
        if nameLower in player["ten_ct"].lower():
            result.append(player)
    return result

def validatePlayerId(playerId: str) -> bool:
    for player in PlayerList:
        if player["ma_ct"] == playerId:
            return False
    return True

def validateIndexs(indexs: int) -> bool:
    return indexs >= 0

def diem_thanh_tich(ban_thang: int, kien_tao: int) -> int:
    return (ban_thang * 2) + kien_tao
    
def danh_hieu(diem_thanh_tich: int) -> str:
    if diem_thanh_tich > 40:
        return "Vàng"
    elif diem_thanh_tich > 20:
        return "Bạc"
    else:
        return "Đồng"
    
def read_data():
    global PlayerList
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        PlayerList = []
        for row in reader:
            player = {
                "ma_ct": row['ma_ct'],
                "ten_ct": row['ten_ct'],
                "so_tran": int(row['so_tran']),
                "ban_thang": int(row['ban_thang']),
                "kien_tao": int(row['kien_tao']),
            }
            player["diem_thanh_tich"] = diem_thanh_tich(
                player["ban_thang"], player["kien_tao"])
            player["danh_hieu"] = danh_hieu(player["diem_thanh_tich"])
            PlayerList.append(player)
        print(f"Đã tải {len(PlayerList)} cầu thủ từ {DATA_FILE}")    


def addPlayer():
    print("\n--- THÊM CẦU THỦ MỚI ---")
    while True:
        playerId = input("Nhập mã cầu thủ: ").strip()
        if not playerId:
            print("Mã cầu thủ không được để trống!")
            continue
        if not validatePlayerId(playerId):
            print("Mã cầu thủ đã tồn tại!")
            continue
        break

    name = input("Nhập tên cầu thủ: ").strip()
    while not name:
        print("Tên không được để trống!")
        name = input("Nhập tên cầu thủ: ").strip()

    while True:
        try:
            so_tran = int(input("Nhập số trận: "))
            if not validateIndexs(so_tran):
                print("Số trận phải là số nguyên không âm!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    while True:
        try:
            ban_thang = int(input("Nhập số bàn thắng: "))
            if not validateIndexs(ban_thang):
                print("Số bàn thắng phải là số nguyên không âm!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    while True:
        try:
            kien_tao = int(input("Nhập số kiến tạo: "))
            if not validateIndexs(kien_tao):
                print("Số kiến tạo phải là số nguyên không âm!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

    newPlayer = {
        "ma_ct": playerId,
        "ten_ct": name,
        "so_tran": so_tran,
        "ban_thang": ban_thang,
        "kien_tao": kien_tao,
    }
    newPlayer["diem_thanh_tich"] = diem_thanh_tich(
        newPlayer["ban_thang"], newPlayer["kien_tao"])
    newPlayer["danh_hieu"] = danh_hieu(newPlayer["diem_thanh_tich"])
    PlayerList.append(newPlayer)

    print(f"\nĐã thêm cầu thủ: {name} (Mã: {playerId})")
    print(f"  Điểm thành tích: {newPlayer['diem_thanh_tich']} - "
          f"Danh hiệu: {newPlayer['danh_hieu']}")
    
def updatePlayer():
    print("\n--- CẬP NHẬT THÔNG TIN CẦU THỦ ---")

    playerId = input("Nhập mã cầu thủ cần sửa: ").strip()
    player = findPlayerById(playerId)
    if not player:
        print(f"Không tìm thấy cầu thủ có mã: {playerId}")
        return
    print("Thông tin hiện tại:")
    print(f"  Mã cầu thủ: {player['ma_ct']}")
    print(f"  Tên cầu thủ: {player['ten_ct']}")
    print(f"  Số trận: {player['so_tran']}")
    print(f"  Bàn thắng: {player['ban_thang']}")
    print(f"  Kiến tạo: {player['kien_tao']}")
    print(f"  Điểm thành tích: {player['diem_thanh_tich']}")
    print(f"  Danh hiệu: {player['danh_hieu']}")
    ban_thang_input = input("Nhập số bàn thắng mới (Enter để giữ nguyên): ").strip()
    if ban_thang_input:
        try:
            ban_thang = int(ban_thang_input)
            if validateIndexs(ban_thang):
                player['ban_thang'] = ban_thang
            else:
                print("Số bàn thắng không hợp lệ, giữ nguyên giá trị cũ")
        except ValueError:
            print("Số bàn thắng không hợp lệ, giữ nguyên giá trị cũ")
    kien_tao_input = input("Nhập số kiến tạo mới (Enter để giữ nguyên): ").strip()
    if kien_tao_input:
        try:
            kien_tao = int(kien_tao_input)
            if validateIndexs(kien_tao):
                player['kien_tao'] = kien_tao
            else:
                print("Số kiến tạo không hợp lệ, giữ nguyên giá trị cũ")
        except ValueError:
            print("Số kiến tạo không hợp lệ, giữ nguyên giá trị cũ")
    player['diem_thanh_tich'] = diem_thanh_tich(
        player['ban_thang'], player['kien_tao'])
    player['danh_hieu'] = danh_hieu(player['diem_thanh_tich'])
    print("Đã cập nhật thông tin cầu thủ!")
    print(f"Mã cầu thủ: {player['ma_ct']} - Tên cầu thủ: {player['ten_ct']} - "
        f"Điểm thành tích mới: {player['diem_thanh_tich']} - "
        f"Danh hiệu: {player['danh_hieu']}")

def deletePlayer():
    print("\n--- XÓA CẦU THỦ ---")

    playerId = input("Nhập mã cầu thủ cần xóa: ").strip()
    player = findPlayerById(playerId)

    if not player:
        print(f"Không tìm thấy cầu thủ có mã: {playerId}")
        return

    print("Thông tin cầu thủ sẽ bị xóa:")
    print(f"Mã: {player['ma_ct']} - Tên: {player['ten_ct']}")

    confirm = input("Bạn có chắc muốn xóa? (y/n): ").strip().lower()
    if confirm in ['y']:
        PlayerList.remove(player)
        print(f"Đã xóa cầu thủ: {player['ten_ct']}")
    else:
        print("Đã hủy thao tác xóa")

def findPlayer():
    print("\n--- TÌM KIẾM CẦU THỦ ---")
    keyword = input("Nhập tên hoặc mã cầu thủ cần tìm: ").strip()

    player = findPlayerById(keyword)
    if player:
        print("\nTìm thấy cầu thủ:")
        print(f"Mã CT: {player['ma_ct']} | Tên CT: {player['ten_ct']} | "
              f"Số trận: {player['so_tran']} | "
              f"Bàn thắng: {player['ban_thang']} | "
              f"Kiến tạo: {player['kien_tao']} | "
              f"Điểm thành tích: {player['diem_thanh_tich']} | "
              f"Danh hiệu: {player['danh_hieu']}")
        return

    results = findPlayersByName(keyword)
    if len(results) > 0:
        print(f"\nTìm thấy {len(results)} cầu thủ:")
        for player in results:
            print(f"Mã CT: {player['ma_ct']} | Tên CT: {player['ten_ct']} | "
                  f"Số trận: {player['so_tran']} | "
                  f"Bàn thắng: {player['ban_thang']} |"
                  f"Kiến tạo: {player['kien_tao']} | "
                  f"Điểm thành tích: {player['diem_thanh_tich']} | "
                  f"Danh hiệu: {player['danh_hieu']}")
    else:
        print(f"Không tìm thấy cầu thủ nào với từ khóa: {keyword}")

def sortPlayers():
    if len(PlayerList) == 0:
        print("\nDanh sách cầu thủ trống!")
        return

    print("\n--- SẮP XẾP DANH SÁCH CẦU THỦ ---")
    print("1. Sắp xếp theo Điểm thành tích giảm dần")
    print("2. Sắp xếp theo Bàn thắng giảm dần")

    choice = input("Chọn cách sắp xếp (1-2): ").strip()

    match choice:
        case '1':
            PlayerList.sort(key=lambda x: x['diem_thanh_tich'], reverse=True)
            print("Đã sắp xếp theo Điểm thành tích giảm dần")
        case '2':
            PlayerList.sort(key=lambda x: x['ban_thang'], reverse=True)
            print("Đã sắp xếp theo Bàn thắng giảm dần")
        case _:
            print("Lựa chọn không hợp lệ!")
            return
    displayAllPlayers()

def menu():
    print("1. Hiển thị danh sách cầu thủ")
    print("2. Thêm mới cầu thủ")
    print("3. Cập nhật thông tin cầu thủ")
    print("4. Xoá cầu thủ")
    print("5. Tìm kiếm cầu thủ")
    print("6. Sắp xếp danh sách cầu thủ")
    print("7. Thống kê cầu thủ theo danh hiệu")
    print("8. Vẽ biểu đồ thống kê số lượng cầu thủ theo danh hiệu")
    print("9. Lưu vào file CSV")
    print("10. Thoát")

def handle_choice(choice):
    match choice:
        case '1':
            displayAllPlayers()
        case '2':
            addPlayer()
        case '3':
            updatePlayer()
        case '4':
            deletePlayer()
        case '5':
            findPlayer()
        case '6':
            sortPlayers()
        case '7':
            print("Thống kê cầu thủ theo danh hiệu")
        case '8':
            print("Vẽ biểu đồ thống kê số lượng cầu thủ theo danh hiệu")
        case '9':
            save_to_csv()
        case '10':
            save_to_csv()
            print("Thoát chương trình.")
            return False
        case _:
            print("Lựa chọn không hợp lệ!")
    return True

def main():
    read_data()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn (1-10): ").strip()
        if not handle_choice(choice):
            break


if __name__ == "__main__":
    main()