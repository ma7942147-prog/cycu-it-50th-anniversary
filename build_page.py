import base64
import os

def build_alumni_page():
    img_path = r"C:\Users\ma794\Downloads\20261017_中原大學系學會校友日\校友日邀請卡.jpg"
    output_html_path = r"C:\Users\ma794\Downloads\20261017_中原大學系學會校友日\index.html"
    
    # Encode image to base64
    base64_img = ""
    if os.path.exists(img_path):
        with open(img_path, "rb") as img_file:
            base64_img = base64.b64encode(img_file.read()).decode('utf-8')
        print("Successfully encoded JPG to Base64.")
    else:
        print(f"Warning: JPG not found at {img_path}")

    # HTML content template
    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>五十年一刻 盼您回家 | 中原國貿50周年慶暨校友日</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Noto+Sans+TC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --primary-bg: #07111E;
            --secondary-bg: #0C1E36;
            --accent-gold: #D4AF37;
            --accent-gold-hover: #F3E5AB;
            --text-light: #F5F7FA;
            --text-muted: #A0AEC0;
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(212, 175, 55, 0.15);
            --card-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
            --transition-smooth: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: 'Noto Sans TC', sans-serif;
            background-color: var(--primary-bg);
            color: var(--text-light);
            line-height: 1.6;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(21, 37, 61, 0.6) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(31, 58, 93, 0.6) 0%, transparent 40%);
            background-attachment: fixed;
        }}

        /* Header / Hero Section */
        header {{
            position: relative;
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 2rem;
            z-index: 2;
            overflow: hidden;
        }}

        .hero-bg-overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(180deg, rgba(7, 17, 30, 0.4) 0%, var(--primary-bg) 100%);
            z-index: -1;
        }}

        .header-badge {{
            font-family: 'Cinzel', serif;
            color: var(--accent-gold);
            font-size: 1.1rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
            font-weight: 700;
            text-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
            animation: fadeInDown 1s ease-out;
        }}

        h1 {{
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 1.5rem;
            letter-spacing: 0.05em;
            background: linear-gradient(135deg, #FFF 30%, var(--accent-gold) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 5px 15px rgba(0,0,0,0.3);
            animation: fadeInUp 1.2s cubic-bezier(0.165, 0.84, 0.44, 1);
        }}

        .sub-tagline {{
            font-size: 1.3rem;
            color: var(--text-muted);
            max-width: 800px;
            margin: 0 auto 2.5rem auto;
            font-weight: 300;
            animation: fadeInUp 1.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        }}

        /* Countdown Container */
        .countdown-container {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 1.5rem 3rem;
            display: flex;
            gap: 2rem;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            box-shadow: var(--card-shadow);
            margin-bottom: 1.5rem;
            animation: scaleIn 1.5s cubic-bezier(0.165, 0.84, 0.44, 1);
        }}

        .countdown-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 80px;
        }}

        .countdown-value {{
            font-family: 'Cinzel', serif;
            font-size: 3rem;
            font-weight: 700;
            color: var(--accent-gold);
            text-shadow: 0 0 8px rgba(212, 175, 55, 0.4);
            line-height: 1;
        }}

        .countdown-label {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 0.5rem;
            letter-spacing: 0.1em;
        }}

        .cta-btn {{
            position: relative;
            display: inline-block;
            background: linear-gradient(135deg, var(--accent-gold) 0%, #B8860B 100%);
            color: #07111E;
            text-decoration: none;
            padding: 1.1rem 3rem;
            font-size: 1.2rem;
            font-weight: 700;
            border-radius: 50px;
            letter-spacing: 0.1em;
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.3);
            transition: var(--transition-smooth);
            overflow: hidden;
            border: none;
            cursor: pointer;
            z-index: 1;
        }}

        .cta-btn::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            transition: 0.5s;
            z-index: -1;
        }}

        .cta-btn:hover::before {{
            left: 100%;
        }}

        .cta-btn:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(212, 175, 55, 0.5);
            background: linear-gradient(135deg, var(--accent-gold-hover) 0%, var(--accent-gold) 100%);
        }}

        /* Section Styling */
        section {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 5rem 2rem;
        }}

        .section-title-wrap {{
            text-align: center;
            margin-bottom: 3.5rem;
        }}

        .section-title {{
            font-size: 2.2rem;
            font-weight: 800;
            display: inline-block;
            position: relative;
            padding-bottom: 1rem;
            background: linear-gradient(to right, #FFF, var(--accent-gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .section-title::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 3px;
            background-color: var(--accent-gold);
            border-radius: 2px;
        }}

        /* Intro Section - Quotes */
        .intro-grid {{
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 3rem;
            align-items: center;
        }}

        @media (max-width: 768px) {{
            .intro-grid {{
                grid-template-columns: 1fr;
                gap: 2.5rem;
            }}
        }}

        .quote-box {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-left: 5px solid var(--accent-gold);
            border-radius: 0 16px 16px 0;
            padding: 2.5rem;
            box-shadow: var(--card-shadow);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            position: relative;
        }}

        .quote-text {{
            font-size: 1.15rem;
            line-height: 1.8;
            font-weight: 300;
            margin-bottom: 1.5rem;
            position: relative;
            color: #E2E8F0;
        }}

        .quote-text-highlight {{
            color: var(--accent-gold);
            font-weight: 500;
        }}

        .author-info {{
            font-size: 0.95rem;
            color: var(--text-muted);
            text-align: right;
            font-style: italic;
        }}

        /* Invitation Card Styling */
        .invite-card-wrap {{
            text-align: center;
            perspective: 1000px;
        }}

        .invite-card-img {{
            width: 100%;
            max-width: 400px;
            border-radius: 12px;
            border: 1px solid var(--glass-border);
            box-shadow: var(--card-shadow);
            transition: var(--transition-smooth);
            cursor: zoom-in;
        }}

        .invite-card-img:hover {{
            transform: scale(1.03) rotateY(5deg);
            box-shadow: 0 20px 40px rgba(212, 175, 55, 0.25);
        }}

        /* Lightbox for Invitation Card */
        .lightbox {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(7, 17, 30, 0.95);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            opacity: 0;
            transition: opacity 0.3s ease;
            padding: 20px;
        }}

        .lightbox.active {{
            display: flex;
            opacity: 1;
        }}

        .lightbox-img {{
            max-width: 90%;
            max-height: 90vh;
            border-radius: 8px;
            box-shadow: 0 0 30px rgba(0,0,0,0.8);
            transform: scale(0.9);
            transition: transform 0.3s ease;
        }}

        .lightbox.active .lightbox-img {{
            transform: scale(1);
        }}

        .lightbox-close {{
            position: absolute;
            top: 25px;
            right: 35px;
            color: #fff;
            font-size: 2.5rem;
            font-weight: 300;
            cursor: pointer;
            transition: var(--transition-smooth);
        }}

        .lightbox-close:hover {{
            color: var(--accent-gold);
            transform: rotate(90deg);
        }}

        /* Video Gallery Section */
        .video-gallery {{
            display: grid;
            grid-template-columns: 1.3fr 0.7fr;
            gap: 2rem;
            align-items: stretch;
        }}

        @media (max-width: 900px) {{
            .video-gallery {{
                grid-template-columns: 1fr;
            }}
        }}

        .video-container {{
            position: relative;
            padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
            height: 0;
            overflow: hidden;
            border-radius: 16px;
            box-shadow: var(--card-shadow);
            border: 1px solid var(--glass-border);
            background-color: #000;
        }}

        .video-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }}

        .video-playlist {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
            max-height: 480px;
            overflow-y: auto;
            padding-right: 5px;
        }}

        /* Custom scrollbar for playlist */
        .video-playlist::-webkit-scrollbar {{
            width: 6px;
        }}
        .video-playlist::-webkit-scrollbar-track {{
            background: rgba(255, 255, 255, 0.01);
            border-radius: 10px;
        }}
        .video-playlist::-webkit-scrollbar-thumb {{
            background: rgba(212, 175, 55, 0.2);
            border-radius: 10px;
        }}
        .video-playlist::-webkit-scrollbar-thumb:hover {{
            background: rgba(212, 175, 55, 0.4);
        }}

        .playlist-item {{
            display: flex;
            gap: 1rem;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 0.8rem;
            cursor: pointer;
            transition: var(--transition-smooth);
            align-items: center;
        }}

        .playlist-item:hover {{
            background: rgba(212, 175, 55, 0.05);
            border-color: rgba(212, 175, 55, 0.2);
            transform: translateX(3px);
        }}

        .playlist-item.active {{
            background: rgba(212, 175, 55, 0.1);
            border-color: var(--accent-gold);
            box-shadow: 0 0 10px rgba(212, 175, 55, 0.15);
        }}

        .playlist-item img {{
            width: 100px;
            height: 60px;
            object-fit: cover;
            border-radius: 6px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            flex-shrink: 0;
        }}

        .playlist-info {{
            flex-grow: 1;
        }}

        .playlist-info h4 {{
            font-size: 0.95rem;
            color: #FFF;
            margin-bottom: 0.2rem;
            font-weight: 500;
        }}

        .playlist-info p {{
            font-size: 0.8rem;
            color: var(--text-muted);
        }}

        /* Timeline Section */
        .timeline {{
            position: relative;
            max-width: 800px;
            margin: 0 auto;
            padding: 1rem 0;
        }}

        .timeline::after {{
            content: '';
            position: absolute;
            width: 2px;
            background: linear-gradient(180deg, var(--accent-gold) 0%, var(--secondary-bg) 100%);
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -1px;
        }}

        @media (max-width: 768px) {{
            .timeline::after {{
                left: 31px;
            }}
        }}

        .timeline-item {{
            padding: 10px 40px;
            position: relative;
            background-color: inherit;
            width: 50%;
        }}

        @media (max-width: 768px) {{
            .timeline-item {{
                width: 100%;
                padding-left: 70px;
                padding-right: 25px;
            }}
        }}

        .timeline-item::after {{
            content: '';
            position: absolute;
            width: 16px;
            height: 16px;
            right: -8px;
            background-color: var(--primary-bg);
            border: 3px solid var(--accent-gold);
            top: 15px;
            border-radius: 50%;
            z-index: 1;
            box-shadow: 0 0 8px var(--accent-gold);
            transition: var(--transition-smooth);
        }}

        .timeline-item:hover::after {{
            background-color: var(--accent-gold);
            transform: scale(1.3);
        }}

        @media (max-width: 768px) {{
            .timeline-item::after {{
                left: 23px;
                right: auto;
                top: 20px;
            }}
        }}

        .left {{
            left: 0;
            text-align: right;
        }}

        .right {{
            left: 50%;
        }}

        @media (max-width: 768px) {{
            .right {{
                left: 0%;
            }}
            .left {{
                text-align: left;
            }}
        }}

        .timeline-content {{
            padding: 1.5rem 2rem;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            position: relative;
            border-radius: 12px;
            box-shadow: var(--card-shadow);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            transition: var(--transition-smooth);
        }}

        .timeline-content:hover {{
            transform: translateY(-3px);
            border-color: rgba(212, 175, 55, 0.4);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.1);
        }}

        .time-badge {{
            display: inline-block;
            padding: 0.3rem 0.8rem;
            background: rgba(212, 175, 55, 0.15);
            color: var(--accent-gold);
            border-radius: 30px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}

        .timeline-content h3 {{
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
            color: #FFF;
        }}

        .timeline-content p {{
            font-size: 0.95rem;
            color: var(--text-muted);
        }}

        /* Travel Planner (Tabs) */
        .tab-buttons {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2.5rem;
        }}

        .tab-btn {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            color: var(--text-light);
            padding: 0.8rem 2rem;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 30px;
            cursor: pointer;
            transition: var(--transition-smooth);
        }}

        .tab-btn:hover {{
            border-color: var(--accent-gold);
            color: var(--accent-gold);
        }}

        .tab-btn.active {{
            background: linear-gradient(135deg, var(--accent-gold) 0%, #B8860B 100%);
            color: #07111E;
            border-color: var(--accent-gold);
            box-shadow: 0 5px 15px rgba(212, 175, 55, 0.2);
        }}

        .tab-content {{
            display: none;
            animation: fadeIn 0.5s ease-in-out;
        }}

        .tab-content.active {{
            display: block;
        }}

        .travel-card {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: var(--card-shadow);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }}

        .itinerary-step {{
            display: flex;
            gap: 1.5rem;
            margin-bottom: 2rem;
            position: relative;
        }}

        .itinerary-step:last-child {{
            margin-bottom: 0;
        }}

        .itinerary-step:not(:last-child)::after {{
            content: '';
            position: absolute;
            left: 20px;
            top: 45px;
            bottom: -25px;
            width: 1px;
            border-left: 1px dashed rgba(212, 175, 55, 0.3);
        }}

        .step-num {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 42px;
            height: 42px;
            background: rgba(212, 175, 55, 0.1);
            border: 1px solid var(--accent-gold);
            color: var(--accent-gold);
            border-radius: 50%;
            font-weight: 700;
            font-family: 'Cinzel', serif;
            flex-shrink: 0;
        }}

        .step-detail h4 {{
            font-size: 1.15rem;
            color: #FFF;
            margin-bottom: 0.4rem;
            font-weight: 500;
        }}

        .step-detail p {{
            font-size: 0.95rem;
            color: var(--text-muted);
        }}

        .highlight-text {{
            color: var(--accent-gold);
            font-weight: 500;
        }}

        /* Info & Pricing Cards */
        .info-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }}

        @media (max-width: 768px) {{
            .info-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        .info-card {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 2.2rem;
            box-shadow: var(--card-shadow);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            transition: var(--transition-smooth);
        }}

        .info-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(212, 175, 55, 0.35);
        }}

        .card-icon-wrap {{
            width: 50px;
            height: 50px;
            background: rgba(212, 175, 55, 0.1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
            color: var(--accent-gold);
        }}

        .info-card h3 {{
            font-size: 1.3rem;
            color: #FFF;
            margin-bottom: 1rem;
        }}

        .info-list {{
            list-style: none;
        }}

        .info-list li {{
            font-size: 0.95rem;
            color: var(--text-muted);
            margin-bottom: 0.8rem;
            display: flex;
            align-items: flex-start;
            gap: 0.5rem;
        }}

        .info-list li::before {{
            content: '✦';
            color: var(--accent-gold);
        }}

        /* Contact Details Card */
        .contact-box-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }}

        .contact-card {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: var(--transition-smooth);
        }}

        .contact-card:hover {{
            background: rgba(212, 175, 55, 0.03);
            border-color: var(--glass-border);
            transform: translateY(-3px);
        }}

        .contact-name {{
            font-size: 1.1rem;
            font-weight: 700;
            color: #FFF;
            margin-bottom: 0.3rem;
        }}

        .contact-title {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 0.8rem;
        }}

        .contact-phone {{
            display: inline-block;
            color: var(--accent-gold);
            text-decoration: none;
            font-weight: 700;
            font-size: 1rem;
            transition: var(--transition-smooth);
            padding: 0.3rem 0.8rem;
            background: rgba(212, 175, 55, 0.08);
            border-radius: 20px;
        }}

        .contact-phone:hover {{
            background: var(--accent-gold);
            color: #07111E;
            transform: scale(1.05);
        }}

        /* Footer */
        footer {{
            background-color: #040A12;
            padding: 3.5rem 2rem;
            text-align: center;
            border-top: 1px solid rgba(212, 175, 55, 0.1);
        }}

        .footer-logo {{
            font-family: 'Cinzel', serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent-gold);
            margin-bottom: 1rem;
            letter-spacing: 0.1em;
        }}

        .footer-text {{
            font-size: 0.9rem;
            color: var(--text-muted);
        }}

        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes fadeInDown {{
            from {{
                opacity: 0;
                transform: translateY(-20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes scaleIn {{
            from {{
                opacity: 0;
                transform: scale(0.95);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}

        /* Responsive adjustments */
        @media (max-width: 600px) {{
            h1 {{
                font-size: 2.2rem;
            }}
            .sub-tagline {{
                font-size: 1rem;
            }}
            .countdown-container {{
                padding: 1rem 1.5rem;
                gap: 1rem;
            }}
            .countdown-value {{
                font-size: 2rem;
            }}
            .countdown-item {{
                min-width: 60px;
            }}
        }}
    </style>
</head>
<body>

    <!-- Header / Hero -->
    <header>
        <div class="hero-bg-overlay"></div>
        <div class="header-badge">CYCU IT 50th Anniversary</div>
        <h1>五十年一刻 盼您回家</h1>
        <p class="sub-tagline">適逢中原大學校慶暨國貿系創系五十週年，誠摯邀請您重返校園，與久違的師長、同窗及系友溫馨相聚。</p>
        
        <!-- Countdown -->
        <div class="countdown-container">
            <div class="countdown-item">
                <span class="countdown-value" id="days">00</span>
                <span class="countdown-label">DAYS</span>
            </div>
            <div class="countdown-item">
                <span class="countdown-value" id="hours">00</span>
                <span class="countdown-label">HOURS</span>
            </div>
            <div class="countdown-item">
                <span class="countdown-value" id="minutes">00</span>
                <span class="countdown-label">MINUTES</span>
            </div>
            <div class="countdown-item">
                <span class="countdown-value" id="seconds">00</span>
                <span class="countdown-label">SECONDS</span>
            </div>
        </div>
    </header>

    <!-- Intro & Quote Section -->
    <section id="intro">
        <div class="intro-grid">
            <div>
                <div class="quote-box" style="margin-bottom: 2rem;">
                    <p class="quote-text">
                        「離開校園 10 年、20 年，你還記得當年<span class="quote-text-highlight">商學大樓前的風</span>，還有那群陪你熬夜 K 書、翹課吃宵夜的人嗎？<br><br>
                        時光走得比想像中還快，轉眼間，中原國貿竟然要迎來 50 周年了！不管是剛畢業的新鮮人，還是畢業滿 19、20 年的學長姐，我們都在各自的人生軌道上記錄著屬於自己的青春。<br><br>
                        10 月 17 日（六），給自己放個假，回中原走走吧。不必帶什麼成就回校，只要帶著當年的笑容，一起回金榮講堂敘舊、抽大獎、吃個感恩餐會。有些回憶，只有跟當年那群人在一起，才找得回來。」
                    </p>
                    <div class="author-info">— 中原國貿系全體師生</div>
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
                <p style="color: var(--accent-gold); font-size: 0.9rem; margin-bottom: 0.8rem; letter-spacing: 0.1em;">▼ 點擊可放大檢視邀請卡</p>
                <img src="data:image/jpeg;base64,{base64_img}" alt="中原國貿50周年校友日邀請卡" class="invite-card-img" onclick="openLightbox()">
            </div>
        </div>
    </section>

    <!-- Video Section -->
    <section id="video" style="padding-top: 1rem; padding-bottom: 3rem;">
        <div class="section-title-wrap">
            <h2 class="section-title">50周年回憶影音專區</h2>
            <p style="color: var(--text-muted); margin-top: 0.5rem; font-weight: 300;">回首半世紀의璀璨，聽聽歌，看看我們一同寫下的故事</p>
        </div>
        
        <div class="video-gallery">
            <div class="main-video">
                <div class="video-container">
                    <iframe id="galleryPlayer" src="https://www.youtube-nocookie.com/embed/cabBO0QSl_I" title="YouTube video player" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            </div>
            
            <div class="video-playlist">
                <div class="playlist-item active" onclick="playVideo('cabBO0QSl_I', this)">
                    <img src="https://img.youtube.com/vi/cabBO0QSl_I/mqdefault.jpg" alt="50周年歌曲 MV (一)">
                    <div class="playlist-info">
                        <h4>50周年歌曲 MV (一)</h4>
                        <p>YouTube 歌曲 MV分享</p>
                    </div>
                </div>
                <div class="playlist-item" onclick="playVideo('jZIrnvmdjGY', this)">
                    <img src="https://img.youtube.com/vi/jZIrnvmdjGY/mqdefault.jpg" alt="50周年歌曲 MV (二)">
                    <div class="playlist-info">
                        <h4>50周年歌曲 MV (二)</h4>
                        <p>YouTube 歌曲 MV分享</p>
                    </div>
                </div>
                <div class="playlist-item" onclick="playVideo('_Scxn-_XgBY', this)">
                    <img src="https://img.youtube.com/vi/_Scxn-_XgBY/mqdefault.jpg" alt="50周年感動回顧影片">
                    <div class="playlist-info">
                        <h4>50周年感動回顧影片</h4>
                        <p>中原國貿五十周年紀念</p>
                    </div>
                </div>
                <div class="playlist-item" onclick="playVideo('NH_M08-hs4Q', this)">
                    <img src="https://img.youtube.com/vi/NH_M08-hs4Q/mqdefault.jpg" alt="47 號家族記憶">
                    <div class="playlist-info">
                        <h4>47 號家族記憶</h4>
                        <p>五十年一刻 盼您回家</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Timeline / Schedule Section -->
    <section id="schedule">
        <div class="section-title-wrap">
            <h2 class="section-title">活動行程規劃</h2>
        </div>
        
        <div class="timeline">
            <div class="timeline-item left">
                <div class="timeline-content">
                    <span class="time-badge">09:30 - 10:00</span>
                    <h3>溫馨報到與相聚</h3>
                    <p>商學大樓金榮講堂前。設有回憶時光簽名牆、懷舊特展，邀請您留下久違的合影。</p>
                </div>
            </div>
            
            <div class="timeline-item right">
                <div class="timeline-content">
                    <span class="time-badge">10:00 - 11:30</span>
                    <h3>創系五十週年大會</h3>
                    <p>重返金榮講堂！師長溫馨問候、傑出系友頒獎典禮、歷史時光沙龍，更有系慶驚喜大抽獎！</p>
                </div>
            </div>
            
            <div class="timeline-item left">
                <div class="timeline-content">
                    <span class="time-badge">11:30 - 12:00</span>
                    <h3>校園巡禮與大合照</h3>
                    <p>漫步至「商學大樓前吹吹風」、恩慈小徑、情人步道，與好久不見的同窗留下經典打卡合照。</p>
                </div>
            </div>
            
            <div class="timeline-item right">
                <div class="timeline-content">
                    <span class="time-badge">12:30 - 14:30</span>
                    <h3>五十周年慶暨感恩餐會</h3>
                    <p>於「綠光花園餐廳」舉辦溫馨午宴。藉由認桌支持或餐券參與，共敘深厚情誼，支持國貿系發展基金。</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Travel Planner Section -->
    <section id="travel">
        <div class="section-title-wrap">
            <h2 class="section-title">學長姐回娘家旅遊指南</h2>
            <p style="color: var(--text-muted); margin-top: 0.5rem; font-weight: 300;">為重返中壢的您，規劃了經典的懷舊一日遊行程</p>
        </div>

        <!-- Day Trip Content -->
        <div id="day-trip" class="tab-content active">
            <div class="travel-card">
                <div class="itinerary-step">
                    <div class="step-num">01</div>
                    <div class="step-detail">
                        <h4>上午：重溫青春記憶 ✦ 系慶慶典</h4>
                        <p>早上 09:30 抵達中原大學商學大樓，參加 <span class="highlight-text">50周年大會</span>，走訪熟悉卻又有些新面貌的金榮講堂，聆聽恩師的叮嚀，重溫求學點滴。</p>
                    </div>
                </div>
                <div class="itinerary-step">
                    <div class="step-num">02</div>
                    <div class="step-detail">
                        <h4>中午：美味聚餐 ✦ 綠光花園餐廳</h4>
                        <p>與老同學在 <span class="highlight-text">綠光花園餐廳</span> 共進午宴，在歡聲笑語中，暢談當年課堂上的趣事，更新彼此的近況，共同舉杯祝賀母系50歲生日。</p>
                    </div>
                </div>
                <div class="itinerary-step">
                    <div class="step-num">03</div>
                    <div class="step-detail">
                        <h4>下午：校園回憶散策 ✦ 經典打卡點</h4>
                        <p>在商學大樓前吹吹當年的風，走走大潤發旁的小路、懷舊麥當勞舊址。重溫那段 K 書熬夜、翹課吃宵夜的快樂時光。</p>
                    </div>
                </div>
                <div class="itinerary-step">
                    <div class="step-num">04</div>
                    <div class="step-detail">
                        <h4>傍晚：美食饗宴 ✦ 中原夜市懷舊</h4>
                        <p>傍晚前往中原夜市，品嚐念念不忘的經典在地特色小吃與手搖飲品，讓味蕾帶您重返大學時光，最後帶著滿滿的暖意與回憶溫馨歸航。</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Info, Location and Price details -->
    <section id="info" style="padding-top: 1rem;">
        <div class="info-grid">
            <!-- Details Card -->
            <div class="info-card">
                <div class="card-icon-wrap">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s-8-4.5-8-11.8A8 8 0 0 1 12 2a8 8 0 0 1 8 8.2c0 7.3-8 11.8-8 11.8z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                </div>
                <h3>交通與停車指引</h3>
                <ul class="info-list">
                    <li><span style="color:#FFF; font-weight:500;">大眾運輸</span>：搭乘台鐵至中壢火車站 / 搭乘高鐵至桃園青埔站，皆可轉乘中壢客運 (如 112 北) 或計程車直達中原大學。</li>
                    <li><span style="color:#FFF; font-weight:500;">自行開車</span>：中原大學設有中原國小地下停車場及校內停車場，校友日當天提供系友停車優惠。</li>
                    <li><span style="color:#FFF; font-weight:500;">餐宴會場</span>：綠光花園餐廳（桃園市中壢區環中東路651C號），備有專屬大型免費停車場。</li>
                </ul>
            </div>

            <!-- Price Card -->
            <div class="info-card">
                <div class="card-icon-wrap">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                </div>
                <h3>感恩餐會支持方案</h3>
                <ul class="info-list">
                    <li><span style="color:#FFF; font-weight:500;">認桌支持</span>：每桌新台幣 12,000 元（共 10 席），歡迎同窗好友或歷屆班級包桌重溫。</li>
                    <li><span style="color:#FFF; font-weight:500;">購買個人餐券</span>：每人新台幣 1,500 元。</li>
                    <li><span style="color:#FFF; font-weight:500;">攜幼同樂</span>：不佔位之幼童免購買餐券，歡迎學長姐攜全家大小一同共襄盛舉。</li>
                    <li>餐會結餘將撥入「中原國貿系發展基金」，用於支持系上學弟妹獎助學金與系所建設。</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Contacts & Registration -->
    <section id="register">
        <div class="travel-card" style="text-align: center;">
            <h2 style="font-size: 2rem; color: #FFF; margin-bottom: 1rem;">立即聯絡與報名</h2>
            <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto 2.5rem auto;">誠摯盼望您的歸來！如有任何疑問或欲進行認桌諮詢，歡迎與我們取得聯繫：</p>
            
            <a href="https://forms.gle/qSWvXK7SNmE1pZzJ9" target="_blank" class="cta-btn" style="margin-bottom: 2rem;">填寫系慶與餐會線上報名表</a>

            <div class="contact-box-grid">
                <div class="contact-card">
                    <div class="contact-name">賴心怡 助教</div>
                    <div class="contact-title">行政諮詢與報名窗口</div>
                    <a href="tel:032655204" class="contact-phone">(03) 265-5204</a>
                </div>
                <div class="contact-card">
                    <div class="contact-name">陳宣輔 助教</div>
                    <div class="contact-title">場地與活動事宜窗口</div>
                    <a href="tel:032655203" class="contact-phone">(03) 265-5203</a>
                </div>
                <div class="contact-card">
                    <div class="contact-name">伍向豪 主任</div>
                    <div class="contact-title">國貿系主任專線</div>
                    <a href="tel:0921899838" class="contact-phone">0921-899838</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-logo">中原大學國際經營與貿易學系</div>
        <p class="footer-text">© 2026 CYCU Department of International Business. All Rights Reserved.</p>
        <p class="footer-text" style="margin-top: 0.5rem; font-size: 0.8rem; color: #4A5568;">中原國貿創系五十週年籌備小組 敬邀</p>
    </footer>

    <!-- Lightbox Modal -->
    <div id="lightboxModal" class="lightbox" onclick="closeLightbox()">
        <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
        <img class="lightbox-img" id="lightboxImg" src="data:image/jpeg;base64,{base64_img}" alt="邀請卡放大預覽">
    </div>

    <!-- JavaScript -->
    <script>
        // Countdown Logic
        const targetDate = new Date("2026-10-17T09:30:00").getTime();
        
        function updateCountdown() {{
            const now = new Date().getTime();
            const difference = targetDate - now;

            if (difference < 0) {{
                document.getElementById("days").innerText = "00";
                document.getElementById("hours").innerText = "00";
                document.getElementById("minutes").innerText = "00";
                document.getElementById("seconds").innerText = "00";
                return;
            }}

            const days = Math.floor(difference / (1000 * 60 * 60 * 24));
            const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((difference % (1000 * 60)) / 1000);

            document.getElementById("days").innerText = days.toString().padStart(2, '0');
            document.getElementById("hours").innerText = hours.toString().padStart(2, '0');
            document.getElementById("minutes").innerText = minutes.toString().padStart(2, '0');
            document.getElementById("seconds").innerText = seconds.toString().padStart(2, '0');
        }}

        setInterval(updateCountdown, 1000);
        updateCountdown(); // Run immediately

        // Tab Switching Logic
        function switchTab(tabId) {{
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(content => content.classList.remove('active'));

            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(button => button.classList.remove('active'));

            document.getElementById(tabId).classList.add('active');
            event.currentTarget.classList.add('active');
        }}

        // Video Gallery Playlist Switch
        function playVideo(videoId, element) {{
            const player = document.getElementById("galleryPlayer");
            player.src = "https://www.youtube-nocookie.com/embed/" + videoId + "?autoplay=1";
            
            const items = document.querySelectorAll('.playlist-item');
            items.forEach(item => item.classList.remove('active'));
            
            element.classList.add('active');
        }}

        // Lightbox Logic
        function openLightbox() {{
            const modal = document.getElementById("lightboxModal");
            modal.classList.add("active");
            document.body.style.overflow = "hidden"; // Prevent scrolling
        }}

        function closeLightbox() {{
            const modal = document.getElementById("lightboxModal");
            modal.classList.remove("active");
            document.body.style.overflow = "auto"; // Restore scrolling
        }}
        
        // Close modal on ESC key
        document.addEventListener('keydown', function(event) {{
            if (event.key === "Escape") {{
                closeLightbox();
            }}
        }});
    </script>
</body>
</html>
"""

    with open(output_html_path, "w", encoding="utf-8") as out_file:
        out_file.write(html_content)
    
    print(f"Successfully generated beautiful HTML at: {output_html_path}")

if __name__ == "__main__":
    build_alumni_page()
