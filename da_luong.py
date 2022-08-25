import  multiprocessing
import taoprofile


def mofile():
    f = open("acccanmo.txt", mode='r', encoding='utf-8')
    tai_khoan = []
    dia_chi=input("ban muon mo nuoc nao : ")
    thu_muc_chua_profie = input("nhap thu muc chua profile (tên thư mục phải có định dạng như sau E:\\mu\\toolgmailusa\\profile ): ")
    tokens = input("dien token cua ban : ")
    for tk in f:
        if tk == None :
            continue
        tk = tk.rstrip().split()
        #tk[2] = "".join(tk[2:])
        tk.append(dia_chi)
        tk.append(tokens)
        tk.append(dia_chi)
        tai_khoan.append(tk)
    f.close()
    return tai_khoan



def thu_tach_chuoi(tong_tai_khoan):
    so_luong = int(input("so luong ban muon chay : " ))
    bien=0
    mang_chay = []
    mang_cuoi=[]
    for so_thu_tu in range(len(tong_tai_khoan)):
        mang_chay.append(tong_tai_khoan[so_thu_tu])
        bien+=1
        if bien % so_luong ==0 or bien == len(tong_tai_khoan):
            mang_cuoi.append(mang_chay)
            mang_chay=[]
    return mang_cuoi




if __name__ == '__main__':

    multiprocessing.freeze_support()
    tong_tai_khoan = mofile()
    mang_bo_vao_chay=thu_tach_chuoi(tong_tai_khoan)
    #lay tai khoan trong ham mofile
    luong=[]

    for b in mang_bo_vao_chay:
        for a in b :
            chay = multiprocessing.Process(target=taoprofile.chay_tien_trinh, args=[a])
            chay.start()
            luong.append(chay)
        for hetluong in luong:
            hetluong.join()





"""a=mofile()
b=thu_tach_chuoi(a)
for duc in b :
    print(duc)"""











