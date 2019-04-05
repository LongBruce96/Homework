dic = {'computer': 'may tinh', 'mouse': 'chuot', 'keyboard':'ban phim'}
while True:
    word = input('moi ban nhap tu can tra: ')
    if word in ['exit', 'quit']:
        print('cam on ban da su dung tu dien')
        break 
    if word in dic:
        print('nghia la', dic[word])
    else:
        print('tu nay k co trong tu dien')
        print('ban muon bo sung tu nay cho tu dien chu?')
        print(' A: Co')
        print(' B: Khong')
        a = input('cau tra loi cua ban: ')
        if a in ['Co', 'CO', 'co', 'a', 'A']:         
            meaning = input('moi ban nhap nghia cua tu nay: ')
            print('ban chac chu?')
            print(' A: Co')
            print(' B: Khong')
            b = input('cau tra loi cua ban: ')
            if b in ['Co', 'CO', 'co', 'a', 'A']:     
                dic[word] = meaning
                print('cam on dong gop cua ban')