"""產生活動後的回顧版首頁 index.html。

樣式沿用 invite.html（由 build_page.py 產生的活動前邀請版），
所以要先有 invite.html，再執行本程式：
    python build_page.py    # 產生 invite.html（邀請版存檔）
    python build_retro.py   # 產生 index.html（回顧版首頁）
照片放在 photos/ 資料夾，新增照片時在下方 GALLERY 清單加一行即可。
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE, "index.html")

# (檔名, 說明)
GALLERY = [
    ("00-zhongli-station.jpg", "09:27 抵達中壢車站"),
    ("01-campus-banner.jpg", "09:56 校園掛起校慶暨校友日旗幟"),
    ("02-checkin-backdrop.jpg", "10:05 商學院校友日背板前合影"),
    ("03-chair-time.jpg", "系主任時間"),
    ("04-memories.jpg", "教師與系友憶當年"),
    ("05-book.jpg", "老師的著作《50+個生命故事》（秦宗泰 著）"),
    ("06-classmates-1108.jpg", "11:08 老同學重逢"),
    ("07-lucky-draw.jpg", "11:16 歡樂摸彩，得獎系友上台領獎"),
    ("08-auditorium.jpg", "11:42 金榮講堂裡的系友們"),
    ("09-lunch.jpg", "13:13 餐敘時光"),
    ("10-campus-heart.jpg", "13:47 飯後回到校園"),
    ("11-classmates-bench.jpg", "13:55 老同學合影"),
    ("12-enci-hall.jpg", "13:59 恩慈樓前"),
    ("13-campus-building.jpg", "14:17 校園建築前合影"),
    ("14-field.jpg", "14:43 下午的操場"),
]

VIDEOS = [
    ("voSIVH401j8", "中原國貿系50周年", "YouTube 歌曲 MV分享"),
    ("cabBO0QSl_I", "83年級畢業歌曲 MV (一)", "YouTube 歌曲 MV分享"),
    ("jZIrnvmdjGY", "83年級畢業歌曲 MV (二)", "YouTube 歌曲 MV分享"),
    ("_Scxn-_XgBY", "83年級畢業感動回顧影片", "中原國貿五十周年紀念"),
    ("NH_M08-hs4Q", "47 號家族記憶", "五十年一刻 盼您回家"),
]

# (時間, 標題, 地點, 說明, 照片檔名或 None)
TIMELINE = [
    ("10:00 - 12:00", "系友報到", "金榮講堂", "系友陸續報到、填寫問卷、領取報到禮，在校友日背板前與久違的同窗重逢。", "02-checkin-backdrop.jpg"),
    ("10:30 - 10:40", "系學會開場表演", "金榮講堂", "國貿系系學會學弟妹帶來開場表演，揭開五十週年系慶序幕。", None),
    ("10:40 - 10:50", "系主任時間", "金榮講堂", "系主任向系友問候致詞，分享國貿系近年發展與未來願景。", "03-chair-time.jpg"),
    ("10:50 - 11:30", "教師與系友憶當年", "金榮講堂", "師長與系友同台，暢談當年課堂點滴與青春往事。", "04-memories.jpg"),
    ("11:30 - 11:40", "歡樂摸彩", "金榮講堂", "系慶摸彩，得獎系友上台領獎，現場笑聲不斷。", "07-lucky-draw.jpg"),
    ("11:40 - 12:00", "五十週年大合照", "金榮講堂", "全體師長與系友一同留下五十週年的紀念合照。", None),
    ("12:30 - 14:00", "感恩餐會", "綠光花園餐廳", "午宴敘舊，系友以認桌與餐券支持國貿系發展基金。", "09-lunch.jpg"),
]

EXTRA_CSS = """
        .hero-photo {
            position: absolute; inset: 0; z-index: -2;
            background: url('photos/01-campus-banner.jpg') center 35% / cover no-repeat;
            filter: brightness(0.45) saturate(0.9);
        }
        header { min-height: 72vh; }
        .hero-date {
            display: inline-block; margin-top: 0.5rem; padding: 0.6rem 1.6rem;
            border: 1px solid var(--glass-border); border-radius: 999px;
            background: rgba(7,17,30,0.55); color: var(--accent-gold-hover);
            letter-spacing: 0.15em; font-size: 1rem;
        }
        .tl-photo {
            display: block; width: 100%; margin-top: 1rem; border-radius: 10px;
            aspect-ratio: 4 / 3; object-fit: cover; cursor: zoom-in;
            border: 1px solid var(--glass-border);
        }
        .gallery-grid {
            display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
            gap: 1rem; max-width: 1100px; margin: 0 auto;
        }
        .gallery-item {
            margin: 0; background: var(--glass-bg); border: 1px solid var(--glass-border);
            border-radius: 12px; overflow: hidden; cursor: zoom-in;
            transition: var(--transition-smooth);
        }
        .gallery-item:hover { transform: translateY(-4px); border-color: var(--accent-gold); }
        .gallery-item img { display: block; width: 100%; aspect-ratio: 3 / 4; object-fit: cover; }
        .gallery-item figcaption { padding: 0.7rem 0.9rem; font-size: 0.9rem; color: var(--text-muted); }
        .lightbox-caption {
            position: absolute; bottom: 4%; left: 0; right: 0; text-align: center;
            color: var(--accent-gold-hover); font-size: 1rem; padding: 0 1rem;
        }
        @media (min-width: 769px) {
            .timeline-item.right::after { left: -8px; right: auto; }
        }
        .archive-link { color: var(--accent-gold); text-decoration: none; border-bottom: 1px dashed var(--accent-gold); }
        @media (max-width: 600px) {
            .gallery-grid { grid-template-columns: repeat(2, 1fr); gap: 0.6rem; }
            .gallery-item figcaption { font-size: 0.8rem; padding: 0.5rem 0.6rem; }
        }
