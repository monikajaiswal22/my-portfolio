import streamlit as st
import base64
import os
import requests

# Page configuration
st.set_page_config(
    page_title="Monika Jaiswal | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== RESUME LOADER ====================
def get_resume_download_link(file_path="resumee.pdf"):
    """Read resumee.pdf and return base64 download link"""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="Monika_Jaiswal_Resume.pdf" class="btn-red">📄 Download Resume</a>'
        return href
    else:
        return '<a href="mailto:monikajaiswal200@gmail.com?subject=Resume Request" class="btn-red">📄 Request Resume</a>'

# ==================== CSS ====================
st.markdown("""
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    .stApp { background: linear-gradient(135deg, #F0F4FF 0%, #E8EEFF 50%, #FFFFFF 100%); }
    .header {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #1E3A8A 100%);
        border-radius: 15px; padding: 40px; margin-bottom: 30px; color: white;
    }
    .name { font-size: 48px; font-weight: 700; color: white; margin-bottom: 10px; line-height: 1.2; }
    .title { font-size: 20px; color: #DBEAFE; margin-bottom: 15px; }
    .location { color: #BFDBFE; margin-bottom: 20px; }
    .btn-blue {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white !important; padding: 12px 30px; border-radius: 8px;
        text-decoration: none; display: inline-block; font-weight: 600;
        margin: 5px 10px 5px 0; border: none; cursor: pointer; transition: all 0.3s;
    }
    .btn-blue:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(37,99,235,0.3); color: white !important; }
    .btn-red {
        background: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
        color: white !important; padding: 12px 30px; border-radius: 8px;
        text-decoration: none; display: inline-block; font-weight: 600;
        margin: 5px 10px 5px 0; border: none; cursor: pointer; transition: all 0.3s;
    }
    .btn-red:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(220,38,38,0.3); color: white !important; }
    .btn-outline {
        background: transparent; color: #1E3A8A !important; padding: 10px 25px;
        border-radius: 8px; text-decoration: none; display: inline-block;
        font-weight: 600; border: 2px solid #1E3A8A; transition: all 0.3s;
    }
    .btn-outline:hover {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white !important; border-color: transparent;
    }
    .section-title {
        font-size: 28px; font-weight: 700;
        background: linear-gradient(135deg, #1E3A8A 0%, #DC2626 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 30px 0 20px 0; padding-bottom: 10px;
        border-bottom: 3px solid #DC2626; display: inline-block;
    }
    .card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border: 1px solid rgba(37,99,235,0.1); border-radius: 12px;
        padding: 20px; margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); transition: all 0.3s;
    }
    .card:hover { box-shadow: 0 6px 16px rgba(0,0,0,0.1); transform: translateY(-2px); }
    .stat-box {
        background: linear-gradient(135deg, #FFFFFF 0%, #F0F4FF 100%);
        border-radius: 12px; padding: 20px; text-align: center;
        border-top: 3px solid #1E3A8A;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); height: 100%;
    }
    .stat-number {
        font-size: 32px; font-weight: 700;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .stat-label { color: #4B5563; margin-top: 5px; }
    .edu-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border-left: 4px solid #DC2626; padding: 20px;
        margin-bottom: 15px; border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .edu-title {
        font-size: 18px; font-weight: 700;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    .skill-badge {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white; padding: 6px 16px; border-radius: 20px;
        display: inline-block; margin: 5px; font-size: 14px; transition: all 0.3s;
    }
    .skill-badge:hover { transform: scale(1.05); box-shadow: 0 4px 12px rgba(37,99,235,0.3); }
    .service-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border: 1px solid rgba(37,99,235,0.1); border-radius: 12px;
        padding: 20px; text-align: center; transition: all 0.3s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 20px; height: 100%;
    }
    .service-card:hover {
        border-color: #2563EB; transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .service-price {
        font-size: 24px; font-weight: 700;
        background: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 10px 0;
    }
    .project-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFF 100%);
        border: 1px solid rgba(37,99,235,0.1); border-radius: 12px;
        padding: 20px; transition: all 0.3s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 20px; height: 100%;
    }
    .project-card:hover {
        border-color: #DC2626; transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .project-tech { color: #DC2626; font-size: 13px; margin: 8px 0; }
    .featured-badge {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white; display: inline-block; padding: 4px 12px;
        border-radius: 20px; font-size: 11px; font-weight: 600; margin-bottom: 8px;
    }
    .social-container {
        display: flex; flex-wrap: wrap; gap: 12px;
        justify-content: center; margin: 20px 0;
    }
    .social-btn {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 12px 22px; border-radius: 10px;
        text-decoration: none; color: white !important;
        font-weight: 600; font-size: 14px; transition: all 0.3s;
        min-width: 140px; justify-content: center;
    }
    .social-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        color: white !important;
    }
    .social-github { background: linear-gradient(135deg, #24292e, #404448); }
    .social-linkedin { background: linear-gradient(135deg, #0077B5, #00A0DC); }
    .social-instagram { background: linear-gradient(135deg, #833AB4, #FD1D1D, #FCB045); }
    .social-fiverr { background: linear-gradient(135deg, #1DBF73, #19A463); }
    .contact-item {
        padding: 12px; border-bottom: 1px solid rgba(37,99,235,0.1);
        color: #1F2937;
    }
    .contact-item strong {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .footer {
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        color: #9CA3AF; padding: 30px; text-align: center;
        border-radius: 12px; margin-top: 40px;
    }
    hr { margin: 20px 0; border: none; border-top: 1px solid rgba(37,99,235,0.2); }
    .text-gradient-blue {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .text-gradient-red {
        background: linear-gradient(135deg, #DC2626 0%, #EF4444 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    @media (max-width: 1024px) {
        .name { font-size: 38px; }
        .title { font-size: 17px; }
        .section-title { font-size: 24px; }
        .header { padding: 30px; }
    }
    @media (max-width: 768px) {
        .header { padding: 25px 20px; text-align: center; }
        .name { font-size: 32px; text-align: center; }
        .title { font-size: 15px; text-align: center; }
        .location { text-align: center; }
        .section-title { font-size: 22px; }
        .stat-number { font-size: 26px; }
        .btn-blue, .btn-red, .btn-outline { padding: 10px 20px; font-size: 14px; margin: 5px 5px 5px 0; }
        .social-btn { padding: 10px 16px; font-size: 13px; min-width: 120px; }
        .card, .stat-box, .service-card, .project-card { padding: 15px; }
    }
    @media (max-width: 480px) {
        .header { padding: 20px 15px; border-radius: 10px; }
        .name { font-size: 26px; }
        .title { font-size: 13px; }
        .location { font-size: 13px; }
        .section-title { font-size: 20px; margin: 20px 0 15px 0; }
        .stat-number { font-size: 22px; }
        .stat-label { font-size: 13px; }
        .btn-blue, .btn-red, .btn-outline { padding: 8px 16px; font-size: 13px; display: block; width: 100%; text-align: center; margin: 6px 0; }
        .social-btn { width: 100%; min-width: unset; }
        .skill-badge { font-size: 12px; padding: 5px 12px; }
        .service-price { font-size: 20px; }
        .edu-title { font-size: 16px; }
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER ====================
resume_link = get_resume_download_link("resumee.pdf")

st.markdown(f"""
<div class="header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 250px;">
            <div class="name">Monika Jaiswal</div>
            <div class="title">💻 Full Stack Web Developer | PHP &amp; Python</div>
            <div class="location">📍 India | Available for Remote Work</div>
            <div style="margin-top: 20px;">
                <a href="mailto:monikajaiswal200@gmail.com?subject=Hire Me - Project Inquiry" class="btn-blue">📞 Hire Me</a>
                {resume_link}
            </div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 80px;">👩‍💻</div>
            <div style="background-color: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; margin-top: 10px;">
                🔥 Open for Work
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== SOCIAL LINKS TOP ====================
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h3 class="text-gradient-blue" style="font-size: 22px;">🌐 Connect With Me</h3>
</div>
<div class="social-container">
    <a href="https://github.com/monikajaiswal22" target="_blank" class="social-btn social-github">🐙 GitHub</a>
    <a href="https://www.linkedin.com/in/er-monika-jaiswal-983a9b179" target="_blank" class="social-btn social-linkedin">💼 LinkedIn</a>
    <a href="https://www.instagram.com/_coder_girl_mj_" target="_blank" class="social-btn social-instagram">📸 Instagram</a>
    <a href="https://www.fiverr.com/s/kXLkmEk" target="_blank" class="social-btn social-fiverr">💚 Fiverr</a>
</div>
""", unsafe_allow_html=True)

# ==================== STATS ====================
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-box"><div class="stat-number">3</div><div class="stat-label">🎓 Qualifications</div><small>Diploma + BCA + MCA</small></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><div class="stat-number">50+</div><div class="stat-label">💻 Projects</div><small>Successfully Completed</small></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><div class="stat-number">20+</div><div class="stat-label">🤝 Happy Clients</div><small>Worldwide</small></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-box"><div class="stat-number">100%</div><div class="stat-label">⭐ Satisfaction</div><small>5 Star Rating</small></div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== PROFESSIONAL PROFILE ====================
st.markdown('<h2 class="section-title">📖 Professional Profile</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class="card">
        <p style="font-size: 16px; line-height: 1.6;">
            Motivated and detail-oriented <strong class="text-gradient-blue">MCA candidate</strong> with a strong foundation 
            in Computer Applications, backed by a BCA and Diploma in Information Technology.
        </p>
        <p style="margin-top: 15px;">
            Proficient in <strong>PHP, Python, Flask, SQL/MySQL, HTML, CSS, JavaScript, and Bootstrap</strong>, 
            with hands-on experience developing responsive and user-friendly web applications.
        </p>
        <p style="margin-top: 15px;">
        <strong class="text-gradient-red">🎯 What I Offer:</strong><br>
        ✓ Clean, professional code with documentation<br>
        ✓ Responsive web development &amp; database integration<br>
        ✓ Timely delivery with regular updates<br>
        ✓ Post-delivery support
        </p>
        <p style="margin-top: 15px;">
        <strong class="text-gradient-red">🚀 Career Objective:</strong><br>
        To start my career in a growth-oriented organization where I can apply my web development 
        and programming skills, work on real-world applications, learn from experienced professionals, 
        and contribute to reliable, user-focused solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <div style="font-size: 60px;">👩‍🎓</div>
        <h3 class="text-gradient-blue">Monika Jaiswal</h3>
        <p>Full Stack Web Developer</p>
        <hr>
        <div style="text-align: left;">
            <p>📧 <strong>monikajaiswal200@gmail.com</strong></p>
            <p>📱 <strong>+91 8736019810</strong></p>
            <p>📍 <strong>India</strong></p>
        </div>
        <hr>
        <p>⭐⭐⭐⭐⭐<br><small>Rated 5/5 by clients</small></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== TECHNICAL SKILLS ====================
st.markdown('<h2 class="section-title">⚡ Technical Skills</h2>', unsafe_allow_html=True)

skill_categories = {
    "Programming": ["Python", "PHP", "JavaScript"],
    "Backend": ["Flask"],
    "Frontend": ["HTML5", "CSS3", "Bootstrap", "JavaScript"],
    "Database": ["SQL", "MySQL"],
    "Tools": ["Git", "GitHub"],
    "Development": ["Responsive Design", "Web Apps", "Database Integration"]
}

for category, skills in skill_categories.items():
    st.markdown(f'<h4 class="text-gradient-red" style="margin-top: 15px;">{category}</h4>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, skill in enumerate(skills):
        with cols[i % 4]:
            st.markdown(f'<div class="skill-badge">{skill}</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== EDUCATION ====================
st.markdown('<h2 class="section-title">🎓 Education</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="edu-card">
        <div class="edu-title">🎓 Master of Computer Applications (MCA)</div>
        <p><strong>IGNOU | Pursuing</strong></p>
        <p>• Advanced Computer Applications<br>• Specialization in Web Development</p>
    </div>
    <div class="edu-card">
        <div class="edu-title">📘 Bachelor of Computer Applications (BCA)</div>
        <p><strong>Completed</strong></p>
        <p>• Foundation in Programming &amp; Databases<br>• Web Development Projects</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="edu-card">
        <div class="edu-title">💻 Diploma in Information Technology</div>
        <p><strong>Completed</strong></p>
        <p>• Programming Fundamentals<br>• Foundation of coding &amp; IT concepts</p>
    </div>
    <div class="card">
        <div class="edu-title" style="font-size: 16px;">📜 Additional Strengths</div>
        <p>✓ Git &amp; GitHub for version control<br>
        ✓ Responsive Web Development<br>
        ✓ Freelancing &amp; client-oriented work<br>
        ✓ Quick learner with strong interest in tech</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== SERVICES ====================
st.markdown('<h2 class="section-title">💼 Freelance Services</h2>', unsafe_allow_html=True)

services = [
    {"icon": "🐍", "name": "Python Development", "price": "₹9,999-₹29,999", "desc": "Flask, Automation, APIs"},
    {"icon": "🌐", "name": "Web Development", "price": "₹7,999-₹39,999", "desc": "Responsive PHP/Python Websites"},
    {"icon": "📱", "name": "Web Applications", "price": "₹12,999-₹49,999", "desc": "Full-Stack Apps"},
    {"icon": "🗄️", "name": "Database Design", "price": "₹3,999-₹9,999", "desc": "MySQL Optimization & Queries"},
    {"icon": "🎨", "name": "Frontend Design", "price": "₹5,999-₹29,999", "desc": "HTML/CSS/Bootstrap UI"},
    {"icon": "📊", "name": "Data Analysis", "price": "₹4,999-₹19,999", "desc": "Visualization & Reports"}
]

service_cols = st.columns(3)
for i, service in enumerate(services):
    with service_cols[i % 3]:
        mailto = f"mailto:monikajaiswal200@gmail.com?subject=Inquiry about {service['name']}&body=Hi Monika,%0D%0A%0D%0AI'm interested in your {service['name']} service."
        st.markdown(f"""
        <div class="service-card">
            <div style="font-size: 40px;">{service['icon']}</div>
            <h3 class="text-gradient-blue">{service['name']}</h3>
            <div class="service-price">{service['price']}</div>
            <p style="color: #6B7280;">{service['desc']}</p>
            <a href="{mailto}" class="btn-outline" style="padding: 6px 15px; font-size: 13px; width: 100%; display: inline-block; text-align: center; box-sizing: border-box;">
                Get Quote →
            </a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== PROJECTS ====================
st.markdown('<h2 class="section-title">🚀 My Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "name": "Portfolio Generator",
        "icon": "🎨",
        "tech": "Streamlit | Python | HTML/CSS | JavaScript",
        "desc": "Create stunning professional portfolios in minutes with live preview and download.",
        "url": "https://monikajaiswal22.github.io/portfolio-generator",
        "featured": True
    },
    {
        "name": "College Management System",
        "icon": "🏫",
        "tech": "Python | Flask | MySQL | Bootstrap",
        "desc": "Web-based application to manage college information and administrative tasks with structured pages.",
        "url": "https://college-management-system-g3z2.onrender.com",
        "featured": False
    },
    {
        "name": "E-Learning Platform",
        "icon": "📚",
        "tech": "Python | Flask | MySQL | Bootstrap",
        "desc": "E-learning web project for presenting courses and learning content in an organized manner.",
        "url": "https://e-learning-platform-8fei.onrender.com",
        "featured": False
    },
    {
        "name": "VBT (Full Stack)",
        "icon": "💼",
        "tech": "PHP | HTML | CSS | JavaScript | MySQL",
        "desc": "Full-stack web project with clean structure, responsive styling and functional user interaction.",
        "url": "mailto:monikajaiswal200@gmail.com?subject=VBT Project Demo Request",
        "featured": False
    }
]

featured = [p for p in projects if p.get("featured")]
others = [p for p in projects if not p.get("featured")]

for project in featured:
    st.markdown(f"""
    <div class="project-card" style="border: 2px solid #10b981;">
        <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
            <div style="font-size: 60px;">{project['icon']}</div>
            <div style="flex: 1; min-width: 250px;">
                <div class="featured-badge">⭐ Featured Project</div>
                <h3 class="text-gradient-blue" style="font-size: 24px; margin-bottom: 5px;">{project['name']}</h3>
                <div class="project-tech">{project['tech']}</div>
                <p style="color: #6B7280; margin: 10px 0;">{project['desc']}</p>
                <a href="{project['url']}" target="_blank" class="btn-blue" style="text-decoration: none; display: inline-block;">
                    🚀 View Live Demo
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if others:
    project_cols = st.columns(3)
    for i, project in enumerate(others):
        with project_cols[i % 3]:
            btn_text = "🔗 Live Demo →" if "http" in project['url'] else "📧 Request Demo →"
            st.markdown(f"""
            <div class="project-card">
                <div style="font-size: 48px; margin-bottom: 10px;">{project['icon']}</div>
                <h4 class="text-gradient-blue">{project['name']}</h4>
                <div class="project-tech">{project['tech']}</div>
                <p style="color: #6B7280; font-size: 14px; min-height: 70px;">{project['desc']}</p>
                <a href="{project['url']}" target="_blank" class="btn-outline" 
                   style="padding: 8px 16px; font-size: 13px; text-decoration: none; 
                          display: inline-block; margin-top: 10px;">
                    {btn_text}
                </a>
            </div>
            """, unsafe_allow_html=True)

st.info("💡 **Note:** College Management & E-Learning apps Render free tier hosted, please wait for 20-30 seconds to open website.")

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== WHY HIRE ME ====================
st.markdown('<h2 class="section-title">✨ Why Choose Me?</h2>', unsafe_allow_html=True)

why_cols = st.columns(4)
why_data = [
    {"icon": "✅", "title": "Quality Work", "desc": "Clean, documented code"},
    {"icon": "⚡", "title": "Fast Delivery", "desc": "On-time delivery"},
    {"icon": "💰", "title": "Affordable", "desc": "Student friendly rates"},
    {"icon": "💬", "title": "24/7 Support", "desc": "Always available"}
]
for i, item in enumerate(why_data):
    with why_cols[i]:
        st.markdown(f"""
        <div class="stat-box">
            <div style="font-size: 32px;">{item['icon']}</div>
            <div class="stat-number" style="font-size: 20px;">{item['title']}</div>
            <div class="stat-label">{item['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==================== CONTACT ====================
st.markdown('<h2 class="section-title">📬 Contact Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="card">
        <h3 class="text-gradient-blue">📞 Get in Touch</h3>
        <div class="contact-item">📧 <strong>Email:</strong> monikajaiswal200@gmail.com</div>
        <div class="contact-item">📱 <strong>Phone:</strong> +91 8736019810</div>
        <div class="contact-item">💬 <strong>WhatsApp:</strong> Available</div>
        <div class="contact-item">🌍 <strong>Location:</strong> India (Remote)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3 class="text-gradient-red">🌐 Find Me On</h3>
        <div style="margin-top: 15px;">
            <a href="https://github.com/monikajaiswal22" target="_blank" class="social-btn social-github" style="width: 100%; margin-bottom: 10px; box-sizing: border-box;">🐙 GitHub - monikajaiswal22</a>
            <a href="https://www.linkedin.com/in/er-monika-jaiswal-983a9b179" target="_blank" class="social-btn social-linkedin" style="width: 100%; margin-bottom: 10px; box-sizing: border-box;">💼 LinkedIn - Monika Jaiswal</a>
            <a href="https://www.instagram.com/_coder_girl_mj_" target="_blank" class="social-btn social-instagram" style="width: 100%; margin-bottom: 10px; box-sizing: border-box;">📸 Instagram - @_coder_girl_mj_</a>
            <a href="https://www.fiverr.com/s/kXLkmEk" target="_blank" class="social-btn social-fiverr" style="width: 100%; box-sizing: border-box;">💚 Fiverr - Hire Me</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== CONTACT FORM ====================
st.markdown('<h3 class="text-gradient-blue" style="margin-top: 20px;">✉️ Send a Message</h3>', unsafe_allow_html=True)

FORMSPREE_URL = "https://formspree.io/f/xgavbglv"

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email")
    with col2:
        service_interest = st.selectbox("I'm interested in", 
                                        ["Python Development", "PHP Development", "Web Development", 
                                         "Web App", "Database Design", "Frontend Design", "Other"])
        phone = st.text_input("Phone (Optional)", placeholder="Enter your phone")
    
    message = st.text_area("Message", placeholder="Tell me about your project...", height=120)
    submitted = st.form_submit_button("📩 Send Message", use_container_width=True)
    
    if submitted:
        if name and email and message:
            try:
                with st.spinner("Sending message..."):
                    response = requests.post(
                        FORMSPREE_URL,
                        data={
                            "Name": name,
                            "Email": email,
                            "Phone": phone if phone else "Not provided",
                            "Service": service_interest,
                            "Message": message
                        },
                        timeout=10
                    )
                if response.status_code == 200:
                    st.success("✅ Message sent! I'll reply within 24 hours.")
                    st.balloons()
                else:
                    st.error("❌ Failed. Please email me at monikajaiswal200@gmail.com")
            except Exception:
                st.error("❌ Network error. Please email me at monikajaiswal200@gmail.com")
        else:
            st.error("❌ Please fill Name, Email and Message fields.")

# ==================== WHATSAPP QUICK CONTACT ====================
st.markdown("""
<div class="card" style="text-align: center; margin-top: 20px; background: linear-gradient(135deg, #E7F9EF 0%, #DCFCE7 100%); border: 1px solid #25D366;">
    <h3 style="background: linear-gradient(135deg, #25D366, #128C7E); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        💬 Prefer WhatsApp?
    </h3>
    <p style="color: #4B5563; margin: 10px 0;">Get instant reply — click below to chat directly</p>
    <a href="https://wa.me/918736019810?text=Hi%20Monika,%20I%20want%20to%20discuss%20a%20project" 
       target="_blank" 
       style="background: linear-gradient(135deg, #25D366, #128C7E); color: white !important;
              padding: 12px 30px; border-radius: 8px; text-decoration: none;
              display: inline-block; font-weight: 600; margin-top: 10px;
              box-shadow: 0 4px 12px rgba(37,211,102,0.3);">
        💬 Chat on WhatsApp
    </a>
</div>
""", unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    <p>© 2025 Monika Jaiswal | Full Stack Web Developer</p>
    <p>💼 Available for Freelance Work | Let's Build Something Great Together</p>
    <p style="margin-top: 10px;">📧 monikajaiswal200@gmail.com | 📱 +91 8736019810</p>
    <div class="social-container" style="margin-top: 20px;">
        <a href="https://github.com/monikajaiswal22" target="_blank" class="social-btn social-github">🐙 GitHub</a>
        <a href="https://www.linkedin.com/in/er-monika-jaiswal-983a9b179" target="_blank" class="social-btn social-linkedin">💼 LinkedIn</a>
        <a href="https://www.instagram.com/_coder_girl_mj_" target="_blank" class="social-btn social-instagram">📸 Instagram</a>
        <a href="https://www.fiverr.com/s/kXLkmEk" target="_blank" class="social-btn social-fiverr">💚 Fiverr</a>
    </div>
    <p style="margin-top: 20px;">
        <a href="https://monikajaiswal22.github.io/portfolio-generator" target="_blank" style="color: #9CA3AF; text-decoration: none;">
            🎨 Try my Portfolio Generator Tool →
        </a>
    </p>
</div>
""", unsafe_allow_html=True)
