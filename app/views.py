from flask import render_template, redirect, url_for, request

from app import app


captions = [
    "First Trip Together",
    "Uống thốt nốt lần 1, nghĩ giữa trưa nè",
    "Đi rừng tràm một mình nè TT, hên gặp được mấy người sau lưng cũng đi du lịch",
    "Chèo đưa em iu ra biển xa nè hehe, nhưng phụ họa là chính",
    "Đợi thuyền về tranh thủ làm tấm hình chụp chung hehe",
    "Xung quanh toàn là lúa haha, phải dừng lại để chụp hình",
    "Ngày thứ 2 đi cáp treo lên Núi Cấm nè, nắng sấm mắt hahahahaha",
    "Ngồi cáp treo lâu quá phải làm một tấm hình lưu lại kỉ niệm",
    "Đi tản bộ một mình nè hic",
    "Bánh xèo miền tây ăn với rau rừng nhưng mà nhà trồng hô hố, ăn thêm 2 cái bánh dứa gì đấy nửa",
    "Đi bộ lên cao xem nhà ta phóng sinh cá nè",
    "Đi bộ chảy mấy kg mở, thì bị dụ ăn kem hoho",
    "Về sài gòn tranh thủ làm một ly thốt nốt nửa cho đỡ thèm hahaa",
    "Ghé Long Xuyên làm tô bún cá cho biết đặc sản như thế nào, haha mà có đứa nhọ ăn trúng tô có con ruồi làm mất ấn tượng với quán nổi tiếng nhất Long Xuyên lun",
    "Bóng Long Xuyên 'Phước An' phải kêu ăn cơm Tấm LX mới gọi là đi Long Xuyên haha, trong khi đó ăn tô bún bồ với cái gì đó quên mất rồi, bánh bèo thì phải",
    "Returning Sai Gon, kết thúc chuyến đi đầu tiên mất rồi, chắc đây là chuyển đi xa nhất cùng nhau còn gì buồn ghê. Mau mau hết dịch để di chuyển nửa không già mất hic.",
    "Dẫn qua quận 1 ăn Lunch Lady nekkk, hôm này được ăn bún Thái hahaha",
    "Ăn xong rồi thì ghé Black Bottle Vạn Kiếp uống nước Dưa hấu ép hahaha, học toàn bị chụp lén hic",
    "Tối lại ghé ăn cho biên Bánh Ướt Buôn Mê, tội con người ở DakLak mà không biên món này, phải lên sài gòn ăn mới biết hehehe xD",
    "Lần đầu đi chơi valentine của người eo sau 25 nồi bánh trưng hahahaha. Lết qua quận 4 ăn quán quen mới chịu cơ",
    "Vô Miniso mua quà cho nè",
    "Gương mặt lúc chưa niềng răng hahahaha",
    "Quà valentine nè, We are bear, lần cuối cùng thấy tụi nó hohohohohoho không biết lúc giận dỗi có vứt đi rồi không nửa",
    "Này qua nhà người ta chơi nè hahaa",
    "Mua hồ lô nướng ăn nè, sau những ngày canh me đi sớm đi trễ mới mưa được hahaa, đậu xe ở công viên ăn nè, ăn trước cánh bảng tuyên truyền chống nghiện mai thúy hahaha",
    "Đi dạo dạo kiếm gì ăn cũng hết giờ",
    "Cuối cùng ghé đại quán ở khu Nguyễn Tri Phương",
    "Chả nhớ bánh này như thế nào nửa hahahaha",
    "Nơi mơ ước của em yêu về già, có cái cầu như này nè",
    "Này hình mới lên lại Sài Gòn, đi bệnh viên bắn mụn ruồi rồi không bắn nửa hahaha, xong uống rau má ở đường Mặc Đỉnh Chi nè, phải đợi Phúc không ra hay sao lết qua tới đây luôn",
    "Haha, bữa cơm đầu tiên người yêu tuổi bỏ công sức ra nấu nè, 1 chén cơm và thức ăn cho 10 chén cơm, hic phải rán ăn cho hết sợ phí không hà, mà ngon hehehe nấu nhiều qua mới nói xong không bao giờ nấu cho ăn nửa huhu huhu",
    "Phần cơm cho mình tui ăn đó mọi người ơi, đừng hỏi sao tăng cân nhaaa",
    "Đi vòng vòng kiếm quán học, cuối cùng vô quán board game ở hẻm Thành Thái nèee",
    "Đang học cũng bị bắt chụp hình TT",
    "Dẫn đi ăn kem nè, cái nào mà Black với than tre đừng ăn nha mn, ăn mấy kem đó đem hết răng đó hahahaha",
    "Đi dạo dạo xong ra nhà thờ",
    "Không biết biết tới hiphop chưa mà đòi làm theo hahahaha",
    "Làm bán nhưng mà mình được ăn ké hehehehe",
    "Này đi camping trong ngày nè, lần đầu với phúc cơ quay vlog mà hình như đi với Phúc cơ, trưa nóng thế mẹ luôn k ngủ nghỉ được đã phải về",
    "Mưa ra chụp hình mấy tấm ahahah",
    "Chụp xong ra đợi mưa tạnh để về hahahaha",
    "Đi miền Tây với Quán Cơm 2000 nè, không biết sao mình lại là người chụp hình, nên không có mất mình đâu huhu. Nổi khổ của Photographer là phải hy sinh đó",
    "Lại phải dẫn đi ăn kem cho mau lớn hahaa",
    "Ra học hay ra làm gì thế",
    "Rồi cũng bị nắm đầu chụp hình hahaa",
    "Đi kiếm bánh tráng nướng mắm ruốt nhưng quán covid dẹp luôn, phải đi ăn cái khác nè",
    "Ăn phở ở Nguyễn Đình Chiểu Q3 nè, đi vòng vòng quài ăn đại luôn, nhìn ăn tô phở mất 20 phút để gắp hành ra hohoho",
    "Ra tini để chill hahaha",
    "Qua quận 7 để ăn lẫu bỏ nè, kiếm chỗ gửi xe mà ỉa lun, quán gì mà đông dã man, hên là ăn ngon mà có đứa mới niềng răng nên chỉ ăn mấy củ khoai đồ thui, thiệt là tội nghiệp, hy sinh vì đẹp",
    "Wearebear hahaa",
    "Năn nỉ lắm mới nấu đồ ăn sáng cho ăn nè huhuh, Thích người iu nấu cho ăn mà quên 2 năm nấu 2 lần ăn hic",
    "Lại một mùa trung thu bên nhau, được ngủ nằm bên cạnh nhau nè hahaha",
    "Sinh nhật tui nè hihi, cảm ơn e iu đã tài trợ nha, mời mấy đứa giờ dây thun nên phải nhờ Tuấn Trình chụp mấy trăm tấm hình",
    "Ăn bắp trước chung cư cũ Phúc cơ nè, hơi bị ngon mà chưa được ăn lại hiu hiu",
    "Đố biết ăn gì đây luôn hahaha, đi ăn mì quảng ngày răng và cái kết TT",
    "Lại đi ăn bánh tráng nướng, thịt cá không ăn được toàn ăn vặt với uống trà sửa qua ngày, siêu thiệt hehehehe",
    "Đi ăn quán OSAKA nè, lần đầu đi ăn và kêu món dở hơn mình hahaha, xong mình phải ăn 1.5 phần",
    "Đi nhà thờ nè, này là không còn cái đồ gì mặt nên mới mặt vậy nhé, mát lắm hehehe",
    "Đi ăn kem tươi nè, mình bã ăn chục câyyy",
    "Gương mặt đợi miến, và mình phải ăn phần gỏi 2 người hohooo",
    "Ngoài bún mì miến phở ra thì còn ăn được món gì nửa không ta",
    "Đi coi phim nè hehe, nhìn mình bụng bự thiệt chứ",
    "Ăn kem MiniStop ở hẻm 606 nè, ăn xong xin vô mua cây nửa",
    "Ăn OSAKA nửa nè, h kêu món gì cũng bắt chước kêu theo",
    "Sinh nhất đợi cả tiếng mới đông đủ kêu nhân viên làm tấm hình nè hehee",
    "Đi học chung với nhauu",
    "Đang đợi coi bắn pháo hoa Tết tây nè hoho, đi về là kẹt xe thế bà lun",
    "Chở xuống Vũng Tàu ăn đám cưới nè",
    "Ăn bánh canh cá lóc xong ra Kai Công Hòa học thuiii",
    "Lại bị chụp lén nửa hoho",
    "Được dẫn đi ăn gà Hanuri trước khi về quê nè, lần đầu được ăn gà ở Hanuri lunnn",
    "Ăn tết xong lên Sài gòn dẫn đi ăn phở gà nè",
    "Đi ăn lẫu bò với Tuấn trình hahahaa, toàn xin mì thêm, ăn sau mới biết thêm thịt cũng rẻ",
    "Trưa đặt đồ ăn về ăn nè, dịch dã ăn uống toàn phải đặt thôi",
    "Thủ tục trước khi ăn hehe",
    "Order Haruni ra Kai Nguyễn Oanh anh luôn hehe",
    "Đang hóng hớt cũng bị chụp nửa",
    "Chụp cái gì có mỗi con mắt vậy trời",
    "Chụp hình lúc người ta đang say mê học hoho",
    "Ăn KFC với Phúc cơ, đợi nó đi làm về mệt nghỉ",
    "Gương mặt đói chờ tô mì quảng",
    "Đi dạo ra nhà thờ nè đâu mọc thêm 4 cái sừng",
    "Qua quận 7 ăn bò lá lốt thuii à",
    "Ăn bánh ở hẻm Nguyễn Thị Nhỏ, đang bị gắp đồ ăn qua ăn cho mập huhu",
    "Lại đi ăn OSAKA lâu rồi chưa ăn huuh",
    "Last picture rồi, này học ở Kai Coffee, sau này dịch cũng ít gặp được nhauuu cũng không còn tấm hình nào chụp thêm hết trơnnn, mong dinh qua mauu"  
]
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/blogs')
def blog():
    return render_template("blogs.html")


@app.route('/blogs/ani2', methods=['GET', 'POST'])
def blogs_ani2():
    return render_template("blogs_ani2.html", captions=captions)