"""


def head_from_invite():
    with open(os.path.join(BASE, "invite.html"), encoding="utf-8") as f:
        src = f.read()
    head = src[: src.index("</style>")]
    head = re.sub(r"<title>.*?</title>", "<title>五十年一刻 感謝您回家 | 中原國貿50周年慶活動回顧</title>", head, flags=re.S)
    return head + EXTRA_CSS + "    </style>\n</head>\n"


def timeline_html():
    out = []
    for i, (t, title, place, desc, photo) in enumerate(TIMELINE):
        side = "left" if i % 2 == 0 else "right"
        img = (f'<img class="tl-photo" src="photos/{photo}" alt="{title}" loading="lazy" '
               f'onclick="openPhoto(this.src, \'{title}\')">') if photo else ""
        out.append(f"""            <div class="timeline-item {side}">
                <div class="timeline-content">
                    <span class="time-badge">{t}</span>
                    <h3>{title}</h3>
                    <p>📍 {place}｜{desc}</p>
                    {img}
                </div>
            </div>""")
    return "\n".join(out)


def gallery_html():
    return "\n".join(
        f"""            <figure class="gallery-item" onclick="openPhoto('photos/{fn}', '{cap}')">
                <img src="photos/{fn}" alt="{cap}" loading="lazy">
                <figcaption>{cap}</figcaption>
            </figure>""" for fn, cap in GALLERY)


def videos_html():
    items = []
    for i, (vid, title, sub) in enumerate(VIDEOS):
        active = " active" if i == 0 else ""
        items.append(f"""                <div class="playlist-item{active}" onclick="playVideo('{vid}', this)">
                    <img src="https://img.youtube.com/vi/{vid}/mqdefault.jpg" alt="{title}">
                    <div class="playlist-info">
                        <h4>{title}</h4>
                        <p>{sub}</p>
                    </div>
                </div>""")
    return "\n".join(items)


BODY = """<body>

    <header>
        <div class="hero-photo"></div>
        <div class="hero-bg-overlay"></div>
        <div class="header-badge">CYCU IB 50th Anniversary</div>
        <h1><span style="white-space:nowrap">五十年一刻</span>　<span style="white-space:nowrap">感謝您回家</span></h1>
        <p class="sub-tagline">中原國貿創系五十週年系友回娘家活動已圓滿落幕。<br>謝謝每一位回到中原的師長、系友與學弟妹。</p>
        <div class="hero-date">2026.10.17（六）｜商學大樓 金榮講堂</div>
    </header>

    <section id="intro">
        <div class="intro-grid">
            <div>
                <div class="quote-box" style="margin-bottom: 2rem;">
                    <p class="quote-text">
                        「真的，有些回憶<span class="quote-text-highlight">只有跟當時那群人在一起</span>才找得回來。<br><br>
                        但，真的難以釋懷相聚後的再分離。矛盾的人生……<br><br>
                        Anyway，這段有你們的回憶，是千金萬銀也換不到的一段快樂歲月。有你們真好，永遠永遠祝福我所遇過的每一個你。」
                    </p>
                    <div class="author-info">— 系友心聲</div>
                </div>
                <div class="quote-box" style="border-left-color: #e53e3e;">
                    <p class="quote-text">
                        「長大之後，最怕的不是變老，而是突然聽懂了54歲寫的那首歌。<br><br>
                        那天聚會回到中原街角，看到熟悉的學長姐跟學弟妹，那一瞬間真的覺得歲月好像從來沒走遠。雖然我們現在的「血量只剩下 28%」，體力不如當年，聊的也是當年被哪科當掉的蠢事，但看著照片裡大家的笑容，才發現原來有些東西從來沒有變過。<br><br>
                        即使生活再累、世界再變，只要那群人還在，我們就永遠是當年那個敢衝、敢夢的自己。下次相聚之前，繼續加油吧，把剩下的電力用到最極致！」
                    </p>
                </div>
            </div>
            <div class="invite-card-wrap">
                <p style="color: var(--accent-gold); font-size: 0.9rem; margin-bottom: 0.8rem; letter-spacing: 0.1em;">▼ 活動邀請卡（紀念）</p>
                <img src="photos/invite-card.jpg" alt="中原國貿50周年校友日邀請卡" class="invite-card-img" onclick="openPhoto(this.src, '活動邀請卡')">
                <p style="color: var(--text-muted); font-size: 0.85rem; margin-top: 0.8rem;">想看活動前的邀請網頁？<a class="archive-link" href="invite.html">點這裡</a></p>
            </div>
        </div>
    </section>

    <section id="gallery">
        <div class="section-title-wrap">
            <h2 class="section-title">活動相簿</h2>
            <p style="color: var(--text-muted); margin-top: 0.5rem; font-weight: 300;">點擊照片可放大</p>
        </div>
        <div class="gallery-grid">
