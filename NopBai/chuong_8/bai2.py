class TuDienAlbum:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, bai_hats):
        # bai_hats là danh sách các tuple (ten_bai_hat, nhac_si, ca_si)
        if ten_album not in self.albums:
            self.albums[ten_album] = bai_hats
        else:
            print("Album đã tồn tại.")

    def XemAlbum(self, ten_album):
        if ten_album in self.albums:
            print(f"Thông tin album '{ten_album}':")
            for bai_hat in self.albums[ten_album]:
                ten_bai, nhac_si, ca_si = bai_hat
                print(f"Bài hát: {ten_bai}, Nhạc sĩ: {nhac_si}, Ca sĩ: {ca_si}")
        else:
            print("Album không tồn tại.")

# Sử dụng lớp TuDienAlbum
td_album = TuDienAlbum()
td_album.NhapAlbum("Album 1", [("Bài hát 1", "Nhạc sĩ A", "Ca sĩ X"), ("Bài hát 2", "Nhạc sĩ B", "Ca sĩ Y")])
td_album.XemAlbum("Album 1")