__GALLERY__
        </div>
    </section>

    <section id="schedule">
        <div class="section-title-wrap">
            <h2 class="section-title">活動回顧</h2>
        </div>
        <div class="timeline">
__TIMELINE__
        </div>
    </section>

    <section id="video" style="padding-top: 1rem; padding-bottom: 3rem;">
        <div class="section-title-wrap">
            <h2 class="section-title">83年級畢業回憶影音專區</h2>
            <p style="color: var(--text-muted); margin-top: 0.5rem; font-weight: 300;">回首半世紀璀璨，聽聽歌，看看我們一同寫下的故事</p>
        </div>
        <div class="video-gallery">
            <div class="main-video">
                <div class="video-container">
                    <iframe id="galleryPlayer" src="https://www.youtube-nocookie.com/embed/voSIVH401j8" title="YouTube video player" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            </div>
            <div class="video-playlist">
__VIDEOS__
            </div>
        </div>
    </section>

    <section id="register">
        <div class="travel-card" style="text-align: center;">
            <h2 style="font-size: 2rem; color: #FFF; margin-bottom: 1rem;">謝謝您，回家</h2>
            <p style="color: var(--text-muted); max-width: 640px; margin: 0 auto 2rem auto;">
                感謝籌備小組、全體師長、系學會學弟妹，以及每一位認桌與參加餐會、支持國貿系發展基金的系友。<br>
                想更新聯絡資料或與系上保持聯繫，歡迎與系辦聯絡。
            </p>
            <div style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 2.5rem; flex-wrap: wrap;">
                <a href="https://ib.cycu.edu.tw/" target="_blank" class="cta-btn">瀏覽中原國貿系官方網站</a>
                <a href="invite.html" class="cta-btn secondary-btn">回顧活動邀請頁</a>
            </div>
            <div class="contact-box-grid">
                <div class="contact-card">
                    <div class="contact-name">賴心怡 助教</div>
                    <div class="contact-title">系友聯絡窗口</div>
                    <a href="tel:032655204" class="contact-phone">(03) 265-5204</a>
                </div>
                <div class="contact-card">
                    <div class="contact-name">陳宣輔 助教</div>
                    <div class="contact-title">系辦聯絡窗口</div>
                    <a href="tel:032655203" class="contact-phone">(03) 265-5203</a>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="footer-logo"><a href="https://ib.cycu.edu.tw/" target="_blank" style="color: var(--accent-gold); text-decoration: none;">中原大學國際經營與貿易學系</a></div>
        <p class="footer-text">© 2026 CYCU Department of International Business. All Rights Reserved.</p>
        <p class="footer-text" style="margin-top: 0.5rem; font-size: 0.8rem; color: #4A5568;">中原國貿創系五十週年籌備小組 敬謝｜下次相聚，我們再見</p>
    </footer>

    <div id="lightboxModal" class="lightbox" onclick="closeLightbox()">
        <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
        <img class="lightbox-img" id="lightboxImg" src="" alt="照片放大預覽">
        <div class="lightbox-caption" id="lightboxCaption"></div>
    </div>

    <script>
        function playVideo(videoId, element) {
            document.getElementById("galleryPlayer").src = "https://www.youtube-nocookie.com/embed/" + videoId + "?autoplay=1";
            document.querySelectorAll('.playlist-item').forEach(item => item.classList.remove('active'));
            element.classList.add('active');
        }
        function openPhoto(src, caption) {
            document.getElementById("lightboxImg").src = src;
            document.getElementById("lightboxCaption").textContent = caption || "";
            document.getElementById("lightboxModal").classList.add("active");
            document.body.style.overflow = "hidden";
        }
        function closeLightbox() {
            document.getElementById("lightboxModal").classList.remove("active");
            document.body.style.overflow = "auto";
        }
        document.addEventListener('keydown', e => { if (e.key === "Escape") closeLightbox(); });
    </script>
</body>
</html>
"""


def build():
    html = (head_from_invite()
            + BODY.replace("__GALLERY__", gallery_html())
                  .replace("__TIMELINE__", timeline_html())
                  .replace("__VIDEOS__", videos_html()))
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"已產生回顧版：{OUTPUT}")


if __name__ == "__main__":
    build()
